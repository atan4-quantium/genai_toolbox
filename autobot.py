from pr_agent import cli
from pr_agent.config_loader import get_settings

def main():
    # Fill in the following values
    provider = "github" # GitHub provider
    user_token = ""  # GitHub user token
    # openai_key = "..."  # OpenAI key
    PROJECT_ID = ""
    pr_url = "https://github.com/atan4-quantium/dspy-theme-generation/pull/2"      # PR URL, for example 'https://github.com/Codium-ai/pr-agent/pull/809'
    command = "/review" # Command to run (e.g. '/review', '/describe', '/ask="What is the purpose of this PR?"', ...)

    # Setting the configurations
    print(get_settings())
    get_settings().set("CONFIG.git_provider", provider)
    # get_settings().set("openai.key", openai_key)
    get_settings().set("vertexai.vertex_project", PROJECT_ID)
    get_settings().set("github.user_token", user_token)

    # Run the command. Feedback will appear in GitHub PR comments
    cli.run_command(pr_url, command)


if __name__ == '__main__':
    main()