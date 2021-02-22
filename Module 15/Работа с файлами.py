heatWaves = open('HeatWaves.txt', 'r')
print(heatWaves.read(13))
print(heatWaves.read(5))
print(heatWaves.readline())
print(heatWaves.readlines())
print()

myFile = open('name_file.txt', 'w')
myFile.write('"Write" method without new line\n')
print('"Print" function with new line on the end of this string\n', file=myFile)
myFile.flush()
myFile.close()

with open('name_file.txt', 'a') as myFile:
    myFile.write('You can open file with construction "with open("file.txt", "rt") as \'Value\'".'
                 'It will close by itself.')


def change_char(text, n=1):
    alpha = 'abcdefghijklmnoprstuvwxyz'
    alpha_up = alpha.upper()
    summary = ''
    for char in text:
        if char in alpha:
            summary += alpha[(alpha.index(char) + n) % len(alpha)]
        elif char in alpha_up:
            summary += alpha_up[(alpha_up.index(char) + n) % len(alpha)]
        else:
            summary += char
    return summary


with open('name_file.txt', 'r') as inputFile:
    with open('output_file.txt', 'w') as outputFile:
        outputFile.write(change_char(inputFile.read()))


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

jFile = open('jFile.json', 'w', encoding='utf8')              # json.dump(value, inFile, ensure_ascii=False, indent=4)
json.dump(dictionary, jFile, ensure_ascii=False, indent=4)    # like .write but in translate for JSON-code
jFile.close()

jFile = open('jFile.json', encoding='utf8')            # json.load(value) like .read but with translation on JSON-code
print('That"s what Json file look like in Python:')
print(json.load(jFile))
jFile.close()

with open('jFile.json', 'a') as jFile:
    stringInPython = r"True, False, None"
    print(stringInPython, 'before .dumps method')
    jFile.write(stringInPython)
    stringInJson = json.dumps(stringInPython)
    print(stringInJson, 'after .dumps method')
    jFile.write(stringInJson)
    stringInPythonAgain = json.loads(stringInJson)
    print(stringInPythonAgain, 'after .loads method')
    jFile.write(stringInPythonAgain)
