from langchain.tools import Tool
from langchain_community.tools import DuckDuckGoSearchRun, ArxivQueryRun, WikipediaQueryRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper, ArxivAPIWrapper, WikipediaAPIWrapper

search = DuckDuckGoSearchRun()
web_search_tool = Tool(
    name = 'search_web',
    func = search.run,
    description = 'searches the internet for information'
)

api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=1000)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
wiki_tool = Tool(
    name = 'wiki_tool',
    func = wiki.run,
    description = 'Useful for getting quick, factual information about people, places or events'
)


arx = ArxivAPIWrapper(top_k_results=3)
arxiv = ArxivQueryRun(api_wrapper=arx)
arxiv_tool = Tool(
    name = 'arxiv_tool',
    func = arxiv.run,
    description = 'Useful for retrieving in-depth scientific information through academic papers from Arxiv.org'
)
