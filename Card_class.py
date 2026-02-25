from enum import Enum
class Card:
    class Color(Enum):
        Spade = 1
        Clubs = 2
        Diamonds = 3
        Hearts = 4
    class Number(Enum):
        Ace = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5
        Six = 6
        Seven = 7
        Eight = 8
        Nine = 9
        Ten = 10
        Jack = 11
        Queen = 12
        King = 13

    def __init__(self, color, number):
        self.Color = color
        self.Number = number

    def display(self):
        suite = ""
        number = str(self.Number.value)
        match self.Color:
            case self.Color.Spade:
                suite = "♠"
            case self.Color.Clubs:
                suite = "♣"
            case self.Color.Diamonds:
                suite = "♦"
            case self.Color.Hearts:
                suite = "♥"
        if self.Number.value == Card.Number.Ace.value or self.Number.value > 9:
            match self.Number:
                case self.Number.Ace:
                    number = "Ace"
                case self.Number.Jack:
                    number = "Jack"
                case self.Number.Queen:
                    number = "Queen"
                case self.Number.King:
                    number = "King"
        print(f"\t{suite} {number} {suite}", end = '   ')