import pack

def test_card_counts():
    deck = pack.get_deck()
    hand = pack.deal(deck, 2)
    assert (len(hand), len(deck)) == (2, 50)

def test_get_pack():
    deck = pack.get_deck()
    assert len(deck) == 52
    assert deck[0] == (0, 'D')