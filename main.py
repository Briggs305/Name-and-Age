#Welcome. This is a simple program that will ask
#the user for  her name , ask for age and tell her age next year.

#Type name
myName = input()
if myName == "Ampofoa":
    print('hello' + (myName))
#if name is not Ampofoa
elif myName != "Ampofoa":
    #End Program
    print('Name not found, Please try again')

#ask of her age
a = input ('How old are you?')
b = int(a) + 1
#Her age next year
print('You will be ' + str (b) + ' next year')

#Close program
print('Happy Birthday in Advance! ')