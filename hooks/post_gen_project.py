# hooks/post_gen_project.py

def print_readme_section(start_marker, end_marker, readme_path="README.MD"):
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


if __name__ == "__main__":
    print("\n📘 \033[1;34mSetup Instructions:\033[0m\n")
    print_readme_section("<!-- FIRST STEPS -->", "<!-- END FIRST STEPS -->")
