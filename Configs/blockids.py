#!/usr/bin/env python
import re
import os
import pdb

configs_dir = 'config'
block_files = {}

block_re = re.compile(r'(\")?(terrain )?block( )?(ids)?(\")?( )?\{(?P<blocksids>.+?)\}', re.I|re.DOTALL)
block_line_re = re.compile(r'I:(?P<blockname>.+?)=(?P<blockid>\d+)')

# add hack for advancedmachine block for config\AdvancedMachines.cfg 
# add hack to search for config\EnderStorage.cfg (block.id=251)


if os.path.exists(configs_dir):
    for dirpath, dirnames, filenames in os.walk(configs_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath,filename)
            with open(file_path, 'r') as conf_file:
                file_contents = conf_file.read()

            match = block_re.search(file_contents)
            if match:
                block_files[file_path] = {}
                for match in block_line_re.finditer(match.group('blocksids')):
                    block_files[file_path][match.group('blockid')] = match.group('blockname')
            else:
                # print(file_path)
                pass


# pdb.set_trace()
# check for conflicts
ids = {}
for blockid in range(23,4096):
    blockid = str(blockid)
    ids[blockid] = []
    for block_file in block_files.keys():
        if blockid in block_files[block_file].keys():
            ids[blockid].append([block_file,block_files[block_file][blockid]])

    if len(ids[blockid]) > 1:
        filelist = ""
        for file_name in ids[blockid]:
            filelist += "%s, " % file_name
        print("Block id %s conflict between %s" % (blockid, filelist))
    
    if len(ids[blockid]) == 0:
        print("%s free" % blockid)

