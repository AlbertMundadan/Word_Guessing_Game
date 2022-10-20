import random

LEXICON_FILE = "Lexicon.txt"    # File to read word list from


def get_word(list):  # Chooses random word list
    index = random.randrange(0, len(list))
    random_word = list[index]
    return random_word


def start_game(length):
    print("Welcome to the Word Guessing Game!")
    blank_list = []
    blank_spaces = create_list(blank_list, length)
    blank_spaces = ''.join(blank_spaces)
    print("This is your secret word: " + blank_spaces)


def user_guess(word, word_length):
    initial_guesses = word_length + 5  # Total guesses is 5 more than the number of letters in the word
    guesses_used = 0
    new_list = []
    create_list(new_list, word_length)
    print("You have", initial_guesses - guesses_used, "guesses left.")
    while initial_guesses - guesses_used != 0:
        if "_" not in new_list:  # If all letters are found, no "_" will be left
            print()
            print("Congratulations, You Won! The secret word was:", word)
            break
        print()
        guess = input("Type a single letter to guess and click enter: ")
        while len(guess) > 1:  # Ensures all guesses are 1 character
            print("That guess is invalid. Guesses should only be a single letter. Please try again.")
            guess = input("Type a single letter to guess and click enter: ")
        guess = guess.upper()  # Converts guess to uppercase to prevent discrepancies
        if word.find(str(guess)) >= 0:  # If letter found in secret word
            print("That guess is correct!")
            i = 0
            for char in word:  # Replaces "_" with the letter guessed in the appropriate location
                if char == guess:
                    new_list.insert(i, guess)
                    del new_list[i+1]
                    i += 1
                else:
                    i += 1
            new_list2 = ''.join(new_list)
            guesses_used += 1
            print("The word now looks like this: " + new_list2)
            print("You now have", initial_guesses - guesses_used, " guesses remaining.")
            print()
        else:
            print("That guess is incorrect. There are no " + guess + "'s in this word.")
            guesses_used += 1
            new_list2 = ''.join(new_list)
            print("The word still looks like this: " + new_list2)
            print("You have", initial_guesses - guesses_used, "guesses remaining.")
            print()
    else:
        print("Game Over")
        print("The secret word was:", word)


def create_list(list, length):
    for i in range(length):
        list.extend("_")
    return list


def find_word_length(word):
    length = len(word)
    return length


def convert_file_to_list(file_name):  # Creates a list of words from a file (used on Lexicon file)
    word_list = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            word_list.append(line)
    return word_list


def main():
    word_list = convert_file_to_list(LEXICON_FILE)
    secret_word = get_word(word_list)
    word_length = find_word_length(secret_word)
    start_game(word_length)
    user_guess(secret_word, word_length)


if __name__ == "__main__":
    main()
