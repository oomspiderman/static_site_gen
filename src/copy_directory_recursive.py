import os
import shutil

def copy_directory_recursive(src: str, dst: str):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    for entry in os.listdir(src):
        src_path = os.path.join(src, entry)
        dst_path = os.path.join(dst, entry)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {dst_path}")
        elif os.path.isdir(src_path):
            copy_directory_recursive(src_path, dst_path)