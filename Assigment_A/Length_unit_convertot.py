def length_convetor(vlaue, direction):
    if direction.upper() == "M":
        return round(value * 3.28084, 2)
    elif direction.upper() == "F":
        return round(value / 3.28084, 2) 
    else:
        return "Invalid direction"
    
value = float(input("Enter value: "))
direction = input("Enter direction (M/F): ")
coverted_value = length_convetor(value, direction)
print(f"Converted value: {coverted_value}")
