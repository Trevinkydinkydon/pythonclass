import random

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f"{rank} of {suit}")

# Define function to calculate the value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        rank = card.split()[0]
        if rank == 'Ace':
            num_aces += 1
            value += 11
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        else:
            value += int(rank)
    while num_aces > 0 and value > 21:
        value -= 10
        num_aces -= 1
    return value

# Define function to check if a hand is a bust (value > 21)
def is_bust(hand):
    return calculate_hand_value(hand) > 21

# Shuffle the deck
random.shuffle(deck)

# Deal initial hands
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop()]

# Player turn
while True:
    print(f"Player's hand: {player_hand}")
    print(f"Dealer's hand: [{dealer_hand[0]}, ?]")
    action = input("Would you like to hit or stand? ")
    if action.lower() == 'hit':
        player_hand.append(deck.pop())
        if is_bust(player_hand):
            print("Bust! Dealer wins.")
            break
    elif action.lower() == 'stand':
        break

# Dealer turn
if not is_bust(player_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print(f"Player's hand: {player_hand}")
    print(f"Dealer's hand: {dealer_hand}")
    if is_bust(dealer_hand):
        print("Dealer busts! Player wins.")
    elif calculate_hand_value(dealer_hand) >= calculate_hand_value(player_hand):
        print("Dealer wins.")
    else:
        print("Player wins!")

