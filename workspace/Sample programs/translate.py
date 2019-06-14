import math



def translate(value, leftmin, leftmax, rightmin, rightmax):
    leftspan = leftmax - leftmin
    rightspan = rightmax - rightmin

    valueScaled = float(value - leftmin) / float(leftspan)
    return (rightmin + (valueScaled * rightspan))



print(math.ceil((translate(10, 0, 100, 0, 1)*100)))
import random
for _ in range(10):
    print(math.floor(random.random()*10))
lo=""
l = ['g','s','h','w']
print(lo.join(l))