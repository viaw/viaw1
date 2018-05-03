import pack

def test_card_counts():
    deck = pack.get_deck()
    hand = pack.deal(deck, 2)
    assert (len(hand), len(deck)) == (2, 50)