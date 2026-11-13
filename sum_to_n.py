# Name: Aljade Bora
# Section: BSCS 1-1
# Program: sum_to_n.py
# Description: Sums the numbers from 1 to n
# sum_to_n.py

n = int(input("Enter a positive whole number: "))

total = 0

for number in range(1, n + 1):
    total += number

print(f"Sum of 1 to {n} = {total}")
