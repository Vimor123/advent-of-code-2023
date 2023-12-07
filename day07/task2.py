import functools

input_file = open("input.txt", "r")

hands = []

power_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

for line in input_file:
    cards, bid = map(str, line.strip().split())
    bid = int(bid)
    cards = list(cards)
    hands.append({"cards" : cards, "bid" : bid})

input_file.close()

hands_by_power_level = { 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [] }

for hand in hands:
    cards = hand["cards"]

    if "J" not in cards:
        count = {}
        for card in cards:
            if card not in count:
                count[card] = 1
            else:
                count[card] += 1

        sorted_count_values = sorted(count.values())
        sorted_count_values.reverse()

        if sorted_count_values[0] == 5:
            hands_by_power_level[7].append(hand)

        elif sorted_count_values[0] == 4:
            hands_by_power_level[6].append(hand)

        elif sorted_count_values[0] == 3 and sorted_count_values[1] == 2:
            hands_by_power_level[5].append(hand)

        elif sorted_count_values[0] == 3:
            hands_by_power_level[4].append(hand)

        elif sorted_count_values[0] == 2 and sorted_count_values[1] == 2:
            hands_by_power_level[3].append(hand)

        elif sorted_count_values[0] == 2:
            hands_by_power_level[2].append(hand)

        else:
            hands_by_power_level[1].append(hand)

    else:
        max_power_level = 0
        for joker_card in power_order:
            current_cards = cards.copy()
            for i in range(len(current_cards)):
                if current_cards[i] == "J":
                    current_cards[i] = joker_card
            count = {}
            for card in current_cards:
                if card not in count:
                    count[card] = 1
                else:
                    count[card] += 1

            sorted_count_values = sorted(count.values())
            sorted_count_values.reverse()

            if sorted_count_values[0] == 5:
                max_power_level = 7

            elif sorted_count_values[0] == 4 and max_power_level < 6:
                max_power_level = 6

            elif sorted_count_values[0] == 3 and sorted_count_values[1] == 2 and max_power_level < 5:
                max_power_level = 5

            elif sorted_count_values[0] == 3 and max_power_level < 4:
                max_power_level = 4

            elif sorted_count_values[0] == 2 and sorted_count_values[1] == 2 and max_power_level < 3:
                max_power_level = 3

            elif sorted_count_values[0] == 2 and max_power_level < 2:
                max_power_level = 2

            elif max_power_level < 1:
                max_power_level = 1

        hands_by_power_level[max_power_level].append(hand)
        

def compare(hand1, hand2):
    cards1 = hand1["cards"]
    cards2 = hand2["cards"]
    
    for i in range(len(cards1)):
        if power_order.index(cards1[i]) > power_order.index(cards2[i]):
            return 1
        elif power_order.index(cards1[i]) < power_order.index(cards2[i]):
            return -1

    return 0


all_hands = []

for power_level in sorted(hands_by_power_level.keys()):
    hands = hands_by_power_level[power_level]
    sorted_hands = sorted(hands, key = functools.cmp_to_key(compare))
    for hand in sorted_hands:
        all_hands.append(hand)

s = 0
for index, hand in enumerate(all_hands):
    s += hand["bid"] * (index + 1)

print(s)
