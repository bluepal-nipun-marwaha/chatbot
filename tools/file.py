def print_repoagent_summary():
    summary = {
        "Classes": {
            "GitHubFile": "Holds GitHub file information (content, path, URL).",
            "RepositoryInfo": "Holds repository info (name, URL, contents).",
            "RepoAgent": "Specialized agent for GitHub repos. Supports FULL_CONTEXT & RAG modes."
        },
        "Key Methods": {
            "__init__": "Initialize RepoAgent with retriever, model, repos, etc.",
            "parse_url": "Parse GitHub URL → (owner, repo_name).",
            "load_repositories": "Load contents of multiple repos.",
            "load_repository": "Load a single repo using GitHub client.",
            "count_tokens": "Return number of tokens.",
            "construct_full_text": "Concatenate repos into full context text.",
            "add_repositories": "Add new repo(s) to context.",
            "check_switch_mode": "Check if switching to RAG mode is needed.",
            "step": "Retrieve context + pass input to model.",
            "reset": "Reset agent state.",
            "search_by_file_path": "Search and reconstruct file contents by path."
        }
    }

    print("\n=== RepoAgent Summary ===\n")
    print("Classes:")
    for cls, desc in summary["Classes"].items():
        print(f"- {cls}: {desc}")

    print("\nMethods:")
    for method, desc in summary["Key Methods"].items():
        print(f"- {method}(): {desc}")


if __name__ == "__main__":
    print_repoagent_summary()
