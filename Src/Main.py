#Try Fizz Buzz

"""Try the following: You must write a program that prints the numbers from 1 to 100, but with these conditions:
If the number is a multiple of 3, instead of the number you should print Fizz.
If the number is a multiple of 5, you must print Buzz.
If the number is a multiple of 3 and 5 at a time, you must print FizzBuzz.
If you don't meet any of those conditions, simply print out the number."""

ValuesFizz = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96]
ValuesBuzz = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
ValuesFizzBuzz = [15, 30, 45, 60, 75, 90]

for i in range(1, 101):
    if i in ValuesFizzBuzz:
        print("FizzBuzz")
    elif i in ValuesFizz:
        print("Fizz")
    elif i in ValuesBuzz:
        print("Buzz")
    else:
        print(i)