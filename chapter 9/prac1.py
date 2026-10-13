import re
# obj = re.compile(r'(\d{3})-(\d{3}-\d{4})')
# obj_match = obj.search('my phone number is 433-533-1234')
# obj_match.groups()
# print(obj_match.groups())
# area , road = obj_match.groups()
# print('area:'+ area)

# pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = pattern.search('My phone number is (415) 555-4242.')
# print(mo.group(1))

# print(mo.group(2))

# obj = re.compile(r'\$')
# searc = obj.search('here is the all special character () another one is $')
# print(searc.group())

#Matching Characters from Alternate Groups

# mod = re.compile(r'cat(ch|chnot|chho)')
# modd = mod.search('if you capalble catchno me and try to catchno also catchnot')
# print(modd)
# modd.group()
# print(modd.group())




# Returning All Matches


# pattern = re.compile(r'\d{3}-\d{3}-\d{4}')  
# find =pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(find)


# Qualifier Syntax: What Characters to Match
pat = re.compile(r'[^aeiouAEIOU]')
find =pat.findall('heywahtasuppitsmee')
print(find)


at = re.compile(r'.at')
new = at.findall('cat eat no fat no gat')
print(new)





pattern = re.compile(r'What\?')

print(pattern.search('What?'))
print(pattern.search('What'))


# pate = re.compile(r'(ha){3,5}')
# patee = pate.search("hahaha")
# print(patee.group())


lazy_pattern = re.compile(r'(Ha){3,5}?')
match2 = lazy_pattern.search('HaHaHaHaHa')
print(match2.group())

# substitude

import re

agent_pattern = re.compile(r'Agent \w+')

result = agent_pattern.sub(
    'CENSORED',
    'Agent Alice contacted Agent Bob.'
)

print(result)



