class handValue:
    @staticmethod
    def handVal(cards):
        valH = 0
        valS = 0
        for card in cards:
            num = card[:-1]
            if num == "2":
                valH+=2
                valS+=2
            elif num == "3":
                valH+=3
                valS+=3
            elif num == "4":
                valH+=4
                valS+=4
            elif num == "5":
                valH+=5
                valS+=5
            elif num == "6":
                valH+=6
                valS+=6
            elif num == "7":
                valH+=7
                valS+=7
            elif num == "8":
                valH+=8
                valS+=8
            elif num == "9":
                valH+=9
                valS+=9
            elif num == "10":
                valH+=10
                valS+=10
            elif num == "J":
                valH+=10
                valS+=10
            elif num == "Q":
                valH+=10
                valS+=10
            elif num == "K":
                valH+=10
                valS+=10
            elif num == "A":
                valH+=11
                valS+=1
        return [valH,valS]
            
