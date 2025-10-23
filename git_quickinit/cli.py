import argparse
from .commands import quickinit_full, quickinit_template, quickinit_interactive, quickinit_dryrun

def main():
    parser = argparse.ArgumentParser(prog="git-quickinit", description="QuickInit: Simplify Git repo setup")
    subparsers = parser.add_subparsers(dest="command")

    # Full setup + push
    full_parser = subparsers.add_parser("full", help="Initialize repo, first commit, branch, remote push")
    full_parser.add_argument("repo_name", help="Repository name")
    full_parser.add_argument("-m", "--message", required=True, help="Commit message")
    full_parser.add_argument("--branch", default="main", help="Branch name (default: main)")
    full_parser.add_argument("--remote", default=None, help="Remote service (github)")

    # Template command
    template_parser = subparsers.add_parser("template", help="Add templates for repo")
    template_parser.add_argument("repo", help="Path to repo")
    template_parser.add_argument("--lang", required=True, help="Language for .gitignore")

    # Interactive
    subparsers.add_parser("interactive", help="Interactive step-by-step setup")

    # Dry run
    subparsers.add_parser("dry-run", help="Preview commands without executing")

    args = parser.parse_args()

    if args.command == "full":
        quickinit_full(args.repo_name, args.message, args.branch, args.remote)
    elif args.command == "template":
        quickinit_template(args.repo, args.lang)
    elif args.command == "interactive":
        quickinit_interactive()
    elif args.command == "dry-run":
        quickinit_dryrun()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
