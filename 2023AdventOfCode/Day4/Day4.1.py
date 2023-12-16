import re

with open ('input.txt') as file:
    data = file.readlines()

line_list = []

#Line Clean Up
for line in data:
    fix_line = line.strip('\n')
    line_list += [fix_line]
#print (line_list) 


def CardsWon(card): 
    cards_won = []
    total_matches = 0
    card_list = re.split('[,|:]',str(card))
        #Get Winning Numbers    
    winning_numbers = card_list [1]
    winning_numbers = str(winning_numbers).split()
        #Get Your Numbers
    your_numbers = card_list [2]
    your_numbers = str(your_numbers).split()

        #Get Game Number
    game_number = str(card_list[0]).split()
    game_number = (int(game_number[1]))


        #print (your_numbers)
    for winning_number in winning_numbers:
            for your_number in your_numbers:
                if winning_number == your_number:
                    total_matches += 1
                    numberofcard = game_number + total_matches
                    cards_won.append(numberofcard)          
    return cards_won


cardswon = CardsWon(line_list[0])
for cards in cardswon:
    cards = int(cards)-1
    x = CardsWon(line_list[cards])
    print (x)
