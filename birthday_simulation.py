import random
from functools import reduce

def simulate_birthdays(num_people=30, trials=100_000):
    two_or_more = 0
    three_or_more = 0
    four_or_more = 0

    # exact theoretical probability
    actual_two = 1 - (reduce(lambda prev, curr: prev * (365 - curr), range(num_people), 1) / pow(365, num_people))

    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        counts = {}
        for b in birthdays:
            counts[b] = counts.get(b, 0) + 1

        if any(c >= 2 for c in counts.values()):
            two_or_more += 1
        if any(c >= 3 for c in counts.values()):
            three_or_more += 1
        if any(c >= 4 for c in counts.values()):
            four_or_more += 1

    sim_two = two_or_more / trials
    sim_three = three_or_more / trials
    sim_four = four_or_more / trials

    percent_error = abs(sim_two - actual_two) / actual_two * 100

    print(f"Out of {trials:,} trials:\n")
    print(f">=2 people share a birthday: {sim_two * 100:.2f}%")
    print(f"The actual value for >=2 is {actual_two * 100:.2f}%. The % error is {percent_error:.2f}%.\n")
    print(f">=3 people share a birthday: {sim_three * 100:.2f}%\n")
    print(f">=4 people share a birthday: {sim_four * 100:.2f}%\n")

simulate_birthdays()
