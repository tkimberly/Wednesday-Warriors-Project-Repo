import math
print("lets find the area and hypotenuse of your right triangle😊 ")
triangle_base=int(input("measurements of the triangle base:📩 "))
triangle_height=int(input("measurements of the triangle height:📩 "))
add_bh=triangle_base*2 + pow(triangle_height,2)
hypotenuse=round(math.sqrt(add_bh),3)
print("the hyposenuse of your triangle is: 🥁 ",hypotenuse)
area=round((triangle_base*triangle_height)/2,3)
print("the area of your triangle is: 🥁 ",area)