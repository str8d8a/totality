import json
import os
import requests

schemas_dir = 'schemas'
root_schema = 'observation.schema.json'

def load_file(fn):
    with open(fn) as fd:
        s = json.load(fd)
        return s

def resolve(uri, cur):
    """Resolve a reference, assuming a relative local path if not a http url"""
    parts = uri.split('#')
    base = parts[0]
    if len(parts) == 1:
        frag = ''
    else:
        frag = parts[1]
        
    if base == '':
        # relative to current file
        s = cur
        new = cur
    else:
        if base.startswith('http'):
            resp = requests.get(base)
            s = resp.json()
        else:
            s = load_file(base)

        new = s
    
    for p in frag.split('/'):
        if p == '':
            continue
        s = s[p]
    return s, new

def expand(s, p):
    """Recursively expand a schema, by checking for `$id` keys and resolving them. 
    Will totally not handle circular references!!"""
    if isinstance(s, dict):
        for k, v in list(s.items()):
            if k == '$ref':
                # print(f"[{k}] => [{v}]")
                r, p = resolve(v, p)
                del s[k]
                s.update(r)
                expand(r, p)
            else:
                expand(v, p)
    elif isinstance(s, list):
        for it in s:
            expand(it, p)
    else:
        return

os.chdir(schemas_dir)
schema = load_file(root_schema)
expand(schema, schema)
print(json.dumps(schema, indent=2))
