num = ""
tryAgain = ""

while True:
    try:
        num = int(input("Please enter a number: "))
        break
    except ValueError:
        # Handle the exception
        print('Please enter an integer')
        
def hailstone(num):
    if (num == 1):
        print("The number has reached 1, and therefore follows the Hailstone Sequence.")
        tryAgain = input("Try again? (Y/N): ")
        if (tryAgain == "Y" or tryAgain == "y"):
            while True:
                try:
                    num = int(input("Please enter a number: "))
                    break
                except ValueError:
                    # Handle the exception
                    print('Please enter an integer')
            
            hailstone(num)
        else:
            SystemExit
    else:
        if (num%2 == 0):
            num = num/2
            print(num)
            hailstone(num)
        elif (num%2 != 0):
            num = (num*3) + 1
            print(num)
            hailstone(num)
        else:
            print("Number invalid. Please try again.\n")

print(hailstone(num))
