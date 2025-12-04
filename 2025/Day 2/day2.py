invalid_ids_1 = []
invalid_ids_2 = []

with open("input.txt", "r") as file:
    line = file.read().strip()
    
    # Split by comma to get ranges
    ranges = line.split(",")
    
    for range_str in ranges:
        # Parse start-end
        start, end = map(int, range_str.split("-"))
        
        # Iterate through all numbers in the range (inclusive)
        for num in range(start, end + 1):
            num_str = str(num)
            
            # Check if number has even number of digits
            if len(num_str) % 2 == 0:
                # Split in two
                mid = len(num_str) // 2
                first_half = num_str[:mid]
                second_half = num_str[mid:]
                
                # Check if first part equals second part
                if first_half == second_half:
                    invalid_ids_1.append(num)
            
            # Check if the number is made of a repeating substring (at least 2 repetitions)
            for substr_len in range(1, len(num_str) // 2 + 1):
                # Check if the string length is divisible by substring length
                if len(num_str) % substr_len == 0:
                    substr = num_str[:substr_len]
                    # Check if repeating this substring gives us the full string
                    repetitions = len(num_str) // substr_len
                    if substr * repetitions == num_str and repetitions >= 2:
                        invalid_ids_2.append(num)
                        break  # Found a match, no need to check other lengths


# Sum the values and print
result_1 = sum(invalid_ids_1)
result_2 = sum(invalid_ids_2)
print(f"1: {result_1}")
print(f"2: {result_2}")
