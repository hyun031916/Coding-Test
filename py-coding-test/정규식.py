import re
p = re.compile('[a-z]+')
m = p.match('python')
print(m)

#search
p = re.compile('[a-z]+')
m = p.match('3 python')
print(m)

#findall
p = re.compile('[a-z]+')
m = p.findall('python')
print(m)

#finditer
p = re.compile('[a-z]+')
m = p.finditer('python')
print(m)