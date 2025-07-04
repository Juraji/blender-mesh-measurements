"""
Development tool: Generate ZIP package for Blender to install
"""
from zipfile import ZipFile, ZIP_DEFLATED
from os import path, remove, walk

if __name__ == '__main__':
    pkg_base_name: str = "blender_mesh_measurements"
    pkg_name: str = f"{pkg_base_name}.zip"

    try:
        remove(pkg_name)
    except OSError:
        pass

    with ZipFile(pkg_name, 'w', ZIP_DEFLATED) as zipf:
        for folder_name, subdir, filenames in walk(pkg_base_name):
            for filename in filenames:
                file_path = path.join(folder_name, filename)
                arcname = path.relpath(file_path, start=pkg_base_name)
                zipf.write(file_path, arcname=arcname)
