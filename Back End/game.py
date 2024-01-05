import deckL
import handValue
from flask import Flask

app = Flask(__name__)

@app.route("/main")
def main():
    #stack = int(input("What's your buy in? \n"))
    #while stack > 0: 
    #    stack = round(stack)
    #    print("Your stack is:", stack)
    return {"bofa":["hi","hi2"]} 
    
def round(stack):
    bet = int(input("How much would you like to bet? \n"))
    while bet > stack or bet < 0: 
        print("Please bet a valid amount")
        bet = int(input("How much would you like to bet? \n"))
        if bet == -1:
            return -1
    deck = deckL.deckL()
    deck.deal(deck.cards)
    handVal = handValue.handValue.handVal(deck.player)
    print("Dealer:",deck.dealer[0])
    print("You:", deck.player[0]+" "+deck.player[1])
    if handVal[0] == 21: 
        print("Blackjack! You win: ",float(bet)*1.5)
        return stack + float(bet)*1.5
    move = input("Hit or Stay? \n")
    while (move == "hit" or move == "Hit") and handVal[1] < 22:
        if move == "hit" or move == "Hit":
            deck.hit(deck.player,deck.cards)
        print("Your Hand:", deck.player)
        if handValue.handValue.handVal(deck.player)[1] > 21:
            print('You lose',bet)
            return stack - bet 
        move = input("Hit or Stay? \n")
        handVal = handValue.handValue.handVal(deck.player)
    print("Dealer's hand:",deck.dealer)
    while (handValue.handValue.handVal(deck.dealer)[0] < 17) or (handValue.handValue.handVal(deck.dealer)[0] > 21 and handValue.handValue.handVal(deck.dealer)[1] < 18): 
        deck.dealHit(deck.dealer,deck.cards)
        print(deck.dealer)
    result = detWin(deck.dealer,handVal, bet)
    return stack + result 
    

def detWin(dealer, handVal, bet):
    if handValue.handValue.handVal(dealer)[1] > 21:
        return bet
    
    # Using player's soft count
    elif handVal[0] > 21: 
        # Comparing player's soft count to dealer's soft count
        if handValue.handValue.handVal(dealer)[0] > 21:
            if handVal[1] > handValue.handValue.handVal(dealer)[1]:
                print("You win", bet)
                return bet
            elif handVal[1] == handValue.handValue.handVal(dealer)[1]:
                print("Push")
                return 0
            else: 
                print("You lose",bet)
                return bet * -1 
        # Comparing player's soft count to dealer's hard count
        else:
            if handVal[1] > handValue.handValue.handVal(dealer)[0]:
                print("You win", bet)
                return bet
            elif handVal[1] == handValue.handValue.handVal(dealer)[0]:
                print("Push")
                return 0
            else: 
                print("You lose",bet)
                return -1 * bet 
            
    # Using player's hard count  
    else: 
        # Comparing player's hard count to dealer's soft count
        if handValue.handValue.handVal(dealer)[0] > 21:
            if handVal[0] > handValue.handValue.handVal(dealer)[1]:
                print("You win", bet)
                return bet
            elif handVal[0] == handValue.handValue.handVal(dealer)[1]:
                print("Push")
                return 0
            else:
                print("You lose",bet) 
                return -1 * bet 
        # Comparing player's hard count to dealer's soft count 
        else:
            if handVal[0] > handValue.handValue.handVal(dealer)[0]:
                print("You win", bet)
                return bet
            elif handVal[0] == handValue.handValue.handVal(dealer)[0]:
                print("Push")
                return 0 
            else: 
                print("You lose",bet) 
                return -1 * bet 

if __name__ == "__main__":
    app.run(debug=True, host = '0.0.0.0')