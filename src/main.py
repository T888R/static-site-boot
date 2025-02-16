from textnode import *
from block_markdown import *
from inline_markdown import *
from htmlnode import *
import os
import shutil

def copy_directory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    recursive_copy(src, dst)

def recursive_copy(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isdir(src_path):
            recursive_copy(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path)
    from_content = from_file.read()

    template_file = open(template_path)
    template_content = template_file.read()

    content = markdown_to_html_node(from_content)
    title = extract_title(from_content)

    content_replaced = template_content.replace("{{ Content }}", content.to_html())
    title_replaced = content_replaced.replace("{{ Title }}", title)

    if os.path.exists(dest_path):
        public_file = os.path.join(dest_path, "index.html")
        dest_file = open(public_file, "w")
        dest_file.write(title_replaced)
        dest_file.close()
        with open(os.path.join(dest_path, "index.html"), "w") as file:
            file.write(title_replaced)
        print("Destination file written")
        print(os.path.join(dest_path, "index.html"))


def main():
    current_dir = os.getcwd()
    static_dir = os.path.join(current_dir, "static")
    public_dir = os.path.join(current_dir, "public")

    copy_directory(static_dir, public_dir)

    from_file = os.path.join(current_dir, "content/index.md")
    template_file = os.path.join(current_dir, "template.html")
    public_file = os.path.join(public_dir, "index.html")

    # generate_page(from_file, template_file, public_file)
    generate_page(from_file, template_file, public_dir)

if __name__ == "__main__":
    main()

