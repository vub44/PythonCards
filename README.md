# PythonCards
A super minimal python playing cards library, capable of sorting, shuffeling and drawing cards. Easy to use and build card games out of.

# Installation
Download the cards.py and place it in either you libraries folder or the project folder. 
Then import it at the top of your code.


# Functions
Deck.shuffle()

takes no argument, shuffles the deck


Deck.sort()

takes no arguments, sorts the deck ascending.
If the deck only contains 1, 2 and 3, it will sort accordingly. Does not add in drawn cards.


Deck.reshuffle()

takes no arguments, resets the deck so it contains all cards, sorted.

Deck.convert(card)

takes one argument; the card you want to convert. Only takes a number between 1 and 52.
it converts the the supplied number into a readable format. Example: ♡11 and ♠3


Deck.draw(amount)

takes two arguments; the amount of cards you want to draw and if it should be converted or not.
Always takes the top card so you need to shuffle the deck to get a random card.
Always returns a list.


Deck.add(card, shuffled)

takes two arguments; the card you want to add (1 --> 52) and if it should shuffle it in.
Adds the supplied card. If shuffled = True, then it will place it in a random spot. If not the it will be added at the top.

# Example
```python
import cards

deck = cards.Deck()

deck.shuffle()

print(deck.draw(1, True))
```

will output a list of cards drawn, in a readable format.
