# 2 Player Game Loop 
# # Variables 
round_number = 0 
player_list=["BOB", "ALICE"] 
score_list = [0,0]
gameIsOn=True

# Make a game loop 
while gameIsOn: #Infinite Loop 
    round_number += 1 
    print("ROUND: ", round_number)
    if round_number%2: 
        #PLAYER 2 TURN 
        print(player_list[1], "GETS TO PLAY") 
        # Show player turn
        input("Press a key: \n\n") 
        # Waiting for command 
        score_list[1]+=1 # Adding scores

        print("SCORES:\n", player_list[0], ":", 
        score_list[0], "\n", player_list[1],":", 
        score_list[1],"\n")# Printing out scores 
        for item in score_list: #loop throughthe score list 
            if item >= 5: 
                print(player_list [1], "WINS") 
                gameIsOn=False 
                break
            else: #PLAYER 1 
                print(player_list[0], "GETS TO PLAY") 
                input("Press a key: \n\n") 
                score_list[0]+=1 
                print("SCORES: \n ",player_list[0], ":", score_list[0], "\n", 
                player_list [1],":",
                score_list[1]) 
                for item in score_list: #loop through
                        #PLAYER 1 
                        print(player_list[0], "GETS TO PLAY") 
                        input("Press a key: \n\n") 
                        score_list[0]+=1 
                        print("SCORES: \n ",player_list[0], ":", 
                        score_list[0], "\n", 
                        player_list [1],": score_list[1]") 
                        for item in score_list: #loop through the score list 
                            if item >= 5: 
                                print(player_list[0], "WINS!\n") 
                                gameIsOn=False 
                                break