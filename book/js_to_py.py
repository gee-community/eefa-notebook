import os
from geemap.conversion import *

# Clone the repository
# git clone https://earthengine.googlesource.com/projects/gee-edu/book

# Add .js file extension to all files in a directory
# find . -type f ! -name "*.*" -exec mv {} {}.js \;


out_dir = os.getcwd()
js_dir = out_dir
js_to_python_dir(in_dir=js_dir, out_dir=out_dir, use_qgis=False, import_geemap=True)
py_to_ipynb_dir(js_dir)

# Remove _geemap suffix from all files in a directory
# find . -type f -name '*_geemap*' -exec sh -c 'mv "$1" "${1//_geemap/}"' _ {} \;
