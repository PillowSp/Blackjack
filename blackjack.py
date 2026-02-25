import Card_funcs as funcs
import os
import msvcrt
import time

class Player:
    hand = []
    total = 0
    aces = 0

#-------------------------------------------------------------------------------------

end_game = False
dealer = Player()
player = Player()
# START OF GAME
while not end_game:
    end_round = False
    dealer.aces = 0
    player.aces = 0
    # PREPARE DECKS
    cards = funcs.create_deck()
    funcs.shuffle_cards(cards)
    dealer.hand = []
    dealer.total = 0
    player.hand = []
    player.total = 0

    funcs.draw(cards, dealer)
    # CHECK IF DEALER GOT BLACKJACK
    if dealer.total >= 10:
        old_dealer_total = dealer.total
        funcs.draw(cards, dealer)
        if dealer.total == 21:
            end_round = True
        else:
            dealer.hand.pop(-1)
            dealer.total = old_dealer_total

    funcs.draw(cards, player)
    funcs.draw(cards, player)

    while not end_round:
        if len(cards) == 0:
            cards = funcs.create_deck()
            funcs.shuffle_cards(cards)
        # BEGIN ROUND
        # TURN ON EMULATE TERMINAL IN OUTPUT CONSOLE
        funcs.show_cards(dealer, player)
        print("\nHit [F] Stand [H] Quit [Q]")
        while(True):
            getch = msvcrt.getwch()
            time.sleep(0.1)
            match getch:
                case 'f' | 'F':     # HIT
                    funcs.draw(cards, player)
                    break
                case 'h' | 'H':     # STAND
                    end_round = True
                    break
                case 'q' | 'Q':     # QUIT
                    end_round = True
                    end_game = True
                    break
        if player.total > 21:
            end_round = True

    # PLAYER'S TURN ENDS
    while dealer.total < 17:
        funcs.draw(cards, dealer)

    funcs.show_cards(dealer, player)
    # WIN CONDITIONS
    if player.total > 21:
        print("You lost")
    elif player.total == 21:
        if dealer.total == 21:
            print("Draw")
        else:
            print("You won")
    elif player.total == dealer.total:
        print("Draw")
    elif player.total > dealer.total:
        print("You won")
    elif dealer.total > 21:
        print("You won")
    elif dealer.total > player.total:
        print("You lost")

    # END ROUND
    print("\nPress any button to continue")
    getch = msvcrt.getwch()
    os.system('cls' if os.name == 'nt' else 'clear')