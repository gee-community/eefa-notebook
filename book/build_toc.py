import os
import geemap

input_dir = os.getcwd()
files = geemap.find_files(input_dir, ext=".ipynb", fullpath=True)
files = [file.replace(f"{input_dir}/docs/", "") for file in files]
files.sort()

fundamentals = []
applications = []

for file in files:
    if file.startswith("book/Part F"):
        fundamentals.append(file)
    elif file.startswith("book/Part A"):
        applications.append(file)

files = fundamentals + applications

sections = []
toc = []

for file in files:
    if file.startswith("book/Part"):
        section = file.split("/")[2]
        if section not in sections:
            sections.append(section)
            toc.append(f"  - {section}:\n")
            print(f"    - {section}:")
        print(f"      - {file}")
        toc.append(f"      - {file}\n")

print(sections)

with open("_toc.yml", "w") as f:
    f.writelines(toc)
