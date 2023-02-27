import random

class Deck:
    def __init__(self):
        self.deck = [i for i in range(1,53)]
        self.spades = [i for i in range(1, 14)]
        self.hearts = [i for i in range(14, 27)]
        self.clubs = [i for i in range(27, 40)]
        self.diamonds = [i for i in range(40, 53)]


    def shuffle(self):
        random.shuffle(self.deck)


    def sort(self):
        self.deck.sort()


    def reshuffle(self):
        self.deck = [i for i in range(1,53)]


    def convert(self, card):
        # order: spades, hearts, clubs, diamonds
        types = ["♠", "♡", "♣", "♢"]

        if type(card) == type(1):
            if card > 0:
                if card < 53:
                    if card in self.hearts:
                        return f"{types[0]}{card % 13}"
                    if card in self.spades:
                        return f"{types[1]}{card % 13}"
                    if card in self.diamonds:
                        return f"{types[2]}{card % 13}"
                    if card in self.clubs:
                        return f"{types[3]}{card % 13}"
                else:
                    return "not a card"
            else:
                return "not a card"
        else:
            return "not a card"




    def draw(self, amount, convert):
        drawn = []
        if amount > len(self.deck):
            amount = len(self.deck)
        for i in range(1, amount+1):
            drawn.append(self.deck.pop(0))


        if convert:
            final = []
            for i in drawn:
                final.append(self.convert(i))

            return final
        else:
            return drawn


    def add(self, card, shuffled):
        if type(card) == type(1):
            if card > 0 and card < 53:
                if shuffled:
                    self.deck.insert(card, random.randrange(1,52))
                else:
                    self.deck.insert(card, 0)
            else:
                return "not a card"
        else:
            return "not a card"
