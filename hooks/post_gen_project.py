# hooks/post_gen_project.py

from pathlib import Path


def print_readme_section(start_marker, end_marker, readme_path="README.md"):
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        inside_section = False
        for line in lines:
            if start_marker in line:
                inside_section = True
                print("\033[1;36m")  # Bright cyan
                continue
            if end_marker in line and inside_section:
                print("\033[0m")  # Reset formatting
                break
            if inside_section:
                print(f"\033[1m{line.rstrip()}\033[0m")  # Bold line
    except FileNotFoundError:
        print(f"\033[91m{readme_path} not found.\033[0m")


def ensure_init_files(root: Path) -> None:
    for rel in [
        "src/{{cookiecutter.package_name}}/__init__.py",
        "src/{{cookiecutter.package_name}}/data/__init__.py",
        "src/{{cookiecutter.package_name}}/models/__init__.py",
        "src/{{cookiecutter.package_name}}/utils/__init__.py",
    ]:
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.touch(exist_ok=True)


if __name__ == "__main__":
    project_root = Path.cwd()
    ensure_init_files(project_root)
    print("\n📘 \033[1;34mSetup Instructions:\033[0m\n")
    print_readme_section("<!-- FIRST STEPS -->", "<!-- END FIRST STEPS -->")
