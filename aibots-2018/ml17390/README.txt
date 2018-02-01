# Contribution

** ml17390.py ** and ** information.py ** define the implementation of a bot for "The Resistance" game 
using a Decision Tree as the Artificial Intelligence technique implemented for the behaviour of the bot.

The bot can be tested against others using the competition.py script, which receives the following parameters:
• Number of games to play.
• Python file(s) that contains all bots to play with.

#Execution

The following example runs 1500 games with all bots included in the beginners file and the one implemented in the ml17390.py file:

' python competition.py 1500 bots/beginners.py aibots-2018/ml17390/ml17390.py '

Once the program has executed, it will show an output script with two tables. One indicating the percentage of victories for the resistance and the other for the spies.
> The two "vote" columns track correct up-votes and correct down-votes, depending on whether it’s spy or or resistance. 
> The "voted" column shows how often others supported a team including this player. 
> The "selected" column shown how often the player was selected.
> The "selection" column tracks the picking of teams with or without spies (depending on role).
