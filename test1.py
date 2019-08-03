"""
Write a program that prints the numbers from 1 to 100 (included). 
But for multiples of 3 print “Fizz” instead of the number 
and for the multiples of  5 print “Buzz”. 
For numbers which are multiples of both  3 and  5 print “FizzBuzz”.
"""

start = 1
end = 101

def is_multiple_3(number):
    return number % 3 == 0

def is_multiple_5(number):
    return number % 5 == 0

def main():
    for i in range(start, end):
        result = "{0}".format(i)
        if is_multiple_3(i) and is_multiple_5(i):
            result = "{0}: FizzBuzz".format(result)
        elif is_multiple_3(i):
            result = "{0}: Fizz".format(result)
        elif is_multiple_5(i):
            result = "{0}: Buzz".format(result)
        
        print(result)

if __name__ == '__main__':
    main()
    
    