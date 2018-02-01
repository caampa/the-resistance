# Contribution

**ml17390.py** and **information.py** define the implementation of a bot for "The Resistance" game 
using a Decision Tree as the Artificial Intelligence technique implemented for the behaviour of the bot.

Two different approaches were considered. First, it was considered the idea of implementing a Decision Tree that indicates the bot the probability of the rest of the players begin spies. (This strategy is also used when the bot plays in the resistance side)
The structure of this Decision Tree was obtained by training the gathered data in the ` mission.arff ` file in Weka:
` missiong.arrf ` file contains the following features:

``` 
@relation 'Identity'

@attribute spies_victories {0,1,2}
@attribute resistance_victories {0,1,2}
@attribute sabotages {0,1,2}
@attribute non_sabotages {0,1,2,3}
@attribute votes_up {0,1,2,3,4,5}
@attribute votes_down {0,1,2,3,4,5}
@attribute identity {RESISTANCE, SPY} 

```

The obtained results were favourable!

Secondly, it was explored the creation of another Decision Tree that indicates the bot if sabotaging a mission was convenient.
In order to do that, the following data was collected in the ` sabotage.arff ` file.

``` 
@relation 'Sabotages'

@attribute spies_victories {0,1,2}
@attribute resistance_victories {0,1,2}
@attribute spies_in_team {1,2}
@attribute size_team {2,3}
@attribute previous_sabotages {0,1,2}
@attribute sabotage {YES, NO} 

```

In this scenario, the Decision Tree built by Weka didn't introduce any improvement. It was proved that was profitable to sabotage always. (As long as the bot was a spy).


# Execution

> The bot can be tested against others using the competition.py script, which receives the following parameters:
>
> • Number of games to play.
>
> • Python file(s) that contains all bots to play with.

The following example runs 1500 games with all bots included in the beginners file and the one implemented in the ml17390.py file:

` python competition.py 1500 bots/beginners.py aibots-2018/ml17390/ml17390.py `

Once the program has executed, it will show an output script with two tables. One indicating the percentage of victories for the resistance and the other for the spies.
> The two "vote" columns track correct up-votes and correct down-votes, depending on whether it’s spy or or resistance. 
> The "voted" column shows how often others supported a team including this player. 
> The "selected" column shown how often the player was selected.
> The "selection" column tracks the picking of teams with or without spies (depending on role).
