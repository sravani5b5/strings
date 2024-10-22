"""
1) Write a program to get a string value and print the same as output:
Sample Input:
Hello World
Sample Output:
Hello World
"""
a="Hello World"
print(a)

"""
2) Write a program to print th length of the given string.
Sample Input:
Hello
Sample Output:
Hello: 5
"""
a=input()
b=len(a)
print(f"{a}:{b}")



""""
3) There are 50 students in the class. The teacher wants to arrange them in the height order. So help the teacher to find the smallest person and tallest to arrange.(count the number of lowercase letters and uppercase letters in a string.)
Problem Description:
The program takes a string and counts the number of lowercase letters and uppercase letters in the string.
Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize the two count variables to 0.
3. Use a for loop to traverse through the characters in the string and increment the first count variable each time a lowercase character is encountered and increment the second count variable each time a uppercase character is encountered.
4. Print the total count of both the variables.
5. Exit.
Input & Output Format:
Input consists of one string.
Output consists of two integers.
First output consists of count of the uppercase.
Second output consists of count of the lowercase.
Sample Input:
Cyfuno
Sample Output:
Uppercase: 1
Lowercase: 5
""""

