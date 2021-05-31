import re

def passwordCheck(pwd):

    if len(pwd) < 8 or len(pwd) > 21 and not re.findall('[0-9]+', pwd) \
        and not re.findall('[a-z]', pwd) or not re.findall('[A-Z]', pwd):
        return False
    elif not re.findall('[`~!@#$%^&*(),<.>/?]+', pwd):
        return False
    return True


def checkEmail(emails):
    check = [len(emails)]
    for i in range(len(emails)):
        if re.findall('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', emails[i]):
            check[i] = True
        else: check[i] = False
    return check

emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
          'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
          'python.dojang@e-xample.com',                                    # 올바른 형식
          '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식
print(checkEmail(emails))
pwd = 'zfadQ123!'
print(passwordCheck(pwd))