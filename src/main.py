import os
import shutil

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

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source = os.path.join(root, "static")
    dest = os.path.join(root, "public")
    source_to_dest(source, dest)

main()
