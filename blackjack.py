from p1_random import P1Random
rng = P1Random()
def printMenu():
    print("1. Get another card", "\n2. Hold hand", "\n3. Print statistics", "\n4. Exit")
game_continue = True
game_num = 0
player_win = 0
dealer_win = 0
ties = 0
#keeps track of number of games
while game_continue:
    game_num += 1
    print(f"START GAME#{game_num}")
    my_hand = 0
    card = rng.next_int(13)+ 1 #card automatically added to player hand
    if 2 <= card <= 10:
        print("\nYour card is a ", card, '!', sep='')
        my_hand = my_hand + card
    elif card == 1:
        print("Your card is a ACE!",)
        card = 1
        my_hand = my_hand + card
    elif card == 11:
        print("Your card is a JACK!")
        card = 10
        my_hand = my_hand + card
    elif card == 12:
        print("Your card is a QUEEN!")
        card = 10
        my_hand = my_hand + card
    else:
        print("Your card is a KING!")
        card = 10
        my_hand = my_hand + card
    print("Your hand is:", my_hand)
    progress = True #boolean loop used so it does not automatically go back to the very top
    while progress:
        printMenu() #prints out the menu options
        print("Choose an option:")
        operation = int(input())
        if operation == 1:
            card = rng.next_int(13) + 1
            if 2 <= card <= 10: #reprinted the card values so that the player hand changes
                print("\nYour card is a ",card,'!',sep='')
                my_hand = my_hand + card
            elif card == 1:
                print("Your card is a ACE!")
                card = 1
                my_hand = my_hand + card
            elif card == 11:
                print("Your card is a JACK!")
                card = 10
                my_hand = my_hand + card
            elif card == 12:
                print("Your card is a QUEEN!")
                card = 10
                my_hand = my_hand + card
            else:
                print("Your card is a KING!")
                card = 10
                my_hand = my_hand + card
            print("Your hand is:", my_hand)
            if my_hand > 21:
                print("You exceeded 21! You lose.")
                dealer_win = dealer_win + 1
                progress = False
            elif my_hand == 21:
                print("BLACKJACK! You win!")
                player_win = player_win + 1
                progress = False
        elif operation == 2:
            dealer_hand = rng.next_int(11) + 16
            print("Dealer's hand:", dealer_hand)
            print("Your hand is:", my_hand)
            if dealer_hand > 21:
                print("You win!")
                player_win = player_win + 1
                progress = False #changed progress to false so that it starts a new game
            elif dealer_hand == my_hand:
                print("It's a tie! No one wins!")
                ties = ties + 1
                progress = False
            elif dealer_hand == 21:
                print("Dealer wins!")
                dealer_win = dealer_win + 1
                progress = False
            elif dealer_hand > my_hand:
                print("Dealer wins!")
                dealer_win = dealer_win + 1
                progress = False
            elif dealer_hand < my_hand:
                print("You win!")
                player_win = player_win + 1
                progress = False
        elif operation == 3:
            game_num -= 1
            print("Number of Player wins:", player_win)
            print("Number of Dealer wins:", dealer_win)
            print("Number of tie games:", ties)
            print("Total # of games played is:", game_num)
            percent = (player_win/game_num) * 100
            print("Percentage of Player wins: ", round(percent,1), '%', sep='')
        elif operation == 4:
            progress = False
            game_continue = False #both progress and game_continue false so that it exits the program
        else:
            print("Invalid input!", "\nPlease enter an integer value between 1 and 4.")
