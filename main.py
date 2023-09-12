import random

def classify_batteries_random():
    # Generate random present capacities for a list of batteries (between 50 and 150 Ah)
    present_capacities = [random.randint(50, 150) for _ in range(10)]

    # Initialize counters for healthy, exchange, and failed batteries
    healthy_count = 0
    exchange_count = 0
    failed_count = 0

    # Rated capacity of a new battery
    rated_capacity = 120

    # Iterate through the list of present capacities
    for present_capacity in present_capacities:
        # Calculate State-of-Health (SoH) using the provided formula
        soh = (present_capacity / rated_capacity) * 100

        # Classify the battery based on SoH
        if soh > 80:
            healthy_count += 1
        elif 63 <= soh <= 80:
            exchange_count += 1
        else:
            failed_count += 1

    # Return the counts as a dictionary
    return {
        "healthy": healthy_count,
        "exchange": exchange_count,
        "failed": failed_count
    }

def test_classify_batteries():
    print("Testing battery classification...\n")

    # Test case 1: Existing test case
    present_capacities_1 = [115, 118, 80, 95, 91, 72]
    counts_1 = classify_batteries_random()
    print("Test Case 1 - Counts:", counts_1)

    # Test case 2: Empty battery list
    present_capacities_2 = []
    counts_2 = classify_batteries_random()
    print("Test Case 2 - Counts:", counts_2)

    # Test case 3: Single battery
    present_capacities_3 = [100]
    counts_3 = classify_batteries_random()
    print("Test Case 3 - Counts:", counts_3)

    # Test case 4: Maximum rated capacity
    present_capacities_4 = [120, 120, 120]
    counts_4 = classify_batteries_random()
    print("Test Case 4 - Counts:", counts_4)

    # Test case 5: Minimum rated capacity
    present_capacities_5 = [50, 50, 50]
    counts_5 = classify_batteries_random()
    print("Test Case 5 - Counts:", counts_5)

    # Test case 6: Random large dataset (100 batteries)
    present_capacities_6 = [random.randint(50, 150) for _ in range(100)]
    counts_6 = classify_batteries_random()
    print("Test Case 6 - Counts:", counts_6)

    # Test case 7: Extreme capacity difference
    present_capacities_7 = [20, 180]
    counts_7 = classify_batteries_random()
    print("Test Case 7 - Counts:", counts_7)

    # Test case 8: Decimal rated capacity
    present_capacities_8 = [119.5, 120.5, 121.5]
    counts_8 = classify_batteries_random()
    print("Test Case 8 - Counts:", counts_8)

    # Test case 9: Negative battery capacity
    present_capacities_9 = [-50, -75, -100]
    counts_9 = classify_batteries_random()
    print("Test Case 9 - Counts:", counts_9)

    # Test case 10: Identical battery capacities
    present_capacities_10 = [80, 80, 80]
    counts_10 = classify_batteries_random()
    print("Test Case 10 - Counts:", counts_10)

    print("Done testing battery classification :)")

if __name__ == '__main__':
    test_classify_batteries()
