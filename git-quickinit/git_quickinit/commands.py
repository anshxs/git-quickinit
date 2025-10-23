import os
import subprocess
from pathlib import Path
from github import Github
import getpass

def run_command(cmd, dry_run=False):
    print(f"$ {' '.join(cmd)}")
    if not dry_run:
        subprocess.run(cmd, check=True)

# -------------------------------
# Full setup + GitHub push
# -------------------------------
def quickinit_full(repo_name, message, branch, remote):
    print(f"Initializing local repo '{repo_name}'...")
    run_command(["git", "init"])
    run_command(["git", "add", "."])
    run_command(["git", "commit", "-m", message])
    run_command(["git", "branch", "-M", branch])

    if remote == "github":
        token = os.environ.get("GITHUB_TOKEN") or getpass.getpass("Enter GitHub Personal Access Token: ")
        g = Github(token)
        user = g.get_user()
        repo = user.create_repo(repo_name)
        repo_url = repo.ssh_url
        run_command(["git", "remote", "add", "origin", repo_url])
        run_command(["git", "push", "-u", "origin", branch])
        print(f"Repo pushed to GitHub: {repo_url}")

# -------------------------------
# Add templates (.gitignore, README, LICENSE)
# -------------------------------
def quickinit_template(repo, lang):
    template_dir = Path(__file__).parent / "templates"
    gitignore_file = template_dir / f"{lang}.gitignore"
    readme_file = template_dir / "README.md"
    license_file = template_dir / "LICENSE"

    if gitignore_file.exists():
        dest = Path(repo) / ".gitignore"
        dest.write_text(gitignore_file.read_text())
    if readme_file.exists():
        dest = Path(repo) / "README.md"
        dest.write_text(readme_file.read_text())
    if license_file.exists():
        dest = Path(repo) / "LICENSE"
        dest.write_text(license_file.read_text())

    print("Templates added successfully!")

# -------------------------------
# Interactive setup
# -------------------------------
def quickinit_interactive():
    repo_name = input("Repo name: ")
    message = input("Commit message: ")
    branch = input("Branch name (main/master, default main): ") or "main"
    remote = input("Remote service (github/none, default github): ") or "github"
    lang = input("Project language for template (python/node/none, default none): ") or None

    quickinit_full(repo_name, message, branch, remote)
    if lang and lang.lower() != "none":
        quickinit_template(".", lang.lower())

# -------------------------------
# Dry run / preview
# -------------------------------
def quickinit_dryrun():
    print("Dry run: commands that would execute")
    commands = [
        "git init",
        "git add .",
        "git commit -m 'first commit'",
        "git branch -M main",
        "git remote add origin <remote-url>",
        "git push -u origin main"
    ]
    for c in commands:
        print(f"$ {c}")
