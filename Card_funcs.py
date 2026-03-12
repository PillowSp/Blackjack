import Card_class as Card
import random
def create_deck():
    cards = []
    for color in Card.Card.Color:
        for number in Card.Card.Number:
            card = Card.Card(color, number)
            cards.append(card)
    return cards

def shuffle_cards(cards):
    new_deck = []
    size = len(cards)
    for i in range(size):
        r = random.randint(0, size - 1)
        new_deck.append(cards[r])
        del cards[r]
        size -= 1
    for c in new_deck:
        cards.append(c)

def draw(deck, player):
    player.hand.append(deck[0])
    deck.pop(0)
    if player.hand[-1].Number.value > 10:
        player.total += 10
    else:
        if player.hand[-1].Number.value == Card.Card.Number.Ace.value:
            player.aces += 1
            player.total += 11
        else:
            player.total += player.hand[-1].Number.value
    if player.total > 21 and player.aces > 0:
        player.total -= 10
        player.aces -= 1

def show_cards(dealer, player):
    print("Dealer\'s hand:")
    for c in dealer.hand:
        c.display()
    print(f"\n\t{dealer.total}")
    print("\nPlayer\'s hand:")
    for c in player.hand:
        c.display()
    print(f"\n\t{player.total}")

def instructions():
    print("Hit [F]: Draw another card. You get a blackjack when your sum will be equal to 21, however when it is greater than 21 you automatically lose")
    print("Stand [G]: Stop drawing cards. End your turn.")
    print("Double Down [H]: Double your bet and draw one more card. You stop drawing after doing this action.")
    print("Surrender [Q]: Give up on this game. Halve your original bet.")