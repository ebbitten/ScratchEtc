def main():
    while True:
        nexuses_left = int(input("Nexuses: \n"))
        cards_left = int(input("cards_left: \n"))
        number_viewed = int(input("number_viewed: \n"))
        print(calc_nexus(nexuses_left, cards_left, number_viewed))
        

def calc_nexus(nexuses_left, cards_left, cards_viewing=4):
    not_drawn = 1
    for card_viewed in range(cards_viewing):
        not_drawn *= (cards_left - nexuses_left) / cards_left
        cards_left -= 1
    return (1 - not_drawn)

main()