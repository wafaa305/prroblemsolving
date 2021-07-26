'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
The linke for this question in leetcode: https://leetcode.com/problems/reverse-integer/
'''
'''This function is used to reverse a giving number'''
def reverse_number(number):
    reversed_number = 0
    sign = 1

    #This piece of code takes the absolute value of the number and stores its sign
    if number < 0:
        sign *= -1
        number = abs(number)

    #This piece of code reverses the given number (always takes a positive number)
    while (number > 0):
        reversed_number = reversed_number*10 + number%10
        number = int(number/10)

    reversed_number *= sign #This line to inherit the sign to the reversed number from the original number
    return reversed_number

'''This function takes the user number as input and is used to ensure that the given number is in the range [-2^31, 2^31 - 1]'''
def is_valid_number(number):
    if number>=-2147483648  and number<=2147483647:
        return True
    else:
        return False

''' This is the main fnction in our program which takes the user number as input and passes it to
other function to make the disered operation on it to rever it 
'''
def main_process(number):
    is_valid = is_valid_number(number) #Check if the number in the range [-2^31, 2^31 - 1] or not
    if is_valid == True:
        reversed_number = reverse_number(number) #Revere the number if it is in the range [-2^31, 2^31 - 1]
        is_valid = is_valid_number(reversed_number) #This check if reversed number is in the range [-2^31, 2^31 - 1] or not
        if is_valid == True:
            print("The inverse of " + str(number) + " is: " + str(reversed_number))
        else:
            print("The inverse result of the given number is out of range!")
    else:
        print("The number entered is out of range!")


number = int(input("Please enter a number to reverse it: ")) #This line used to inform user to enter a number that wants to reverse it
main_process(number) #calling the main function in our program


