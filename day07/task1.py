import functools

input_file = open("input.txt", "r")

hands = []

power_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

for line in input_file:
    cards, bid = map(str, line.strip().split())
    bid = int(bid)
    cards = list(cards)
    hands.append({"cards" : cards, "bid" : bid})

input_file.close()

hands_by_power_level = { 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [] }

for hand in hands:
    cards = hand["cards"]
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
