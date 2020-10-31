import json
import os
import tinydb
from tinydb import Query, where

db = tinydb.TinyDB('sauvegardes/db.json')

admin_confs = db.table('admin_confs')
works = db.table('works')

# Demo
"""
db.insert({'var_name': 'default_admin_conf', 'value': 'example'})
admin_confs.insert({'name': 'example', 'data': 'data'})
"""

default_conf_name = db.search(tinydb.Query().var_name == 'default_admin_conf')[0]['value']


def get_default_conf():
    return default_conf


print(default_conf_name)

q_conf = Query()

default_conf = admin_confs.search(where('name') == default_conf_name)[0].get('data')

print(default_conf)
