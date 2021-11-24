print('Welcome to the Bank! Please enter your names below!')
names = []

while len(names)< 10:
    acceptedName=input("Enter your name here: ")
    names.append(acceptedName)
while len(names)> 0:
    print(names.pop(0))
