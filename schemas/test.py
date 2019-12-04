from jsonschema import validate
import json

s = json.load(open('observation.schema.json'))

j = {
    'observer': 'foo',
    'method': 'bar',
    'items': []
}

validate(instance=j, schema=s)
