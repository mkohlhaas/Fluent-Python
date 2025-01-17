import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # basedpyright complains without it (__getitem__ is not sufficient):
    def __iter__(self):
        return self._cards.__iter__()


def spades_high(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    beer_card = Card("7", "diamonds")
    print(f"Just an ordinary card: {beer_card}")
    deck = FrenchDeck()
    print(f"Number of cards in deck: {len(deck)}")
    print(f"Lowest card: {deck[0]}")
    print(f"Highest card: {deck[-1]}")
    print(f"Just a random card: {choice(deck)}")
    print(f"Three lowest cards: {deck[:3]}")
    print(f"All aces: {deck[12::13]}")
    for card in deck:
        print(card)
    for card in reversed(deck):
        print(card)
    print(Card("Q", "hearts") in deck)
    print(Card("7", "beasts") in deck)
    print(spades_high(beer_card))
    print("Sorted card deck:")
    for card in sorted(deck, key=spades_high):
        print(card)
