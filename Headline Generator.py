from curses.ascii import isdigit
import random

# Initiate dictionary of words

nouns = ['actor', 'advertisement', 'gold',
         'helicopter', 'plastic', 'Portugal', 'Rainbow']
verbs = ['run', 'fly', 'drive', 'swim', 'throw', 'kick', 'walk']
whens = ['today', 'yesterday', 'Friday', 'next month', 'last week']
adjectives = ['cute', 'calm', 'annoyed',
              'angry', 'creepy', 'curious', 'determined']
adverbs = ['abnormally', 'hopelessly', 'playfully',
           'quickly', 'politely', 'thoughtfully']


def main():

    print('Welcome to the headline generator')
    while True:
        userInput = input('Please enter a digit from 1 to 5 ')
        try:
            val = int(userInput)
        except ValueError:
            print("That's not a valid input please try again")
        if userInput > str(5):
            print("That's not a valid input please try again")
        elif userInput < str(1):
            print("That's not a valid input please try again")
        else:
            break

    print('Thank you for inputting a valid number your headline will now be generated')
    if userInput == 1:
        headline = PoliticsHeadline()
    elif userInput == 2:
        headline = NaturalDisasterHeadline()
    elif userInput == 3:
        headline = FeelGoodStoryHeadline()
    elif userInput == 4:
        headline = ForeignAffairsHeadline()
    elif userInput == 5:
        headline = EconomyHeadline()

    print(headline)


print()


def PoliticsHeadline():
    noun = random.choice(nouns)
    when = random.choice(whens)
    adjective = random.choice(adjectives)

    return 'The midterms are soon approaching and {} is taking the lead {} {}'.format(noun, when, adjective)


def NaturalDisasterHeadline():
    noun = random.choice(nouns)
    when = random.choice(whens)
    adjective = random.choice(adjectives)
    adverb = random.choice(adverbs)

    return ' A {} strom has blown in on the island of Fiji {}. {} has agreed to help, {}'.format(adjective, when, noun, adverb)


def FeelGoodStoryHeadline():
    when = random.choice(whens)

    return ' Cute puppies were seen {}'.format(when)


def ForeignAffairsHeadline():
    noun = random.choice(nouns)
    verb = random.choice(verbs)
    when = random.choice(whens)
    adjective = random.choice(adjectives)
    adverb = random.choice(adverbs)

    return ' The kingdom of Great Britain is punishing the {} {}. They will begin {} {} and do so with a '.format(noun, adverb, adjective, when, verb)


def EconomyHeadline():
    noun = random.choice(nouns)

    return ' The economy is rebounding thanks to {}'.format(noun)


main()
