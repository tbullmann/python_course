"""
Result for 5a
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


# Measurements
counts = [10000, 12900, 16800, 22000, 28400, 37000]

# Get growth curve parameters from measurements
max_t = len(counts) - 1  # hours are one less than measurements
initial_count = counts[0]
rate = growth_rate(counts)

# Prediction growth
pred_count_next = initial_count * pow(rate, max_t + 1)
pred_count_24h = initial_count * pow(rate, 24)

print("Anzahl der Bakterien nach", max_t + 1, "Stunden: ", pred_count_next)
print("Anzahl der Bakterien nach 24 Stunden: ", pred_count_24h)


