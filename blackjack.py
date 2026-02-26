import Card_funcs as funcs
import os
import msvcrt
import time

class Player:
    hand = []
    total = 0
    aces = 0

#-------------------------------------------------------------------------------------
# TURN ON EMULATE TERMINAL IN OUTPUT CONSOLE

# GET SAVED MONEY
with open('bet.txt', 'r') as file:
    bank = int(file.readline())

# CREATE DATA FOR PLAYER AND DEALER
end_game = False
dealer = Player()
player = Player()

# START OF GAME
while not end_game:

    # STARTING VALUES
    player_win = False
    end_round = False
    dealer.hand = []
    player.hand = []
    dealer.total = 0
    player.total = 0
    dealer.aces = 0
    player.aces = 0

    # PLACE BET
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Bet 0 to quit\nMoney: {bank}\nBet: ", end = '')
        bet = int(input())
        if 0 < bet <= bank:
            break
        elif bet > bank:
            bet = bank
            break
        elif bet == 0:
            end_game = True
            end_round = True
    os.system('cls' if os.name == 'nt' else 'clear')

    # PREPARE DECKS
    cards = funcs.create_deck()
    funcs.shuffle_cards(cards)

    # START DRAWING
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
        # CHECK IF REACHED END OF DECK
        if len(cards) == 0:
            cards = funcs.create_deck()
            funcs.shuffle_cards(cards)

        # BEGIN ROUND
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Money: {bank}\nBet: {bet}")
        funcs.show_cards(dealer, player)
        print("\nHit [F] Stand [H] Quit [Q]")
        while True:
            getch = msvcrt.getwch()
            time.sleep(0.1)
            match getch:
                case 'f' | 'F':     # HIT
                    funcs.draw(cards, player)
                    break
                case 'h' | 'H':     # STAND
                    end_round = True
                    break
                case 'q' | 'Q':     # QUIT - AUTO LOSE
                    player.total = 22
                    end_round = True
                    end_game = True
                    break
        if player.total > 21:
            end_round = True

    # PLAYER'S TURN ENDS - DEALER DRAWS
    while dealer.total < 17:
        funcs.draw(cards, dealer)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Money: {bank}\nBet: {bet}")
    funcs.show_cards(dealer, player)

    # WIN CONDITIONS
    if player.total > 21:
        print("You lost")
    elif player.total == 21:
        if dealer.total == 21:
            print("Draw")
            bank += bet
        else:
            print("You won")
            player_win = True
    elif player.total == dealer.total:
        print("Draw")
        bank += bet
    elif player.total > dealer.total:
        print("You won")
        player_win = True
    elif dealer.total > 21:
        print("You won")
        player_win = True
    elif dealer.total > player.total:
        print("You lost")

    # GET OR LOSE MONEY
    if player_win:
        bank += bet
    else:
        bank -= bet
        # don't go broke - doesn't work in real life
        if bank <= 0:
            bank += 1000

    # END ROUND
    print("\nPress any button to continue or [Q] to quit")
    getch = msvcrt.getwch()
    if getch == 'q' or getch == 'Q':
        end_round = True
        end_game = True
    os.system('cls' if os.name == 'nt' else 'clear')

# SAVE NEW BANK VALUE
with open("bet.txt", 'w') as file:
    file.write(str(bank))