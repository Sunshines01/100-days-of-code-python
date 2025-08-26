import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    card_sum = sum(card_list)

    if card_sum == 21 and len(card_list) == 2:
        return 0  # 0 represents blackjack

    # If over 21 and has Ace, convert Ace from 11 to 1
    if card_sum > 21:
        ace_count = card_list.count(11)
        while card_sum > 21 and ace_count > 0:
            card_list.remove(11)
            card_list.append(1)
            card_sum = sum(card_list)
            ace_count -= 1

    return card_sum


print(art.logo)
play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()

while play == 'y':
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    # Player's turn: keep drawing if they want
    while player_score < 21 and player_score != 0 and input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
        player_cards.append(deal_card())
        player_score = calculate_score(player_cards)  # Recalculate after new card
        print(f"Your cards: {player_cards}, current score: {player_score}")

    # Computer's turn: draw until at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if player_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21:
        print("Computer went over. You win!")
    elif computer_score == 0:
        print("Computer has Blackjack! You lose.")
    elif player_score == 0:
        print("Blackjack! You win!")
    elif player_score == computer_score:
        print("It's a draw.")
    elif player_score > computer_score:
        print("You win!")
    else:
        print("You lose.")

    play = input("Do you want to play again? Type 'y' or 'n': ").lower()

print("Thanks for playing!")
