import argparse
import json
import os
import sys
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

parser = argparse.ArgumentParser()
parser.add_argument('--key', default=None)
parser.add_argument('--val', default=None)
name_key = parser.parse_args(sys.argv[1:])

dict_q = dict()
if os.path.exists(storage_path):
    with open(storage_path, 'r') as f:
        dict_q = json.load(f)

if name_key.key is not None and name_key.val is None:
    if name_key.key in dict_q:
        print(", ".join(dict_q[name_key.key]))
    else:
        print(None)
elif name_key.key is not None and name_key.val is not None:
    if name_key.key in dict_q:
        dict_q[name_key.key].append(name_key.val)
    else:
        dict_q.setdefault(name_key.key, [name_key.val, ])
else:
    print("")

with open(storage_path, "w") as fp:
    fp.write(json.dumps(dict_q))
