import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """gives cards at random to both player and computer"""
    card =random.choice(cards)
    return card

def calculate_score(cards):
    """It ensures the cards are the required number at the start,
    adds the given to ensure their 21 and finally works the logic of whether an ACE should be 11 or 1"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    """contains teh comparasion logic"""
    if u_score == 0 and c_score == 0:
        return "It's a draw, both have BlackJacks!"
    elif c_score == 0:
        return "Lose, Computer has a Blackjack"
    elif u_score == 0:
        return "You win, Blackjack!"
    elif u_score > 21:
        return "You lose. score over 21!"
    elif c_score > 21:
        return "Computer loses, score over 21!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

def play_again():
    """contains main game logic"""
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = 0
    user_score = 0
    game_over = False

    for card in range(2):
        user_cards.append(deal_card()) #here i attached cards to the user and computer list by calling the deal function
        computer_cards.append(deal_card()) # then attaching 2 cards, in list we count from 0

    while not game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"Your cards are: {user_cards} & current score: {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal_again = input("Type Y for another card or N not to.\n").lower()
            if user_deal_again == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score <= 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards are: {user_cards} & current score: {user_score}")
    print(f"Computer's final cards are: {computer_cards} & current score: {computer_score}")
    print(compare(user_score, computer_score))


while True:
    play = input("Do you want to play Black game?? Type 'Y' to play or 'N' not to.\n").lower()
    if play == "y":
        print("\n" * 25)
        play_again()
    elif play == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice, please enter Y/N")


if __name__ =="__main.py__":
     play_again()










