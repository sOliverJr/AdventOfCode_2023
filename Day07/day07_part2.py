
file_name = 'Day07/input_day07.txt'
input_array = []
file = open(file_name, 'r')
for line in file:
    input_array.append(line.strip())


card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}


class Hand:
    def __init__(self, cards: str, bid):
        self.cards_string = cards
        self.cards = list(cards)
        self.bid = int(bid)


# Cast input into hands
sorted_input_array = []
for line in input_array:
    split_line = line.split(' ')
    sorted_input_array.append(Hand(split_line[0], split_line[1]))


def get_type_of_hand(hand: Hand):
    # {card: amount, card2: amount2}
    cards_with_amount = {'J': 0}
    for card in hand.cards:
        if card in cards_with_amount.keys():
            cards_with_amount[card] += 1
        else:
            cards_with_amount.update({card: 1})

    amount_of_jokers = cards_with_amount['J']
    if amount_of_jokers == 5:
        return 6        # 'Five of a kind'
    del cards_with_amount['J']

    # Add the amount of jokers to the card with the highest amount
    highest_amount_of_cards = 0
    card_with_highest_amount = 'X'
    for card in cards_with_amount:
        if cards_with_amount[card] > highest_amount_of_cards:
            card_with_highest_amount = card
            highest_amount_of_cards = cards_with_amount[card]
    cards_with_amount[card_with_highest_amount] += amount_of_jokers

    if 5 in cards_with_amount.values():
        return 6        # 'Five of a kind'
    elif 4 in cards_with_amount.values():
        return 5        # 'Four of a kind'
    elif 3 in cards_with_amount.values() and 2 in cards_with_amount.values():
        return 4        # 'Full house'
    elif 3 in cards_with_amount.values():
        return 3        # 'Three of a kind'
    elif list(cards_with_amount.values()).count(2) == 2:
        return 2        # 'Two pair'
    elif 2 in cards_with_amount.values():
        return 1        # 'One pair'
    else:
        return 0        # 'High card'


def compare_hands(hand_one: Hand, hand_two: Hand) -> bool:
    """Returns True if both cards are in order and False if not"""
    type_hand_one = get_type_of_hand(hand_one)
    type_hand_two = get_type_of_hand(hand_two)

    if type_hand_one < type_hand_two:       # hand one is lower than hand two
        return True
    if type_hand_one > type_hand_two:       # hand one is higher than hand two
        return False
    if type_hand_one == type_hand_two:
        for i in range(len(hand_one.cards)):
            if card_values[hand_one.cards[i]] < card_values[hand_two.cards[i]]:
                return True
            if card_values[hand_one.cards[i]] > card_values[hand_two.cards[i]]:
                return False
            else:
                continue


def bubble_sort_hands(array_of_hands: [Hand]):
    """Standard bubble-sort adapted fpr sorting hands"""
    n = len(array_of_hands)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if not compare_hands(array_of_hands[j], array_of_hands[j+1]):
                array_of_hands[j], array_of_hands[j + 1] = array_of_hands[j+1], array_of_hands[j]


output = 0
bubble_sort_hands(sorted_input_array)

for x, hand in enumerate(sorted_input_array):
    output += (x+1) * hand.bid

print(output)
