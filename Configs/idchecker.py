#!/usr/bin/env python
import re
import os
import pdb

configs_dir = 'config'
id_files = {}

idre = re.compile(r'(?P<id>\d+)', re.I|re.DOTALL)
# item_line_re = re.compile(r'I:(?P<itemname>.+?)=(?P<itemid>\d+)')

# add hack for advancedmachine block for config\AdvancedMachines.cfg 
# add hack to search for config\EnderStorage.cfg (block.id=251)


if os.path.exists(configs_dir):
    for dirpath, dirnames, filenames in os.walk(configs_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath,filename)
            with open(file_path, 'r') as conf_file:
                file_contents = conf_file.read()

            match = idre.search(file_contents)
            if match:
                # print(file_path)
                id_files[file_path] = {}
                for match in idre.finditer(match.group('id')):
                    id_files[file_path][match.group('id')] = match.group('id')
            else:
                pass


# pdb.set_trace()
# check for conflicts
ids = {}
for mid in range(1,31999):
    mid = str(mid)
    ids[mid] = []
    for id_file in id_files.keys():
        if mid in id_files[id_file].keys():
            ids[mid].append([id_file,id_files[id_file][mid]])

    if len(ids[mid]) > 1:
        filelist = ""
        for file_name in ids[mid]:
            filelist += "%s, " % file_name
        print("id %s conflict between %s" % (mid, filelist))
