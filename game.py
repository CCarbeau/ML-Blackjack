import Deck
import handValue

def main():
    deck = Deck.Deck()
    round(deck.deck)
    
def round(stack):
    deck = Deck.Deck()
    deck.deal(deck.deck)
    handVal = handValue.handValue.handVal(deck.player)
    print(deck.player)
    print(handVal)

if __name__ == "__main__":
    main()