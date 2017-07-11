import random
def toss(num):
    heads, tails = 0, 0
    attempt = 1
    print "Let's test our luck..."
    while attempt < num+1:
        if round(random.random()) == 0:
            heads += 1
            print "Attempt #" + str(attempt) + " Tossing a coin...It's a head!...Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."
        else:
            tails += 1
            print "Attempt #" + str(attempt) + " Tossing a coin...It's tails!...Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far."
        attempt += 1
    print "Ending the program, thanks!"

toss(5000)