def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Using a predefined integer instead of interactive input to avoid I/O errors
user_input = 10  # Change this value as needed
print(f"The number {user_input} is {check_even_odd(user_input)}.")

# Using a for loop to generate a list of even numbers from 1 to 50
even_numbers = [num for num in range(1, 51) if num % 2 == 0]
print("Even numbers from 1 to 50:", even_numbers)

# Using a while loop to print numbers from 10 down to 1
count = 10
print("Countdown from 10 to 1:")
while count > 0:
    print(count)
    count -= 1
