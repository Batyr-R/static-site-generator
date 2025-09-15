import os
import shutil

from block_markdown import markdown_to_html_node

def source_to_dest(source, dest, first_call=True):
    if not os.path.exists(source):
        raise Exception("source path dont exist")
    if os.path.exists(dest) and first_call:
        shutil.rmtree(dest)
    os.makedirs(dest, exist_ok=True)
    source_files = os.listdir(source)
    for f in source_files:
        file_path = os.path.join(source, f)
        dst_path = os.path.join(dest, f)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dst_path)
            print(f"copying file: {f} from: {file_path} to: {dst_path}")
        elif os.path.isdir(file_path):
            os.makedirs(dst_path, exist_ok=True)
            source_to_dest(file_path, dst_path, first_call=False)
        else:
            print(f"WARNING: skipping unsupported entry {file_path}")

def extract_title(markdown):
    lines = markdown.split("\n")
    for l in lines:
        if l.startswith("# "):
            title = l[2:].strip()
            return title
    raise Exception("h1 head not found")

def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path) or not os.path.exists(template_path):
        raise Exception("from or template path doesn't exist")
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        md_data = f.read()
    with open(template_path, "r") as f:
        tmpl_data = f.read()
    html = markdown_to_html_node(md_data).to_html()
    title = extract_title(md_data)
    tmpl_data_title = tmpl_data.replace("{{ Title }}", title)
    tmpl_data_finish = tmpl_data_title.replace("{{ Content }}", html)
    dir_name = os.path.dirname(dest_path)
    os.makedirs(dir_name, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(tmpl_data_finish)

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source = os.path.join(root, "static")
    dest = os.path.join(root, "public")
    source_to_dest(source, dest)
    index = os.path.join(root, "content/index.md")
    template = os.path.join(root, "template.html")
    index_dest = os.path.join(root, "public/index.html")
    generate_page(index, template, index_dest)


main()
