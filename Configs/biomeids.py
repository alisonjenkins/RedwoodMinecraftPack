#!/usr/bin/env python
import re
import os
import pdb

configs_dir = 'config'
biome_files = {}

# biome_re = re.compile('biome\w+?{(?P<biomeids>.+?)}', re.DOTALL)
biome_re = re.compile(r'(\")?biome (ids\" )?\{(?P<biomesids>.+?)\}', re.DOTALL)
biome_line_re = re.compile(r'I:(?P<biomename>.+?)=(?P<biomeid>\d+)')


if os.path.exists(configs_dir):
    for dirpath, dirnames, filenames in os.walk(configs_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath,filename)
            # file_path = 'config/extrabiomes/extrabiomes.cfg'
            # file_path = 'config/BiomesOPlenty.cfg'
            # file_path = 'config/TwilightForest.cfg'
            with open(file_path, 'r') as conf_file:
                file_contents = conf_file.read()

            # print('Checking: %s' % file_path)
            match = biome_re.search(file_contents)
            if match:
                biome_files[file_path] = {}
                # print(file_path)
                for match in biome_line_re.finditer(match.group('biomesids')):
                    biome_files[file_path][match.group('biomeid')] = match.group('biomename')


# pdb.set_trace()
# check for conflicts
ids = {}
for biomeid in range(23,256):
    biomeid = str(biomeid)
    ids[biomeid] = []
    for biome_file in biome_files.keys():
        if biomeid in biome_files[biome_file].keys():
            ids[biomeid].append([biome_file,biome_files[biome_file][biomeid]])

    if len(ids[biomeid]) > 1:
        filelist = ""
        for file_name in ids[biomeid]:
            filelist += "%s, " % file_name
        print("Biome id %s conflict between %s" % (biomeid, filelist))
    
    if len(ids[biomeid]) == 0:
        print("%s free" % biomeid)

