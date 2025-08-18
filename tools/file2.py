def summarize_repo():
    summary = """
    📘 Repo: docAider

    docAider is a multi-agent system that automates code documentation
    using Semantic Kernel and Autogen. It generates, reviews, and updates
    documentation for repositories through orchestrated agents.

    Key Features:
    - Automates initial documentation generation.
    - Multi-agent workflow:
        • CodeContextAgent → explains code.
        • DocumentationGenerationAgent → writes docs.
        • ReviewAgent → improves docs.
        • AgentManager → orchestrates the workflow.
    - Produces outputs like docs, prompts, call graphs, and flow diagrams.
    - Supports GitHub Actions workflows for continuous documentation updates.
    - Helps untangle complex code, find unused functions, and onboard developers faster.

    Usage:
    - Run via Docker (`docker compose up --build`).
    - Generate documentation (`docker exec docAider python3 /docAider/repo_documentation/multi_agent_app.py`).
    - Set up workflows (`docker exec docAider python3 /docAider/setup_workflows.py`).
    - Workflows:
        • update-docs.yml → auto-updates docs on PRs.
        • update-comments.yml → lets users request doc changes via comments.
    """
    print(summary)


if __name__ == "__main__":
    summarize_repo()
