# Name: Aljade Bora
# Section: BSCS 1-1
# Program: savings_tracker.py
# Description: Totals daily savings until 0 is entered
# savings_tracker.py

savings = [20, 0]  # sample input: save PHP 20, then enter 0 to stop

total_saved = 0.0
days = 0

for amount in savings:
    if amount == 0:
        break
    total_saved += amount
    days += 1

print(f"Days: {days}")
print(f"Total saved: PHP {total_saved:,.2f}")
