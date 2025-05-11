# hooks/post_gen_project.py

def print_readme_section(start_marker, end_marker, readme_path="README.MD"):
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        inside_section = False
        for line in lines:
            if start_marker in line:
                inside_section = True
                continue
            if end_marker in line and inside_section:
                break
            if inside_section:
                print(line, end="")  # avoid adding extra newlines
    except FileNotFoundError:
        print(f"{readme_path} not found.")


if __name__ == "__main__":
    print("\n📘 Highlighted Section from README.md:\n")
    print_readme_section("<!-- FIRST STEPS -->", "<!-- END FIRST STEPS -->")