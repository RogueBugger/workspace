



#used to map a value between certain range and normalize them between the zero and one
def translate(value, leftmin, leftmax, rightmin, rightmax):
    leftspan = leftmax - leftmin
    rightspan = rightmax - rightmin

    valueScaled = float(value - leftmin) / float(leftspan)
    return (rightmin + (valueScaled * rightspan))


def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y


#calling function
#         value to map,minstart, maxrange, starting and ending value
translate(9, 0, 3, 0, 1)