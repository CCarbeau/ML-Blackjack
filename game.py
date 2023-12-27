import Deck
import handValue

def main():
    deck = Deck.Deck()
    round(deck.deck)
    
def round(stack):
    bet = input("How much would you like to bet? \n")
    deck = Deck.Deck()
    deck.deal(deck.deck)
    handVal = handValue.handValue.handVal(deck.player)
    print("Dealer:",deck.dealer[0])
    print("You:", deck.player[0]+" "+deck.player[1])
    if handVal[0] == 21: 
        print("Blackjack! You win: ",float(bet)*1.5)
        return 
    move = input("Hit or Stay? \n")
    while (move == "hit" or move == "Hit") and handVal[1] < 22:
        if move == "hit" or move == "Hit":
            deck.hit(deck.player,deck.deck)
        print("Your Hand:", deck.player)
        if handValue.handValue.handVal(deck.player)[1] > 21:
            print('You lose',bet)
            return
        move = input("Hit or Stay? \n")
        handVal = handValue.handValue.handVal(deck.player)
    print("Dealer's hand:",deck.dealer)
    while handValue.handValue.handVal(deck.dealer)[1] < 17: 
        deck.dealHit(deck.dealer,deck.deck)
        print(deck.dealer)
    print(detWin(deck.dealer,handVal, bet))

def detWin(dealer, handVal, bet):
    if handValue.handValue.handVal(dealer)[1] > 21:
        return "You win: " + bet
    
    # Using player's soft count
    elif handVal[0] > 21: 
        # Comparing player's soft count to dealer's soft count
        if handValue.handValue.handVal(dealer)[0] > 21:
            if handVal[1] > handValue.handValue.handVal(dealer)[1]:
                return"You win: " + bet
            elif handVal[1] == handValue.handValue.handVal(dealer)[1]:
                return "Tie"
            else: 
                return "You lose: " + bet
        # Comparing player's soft count to dealer's hard count
        else:
            if handVal[1] > handValue.handValue.handVal(dealer)[0]:
                return "You win: " + bet
            elif handVal[1] == handValue.handValue.handVal(dealer)[0]:
                return"Tie"
            else: 
                return"You lose: " + bet
            
    # Using player's hard count  
    else: 
        # Comparing player's hard count to dealer's soft count
        if handValue.handValue.handVal(dealer)[0] > 21:
            if handVal[0] > handValue.handValue.handVal(dealer)[1]:
                return "You win: " + bet
            elif handVal[0] == handValue.handValue.handVal(dealer)[1]:
                return "Tie"
            else: 
                return "You lose: " + bet
        # Comparing player's hard count to dealer's soft count 
        else:
            if handVal[0] > handValue.handValue.handVal(dealer)[0]:
                return"You win: " + bet
            elif handVal[0] == handValue.handValue.handVal(dealer)[0]:
                return"Tie"
            else: 
                return"You lose: " +  bet

if __name__ == "__main__":
    main()