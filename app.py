
password = "python"
guess_count = 0
guess_limit = 3

for i in range(3):
    ok = input("Guess the password: ")
    guess_count += 1

if guess_count == guess_limit:
    print("you lose")
elif ok == password:
    print('you win!')

