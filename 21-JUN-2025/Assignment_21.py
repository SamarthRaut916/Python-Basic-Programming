import os, shutil

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)

def append(path, data):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(data)

def exists(path):
    return os.path.isfile(path)

def delete(path):
    if exists(path): os.remove(path)

def copy(src, dst):
    shutil.copy(src, dst)

def move(src, dst):
    shutil.move(src, dst)

def size(path):
    return os.path.getsize(path)

def list_dir(path, ext=None):
    return [f for f in os.listdir(path) if ext is None or f.endswith(ext)]

def mkdir(path):
    os.makedirs(path, exist_ok=True)
