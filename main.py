# CS 461 Spring 2022 Program 1
# Jake Cross: jackgw@umsystem.edu

"""for a in deck:
    print(a, end=" ")
print()"""
import random


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = self.rank
        return str(rank) + self.suit

    def __eq__(self, other):
        return self.rank == other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __sub__(self, other):
        return self.rank - other.rank


class Player:
    def __init__(self, hand, value=1):
        self.hand = hand
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def evaluate(self):
        self.hand.sort(reverse=True)
        if isFlush(self.hand) and isStraight(self.hand):
            self.value = 9
        elif isFour(self.hand):
            self.value = 8
        elif isFull(self.hand):
            self.value = 7
        elif isFlush(self.hand):
            self.value = 6
        elif isStraight(self.hand):
            self.value = 5
        elif isThree(self.hand):
            self.value = 4
        elif isTwo(self.hand):
            self.value = 3
        elif isOne(self.hand):
            self.value = 2
        else:
            self.value = 1


def isOne(hand):
    for i in range(4):
        for j in range(i + 1, 5):
            if hand[i] == hand[j]:
                return True
    return False


def isTwo(hand):
    count = 0
    for i in range(4):
        for j in range(i + 1, 5):
            if hand[i] == hand[j]:
                count += 1
                break
        if count == 2:
            return True
    return False


def isThree(hand):
    for i in range(4):
        count = 0
        for j in range(i + 1, 5):
            if hand[i] == hand[j]:
                count += 1
        if count == 2:
            return True
    return False


def isFull(hand):
    if isThree(hand):
        count = 0
        for i in range(4):
            for j in range(i + 1, 5):
                if hand[i] == hand[j]:
                    count += 1
            if count == 4:
                return True
    return False


def isFour(hand):
    for i in range(4):
        count = 0
        for j in range(i + 1, 5):
            if hand[i] == hand[j]:
                count += 1
        if count == 3:
            return True
    return False


def isStraight(hand):
    if hand[0].rank == 14 and hand[4].rank == 2 and hand[3].rank == 3 and hand[2].rank == 4 and hand[1].rank == 5:
        return True
    else:
        for i in range(4):
            if hand[i] - hand[i + 1] != 1:
                return False
        return True


def isFlush(hand):
    ini_suit = hand[0].suit
    for i in range(1, 5):
        if hand[i].suit != ini_suit:
            return False
    return True


def isRoyal(hand):
    if isFlush(hand) and isStraight(hand):
        if hand[4].rank == 10:
            return True
    return False


def strongest(players):
    high_p = players[0]
    for p in range(1, len(players) - 1):
        if high(high_p, players[p]) == 0:
            high_p = players[p]
    return high_p


def high(p1, p2):
    if p1 > p2:
        return 1
    elif p1 == p2:
        for k in range(5):
            if p1.hand[k] > p2.hand[k]:
                return 1
            elif p1.hand[k] == p2.hand[k]:
                continue
            else:
                return 0
        return 0.5
    else:
        return 0


RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
SUITS = ('S', 'H', 'D', 'C')
deck = []
high_card = {"win": 0, "count": 0}
one_pair = {"win": 0, "count": 0}
two_pair = {"win": 0, "count": 0}
three_card = {"win": 0, "count": 0}
full_house = {"win": 0, "count": 0}
four_card = {"win": 0, "count": 0}
straight = {"win": 0, "count": 0}
flush = {"win": 0, "count": 0}
st_flush = {"win": 0, "count": 0}
# Create a deck
for number in RANKS:
    for char in SUITS:
        deck.append(Card(number, char))

outfile = open("log.txt", 'w')
# Continuing for more than 500 times
for i in range(1, 1001):
    computers = []
    random.shuffle(deck)
    you = Player(deck[:5])
    com1 = Player(deck[5:10])
    com2 = Player(deck[10:15])
    com3 = Player(deck[15:20])
    com4 = Player(deck[20:25])
    com5 = Player(deck[25:30])
    you.evaluate()
    com1.evaluate()
    com2.evaluate()
    com3.evaluate()
    com4.evaluate()
    com5.evaluate()
    computers.append(com1)
    computers.append(com2)
    computers.append(com3)
    computers.append(com4)
    computers.append(com5)
    for c in you.hand:
        outfile.write(str(c) + ", ")
    """
    outfile.write(" vs ")
    print()
    for c in strongest(computers).hand:
        outfile.write(str(c) + ", ")
    """

    result = high(you, strongest(computers))
    percentage = 0
    if you.value == 9:
        st_flush["win"] += result
        st_flush["count"] += 1
        percentage = round(st_flush["win"] / st_flush["count"] * 100, 2)
        if isRoyal(you.hand):
            outfile.write("Royal Straight Flush!!!, " + str(percentage) + "%")
        else:
            outfile.write("Straight Flush, " + str(percentage) + "%")
    elif you.value == 8:
        four_card["win"] += result
        four_card["count"] += 1
        percentage = round(four_card["win"] / four_card["count"] * 100, 2)
        outfile.write("Four of a Kind, " + str(percentage) + "%")
    elif you.value == 7:
        full_house["win"] += result
        full_house["count"] += 1
        percentage = round(full_house["win"] / full_house["count"] * 100, 2)
        outfile.write("Full House, " + str(percentage) + "%")
    elif you.value == 6:
        flush["win"] += result
        flush["count"] += 1
        percentage = round(flush["win"] / flush["count"] * 100, 2)
        outfile.write("Flush, " + str(percentage) + "%")
    elif you.value == 5:
        straight["win"] += result
        straight["count"] += 1
        percentage = round(straight["win"] / straight["count"] * 100, 2)
        outfile.write("Straight, " + str(percentage) + "%")
    elif you.value == 4:
        three_card["win"] += result
        three_card["count"] += 1
        percentage = round(three_card["win"] / three_card["count"] * 100, 2)
        outfile.write("Three of a Kind, " + str(percentage) + "%")
    elif you.value == 3:
        two_pair["win"] += result
        two_pair["count"] += 1
        percentage = round(two_pair["win"] / two_pair["count"] * 100, 2)
        outfile.write("Two Pair, " + str(percentage) + "%")
    elif you.value == 2:
        one_pair["win"] += result
        one_pair["count"] += 1
        percentage = round(one_pair["win"] / one_pair["count"] * 100, 2)
        outfile.write("One Pair, " + str(percentage) + "%")
    else:
        high_card["win"] += result
        high_card["count"] += 1
        percentage = round(high_card["win"] / high_card["count"] * 100, 2)
        outfile.write("High Card, " + str(percentage) + "%")
    outfile.write("\n")
outfile.close()
