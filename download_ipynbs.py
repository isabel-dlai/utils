import os
import shutil
from pathlib import Path
from git import Repo

# GitHub organization URL
org_url = "https://github.com/https-deeplearning-ai"

# Create a temporary directory to clone the repository
temp_dir = Path("temp_repo")
temp_dir.mkdir(exist_ok=True)

# Clone the organization repository
repo_url = f"{org_url}.git"
repo_path = temp_dir / "org_repo"
Repo.clone_from(repo_url, repo_path)

# Traverse the directories in the repository
for dir_name in os.listdir(repo_path):
    if dir_name.lower().endswith("-platform"):
        print(dir_name)

# Remove the temporary directory
shutil.rmtree(temp_dir)

print("Script execution completed.")