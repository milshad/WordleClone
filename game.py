

# initialise the word we want to play with


word = ["H", "O", "U", "S", "E"]

# user has six attempts before game ends
attempts = 6

# boolean to see if they have got the right answer set to false by default

correct_answer = False


# sorting algorithms

# will firstly take the letter and look if in the main word, if not in main word instantly send to unavailable alphabet
# if it is in the same word it will compare the index of the letter in the guess vs the index of the letter in the word
# if they are not the same it goes to the wrong_position letters array and if it is the same it goes to the good letters array
# can be attempted 6 times, also has a check for if attempts hits 0 but answer is still right as to not break the game just cause all
# attempts have been used



count = 0 # count to compare indexes 

# initialise alphabet removing letters when used 
available_alphabet = [
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

# will need to be a function so we can use recursion feeding back necessary variables requried to continue
def game_sorter(count, attempts, available_alphabet, correct_answer, word): 


  # letters in a guess where they are not in the word at all and will be added to unnavailable_alphabet
  # REDUNDANT CURRENTLY
  guess_bad_letters = []

  # letters in a guess but are in the word, just in the wrong position 
  guess_wrong_position_letters = []

  # guess letters which are in the correct spot
  guess_good_letters = []

  # where all wrong letters are gone
  # REDUNDANT CURRENTLY
  unavailable_alphabet = []

  guess = str(input("Enter Your Guess: "))

  guess_array = list(guess) # takes the guess and splits it into array to match word format
  
  while ( (attempts != 0) and (correct_answer != True) ):             
    if (guess_array == word):                               
      print("Congratulations you have got the word!")         
      correct_answer = True
      break
    for guess_letter in guess_array: # for each letter in array we do some checks
      if not (guess_letter in word): # if the letter is not in word we add to the two arrays then continue to next letter
        available_alphabet.remove(guess_letter) # removes a letter from the main alphabet if not in the main word
        count += 1
        continue
      if (guess_letter == word[count]): # if the letter matches the letter in same position in main word  it adds it to good letters
        guess_good_letters.append(guess_letter) # array so you know where the letter belongs
        count += 1
        continue
      else: 
        guess_wrong_position_letters.append(guess_letter) # if the letter is in the word and not in right place then falls into this array
        count += 1
    else:
      print(f"You ran out of attempts the word was: {word}")

    print(f"These letters were in the right spot: {guess_good_letters}")
    print(f"These letters were correct but in the wrong spot: {guess_wrong_position_letters}")
    print(f"These letters are the current available letters: {available_alphabet}")
    attempts -= 1
    game_sorter(0, attempts, available_alphabet, correct_answer, word)

  
game_sorter(0, attempts, available_alphabet, correct_answer, word)