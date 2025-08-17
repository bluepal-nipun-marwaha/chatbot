from camel.agents.repo_agent import RepoAgent
from camel.storages.vectordb_storages import QdrantStorage
from camel.retrievers import VectorRetriever
from camel.embeddings import OpenAIEmbedding
from camel.models import ModelFactory
from camel.types import EmbeddingModelType
from dotenv import load_dotenv
import os

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPO_URL = "https://github.com/bluepal-nipun-marwaha/chatbot"

# -----------------------------
# Settings
# -----------------------------
COLLECTION_NAME = "repo_code_docs"
TOP_K = 5
SIMILARITY = 0.6
MAX_CONTEXT_TOKENS = 2000
CHUNK_SIZE = 2000  # characters per chunk

# -----------------------------
# Setup Embedding Model
# -----------------------------
embedding_model = OpenAIEmbedding(model_type=EmbeddingModelType.TEXT_EMBEDDING_ADA_2)
vector_dim = embedding_model.get_output_dim()  # usually 1536

# -----------------------------
# Setup Qdrant Storage
# -----------------------------
vector_storage = QdrantStorage(
    collection_name=COLLECTION_NAME,
    path="qdrant_local",
    vector_dim=vector_dim
)

# -----------------------------
# Setup Vector Retriever
# -----------------------------
vector_retriever = VectorRetriever(
    embedding_model=embedding_model,
    storage=vector_storage
)

# -----------------------------
# Setup Model Backend
# -----------------------------
model_backend = ModelFactory.create(
    model_platform="openai",
    model_type="gpt-4o-mini",
    api_key=OPENAI_API_KEY
)

# -----------------------------
# Initialize RepoAgent
# -----------------------------
repo_agent = RepoAgent(
    vector_retriever=vector_retriever,
    model=model_backend,
    github_auth_token=GITHUB_TOKEN,
    repo_paths=[REPO_URL],
    max_context_tokens=MAX_CONTEXT_TOKENS,
    collection_name=COLLECTION_NAME,
    top_k=TOP_K,
    similarity=SIMILARITY,
    chunk_size=CHUNK_SIZE
)

# -----------------------------
# Load / Index Repository
# -----------------------------
print("Loading repository and indexing files into Qdrant...")
repo_agent.load_repositories([REPO_URL])
print(f"Repository loaded. Current token count: {repo_agent.count_tokens()}")
print("Repository files are now indexed in Qdrant.")

# -----------------------------
# Generate Documentation
# -----------------------------
# The agent will automatically handle full context or RAG mode internally.
query = """
Generate detailed Markdown documentation for all source code files in this repository,
including files in Python, JavaScript, TypeScript, Java, C, C++, Go, and any other programming languages present.
For each file, include:

- File summary and purpose
- Descriptions of all classes, functions, and methods
- Input arguments and return types (if applicable)
- Usage examples
- Any important notes or dependencies

Use GitHub-flavored Markdown and organize the documentation by file and folder structure.
"""

response = repo_agent.step(query)

# -----------------------------
# Extract text and write to file
# -----------------------------
if hasattr(response, "msgs") and response.msgs:
    doc_text = response.msgs[0].content
else:
    doc_text = str(response)

output_path = os.path.join(os.path.dirname(__file__), "Repository_Documentation.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(doc_text)