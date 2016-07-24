import re

phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_number_regex.search('My number is 415-813-1234.')
print('mo.group(1) : ' + mo.group(1))
print('mo.group(2) : ' + mo.group(2))
print('mo.group() : ' + mo.group())
print('mo.groups() : ' + mo.groups())