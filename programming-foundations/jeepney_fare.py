# Name: Aljade Bora
# Section: BSCS 1-1
# Program: jeepney_fare.py
# Description: Computes the jeepney fare with discount

# jeepney_fare.py

distance = int(input("Distance in whole kilometers: "))
discount = input("Discount? (Y/N): ").strip().upper()

if distance <= 4:
    fare = 13.00
else:
    fare = 13.00 + (distance - 4) * 1.80

if discount == "Y":
    fare *= 0.80

print(f"Fare: PHP {fare:.2f}")
