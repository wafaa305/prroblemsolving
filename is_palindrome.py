'''Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
The linke for this question in leetcode: https://leetcode.com/problems/palindrome-number/
'''
'''This function is used to reverse a giving number'''
def reverse_number(number):
    reversed_number = 0
    while (number > 0):
        reversed_number = reversed_number*10 + number%10
        number = int(number/10)
    return reversed_number

'''This function takes the numberand its inverse as input and make sure that the number is palindrome pr not ...'''
def is_palindrome(number,reversed_number):
    if number == reversed_number:
        print(str(number) + " is palindrome.")
    else:
        print(str(number) + " is not palindrome.")


number = int("Please enter a number to check if its Palindrome or not: "+input()) #This line used to inform user to enter a number that wants to check if its palindrome or note
reversed_number = reverse_number(number)
is_palindrome(number,reversed_number)
