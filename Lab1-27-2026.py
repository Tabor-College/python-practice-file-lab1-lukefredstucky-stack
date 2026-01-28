import math

'''
for eachpass in range(7):
    print("live", end="")

for count in range(6):
    print(count)

list (range(6))
list(vary(1,5))

for count in range(1,4):
    print(count)
'''


radius = float(input("what is the radius of the circle: "))
area = (math.pi)*radius**2
print(f"the area of the circle is {area}")
radius = math.sqrt(area/math.pi)
print(radius)
n = 0
if n > 90:
    grade =  "A"
elif n > 80:
    grade =  "B"
elif n > 70:
    grade =  "C"
elif n > 60:
    grade =  "D"
else:
    grade =  "F"




