#Variables
temp = 0
#Asking for user input
temp = int(input('Please enter the current temperature: '))
#While loop used to indicate words to print when a certain temp is inputted.
while temp != 999:

    if temp >= 90:
        print('Wear Shorts')

    elif temp >= 70:
        print('Short sleeves are fine')

    elif temp >= 50:
            print('Wear a jacket')

    elif temp >= 32:
                print('Wear a heavy coat')

    elif temp < 32:
                print('Stay Inside')

    temp = int(input('Please enter the current temperature: '))

   
               
               




    
