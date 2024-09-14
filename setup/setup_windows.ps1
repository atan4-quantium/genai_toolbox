Write-Output "Creating virtual environment..."
python -m venv ./.venv

Write-Output "Activating virtual environment..."
& ./.venv/Scripts/Activate.ps1

Write-Output "Installing project dependencies..."
pip install -r requirements.txt

# Write-Output "Installing git hooks"
# pre-commit install

Write-Output "Done!"