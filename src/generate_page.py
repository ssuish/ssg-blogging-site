import os
from block import markdown_to_html_node


def extract_title(md):
    if len(md) - len(md.lstrip("#")) == 1:
        return md.lstrip("#").strip(" ")
    raise ValueError("There's no h1 header.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md = None
    template = None

    try:
        with open(from_path, 'r') as f: 
            md = f.read()
    except FileNotFoundError:
        print(f"Missing file at {from_path}")

    try:
        with open(template_path, "r") as f:
            template  = f.read()
    except FileNotFoundError:
        print(f"Missing file at {from_path}")

    html_str = markdown_to_html_node(md).to_html()

    title = extract_title(md)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_str)

    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(template)