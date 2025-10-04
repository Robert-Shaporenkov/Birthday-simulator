import random

def simulate_birthdays(num_people=30, trials=100_000):
    two_or_more = 0
    three_or_more = 0
    four_or_more = 0

    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]

        # Count occurrences of each birthday
        counts = {}
        for b in birthdays:
            counts[b] = counts.get(b, 0) + 1

        # Check conditions
        if any(c >= 2 for c in counts.values()):
            two_or_more += 1
            print(two_or_more)
        if any(c >= 3 for c in counts.values()):
            three_or_more += 1
        if any(c >= 4 for c in counts.values()):
            four_or_more += 1

    print(f"Out of {trials:,} trials:")
    print(f"  ≥=2 people share a birthday: {two_or_more / trials * 100:.2f}%")
    print(f"  >=3 people share a birthday: {three_or_more / trials * 100:.2f}%")
    print(f"  >=4 people share a birthday: {four_or_more / trials * 100:.2f}%")

simulate_birthdays()