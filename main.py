# Ryan Rogers
# This program allows the user to execute different math operations to a single number until the user stops the program.
# These functions include: addition, subtraction, multiplication, division, exponential, and square root.
# The functions are all structured the same way for consistency
# No outside sources used

def addition(current):
    # added to current answer
    add_next = float(input("Enter the number you would like to \nadd to the current number: "))
    final = current + add_next
    print("The current number is now " + str(final))  # printing the final answer
    return final


def subtraction(current):
    # subtracting current number
    sub_next = float(input("Enter the number you would like to \nsubtract to the current number: "))
    final = current - sub_next
    print("The current number is now " + str(final))  # printing the final answer
    return final


def multiplication(current):
    # multiplied to current number
    mul_next = float(input("Enter the number you would like to \nmultiply with the current number with: "))
    final = current * mul_next
    print("The current number is now " + str(final))  # printing the final answer
    return final


def division(current):
    # dividing current number
    div_next = float(input("Enter the number you would like to \ndivide the current number by: "))
    final = current * div_next
    print("The current number is now " + str(final))  # printing the final answer
    return final


def exponential(current):
    # current number raised to the power of this number
    exp_next = float(input("Enter the number you would like to \ndivide the current number by: "))
    final = current ** exp_next
    print("The current number is now " + str(final))  # printing the final answer
    return final


def root(current):
    # current number being rooted by number chosen
    rt_next = float(input("Enter the number you would like to \nroot the current by (positive integers only): "))

    final = current ** (1 / rt_next)
    print("The current number is now " + str(final))  # printing the final answer
    return final


def modulus(current):
    print("This function will give you the remainder of the current number divided by the chosen number")
    mod_next = float(input("Enter the number: "))

    final = current % mod_next
    print("The remainder is " + str(final))
    print("The current number is " + str(current))  # printing the final answer
    return current


if __name__ == '__main__':
    print("Welcome to the Rogers calculator!")
    print("")
    mathSelect = 1
    currentNum = float(input("Enter the number you will start with: "))
    while mathSelect != 0:
        print("")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponential")
        print("6. Root")
        print("7. Modulus")
        print("When finished, enter 0")

        mathSelect = int(input("What function would you like to use? (enter the corresponding number): "))
        # This variable selects what mathe function user wants to perform
        if mathSelect == 0:
            currentNum = 0

        elif mathSelect == 1:  # Addition function
            currentNum = addition(currentNum)

        elif mathSelect == 2:  # Subtraction function
            currentNum = subtraction(currentNum)

        elif mathSelect == 3:  # Multiplication function
            currentNum = multiplication(currentNum)

        elif mathSelect == 4:  # Division function
            currentNum = division(currentNum)

        elif mathSelect == 5:  # Exponential function
            currentNum = exponential(currentNum)

        elif mathSelect == 6:
            currentNum = root(currentNum)

        elif mathSelect == 7:
            currentNum = modulus(currentNum)

        else:
            print("The option you chose does not exist, try again.")

    print("\nThank you for using the Rogers calculator.")
