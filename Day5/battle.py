# You are implementing a battle system for a simple role-playing game. A hero is fighting various monsters, and you have to determine the battle's outcome for each engaged skirmish. Hero and monsters share some stats:
# HP or Health Points: The amount of damage the character can sustain. If it reaches 0 (or less) the character dies.
# ATT or Attack: The character offensive capacity.
# DEF or Defense: The character defensive capacity.
# For either hero and monster, the damage inflicted is calculated subtracting the opponent's defense score from the attacker doubled attack score.
# In each round hero attacks first, and his damage rate is subtracted from the monster's HP. If the monster survives (HP > 0), it is his turn to attack. If the hero survives (HP > 0), a new round starts. The hero can also have some POT, or Healing Potions, in his backpack: only when his HP is equal to or lower than 10, a potion can (and must) be used for regaining 10 HP at the start of a new round. When the hero heals, he can't attack, but he receives only half damage from the monster's attack. Every potion can be used only once, then it must be discarded.
# Given a dictionary containing the character's stats (with p-prefix ones being the hero's stats and m-prefix ones being the monster's) you must return a string:
# "Victory in x rounds" if the hero wins.
# "Game Over in x rounds" if the monster wins.
# (with x being the number of rounds elapsed)



def bat():
    pHP=12
    pATK=10
    pDEF=10
    pPOT=0
    mHP=20
    mATK=6
    mDEF=10
    i=1
    while(pHP>0 and mHP>0):
        mHP=mHP-((pATK * 2) - mDEF)
        print("monster hp",mHP)
        if(mHP>0):
            pHP=pHP-((mATK * 2) - pDEF)
            print("player hp",pHP)
            if((pHP<=10) and (pHP>0) and pPOT!=0):
                pHP = pHP+pPOT
                print("player hp after healing",pHP)
                pPOT = 0
            elif(pHP<=0):
                print("MOnster is winner")
                
        else:
            print("round is ",i)
            print("player is the winner")
            
        i=i+1    

             
bat()