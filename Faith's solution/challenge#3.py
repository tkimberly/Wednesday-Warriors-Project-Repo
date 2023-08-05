
print("welcome to the temparature conversion app😎")
fah_input=float(input("your tempature in degree fahrenheit is: "))# data type to be converted first before input value
print("temparature in degree fahrenheit:😀\t",fah_input)#use a comma to separate string and variable
celsius_convert=round(fah_input*-17.222,4)
kelvin_convert=round(fah_input*255.928,4)
print("temparature in kelvin:🙂\t \t\t",kelvin_convert)# there is better way of writing a table
print("temparature in celsius:👌\t\t \t",celsius_convert)#\t- is used as a tab in python