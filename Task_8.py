width = 104.32
height = 15.654
area = width * height
message = f"The area of a rectangle with a width of {width} and a height of {height} is {area:.2f}."
print(message)



width = 104.32
height = 15.654
area = width * height
message = f"The area of a rectangle with a width of {width} and a height of {height} is {area:.3f}."
print(message)



name1 = "Isaac"
age1 = 25

name2 = "Afrifa"
age2 = 30

print(f"{name1:15} - {age1:10}")
print(f"{name2:15} - {age2:10}")



name = "Isaac Afrifa"
age = 100
print(f"{name: >20} - ${age: >20.2f}")



r = 52
area = 3.14159 * r**2
output = "A circle with radius {} has an area of {:.13f}".format(r, area)
print(output)



name = "Isaac"
age = 100
output = "{name:@^15} - {age:#^10}".format(name=name, age=age)
print(output)
