print("Welcome to the Miles Per Hour Conversion App \n") #display the welcome message
speed_mph = float(input("Please enter your speed in miles per hour: ")) #user to input a float value in miles per hour
mps_conversion = float(0.4474) #variable name for meters per second conversion
speed_mps = round((speed_mph * mps_conversion), 2) #converting miles per hour to meters per second and round it off to two decimal places
print("Your speed in meters per second is: ", speed_mps) #display message of the conversion