from math import factorial

pas="afasttdfsdfh"

for i in range(factorial(len(pas))):
    if chr(i) == pas:
        print('found')
    else:
        print(i)