import pack
deck = pack.get_deck()
hand = pack.deal(deck, 2)
print(len(hand), len(deck))