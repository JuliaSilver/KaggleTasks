def blackjack_hand_greater_than(hand_1, hand_2):
    """

    TASK STARTS
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    pass
 #MY CODE STARTS

    def counts(list):
        a = 0
        total = 0
        for elem in list:
            if (elem == 'J') or (elem == 'Q') or (elem == 'K'):
                total += 10
            elif elem in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                total += int(elem)
            elif elem == 'A':
                a += 1
                total += 11
        return total, a

    def check_total(total, a):
        if total > 21:
            total = total - 11 + 1
            if total > 21 and a > 1:
                total = total - 11 + 1
        return total


    total_1, a_1 = counts(hand_1)
    total_2, a_2 = counts(hand_2)
    if a_1 != 0:
        total_1 = check_total(total_1, a_1)
    if a_2 != 0:
        total_2 = check_total(total_2, a_2)


    print(total_1, total_2)
    if (total_1 > total_2) and (total_1 <= 21):
        return True
    if (total_1 <= 21) and (total_2 > 21):
        return True
    else:
        return False
