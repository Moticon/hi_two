print("Hello")

print('#### list #########')
names = ['pat', 'kate', 'josh', 'virginia', 'mom', 'dad']

for name in names:
    print(name)


import yaml
print("#########after import")
with open('example.yml', 'r') as yamlFile:
    data = yaml.safe_load(yamlFile)
user = data['user']

print(user['roles'])

role = user['location']
city = role['city']
for role in data['user']['roles']:
    print(role)

user['location']['city'] = 'Dallas2'
with open('modified_yaml.yml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)

#  JSON SECTION
########################
import json
with open('example.json', 'r') as file:
    data = json.load(file)
print('JSON STUFF+++++++++++++++++')
user2 = data['user']
print(user2['name'])

for role in user['roles']:
    print(role)

data['user']['location']['city'] = "Katmandu"
with open('editedJson.json', 'w') as jsonFile:
    json.dump(data, jsonFile, indent=4)
################################
# XML Example
print('XML#############')
import xml.etree.ElementTree as ET
with open('example.xml', 'r') as xmlFile:
    mytree = ET.parse(xmlFile)
    myRoot = mytree.getroot()

user = mytree.find('user')
print(user.find('name').text)

for role in user.findall('roles'):
    print(role.text)

user.find('location').find('city').text = "Ninevah"
with open('xmlChanged.xml', 'w') as outputFile:
    mytree.write(outputFile, encoding='unicode')

print('############\n more lists!! \n ##########')
famousPeople = ['ghandi', 'lincoln', 'reagan']
secretaries = ['millie', 'bob']
for leaders in famousPeople:
    print(leaders.title(), 'please come to dinner, even though you''dead!')
absent = famousPeople.pop(1)
print('Sorry,', absent,'can\'t make it')
famousPeople.insert(1,'Bush')
for leaders in famousPeople:
    for secretary in secretaries:
        print(leaders.title(), 'has secretary', secretary)
        print('-------------')

famousPeople.sort()
famousPeople.reverse()
print(f"{famousPeople}\n{secretaries}")

for value in range(1, 21):
    print(value)

bigList = range(1, 1000001)
print(bigList[0], bigList[-1], sum(bigList))

oddList = list(range(1, 20, 2))
print(oddList)

threes = list(value**3 for value in range(1, 11));

for number in threes:
    print(number)

from dice import sum_of_dice
print('########## DICE ###########')
threeD8 = sum_of_dice(8, 3)
print(f"You rolled {threeD8} on three 8-sided dice.")

print('############ class instantiaion ############')
from device import Device
dev1 = Device('Router')
dev2 = Device('Switch')
print(f"Device 1 name: {dev1.hostname}, Message: {dev1.motd}")
print(dev1.show('hostname'))

print('########### using while with dictionary ##############')
playerChoices = {}

keepOn = True

while keepOn:
    name = input("Enter your name ")
    classOfPC = input("Enter your class ")

    playerChoices[name] = classOfPC

    keepOn = (input("Keep Going? (enter y to go on) ") == 'y')

print(playerChoices)
