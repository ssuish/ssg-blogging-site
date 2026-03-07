import os
from block import markdown_to_html_node


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("There's no title")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = None
    template = None

    try:
        with open(from_path, "r") as f:
            md = f.read()
    except FileNotFoundError:
        print(f"Missing file at {from_path}")

    try:
        with open(template_path, "r") as f:
            template = f.read()
    except FileNotFoundError:
        print(f"Missing file at {from_path}")

    html_str = markdown_to_html_node(md).to_html()

    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_str)

    dir_path = os.path.dirname(dest_path)
    os.makedirs(os.path.abspath(dir_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)
