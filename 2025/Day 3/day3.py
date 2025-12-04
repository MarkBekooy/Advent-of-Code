import numpy as np

# Read the file
with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

# Convert to numpy array where each character is a string
grid = np.array([list(line) for line in lines])

# Array to store largest concatenated values for each row
largest_values_1 = []
largest_values_2 = []

# Process each row
for row in grid:
    # Convert row to list of strings (digits)
    digits = row.tolist()
    # Find the first occurrence of the largest digit
    max_digit = max(digits)
    first_max_idx = digits.index(max_digit)
    # Find the largest digit that appears after the first max digit
    remaining_digits = digits[first_max_idx + 1:]
    if remaining_digits:
        second_max_digit = max(remaining_digits)
        # Concatenate them as strings and convert to int
        concatenated = int(max_digit + second_max_digit)
    else:
        # If no digit after the max (max is at end), find largest digit before it
        before_digits = digits[:first_max_idx]
        if before_digits:
            second_max_digit = max(before_digits)
            concatenated = int(second_max_digit + max_digit)
        else:
            # Only one digit in row, use it twice
            concatenated = int(max_digit + max_digit)
    print(concatenated)
    largest_values_1.append(concatenated)


for row in grid:
    # Convert row to list of strings (digits)
    digits = row.tolist()
    # Find 12 digits that form the largest concatenated value (reading left to right)
    selected_digits = []
    start_idx = 0
    digits_needed = 12
    
    for _ in range(digits_needed):
        # Calculate how many digits we still need after this selection
        remaining_needed = digits_needed - len(selected_digits) - 1
        # We can only look at digits that leave enough remaining digits
        end_idx = len(digits) - remaining_needed
        
        if start_idx >= len(digits):
            # Not enough digits left, break
            break
            
        if end_idx <= start_idx:
            # Only one option left, take it
            selected_digits.append(digits[start_idx])
            start_idx += 1
        else:
            # Find the largest digit in the valid range
            valid_range = digits[start_idx:end_idx]
            max_digit = max(valid_range)
            # Find the first occurrence of this max digit in the valid range
            max_idx = start_idx + valid_range.index(max_digit)
            selected_digits.append(max_digit)
            start_idx = max_idx + 1
    
    # Concatenate all selected digits and convert to int
    concatenated = int(''.join(selected_digits))
    print(concatenated)
    largest_values_2.append(concatenated)

# Sum all values
result1 = sum(largest_values_1)
result2 = sum(largest_values_2)
print(f"Result 1: {result1}")
print(f"Result 2: {result2}")

