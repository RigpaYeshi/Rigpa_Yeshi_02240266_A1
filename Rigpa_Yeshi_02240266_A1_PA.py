import math
def start():
    while True:
        print("Select a function(1-6):")
        print("1. Calculate the sum of prime numbers \n2. Convert length units \n3. Count consonants in string \n4. Find min and max numbers \n5. Check for palindrome \n6. Word Counter \n0. Exit program")
        user_choice = int(input("Enter your choice:"))
        if user_choice == 1:
            def prime_number(number):
                if number < 2:
                    return False
                for i in range(2, int(number**0.5) + 1):
                    if number % i == 0:
                        return False
                return True
                
            def sum_of_prime(start, end):
                return sum(number for number in range(start, end + 1) if prime_number(number))

            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range: "))
            print("Sum of prime numbers in range:", sum_of_prime(start, end))
        elif user_choice == 2:
            value = float(input("Enter value: "))#
            direction = input("Enter direction (M/F):")
            if direction.upper() == "M":
                converted_value = round(value * 3.28084, 2)
            elif direction.upper() == "F":
                converted_value = round(value / 3.28084, 2)
            else:
                 converted_value = "Invalid direction"
            print(f"Converted value: {converted_value}")
        elif user_choice==3:
            text=input("Enter a text string :")
            count_consonants = lambda text: sum(1 for char in text.lower() if char.isalpha() and char not in "aeiou")
            print("Number of consonants:", count_consonants(text))
        elif user_choice == 4:
            def min_max_finder():
                while True:
                    try:
                        number = int(input("How many numbers will you enter? : "))
                        if number <= 0:
                            print(" Please enter a valid number greater than 0.")
                            continue  
                        break
                    except ValueError:
                        print(" Invalid input! Please enter a whole number.")
                numbers = []
                for i in range(number):
                    while True:
                        try:
                            num = float(input(f"Enter number {i+1}: "))
                            numbers.append(num)
                            break
                        except ValueError:
                            print("Invalid input! Please enter a numeric value.")
                return min(numbers), max(numbers)
            min_val, max_val = min_max_finder()
            print(f" Min: {min_val}, Max: {max_val}")
        elif user_choice == 5:
            def is_palindrome(text):
                cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
                return cleaned_text == cleaned_text[::-1] 

            text = input("Enter a text string: ")
            print("Palindrome check:", is_palindrome(text))
        elif  user_choice== 6:
            
        else:
            print("Invalid option")
start()

