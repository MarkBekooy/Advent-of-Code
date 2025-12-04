# PART 2 IS NOT FINISHED

from collections import Counter

counter_value = 50  # Initial counter value
passes_by_zero_count = 0
value_counter = Counter()  # Track how often each value occurs

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
            
        # Parse the first character (L or R) and the number
        direction = line[0]
        number = int(line[1:])
        
        # Store previous value to count crossings of multiples of 100
        prev_value = counter_value
        
        # Apply operation based on direction
        if direction == 'L':
            counter_value -= number
        elif direction == 'R':
            counter_value += number
        
        # Count how many times the dial crosses multiples of 100 (including 0)
        # This is the difference in how many times 100 fits into the values
        prev_multiple = prev_value // 100
        new_multiple = counter_value // 100
        passes_by_zero_count += abs(new_multiple - prev_multiple)
        
        # Apply modulo 100
        counter_value = counter_value % 100
        
        # Record the result in Counter
        value_counter[counter_value] += 1

print(passes_by_zero_count)

# Return the count for value 0
print(f"1: Count for value 0: {value_counter[0]}")
print(f"2: Count: {passes_by_zero_count}")
