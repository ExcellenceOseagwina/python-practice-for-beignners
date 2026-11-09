# Secret Number
secret_number = 6
message = None

# Getting user guesses
user_guess = int(input("Enter Guess The Number (1-10): "))

# Guessing....................
if user_guess > 10 or user_guess < 1:
    message = "Invalid! Try a number 1-10"
elif user_guess > secret_number:
    message = "Too high! Try a lower number."
elif user_guess < secret_number:
    message = "Too low! Try a higher number."
else:
    message = "Congratulations! You guessed correctly!✅"

    # or
if user_guess > secret_number:
    message = "Invalid! Try a lower number."
    if user_guess > 10:
        message = "That's too high! Try a number 1-10"
elif user_guess < secret_number:
    message = "Too low! Try a higher number."
    if user_guess < 1:
        message = "Too low! Try a number 1 - 10"
else:
    message = "Congratulations! You guessed correctly!✅"

# Display Message
print(message)
