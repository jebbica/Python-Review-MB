# Jessica Lin
'''
1.
Create Input Variables for your first name, last name and age.
Then print out your full name and age within a sentence -> My name is Hunter Macias & 
I am 20 years old
'''
# first_name = input("What is your first name? ")
# last_name = input("What's your last name? ")
# age = input("Enter your age. ")
# print(f"My name is {first_name} {last_name} & I am {age} years old.")

'''
2. 
create 3 different variables with any whole number assined as the value and convert them into a string using the str() constructor.
once you convert them print out the variables. Example: convert 3 to '3'
if you use print(type(<var_name>)) this will print out the type of variable for example x = 3 would print 'int' and x = '3' would print 'str'
'''
# num1 = str(3243)
# num2 = str(4849)
# num3 = str(42069)

# print(num1, type(num1))
# print(num2)
# print(num3)

'''
3.
Write a program that asks the user for the current temperature (F) and then use their Input calculate temperature in (C). 
Here is the formula to conver F to C => C = (Fahrenheit - 32) * 5.0/9.0
Once you calculate Celcius print out the conversion to the user
'''
# current_temp = int(input("What is the current temperature in faren-i-cant-spell-this-heit? "))
# celcius = (current_temp - 32) * 5.0/9.0
# print(f"The Celcius temperature (who even like C) is {celcius} degrees. ")

'''
4a.
Hint: You can solve this problem without a forloop, but if you can figure it out using a for loop try to do it that way
Write a program that asks the user to input how much money they have saved up. 
Then ask the user to input a monthly growth rate (%) example: 5% would mean their savings would increase by 5% monthly. 
Calculate how much the user would have at the end of each month for 12 months & print it all to the user
Example: 
savings = 100
growth_rate = 5%

End of Januaray = $105
End of February = 110.25
End of March = $115.76...
End of Decemeber...
'''
savings = int(input("How many money in da bank? "))
growth_rate = int(input("What da growth rate be? "))
months = ['Janurary', 'February', 'March', 'April', 'May','June','July','August','September','October','November','December']
for x in months:
    savings = savings * (1+(growth_rate/100))
    print(f"End of {x} = ${savings}")