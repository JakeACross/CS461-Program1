# CS461-Program1
Poker is a card game using a standard 52-card deck.1  There are many variations, but as our focus here is on applying statistical learning rather than playing a game, we’ll restrict ourselves to the simplest form —5 cards.
</br>
</br>
Assume the game has 6 players – ‘you’ and 5 others. Your program will carry out the following actions: 
- Repeatedly (500-1000 times): 
  - Shuffle the 52-card deck, and deal yourself a 5-card hand. 
  - Repeatedly (500-1000 times): 
    - Using the remaining 47 cards, deal the other 5 players their hands
    - Determine if you would win or lose that hand; that is, if your hand would rank highest. Update some counters accordingly. 
    - Reshuffle the deck of 47 cards
  - Record the proportion of the above hands which you won. 
- For each rank of hand, report the percentage of hands having that rank, and the average winning percentage (average of the averages) for each rank. 

Your program should produce 2 output files: 
- A session log output as a CSV (comma-separated value) file, with each hand on a separate line. 
For each hand: the cards in the hand; what the hand was evaluated as; and its winning 
percentage. 
- A summary showing the percentage of hands falling into each rank, and the overall win 
percentage for each rank, as a ‘normal’ text file. Don’t just list the percentages; add enough text 
to make it reader-friendly.


### Reference
- Python Porker Project: https://github.com/annaymj/Python-Code/blob/master/Poker.py
- Operator Ovaloading: https://www.geeksforgeeks.org/operator-overloading-in-python/
- Rank of Porker Hand: https://en.wikipedia.org/wiki/List_of_poker_hands#Hand-ranking_categories
