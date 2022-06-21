def game():
    import os
    import time
    from wordfile import words
    from wordfile import e
    from wordfile import m
    from wordfile import h
    import random

    clear = lambda: os.system('cls')

    #rules
    def rule():
        print(
            "--> Hangman is a game in which you have to guess a given word, letter-by-letter."
        )
        time.sleep(2)
        print()
        print(
            "--> If the letter you guess isn't in the word, the man moves one step closer to death."
        )
        time.sleep(2)
        print()
        print("  - If you have 7 incorrect answers, the man is hanged.")
        time.sleep(2)
        print()
        print(
            "--> To play, just select your difficulty, start entering letters into the guess area, and you're good to go!"
        )
        time.sleep(2)
        print()
        print(
            "--> If you want to see the commands, type in 'cmds' into the guess area!"
        )
        time.sleep(2)
        print()
        input("Press 'enter' to continue! ")
        return ("")
        clear()

    #replay func vvv
    def replay():
        replay = input("Replay? [Y/N] ")
        print()
        replay = replay.lower()
        while True:
            if replay not in ("y", "n"):
                clear()
                print()
                print("Please enter 'Y' or 'N'!")
                print()
                replay = input("Replay? [Y/N] ")
            elif replay in ("y", "n"):
                if replay == "y":
                    clear()
                    start()
                else:
                    print("Goodbye!")
                    print()
                    quit()

    print("*-~_ H A N G M A N _~-*")
    print()
    rules = input(" > Do you know how to play? [Y/N] ")
    print()
  
    while True:
        if rules.lower() not in ("y", "n"):
            clear()
            print()
            print("Please enter 'Y' or 'N'!")
            print()
            rules = input(" > Do you know how to play? [Y/N] ")
        elif rules.lower() in ("y","n"):
          break

    if rules.lower() == "n":
        print(rule())
        clear()
    elif rules.lower() == "y":
        clear()
        print()
        time.sleep(0.3)

    def start():
        w_no = len(words)
        c = 7
        x = []
        hc = 0
        alpha = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ]
        cmdwords = ["no hints", "cmds", "hint", "rules"]
        tipoff = ""
        game = 0
        print("*-~_ H A N G M A N _~-*")
        print()
        print(
            " > Welcome! Choose your difficulty: \n \n - Easy \n - Medium \n - Hard \n - Random \n"
        )
        difficulty = input()
        difficulty = difficulty.lower()
        print()

        #word selection func vvv
        def ranWo():
            if difficulty == "easy" or difficulty == 'e':
                word = random.choice(e)
            elif difficulty == "medium" or difficulty == 'm':
                word = random.choice(m)
            elif difficulty == "hard" or difficulty == 'h':
                word = random.choice(h)
            else:
                word = random.choice(words)
            return word

        #defining some variables and stuff
        a = ranWo()
        le_word = a
        a = list(a)
        alen = len(a) - 1
        ans = ("_" * len(a))
        ans = list(ans)
        done = []

        if difficulty not in ('easy', 'medium', 'hard', 'random', 'e', 'm',
                              'h', 'r'):
            print(
                "Invalid input. A random word has been chosen automatically.")
            print()
            time.sleep(1)

        #"difficulty: x"
        if le_word in e:
            print("Difficulty: Easy")
            print()
        elif le_word in m:
            print("Difficulty: Medium")
            print()
        elif le_word in h:
            print("Difficulty: Hard")
            print()

        #drawing hangman func vvv
        def hangDraw(c):
            if c == 7:
                print("--____ \n -| \n -| \n -| \n -| \n _______ \n")
                return ("")
            elif c == 6:
                print("--____ \n -|--| \n -| \n -| \n -| \n _______ \n")
                return ("")
            elif c == 5:
                print("--____ \n -|--| \n -|--o \n -| \n -| \n _______ \n")
                return ("")
            elif c == 4:
                print("--____ \n -|--| \n -|--o \n -|--| \n -| \n _______ \n")
                return ("")
            elif c == 3:
                print("--____ \n -|--| \n -|--o \n -|-/| \n -| \n _______ \n")
                return ("")
            elif c == 2:
                print("--____ \n -|--| \n -|--o \n -|-/|\ \n -| \n _______ \n")
                return ("")
            elif c == 1:
                print(
                    "--____ \n -|--| \n -|--o \n -|-/|\ \n -|-/ \n _______ \n")
                return ("")
            else:
                print(
                    "--____ \n -|--| \n -|--o \n -|-/|\ \n -|-/-\ \n _______ \n"
                )
                return ("")

        print()
        print(
            " > Guess the word, letter-by-letter, or else the man will hang!")
        print()
        print(
            "--____ \n -| \n -| \n -|             o/ \n -|            /| \n _______       / \ "
        )
        time.sleep(1)
        print()
        print(
            " >>> To see a command list, type 'cmds' without the quotation marks! <<<"
        )
        time.sleep(2)
        print()
        print("_ " * len(a))
        print()
        while True:
            left = len(done)
            guesses = ' '.join([str(letter) for letter in x])

            #win vvv
            if ans == a:
                clear()
                print()
                print("\o/")
                print(" | ")
                print("/ \ ")
                print()
                print("*-* You won! *-*")
                print()
                print("The word was:", le_word)
                print()
                game == 1
                print(replay())

            #lose vvv
            if c == 0:
                clear()
                print()
                print(
                    "--____ \n -|--| \n -|--o \n -|-/|\ \n -|-/-\ \n _______")
                print()
                print("-- Too many attempts! You die! :) --")
                print()
                print("The word was:", le_word)
                print()
                game == 1
                print(replay())

            print(" -> Your previous guesses:", guesses)
            print()
            guess = input("Enter your guess! ")
            guess = guess.lower()
            clear()
            print()

            #cmds cmd vvv
            if guess == "cmds":
                print(
                    "hint - gives you a hint (one time only, and won't work if you have only 1 letter left - use it wisely!)"
                )
                print()
                print("no hints - turns off hints")
                print()
                print("rules - shows the rules")
                print()
                print(hangDraw(c))
                print(" ".join(ans))
                print()
                print("You have", c, "guesses left!")
                print()
                time.sleep(1)
                continue

            #no hints cmd
            if guess == "no hints" or guess == "no hint" or guess == "nohints" or guess == "nohint":
                print("Okay!")
                print()
                print("You have", c, "guesses left!")
                print()
                print(hangDraw(c))
                print(" ".join(ans))
                print()
                tipoff = "no hints"
                continue

            #hint cmd
            if guess == "hint" and hc == 0 and tipoff != "no hints":
                if left != alen:
                    print()
                    hi = random.choice(a)
                    while hi in x:
                        hi = random.choice(a)
                    print(" > Have you tried", hi, "yet?")
                    time.sleep(1)
                    print()
                    print("You have", c, "guesses left!")
                    print()
                    print(hangDraw(c))
                    print(" ".join(ans))
                    print()
                    hc += 1
                    continue
                elif left != 0 and left == alen and c != 0:
                    print("You only have one letter left!")
                    print()
                    print("You have", c, "guesses left!")
                    print()
                    print(hangDraw(c))
                    print(" ".join(ans))
                    print()
                    continue
            elif guess == "hint" and tipoff == "no hints":
                print("Hints are off!")
                print()
                print("You have", c, "guesses left!")
                print()
                print(hangDraw(c))
                print(" ".join(ans))
                print()
                print("You have", c, "guesses left!")
                print()
                continue

            #rules cmd
            if guess == "rules" or guess == "rule":
                print(rule())
                clear()
                print("You have", c, "guesses left!")
                print()
                print(hangDraw(c))
                print(" ".join(ans))
                print()
                continue

            #guess 1 at a time vvv
            if len(guess) > 1 and guess not in cmdwords:
                print("Only guess one letter at a time!")
                print()
                time.sleep(1)
                print("You have", c, "guesses left!")
                print()
                print(hangDraw(c))
                print(" ".join(ans))
                print()
                continue

            #only alpha vvv
            if guess not in alpha and guess not in cmdwords:
                print("You should only enter letters!")
                print()
                time.sleep(1)
                print("You have", c, "guesses left!")
                print()
                print(hangDraw(c))
                print(" ".join(ans))
                print()
                continue

            #you already guessed this vvv
            if guess in x:
                print(" > You already guessed this!")
                print()
                time.sleep(1)
                print("You have", c, "guesses left!")
                print()
                print(hangDraw(c))
                print(" ".join(ans))
                print()

                continue

            #guess=correct/wrong vvv
            if guess in a:
                print(" > Correct! You have", c, "guesses left!")
                print()
                print(hangDraw(c))
                for i in range(len(a)):
                    if a[i] == guess:
                        ans[i] = guess
                        done.append(guess)
                        print(" ".join(ans))
                        print()
            else:
                c -= 1
                print(" > Incorrect! You have", c, "guesses left!")
                print()
                print(hangDraw(c))
                print(" ".join(ans))
                print()

            #hint system vvv
            if left != alen:
                if c == 1 and hc == 0 and tipoff != "no hints":
                    hint = input(" >>> Would you like a hint? [Y/N] ")
                    print()
                    hint = hint.upper()
                    if hint == "Y":
                        hi = random.choice(a)
                        while hi in x:
                            hi = random.choice(a)
                        print(" > Have you tried", hi, "yet?")
                        time.sleep(1)
                        print()
                        hc += 1

            if len(guess) == 1:
                x.append(guess)

    print(start())
    return (" ")


# ---------changelog---------

# > base game (random word generator, dashes, basic guessing system)

# > guess limit

# > added guess counter (shows no. of guesses)

# > added "You've already guessed this!"

# > added "The word was --- " (for when you lose)

# > added guess.lower

# > added cmd for checking guesses in-game

# > made it so you're only allowed to type in one letter at a time

# > added hangman drawing thing

# > added hint system

# > added cmd to check your progress

# > added difficulty levels [easy, medium, hard, random]

# > made it so only letters can be inputted

# > added a way to turn off hints

# > better command organisation

# > presentation changes (clear screen, pauses here and there, etc.)

# > stats cmd

# > hint cmd

# > figured out the replay thing

# > deleted all cmds but "guesses","no hints","hint","cmds"

# > better ui

# > minor edits to presentation

# > removed guesses cmd, converted guesses to string and displayed it in the console automatically

# > made it so that if you have 1 letter left you can't use hints

# > made it so that it displays the chosen difficulty

# > added rules and the rule cmd

# > presentation changes

# ~-~ to do ~-~

# > N/A
