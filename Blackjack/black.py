import random
cards=[]
suits=["spades","club","haerts","diamonds"]
ranks=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit,rank])

def shuffle():
    random.shuffle(cards)

def deal(number):
    cards_dealt=[]
    for x in range(number)
        card=cards.pop()
        cards_dealt.append(card)
    return card_dealt

shuffle()
card_dealt=deal(2)
card = cards_dealt[]

print(card_dealt)        