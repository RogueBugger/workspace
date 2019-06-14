import os

text = 'asdf'
text = open('/home/naruto/google competition/google competiton/sample programs/text.txt', "r")
final = []
text = text.readlines()
for i in text:
    l = list(map(str, i))
    b = []
    if '(' in l or ')' in l or '[' in l or ']' in l or True in [e.isdigit() for e in l] :
        for k in l:
            if k is '(' or k is')' or  k is'[' or k is ']' or k.isdigit():
                b.append(' ')
            else:
                b.append(k)
        final.append("".join(b))
    else:
        final.append(i)
final = [f"{i} " for i in final]
destination = open('/home/naruto/google competition/google competiton/sample programs/text.txt', 'w')
destination.write("".join(final))
