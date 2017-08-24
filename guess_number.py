import random
secret = str(random.randint(1, 10))
guesses = 5
print "I'm thinking of a number between 1 and 10."

player_num = 0
while player_num != secret:
    print "secret %s" % (secret)
    print "Number of guesses left %d" % (guesses)
    player_num = raw_input("What's the number? ")

    if guesses == 1:
        print "No more guesses."
        break


    if player_num > secret:
        print "Too high! Try again."

    if player_num < secret:
        print "Too low! Try again."
    guesses -= 1

    if player_num == secret:
        print "Yes! You win!"
        break
