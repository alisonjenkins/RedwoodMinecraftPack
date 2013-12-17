#!/usr/bin/env python
import os
import os.path
import zipfile

configs_zip_name = 'Configs.zip'

script_dir = os.getcwd() #os.path.dirname(os.path.realpath(__file__))
exclude_files = ['idchecker.py', 'genconfigszip.py', 'blockids.py', 'biomeids.py', 'itemids.py', configs_zip_name]
exclude_dirs = ['options_gen']

dircontents = os.listdir(".")
# remove old configs zip
if os.path.exists(configs_zip_name):
    os.remove(configs_zip_name)

with zipfile.ZipFile('Configs.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
    for dirpath, dirnames, filenames in os.walk(script_dir):
        reldirpath = os.path.relpath(dirpath)
        if reldirpath not in exclude_dirs:
            for filename in filenames:
                if filename not in exclude_files:
                    filepath = os.path.join(reldirpath, filename)
                    print("Adding file: " + filepath)
                    
                    zip.write(filepath)
