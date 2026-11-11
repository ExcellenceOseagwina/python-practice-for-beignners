# LESSON: Comparisons and mutually exclusive decisions
# The secret number is set to 6. input() gives us text, and int() changes the
# guess into a whole number. The player must type a number for this example.
secret_number = 6
message = None

# Getting user guesses
user_guess = int(input("Enter Guess The Number (1-10): "))

# First, check that the guess is from 1 to 10. Then compare it with the secret.
# elif means “otherwise, check this”; only one of these choices runs.
if user_guess > 10 or user_guess < 1:
    message = "Invalid! Try a number 1-10"
elif user_guess > secret_number:
    message = "Too high! Try a lower number."
elif user_guess < secret_number:
    message = "Too low! Try a higher number."
else:
    message = "Congratulations! You guessed correctly!✅"

# This second set of choices runs after the first and may replace message.
# The last value assigned to message is the one printed at the end.
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
