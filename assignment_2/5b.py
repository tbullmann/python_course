"""
Result for 5b
"""
from math import pow


def growth_rate(measured_counts):
    counts = measured_counts.copy()
    ratios = []
    while len(counts) != 1:
        before = counts[-1]
        after = counts[-2]
        ratios.append(before/after)
        counts.pop()
    rate = sum(ratios)/len(ratios)
    return rate


# Input Measurements
n = 0
while n<4 or n>10:
    n = int(input("Bitte Anzahl der Messungen angeben (4<=n<=10):"))

f = []   # You might also use counts as in the previous example
for i in range(n):
    new_value = int(input("Anzahl zum Zeitpunkt " + str(i) + " = ? "))
    f.append(new_value)

# Get growth curve parameters from measurements
max_t = len(f) - 1  # hours are one less than measurements
initial_count = f[0]
rate = growth_rate(f)

# Prediction growth
pred_count_next = initial_count * pow(rate, max_t + 1 )
pred_count_24h = initial_count * pow(rate, 24)

print("Anzahl der Bakterien nach", max_t + 1, "Stunden: ", pred_count_next)
print("Anzahl der Bakterien nach 24 Stunden: ", pred_count_24h)


