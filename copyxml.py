#!/usr/bin/env python
import xml.etree.ElementTree as ET
import pdb
import urllib2
import json
from Tkinter import Tk
# import ipdb

minecraft_version = '1.6.2'
bot_url = "http://bot.notenoughmods.com/%s.json" % minecraft_version


response = urllib2.urlopen(bot_url)
mod_list = json.loads(response.read())

def copy_to_clipboard(text):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.destroy()

def find_mod_version(mod_list, mod_name):
    for mod in mod_list:
        if mod['name'].lower() == mod_name.lower():
            return mod
    return None

tree = ET.parse('pack.xml')
root = tree.getroot()
for mod in root[2]:
    if mod.attrib['version'] == '':
        root[2].remove(mod)
    # current_version = find_mod_version(mod_list, mod.attrib['name'])

    # try:
    #     if current_version == None:
    #         current_version = {}
    #         current_version['version'] = "Unknown"
    #         current_version['longurl'] = "Unknown"
    #     if current_version['version'] == 'dev-only':
    #         if current_version['dev'] != mod.attrib['version'].replace('%s-' % minecraft_version, ''):
    #             contents += "<tr><td><a href=\"%s\">%s</a></td>" % (mod.attrib['website'], mod.attrib['name'])
    #             if current_version['longurl'] != "Unknown":
    #                 contents += "<td><a href=\"%s\">Update</a></td>" % current_version['longurl']
    #             else:
    #                 contents += "<td></td>"
    #             contents += "<td>%s</td><td>%s</td></tr>" % (mod.attrib['version'], current_version['dev'])
    #     else:
    #         if current_version['version'] != mod.attrib['version'].replace('%s-' % minecraft_version, ''):
    #             contents += "<tr><td><a href=\"%s\">%s</a></td>" % (mod.attrib['website'], mod.attrib['name'])
    #             if current_version['longurl'] != "Unknown":
    #                 contents += "<td><a href=\"%s\">Update</a></td>" % current_version['longurl']
    #             else:
    #                 contents += "<td></td>"
    #             contents += "<td>%s</td><td>%s</td></tr>" % (mod.attrib['version'], current_version['version'])
    # except:
    #     print(mod.attrib['name'])
copy_to_clipboard(ET.tostring(root))
