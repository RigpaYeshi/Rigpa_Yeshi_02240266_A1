def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_prime(start, end):
    return sum(n for n in range(start, end + 1) if prime(n))

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Sum of prime numbers in range:", sum_of_prime(start, end))

