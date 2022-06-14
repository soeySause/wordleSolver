all_words = open("words.txt", "r")
word_list = []
winner = False

secret_word = "hello"

for word in all_words:
    word_list.append(word.strip())

# 6 Guesses
x = 0
while x < 6 and not winner:
    print("guess " + str(x + 1))

    valid_guess = False

    # Keeps asking for a word until they give a valid word
    while not valid_guess:

        # Asks for an input. If its valid it does a full loop
        guess = input("Enter your guess: ")
        if len(guess) == 5 and guess in word_list:
            valid_guess = True

            guess_results = ""

            # Calculate what user got right / wrong
            for i in range(5):
                if guess[i] in secret_word:
                    if guess[i] == secret_word[i]:
                        guess_results += "GREEN "
                    else:
                        guess_results += "YELLOW "
                else:
                    guess_results += "GREY "

            if guess_results == "GREEN GREEN GREEN GREEN GREEN ":
                winner = True

            #guess_list = [char for char in guess]
            print(guess_results)
            x += 1

        else:
            print("Invalid!")
            print("Word must be 5 letters and valid.")

if winner:
    print("You win!")
