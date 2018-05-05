#!/usr/bin/python3
# Finding Patterns of Text Without Regular Expressions
# ref: 1. http://automatetheboringstuff.com/chapter7/
#      2. https://github.com/iliyahoo/Automate-The-Boring-Stuff-With-Python

import sys, re

number = '311-335-4433' # the default format of a phone number

def isPhoneText(text):
    if len(text) !=12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


def isPhoneNumber(number):
    num = []
    number = number.split('-')
    for i in range(len(number)):
        if not number[i].isdigit():
            sys.exit()
        elif i < 2 and len(number[i]) == 3:
            num.append(number[i])
            continue
        elif i == 2 and len(number[i]) == 4:
            num.append(number[i])
            continue
        else:
            sys.exit()
    return '-'.join(num)

print(isPhoneText(number))
print(isPhoneNumber(number))

number = 'fsfddsf 311-335-4433 fwfgeg 311-335-44354'


pattern = re.compile(r'\s\d{3}-\d{3}-\d{4}\s')
print(pattern)
result = re.findall(pattern, number)
for i in result:
    print (i.strip())
