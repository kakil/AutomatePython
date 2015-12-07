import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 at my office number.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())
