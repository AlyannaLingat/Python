"""
Exercise 1: Calculate the multiplication and sum of two numbers
Given two integer numbers return their product only if the product is 
equal to or lower than 1000, else return their sum. 
"""
"""
1. Create a fuction that will take two numbers as parameters
2. Inside a function, multiply two numbers and save their product in a product variable
3. Next, use the if condition to check if the product >1000. If yes, return the product
4. Otherwise, use the else block to calculate the sum of two numbers and return it.
"""
"""
def numbers (num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else: 
        return num1 + num2

result = numbers (20,30)
print("THE RESULTS IS", + result)
"""

"""
Exercise 2: Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers and in each iteration, 
print the sum of the current and previous number.
"""
"""
Create a variable called previous_num and assign it to 0
Iterate the first 10 numbers one by one using for loop and range() function
display the current number (i), previous number, and the addition of both numbers in each iteration of the loop. 
At last, change the value previous number to current number ( previous_num = i).
"""
"""
print("Printing Current and Previous Number Sum in a Range (10)")
previous_num = 0
# for loop from 1-10
for i in range (1, 11):
    x_sum = previous_num + i
    print("Current Number", i ,"Previous Number", previous_num, "Sum: ", previous_num + i)
    #modify previous number
    #set it to the current number
    previous_num = i
"""
"""
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string 
from the user and display characters that are present at an even index number.
For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""
print("Original String is")
print("Printing only even index chars")
str = input("Enter a String: ")
