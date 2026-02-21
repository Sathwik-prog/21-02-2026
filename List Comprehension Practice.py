# 1. Odd numbers using list comprehension
n = int(input("Enter a number: "))

odd_numbers = [i for i in range(n) if i % 2 != 0]

print("Odd numbers below", n, ":", odd_numbers)


# 2. Capitalize fruit names
fruits = ["apple", "banana", "cherry", "mango"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Original list:", fruits)
print("Updated list:", capitalized_fruits)