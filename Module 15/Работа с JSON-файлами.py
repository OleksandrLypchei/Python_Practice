import json

# If we have dict, that we have to write in JSON file, we can use module "json".
# Look at 'isAlive' and 'spouse' params.

dictionary = {
    'firstname': 'Коля',
    'lastname': 'Петренко',
    'isAlive': True,
    'age': 19,
    'address':
    {
        'region': 'Киевская обл.',
        'city': 'Белая Церковь',
        'street': 'ул. Набережна 42',
        'postal': ''
    },
    'phoneNumbers':
    [
        {
            'type': 'mob',
            'number': '033355523'
        },
        {
            'type': 'office',
            'number': '031652654'
        }
    ],
    'children': [],
    'spouse' : None
}

with open('jFile.json', 'w', encoding='utf8') as jFile:         # json.dump(value, inFile, ensure_ascii=False, indent=4)
    json.dump(dictionary, jFile, ensure_ascii=False, indent=4)  # like .write but in translate for JSON-code

with open('jFile.json', 'r', encoding='utf8') as jFile:  # json.load(value) like .read but with translation on JSON-code
    print(json.load(jFile))
print()


stringInPython = r"True\False\None"
print(stringInPython, 'before .dumps method')

stringInJson = json.dumps(stringInPython)
print(stringInJson, 'after .dumps method')

stringInPythonAgain = json.loads(stringInJson)
print(stringInPythonAgain, 'after .loads method')
