from random import choice
class deckL:
    def __init__(self):
        self.cards=["A♠", "A♥","A♦","A♣",
                   "K♠", "K♥","K♦","K♣", 
                   "Q♠","Q♥","Q♦","Q♣",
                   "J♠","J♥","J♦","J♣",
                   "10♠","10♥","10♦","10♣",
                   "9♠","9♥","9♦","9♣",
                   "8♠","8♥","8♦","8♣",
                   "7♠","7♥","7♦","7♣",
                   "6♠","6♥","6♦","6♣",
                   "5♠","5♥","5♦","5♣",
                   "4♠","4♥","4♦","4♣",
                   "3♠","3♥","3♦","3♣",
                   "2♠","2♥","2♦","2♣"]
        self.dealer=[]
        self.player=[]
    def deal(self,deck):
        c1=choice(deck)
        deck.remove(c1)
        c2=choice(deck)
        deck.remove(c2)
        c3=choice(deck)
        deck.remove(c3)
        c4=choice(deck)
        deck.remove(c4)
        self.dealer = [c1,c3]
        self.player = [c2,c4]
    
    def hit(self,hand,deck):
        card = choice(deck)
        deck.remove(card)
        self.player = self.player + [card]

    def dealHit(self,hand,deck):
        card = choice(deck)
        deck.remove(card)
        self.dealer = self.dealer + [card]

    
