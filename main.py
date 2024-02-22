import random

cash = 100
dealers_mystery_card = random.randint(2,11)
dealers_main_card = random.randint(2,11)
dealers_cards = [dealers_main_card]
is_blackjack_dealer = dealers_mystery_card + dealers_main_card == 21
users_first_card = random.randint(2,11)
if users_first_card < 11:
    users_second_card = random.randint(1,10)
else:
    users_second_card = random.randint(2,11)
total_card_pile = users_first_card + users_second_card
current_pile = [users_first_card,users_second_card]
future_pile = []
is_blackjack_user = users_first_card + users_second_card == 21
status = 1

def card_addition(list): #This function is to find the total value of cards in the stack
    total_value = 0
    for card in list:
        total_value += card
    return total_value
    
def hit(card_pile, dealers_pile):
    global cash
    global future_pile
    status = ''
    if card_addition(card_pile) < 11:
        card_select = random.randint(2,11)
    else:
        card_select = random.randint(1,10)
    card_pile.append(card_select)
    total_card_pile = card_addition(card_pile)

    total_dealers_pile = card_addition(dealers_pile)
    print()
    
    
    if len(card_pile) == 2 and card_pile[0] == card_pile[1]:
        print("User's cards: "+str(card_pile))
        if cash - bet >= 0 :
            selection = int(input("1. Would you like to split your cards or 2. double your bet? 3. Keep hiting"))
            if selection == 1: #if user wants to split cards
                future_pile.append(card_pile[0])
                card_pile.remove(card_pile[0])
        print()
    if total_card_pile == 21:
        while total_dealers_pile < 16:
            card_select = random.randint(1,11) #same here
            dealers_pile.append(card_select)
            total_dealers_pile = card_addition(dealers_pile)
            print("Dealers")
            print(total_dealers_pile) 
        if total_dealers_pile <= 21 and total_dealers_pile > total_card_pile or is_blackjack_dealer and is_blackjack_user == False :
            print("Dealer won!")
        elif total_card_pile <= 21 and total_dealers_pile < total_card_pile or is_blackjack_user and is_blackjack_dealer == False:
            if is_blackjack_user:
                print("BLACKJACK!")
                cash += bet*1.5
            else:
                print("User won!")
        
        if total_card_pile == total_dealers_pile or is_blackjack_user and is_blackjack_dealer:
            print("It's a tie")
        status = "done"
        
    elif total_card_pile > 21:
        dealers_pile.append(dealers_mystery_card)
        total_dealers_pile = card_addition(dealers_pile)
        print(dealers_pile)
        print()
        print("Dealer's total: "+str(total_dealers_pile))
        print()
        print("its a burst")
        status = "done"
    else:
        total_card_pile = card_addition(card_pile)
        print("Dealer's cards: "+str(dealers_pile))
        print("Dealer's total: "+str(total_dealers_pile))
        print()
        print("User's cards: "+str(card_pile))
        print("User's total cards: "+str(total_card_pile))
        print()
    return status
    
def stand(card_pile, dealers_pile, status): 
    global cash
    total_card_pile = card_addition(card_pile) #checks for the total # of players cards
    dealers_cards.append(dealers_mystery_card) #adds the dealers hidden card
    dealers_total = card_addition(dealers_pile) #updates the dealers total
    print()
    while dealers_total < 16: #dealer keeps hitting until the total is at least 16
        if dealers_total < 11:
            card_select = random.randint(2,11) #add a check for aces
        else:
            card_select = random.randint(1,10)
        dealers_cards.append(card_select)
        dealers_total = card_addition(dealers_pile)
        print("Dealer's cards: "+str(dealers_cards))
        
    if dealers_total > total_card_pile and dealers_total < 22 :
        #print("Dealer's cards: "+str(dealers_cards))
        print("Dealer's total: "+str(dealers_total))
        print()
        print("Dealer won")
        print()
    elif total_card_pile > dealers_total:
        print("Dealers cards: "+str(dealers_cards))
        print("Dealers total: "+str(dealers_total))
        print()
        print("User won")
        print()
        cash += bet*2
    elif dealers_total > 21:
        print("Dealer's total: "+str(dealers_total))
        print()
        print("Dealer bust!")
        print()
        print("User won!")
        cash += bet*2
    else:
        print("Dealers cards: "+str(dealers_pile))
        print('Dealers total: '+str(dealers_total))
        print()
        print("Push!")
        cash += bet
    status = 'done'
    return status
    
#----------------------Game-----------------------------------------------------    

print("Welcome to blackjack.") 
print("Bank: "+str(cash))
print()
bet = int(input("Enter your bet: "))
cash -= bet
print()
print("Dealer's cards: "+str(dealers_cards))
print("Dealer's total: "+str(card_addition(dealers_cards))) #cards dealt
print()
print("User's cards: "+str(current_pile))
print("User's total: "+str(total_card_pile))
print()    


while len(current_pile) > 0 and current_pile[0] == current_pile[1]: #this checks for the split 
    
    if cash - bet >= 0 :
        print()
        selection = int(input("Would you like to split or double your cards? "))
    else:
        selection = int(input("Would you like to double your bet? "))
    
    if selection == 1: #if user wants to split
        cash -= bet
        round = 0 #
        print()
        print()
        future_pile.insert(0, current_pile[0]) 
        current_pile.remove(current_pile[0])

        while len(future_pile) != 0:
            print("Pile "+str(round+1)+":")
            print()
            print("User's cards: "+str(current_pile))
            print("User's total: "+str(total_card_pile))
            print()
            if round > 0:
                future_pile.remove(future_pile[0])
            #print(len(future_pile))
            status = ''
            while status != "done":
                hit_or_not = int(input("Would you like to hit or stand? "))
                print()
                if hit_or_not == 1:
                    status = hit(current_pile, dealers_cards)
                else:
                    status = stand(current_pile, dealers_cards, status)
                if status == 'done':
                    current_pile.clear()
                    if len(future_pile) > 0:
                        current_pile.append(future_pile[0])
                        
                        if future_pile[0] > 10:
                            card_select = random.randint(2,10)
                        else:
                            card_select = random.randint(1,11)
                        current_pile.append(card_select)
                        round += 1
                        
                        break
                    else:
                        break
    elif selection == "2":
        bet *= 2
        cash -= bet/2

     
        status = hit(current_pile, dealers_cards)
        
        status = stand(current_pile, dealers_cards)
        break
    else:
        break
    
    
double = int(input("Would you like to double? 1. Yes 2. No: "))

if double == 1:
    bet *= 2
    cash -= bet/2
        
    status = hit(current_pile, dealers_cards)
        
    status = stand(current_pile, dealers_cards, status)
    


while status != "done":
    if is_blackjack_user: #work on this more
        if is_blackjack_dealer:
            print("Tie")
        else:
            print("User won")
            break
    hit_or_not = int(input("Would you like to hit or stand? "))
    if hit_or_not == 1:
        status = hit(current_pile, dealers_cards)
    else:
        status = stand(current_pile, dealers_cards, status)
