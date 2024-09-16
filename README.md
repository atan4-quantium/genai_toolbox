### Setup
---
For Windows users:
- Install Python
- Setup Virtual Environment:
    - Open PowerShell and navigate to the project directory
    - Run the setup script `setup/setup_windows.ps1` in PowerShell
    - This script creates a virtual environment using `venv` and install the necessary dependencies
- Configure your IDE to this project's virtual environment
    - VS Code: Open Command Palette (Ctrl+Shift+P) > Python: Select Interpreter
    - Select the recently created environment


### PR Agent
---
- Create `.env` file:
    - In the project directory, make a copy of `.env.template` file and rename it to `.env`
- Add your credentials:
    - Open the `.env` file and add the following variables
        ```
        GITHUB_USER_TOKEN=<YOUR_GITHUB_USER_TOKEN>
        VERTEX_PROJECT_ID=<YOUR_VERTEX_PROJECT_ID>
        ```
    - Obtain GitHub User Token: If you don't have a GitHub user token, you can generate one at https://github.com/settings/tokens. Make sure to grant the token appropriate permissions for accessing pull requests.
    - Obtain Vertex Project ID: You can find your vertex AI project ID in the Google Cloud Console
- Run PR Agent:
    - Navigate to `pr-agent.ipynb` Jupyter Notebook file in the project directory
    - Locate the `PR_URL` variable in the notebook
    - Paste the URL of the pull request you want to analyse
    - Run the notebook 