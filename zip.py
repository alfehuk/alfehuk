import os
import zipfile

base_folder = os.path.dirname(os.path.abspath(__file__))
steve_folder = os.path.join(base_folder, "steve")
zip_path = os.path.join(base_folder, "steve.zip")

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
    for root, dirs, files in os.walk(steve_folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, steve_folder)
            zip_file.write(full_path, relative_path)

print("ZIP created")