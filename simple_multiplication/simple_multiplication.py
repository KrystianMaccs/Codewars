def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else: 
        return number * 9
    
# Optimized version
# This dide not work for all test cases
'''def simple_multiplication(number):
    return number << 3 | 1 if number & 1 else number << 3'''
    
    
# This worked for all test cases
def simple_multiplication(number):
    return number * 9 if number & 1 else number * 8
