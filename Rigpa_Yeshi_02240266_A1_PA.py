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
                           count = int(input("How many numbers will you enter? "))
                           if count > 0:
                                break
                           print("Enter a number greater than 0.")
                      except ValueError:
                           print("Invalid input! Enter a whole number.")
                           numbers = [float(input(f"Enter number {i+1}: ")) for i in range(count)]
                           return min(numbers), max(numbers)
                      min_val, max_val = min_max_finder()
                      print(f"Min: {min_val}, Max: {max_val}")
        elif user_choice == 5:
            def is_palindrome(text):
                cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
                return cleaned_text == cleaned_text[::-1] 
            text = input("Enter a text string: ")
            print("Palindrome check:", is_palindrome(text))
        elif user_choice == 6:
            def word_counter(file_path):
                words_to_count = ["the", "was", "and"]
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        text = file.read().lower().split()
                        return {word: text.count(word) for word in words_to_count}
                except FileNotFoundError:
                    print("Error: File not found!")
            file_path = input("Enter the file path: ")
            print("Word counts:", word_counter(file_path))
        elif user_choice == 0:
            print("Exit program")
            break
        else:
            print("Invalid option, Please enter a valid option")
start()

