import stdarray 
import stdio 
import random

suits = ["clubs","spades", "hearts", "diamonds"]
ranks = ["2","3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
#13 ranks
card_num = range(51)


final_list = []

j = 0
k = 0

for i in range(len(card_num)):
    final_list.append(ranks[k] + " of " + suits[j])
    k += 1
    if k == 12:
        j+= 1
        k = 0 
    if j > 3:
        break
final_list =random.shuffle(final_list)
stdio.writeln(final_list)





    

