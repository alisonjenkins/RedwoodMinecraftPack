#!/usr/bin/env python
import re
import os
import pdb

configs_dir = 'config'
item_files = {}

item_re = re.compile(r'(\")?item( )?(ids)?(\")?( )?\{(?P<itemids>.+?)\}', re.I|re.DOTALL)
item_line_re = re.compile(r'I:(?P<itemname>.+?)=(?P<itemid>\d+)')

# add hack for advancedmachine block for config\AdvancedMachines.cfg 
# add hack to search for config\EnderStorage.cfg (block.id=251)


if os.path.exists(configs_dir):
    for dirpath, dirnames, filenames in os.walk(configs_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath,filename)
            with open(file_path, 'r') as conf_file:
                file_contents = conf_file.read()

            match = item_re.search(file_contents)
            if match:
                print(file_path)
                item_files[file_path] = {}
                for match in item_line_re.finditer(match.group('itemids')):
                    item_files[file_path][match.group('itemid')] = match.group('itemname')
            else:
                # print(file_path)
                pass


# pdb.set_trace()
# check for conflicts
ids = {}
for itemid in range(4097,31999):
    itemid = str(itemid)
    ids[itemid] = []
    for item_file in item_files.keys():
        if itemid in item_files[item_file].keys():
            ids[itemid].append([item_file,item_files[item_file][itemid]])

    if len(ids[itemid]) > 1:
        filelist = ""
        for file_name in ids[itemid]:
            filelist += "%s, " % file_name
        print("item id %s conflict between %s" % (itemid, filelist))
    
    # if len(ids[itemid]) == 0:
    #     print("%s free" % itemid)

