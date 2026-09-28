# Maincrafts Technology - Python Programming Internship
# Task 1: Core Python Challenges
#
# This single file contains solutions for all 8 tasks.

# 1. Sum of Two Numbers
def sum_of_two_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum =", a + b)


# 2. Odd or Even Checker
def odd_or_even():
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


# 3. Factorial Calculation
def factorial():
    num = int(input("Enter a non-negative integer: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
        return

    result = 1

    for i in range(1, num + 1):
        result *= i

    print(f"{num}! =", result)


# 4. Fibonacci Sequence
def fibonacci():
    n = int(input("How many Fibonacci numbers do you want? "))

    if n <= 0:
        print("Please enter a positive number.")
        return

    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:", sequence)


# 5. String Reverse
def string_reverse():
    text = input("Enter a string: ")
    print("Reversed string:", text[::-1])


# 6. Palindrome Check
def palindrome_check():
    text = input("Enter a word or string: ")

    # Ignore spaces, punctuation, and letter case
    cleaned = "".join(char.lower() for char in text if char.isalnum())

    if cleaned == cleaned[::-1]:
        print("It is a Palindrome.")
    else:
        print("It is not a Palindrome.")


# 7. Leap Year Check
def leap_year_check():
    year = int(input("Enter a year: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a Leap Year.")
    else:
        print(year, "is not a Leap Year.")


# 8. Armstrong Number
# Example: 153 = 1^3 + 5^3 + 3^3 = 153
def armstrong_number():
    num = int(input("Enter a number: "))

    if num < 0:
        print("Negative numbers are not considered Armstrong numbers here.")
        return

    digits = str(num)
    order = len(digits)

    total = sum(int(digit) ** order for digit in digits)

    if total == num:
        print(num, "is an Armstrong Number.")
    else:
        print(num, "is not an Armstrong Number.")


# Main menu
def main():
    while True:
        print("\n========== PYTHON TASK 1 ==========")
        print("1. Sum of Two Numbers")
        print("2. Odd or Even Checker")
        print("3. Factorial Calculation")
        print("4. Fibonacci Sequence")
        print("5. String Reverse")
        print("6. Palindrome Check")
        print("7. Leap Year Check")
        print("8. Armstrong Number")
        print("9. Run All Tasks")
        print("0. Exit")
        print("===================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            sum_of_two_numbers()
        elif choice == "2":
            odd_or_even()
        elif choice == "3":
            factorial()
        elif choice == "4":
            fibonacci()
        elif choice == "5":
            string_reverse()
        elif choice == "6":
            palindrome_check()
        elif choice == "7":
            leap_year_check()
        elif choice == "8":
            armstrong_number()
        elif choice == "9":
            sum_of_two_numbers()
            odd_or_even()
            factorial()
            fibonacci()
            string_reverse()
            palindrome_check()
            leap_year_check()
            armstrong_number()
        elif choice == "0":
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
