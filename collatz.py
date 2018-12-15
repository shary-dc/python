def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        oddNumber = 3 * number + 1
        print(oddNumber)
        return(oddNumber)

while True:
    try:
        inputNumber = int(input("Enter number: "))
    except ValueError:
        print("Error: Please enter an integer.")
    else:
        inputNumber = collatz(inputNumber)

    

    
