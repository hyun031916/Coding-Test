import re
p = re.compile('[a-z]+')
m = p.match('python')
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

#search
p = re.compile('[a-z]+')
m = p.search('3 python')
print(m)

#findall
p = re.compile('[a-z]+')
m = p.findall('3 python')
print(m)

#finditer
p = re.compile('[a-z]+')
m = p.finditer('3 python')
print(m)

#DOTALL, S
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

# Ignorecase, I
p = re.compile('[a-z]', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))

#Multiline, M
p = re.compile("^python\s\w+", re.M)
data = """
python one
life is too short
python two
you need python
python tree
"""
print(p.findall(data))