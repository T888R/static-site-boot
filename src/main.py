from textnode import *
import os
import shutil

def copy_directory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)

    recursive_copy(src, dst)

def recursive_copy(src, dst):
    if not os.path.exists(dst):
        # os.mkdir(dst)
        os.makedirs(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        print(src_path, dst_path)

        if os.path.isdir(src_path):
            recursive_copy(src_path, dst_path)
        else:
            shutil.copy(src_path, dst_path)

def main():
    current_dir = os.getcwd()
    # static_dir = current_dir + "/static/"
    # public_dir = current_dir + "/public/"
    static_dir = os.path.join(current_dir, "static")
    public_dir = os.path.join(current_dir, "public")
    copy_directory(static_dir, public_dir)

main()

