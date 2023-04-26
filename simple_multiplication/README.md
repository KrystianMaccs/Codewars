This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.


# Optimised Solution
```The given code appears to be a simple implementation of a function that multiplies an input number by 8 if it is even and by 9 if it is odd. While this code is correct and functional, it may be possible to optimize it in a few ways. Here are a few suggestions:

Use a bitwise operator instead of modulus: Instead of using the modulus operator (%) to check whether the input number is even or odd, you can use a bitwise operator (&). Specifically, the expression number & 1 will evaluate to 1 if number is odd and 0 otherwise. Using this expression can make the code slightly faster and more concise:


def simple_multiplication(number):
    if number & 1:
        return number * 9
    else:
        return number * 8
Use a ternary operator instead of an if statement: Instead of using an if statement to determine which multiplication factor to use, you can use a ternary operator to make the code more concise:
```
def simple_multiplication(number):
    return number * 9 if number & 1 else number * 8

This code is functionally equivalent to the original implementation, but it uses a single line of code instead of two.

Use integer literals instead of multiplication: Instead of performing a multiplication operation, you can use integer literals to achieve the same result. Specifically, you can use the expressions number << 3 and number << 3 | 1 to multiply an even or odd number by 8 or 9, respectively. This can make the code slightly faster, especially for large input numbers:

def simple_multiplication(number):
    return number << 3 | 1 if number & 1 else number << 3

This code uses bitwise shifting (<<) to multiply the input number by 8, and the | operator to add 1 to the result if the input number is odd.

Overall, these optimizations are relatively minor and may not be necessary for small input numbers or in cases where performance is not critical. However, they can help to make the code faster, more concise, and more readable in certain situations.