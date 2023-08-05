print("Welcome to the Letter Counter App\n")
username = input("What is your name?")
print("Hello", username.capitalize() )
print("This program is meant to count how many times a specific letter has featured in each sentence.")
message = input("\n Kindly write the message you'd like to use:")
letter = input("\n what letter would you like to for the program to count?")

message = message.lower()
letter = letter.lower()
username = username.capitalize()
count = 0
for x in message:
    if x == letter:
        count = count + 1

print(username +  "your message has " + str(count) + letter + "'s in it")

