import time



#KEY:
#POG-- = Player 1 Grid Position Array (from left to right, top to bottom)
#PTG-- = Player 2 Grid Position Array (from left to right, top to bottom)
#POGO-- = Player 1 Opposition Grid Position Array (to display enemy grid, without ships, to mark own hits and misses)
#PTGO-- = Player 2 Opposition Grid Position Array (to display enemy grid, without ships, to mark own hits and misses)

#DEFINITIONS:
#MainMenu = The main menu, to show the title and select game mode and board mode.
#RoundZeroMenu = The menu that displays between either player's turn.
#RoundOneMenu = The menu that player 1 plays in.
#RoundTwoMenu = The menu that player 2 plays in.
#PlayerOneDefeatMenu = The end menu for player one's demise.
#PlayerTwoDefeatMenu = The end menu for player two's demise.

POG=[" "]*100
POGO=[" "]*100
PTG=[" "]*100
PTGO=[" "]*100
#^The above are 1D lists of the contents of a 2D grid.
#To find the correlating position in the list for a row and column position on the grid, use this equation: (((Row*10)-10)+Column)-1

def MainMenu():
    print("===== CRUISERS ======")
    
    print("As designed by: Jack Langmead")
    print(" ")
    print("Enter 1, to start")
    print("'1' = 2 Player")
    
    GameMode=int(input("Mode: "))
    while True:
        if GameMode==1:
            RoundZeroMenu()

        print("Invalid mode, please retry.")
        GameMode=int(input("Mode: "))

def RoundZeroMenu():
    print("\n"*30)
    print("\n"*30)
    global BuildPhase
    try:
        BuildPhase
    except NameError:
        BuildPhase=0
    if BuildPhase==0:
        print("CRUISERS plays much like the Battleship boardgame. Both players will place their ships, and then strategically locate their")
        print("opponent's ships by blowing up grid positions, while the game displays whether the attempt was a splash or a hit.")
        print(" ")
        print("Because this game plays on the same monitor, only one player will be allowed to look at a time, while the other is turned around.")
        print("Between turns, there will be a blank switch-over screen for the two players to switch over during.")
        print(" ")
        print("Please may PLAYER TWO now turn away, while PLAYER ONE places their ships on the next screen.")
    if BuildPhase==1:
        print("It is now time for PLAYER TWO to place their ships. Please may PLAYER ONE turn away.")
    if BuildPhase==2:
        print("Both players have now placed their ships!")
        print("Now, PLAYER ONE will begin the game proper on the next screen. PLAYER TWO please turn away.")
    if BuildPhase==3:
        print("PLAYER TWO's turn. PLAYER ONE please turn away.")
    if BuildPhase==4:
        print("PLAYER ONE's turn. PLAYER TWO please turn away.")
    print(" ")
    RoundZeroContinue=int(input("Input '1' to continue: "))
    while True:
        if RoundZeroContinue==1:
            break
        print("Invalid input, please retry.")
        RoundZeroContinue=int(input("Input '1' to continue: "))
    RoundZeroContinue=0
    if BuildPhase==0:
        BuildPhase=BuildPhase+1
        RoundOneMenu()
    if BuildPhase==1:
        BuildPhase=BuildPhase+1
        RoundTwoMenu()
    if BuildPhase==2:
        BuildPhase=BuildPhase+1
        RoundOneMenu()
    if BuildPhase==3:
        BuildPhase=BuildPhase+1
        RoundTwoMenu()
    if BuildPhase==4:
        BuildPhase=3
        RoundOneMenu()

def RoundOneMenu():
    print("\n"*30)
    print("\n"*30)
    print("PLAYER ONE")
    if BuildPhase>2:
        print("Enemy Grid:")
        print(" ┼─1─┼─2─┼─3─┼─4─┼─5─┼─6─┼─7─┼─8─┼─9─┼10─")
        print(" 1",POGO[0],"│",POGO[1],"│",POGO[2],"│",POGO[3],"│",POGO[4],"│",POGO[5],"│",POGO[6],"│",POGO[7],"│",POGO[8],"│",POGO[9])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 2",POGO[10],"│",POGO[11],"│",POGO[12],"│",POGO[13],"│",POGO[14],"│",POGO[15],"│",POGO[16],"│",POGO[17],"│",POGO[18],"│",POGO[19])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 3",POGO[20],"│",POGO[21],"│",POGO[22],"│",POGO[23],"│",POGO[24],"│",POGO[25],"│",POGO[26],"│",POGO[27],"│",POGO[28],"│",POGO[29])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 4",POGO[30],"│",POGO[31],"│",POGO[32],"│",POGO[33],"│",POGO[34],"│",POGO[35],"│",POGO[36],"│",POGO[37],"│",POGO[38],"│",POGO[39])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 5",POGO[40],"│",POGO[41],"│",POGO[42],"│",POGO[43],"│",POGO[44],"│",POGO[45],"│",POGO[46],"│",POGO[47],"│",POGO[48],"│",POGO[49])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 6",POGO[50],"│",POGO[51],"│",POGO[52],"│",POGO[53],"│",POGO[54],"│",POGO[55],"│",POGO[56],"│",POGO[57],"│",POGO[58],"│",POGO[59])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 7",POGO[60],"│",POGO[61],"│",POGO[62],"│",POGO[63],"│",POGO[64],"│",POGO[65],"│",POGO[66],"│",POGO[67],"│",POGO[68],"│",POGO[69])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 8",POGO[70],"│",POGO[71],"│",POGO[72],"│",POGO[73],"│",POGO[74],"│",POGO[75],"│",POGO[76],"│",POGO[77],"│",POGO[78],"│",POGO[79])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 9",POGO[80],"│",POGO[81],"│",POGO[82],"│",POGO[83],"│",POGO[84],"│",POGO[85],"│",POGO[86],"│",POGO[87],"│",POGO[88],"│",POGO[89])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print("10",POGO[90],"│",POGO[91],"│",POGO[92],"│",POGO[93],"│",POGO[94],"│",POGO[95],"│",POGO[96],"│",POGO[97],"│",POGO[98],"│",POGO[99])
        print(" ")
    print("Your Grid:")
    print(" ┼─1─┼─2─┼─3─┼─4─┼─5─┼─6─┼─7─┼─8─┼─9─┼10─")
    print(" 1",POG[0],"│",POG[1],"│",POG[2],"│",POG[3],"│",POG[4],"│",POG[5],"│",POG[6],"│",POG[7],"│",POG[8],"│",POG[9])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 2",POG[10],"│",POG[11],"│",POG[12],"│",POG[13],"│",POG[14],"│",POG[15],"│",POG[16],"│",POG[17],"│",POG[18],"│",POG[19])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 3",POG[20],"│",POG[21],"│",POG[22],"│",POG[23],"│",POG[24],"│",POG[25],"│",POG[26],"│",POG[27],"│",POG[28],"│",POG[29])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 4",POG[30],"│",POG[31],"│",POG[32],"│",POG[33],"│",POG[34],"│",POG[35],"│",POG[36],"│",POG[37],"│",POG[38],"│",POG[39])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 5",POG[40],"│",POG[41],"│",POG[42],"│",POG[43],"│",POG[44],"│",POG[45],"│",POG[46],"│",POG[47],"│",POG[48],"│",POG[49])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 6",POG[50],"│",POG[51],"│",POG[52],"│",POG[53],"│",POG[54],"│",POG[55],"│",POG[56],"│",POG[57],"│",POG[58],"│",POG[59])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 7",POG[60],"│",POG[61],"│",POG[62],"│",POG[63],"│",POG[64],"│",POG[65],"│",POG[66],"│",POG[67],"│",POG[68],"│",POG[69])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 8",POG[70],"│",POG[71],"│",POG[72],"│",POG[73],"│",POG[74],"│",POG[75],"│",POG[76],"│",POG[77],"│",POG[78],"│",POG[79])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 9",POG[80],"│",POG[81],"│",POG[82],"│",POG[83],"│",POG[84],"│",POG[85],"│",POG[86],"│",POG[87],"│",POG[88],"│",POG[89])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print("10",POG[90],"│",POG[91],"│",POG[92],"│",POG[93],"│",POG[94],"│",POG[95],"│",POG[96],"│",POG[97],"│",POG[98],"│",POG[99])
    print(" ")
    global RoundOneFired
    try:
        RoundOneFired
    except NameError:
        RoundOneFired=False
    if BuildPhase>2 and RoundOneFired==False:
        ShellColumn=int(input("Target the column to fire your shells at: "))
        ShellRow=int(input("Target the row to fire your shells at: "))
        print("BANG!")
        RoundOneFired=True
        time.sleep(1)
        ShellPos=(((ShellRow*10)-10)+ShellColumn)-1
        if PTG[ShellPos] == " " or PTG[ShellPos] == "O":
            POGO[ShellPos]="O"
            PTG[ShellPos]="O"
        else:
            POGO[ShellPos]="X"
            PTG[ShellPos]="X"
        RoundOneMenu()
    if RoundOneFired==True:
        print("Turn complete.")
        RoundOneFired=False
        time.sleep(1)
        PlayerTwoDefeated=all(Content==" " or Content=="X" or Content=="O" for Content in PTG)
        if PlayerTwoDefeated==True:
            PlayerTwoDefeatMenu()
        RoundZeroContinue=int(input("Input '1' to continue: "))
        while True:
            if RoundZeroContinue==1:
                RoundZeroMenu()
            print("Invalid input, please retry.")
            RoundZeroContinue=int(input("Input '1' to continue: "))
    if BuildPhase==1:
        global RoundOneBattleships
        global RoundOneCruisers
        global RoundOneDestroyers
        try:
            RoundOneBattleships
        except NameError:
            RoundOneBattleships=2
        try:
            RoundOneCruisers
        except NameError:
            RoundOneCruisers=2
        try:
            RoundOneDestroyers
        except NameError:
            RoundOneDestroyers=2
        print("First, you need to place your ships!")
        print("Please take care not to make them overlap or go off the grid.")
        print("These are your ships left to place:")
        print("1-Battleships (3 long): ",RoundOneBattleships," left.")
        print("2-Cruisers (2 long): ",RoundOneCruisers," left.")
        print("3-Destroyers (1 long): ",RoundOneDestroyers," left.")
        print(" ")
        if RoundOneBattleships + RoundOneCruisers + RoundOneDestroyers == 0:
            print("You have no ships left to place!")
            RoundZeroContinue=int(input("Input '1' to continue: "))
            while True:
                if RoundZeroContinue==1:
                    RoundZeroMenu()
                print("Invalid input, please retry.")
                RoundZeroContinue=int(input("Input '1' to continue: "))
        ShipType=int(input("What would you like to place? (input its number): "))
        while (ShipType==1 and RoundOneBattleships==0) or (ShipType==2 and RoundOneCruisers==0) or (ShipType==3 and RoundOneDestroyers==0):
            print("You're out of that ship type!")
            ShipType=int(input("What would you like to place? (input its number): "))
        if not ShipType==3:
            ShipDirection=int(input("What direction is it facing? (1=Up, 2=Right, 3=Down, 4=Left): "))
        Column=int(input("What column will you place the front of your ship in? "))
        Row=int(input("What row will you place the front of your ship in? "))
        ShipPos1=(((Row*10)-10)+Column)-1
        if ShipType==1 and ShipDirection==1:
            ShipPos2=ShipPos1+10
            ShipPos3=ShipPos1+20
            POG[ShipPos1]="▲"
            POG[ShipPos2]="█"
            POG[ShipPos3]="▼"
            RoundOneBattleships=RoundOneBattleships-1
            RoundOneMenu()
        if ShipType==1 and ShipDirection==2:
            ShipPos2=ShipPos1-1
            ShipPos3=ShipPos1-2
            POG[ShipPos1]="►"
            POG[ShipPos2]="■"
            POG[ShipPos3]="◄"
            RoundOneBattleships=RoundOneBattleships-1
            RoundOneMenu()
        if ShipType==1 and ShipDirection==3:
            ShipPos2=ShipPos1-10
            ShipPos3=ShipPos1-20
            POG[ShipPos1]="▼"
            POG[ShipPos2]="█"
            POG[ShipPos3]="▲"
            RoundOneBattleships=RoundOneBattleships-1
            RoundOneMenu()
        if ShipType==1 and ShipDirection==4:
            ShipPos2=ShipPos1+1
            ShipPos3=ShipPos1+2
            POG[ShipPos1]="◄"
            POG[ShipPos2]="■"
            POG[ShipPos3]="►"
            RoundOneBattleships=RoundOneBattleships-1
            RoundOneMenu()
        if ShipType==2 and ShipDirection==1:
            ShipPos2=ShipPos1+10
            POG[ShipPos1]="┴"
            POG[ShipPos2]="║"
            RoundOneCruisers=RoundOneCruisers-1
            RoundOneMenu()
        if ShipType==2 and ShipDirection==2:
            ShipPos2=ShipPos1-1
            POG[ShipPos1]="├"
            POG[ShipPos2]="═"
            RoundOneCruisers=RoundOneCruisers-1
            RoundOneMenu()
        if ShipType==2 and ShipDirection==3:
            ShipPos2=ShipPos1-10
            POG[ShipPos1]="┬"
            POG[ShipPos2]="║"
            RoundOneCruisers=RoundOneCruisers-1
            RoundOneMenu()
        if ShipType==2 and ShipDirection==4:
            ShipPos2=ShipPos1+1
            POG[ShipPos1]="┤"
            POG[ShipPos2]="═"
            RoundOneCruisers=RoundOneCruisers-1
            RoundOneMenu()
        if ShipType==3:
            POG[ShipPos1]="±"
            RoundOneDestroyers=RoundOneDestroyers-1
            RoundOneMenu()

def RoundTwoMenu():
    print("\n"*30)
    print("\n"*30)
    print("PLAYER TWO")
    if BuildPhase>2:
        print("Enemy Grid:")
        print(" ┼─1─┼─2─┼─3─┼─4─┼─5─┼─6─┼─7─┼─8─┼─9─┼10─")
        print(" 1",PTGO[0],"│",PTGO[1],"│",PTGO[2],"│",PTGO[3],"│",PTGO[4],"│",PTGO[5],"│",PTGO[6],"│",PTGO[7],"│",PTGO[8],"│",PTGO[9])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 2",PTGO[10],"│",PTGO[11],"│",PTGO[12],"│",PTGO[13],"│",PTGO[14],"│",PTGO[15],"│",PTGO[16],"│",PTGO[17],"│",PTGO[18],"│",PTGO[19])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 3",PTGO[20],"│",PTGO[21],"│",PTGO[22],"│",PTGO[23],"│",PTGO[24],"│",PTGO[25],"│",PTGO[26],"│",PTGO[27],"│",PTGO[28],"│",PTGO[29])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 4",PTGO[30],"│",PTGO[31],"│",PTGO[32],"│",PTGO[33],"│",PTGO[34],"│",PTGO[35],"│",PTGO[36],"│",PTGO[37],"│",PTGO[38],"│",PTGO[39])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 5",PTGO[40],"│",PTGO[41],"│",PTGO[42],"│",PTGO[43],"│",PTGO[44],"│",PTGO[45],"│",PTGO[46],"│",PTGO[47],"│",PTGO[48],"│",PTGO[49])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 6",PTGO[50],"│",PTGO[51],"│",PTGO[52],"│",PTGO[53],"│",PTGO[54],"│",PTGO[55],"│",PTGO[56],"│",PTGO[57],"│",PTGO[58],"│",PTGO[59])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 7",PTGO[60],"│",PTGO[61],"│",PTGO[62],"│",PTGO[63],"│",PTGO[64],"│",PTGO[65],"│",PTGO[66],"│",PTGO[67],"│",PTGO[68],"│",PTGO[69])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 8",PTGO[70],"│",PTGO[71],"│",PTGO[72],"│",PTGO[73],"│",PTGO[74],"│",PTGO[75],"│",PTGO[76],"│",PTGO[77],"│",PTGO[78],"│",PTGO[79])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print(" 9",PTGO[80],"│",PTGO[81],"│",PTGO[82],"│",PTGO[83],"│",PTGO[84],"│",PTGO[85],"│",PTGO[86],"│",PTGO[87],"│",PTGO[88],"│",PTGO[89])
        print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
        print("10",PTGO[90],"│",PTGO[91],"│",PTGO[92],"│",PTGO[93],"│",PTGO[94],"│",PTGO[95],"│",PTGO[96],"│",PTGO[97],"│",PTGO[98],"│",PTGO[99])
        print(" ")
    print("Your Grid:")
    print(" ┼─1─┼─2─┼─3─┼─4─┼─5─┼─6─┼─7─┼─8─┼─9─┼10─")
    print(" 1",PTG[0],"│",PTG[1],"│",PTG[2],"│",PTG[3],"│",PTG[4],"│",PTG[5],"│",PTG[6],"│",PTG[7],"│",PTG[8],"│",PTG[9])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 2",PTG[10],"│",PTG[11],"│",PTG[12],"│",PTG[13],"│",PTG[14],"│",PTG[15],"│",PTG[16],"│",PTG[17],"│",PTG[18],"│",PTG[19])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 3",PTG[20],"│",PTG[21],"│",PTG[22],"│",PTG[23],"│",PTG[24],"│",PTG[25],"│",PTG[26],"│",PTG[27],"│",PTG[28],"│",PTG[29])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 4",PTG[30],"│",PTG[31],"│",PTG[32],"│",PTG[33],"│",PTG[34],"│",PTG[35],"│",PTG[36],"│",PTG[37],"│",PTG[38],"│",PTG[39])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 5",PTG[40],"│",PTG[41],"│",PTG[42],"│",PTG[43],"│",PTG[44],"│",PTG[45],"│",PTG[46],"│",PTG[47],"│",PTG[48],"│",PTG[49])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 6",PTG[50],"│",PTG[51],"│",PTG[52],"│",PTG[53],"│",PTG[54],"│",PTG[55],"│",PTG[56],"│",PTG[57],"│",PTG[58],"│",PTG[59])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 7",PTG[60],"│",PTG[61],"│",PTG[62],"│",PTG[63],"│",PTG[64],"│",PTG[65],"│",PTG[66],"│",PTG[67],"│",PTG[68],"│",PTG[69])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 8",PTG[70],"│",PTG[71],"│",PTG[72],"│",PTG[73],"│",PTG[74],"│",PTG[75],"│",PTG[76],"│",PTG[77],"│",PTG[78],"│",PTG[79])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print(" 9",PTG[80],"│",PTG[81],"│",PTG[82],"│",PTG[83],"│",PTG[84],"│",PTG[85],"│",PTG[86],"│",PTG[87],"│",PTG[88],"│",PTG[89])
    print(" ┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───")
    print("10",PTG[90],"│",PTG[91],"│",PTG[92],"│",PTG[93],"│",PTG[94],"│",PTG[95],"│",PTG[96],"│",PTG[97],"│",PTG[98],"│",PTG[99])
    print(" ")
    global RoundTwoFired
    try:
        RoundTwoFired
    except NameError:
        RoundTwoFired=False
    if BuildPhase>2 and RoundTwoFired==False:
        ShellColumn=int(input("Target the column to fire your shells at: "))
        ShellRow=int(input("Target the row to fire your shells at: "))
        print("BANG!")
        RoundTwoFired=True
        time.sleep(1)
        ShellPos=(((ShellRow*10)-10)+ShellColumn)-1
        if POG[ShellPos] == " " or POG[ShellPos] == "O":
            PTGO[ShellPos]="O"
            POG[ShellPos]="O"
        else:
            PTGO[ShellPos]="X"
            POG[ShellPos]="X"
        RoundTwoMenu()
    if RoundTwoFired==True:
        print("Turn complete.")
        RoundTwoFired=False
        time.sleep(1)
        PlayerOneDefeated=all(Content==" " or Content=="X" or Content=="O" for Content in POG)
        if PlayerOneDefeated==True:
            PlayerOneDefeatMenu()
        RoundZeroContinue=int(input("Input '1' to continue: "))
        while True:
            if RoundZeroContinue==1:
                RoundZeroMenu()
            print("Invalid input, please retry.")
            RoundZeroContinue=int(input("Input '1' to continue: "))
    if BuildPhase==2:
        global RoundTwoBattleships
        global RoundTwoCruisers
        global RoundTwoDestroyers
        try:
            RoundTwoBattleships
        except NameError:
            RoundTwoBattleships=2
        try:
            RoundTwoCruisers
        except NameError:
            RoundTwoCruisers=2
        try:
            RoundTwoDestroyers
        except NameError:
            RoundTwoDestroyers=2
        print("First, you need to place your ships!")
        print("Please take care not to make them overlap or go off the grid.")
        print("These are your ships left to place:")
        print("1-Battleships (3 long): ",RoundTwoBattleships," left.")
        print("2-Cruisers (2 long): ",RoundTwoCruisers," left.")
        print("3-Destroyers (1 long): ",RoundTwoDestroyers," left.")
        print(" ")
        if RoundTwoBattleships + RoundTwoCruisers + RoundTwoDestroyers == 0:
            print("You have no ships left to place!")
            RoundZeroContinue=int(input("Input '1' to continue: "))
            while True:
                if RoundZeroContinue==1:
                    RoundZeroMenu()
                print("Invalid input, please retry.")
                RoundZeroContinue=int(input("Input '1' to continue: "))
        ShipType=int(input("What would you like to place? (input its number): "))
        while ShipType>3 or ShipType<1:
            print("Invalid ship type!")
            ShipType=int(input("What would you like to place? (input its number): "))
        while (ShipType==1 and RoundTwoBattleships==0) or (ShipType==2 and RoundTwoCruisers==0) or (ShipType==3 and RoundTwoDestroyers==0):
            print("You're out of that ship type!")
            ShipType=int(input("What would you like to place? (input its number): "))
        if not ShipType==3:
            ShipDirection=int(input("What direction is it facing? (1=Up, 2=Right, 3=Down, 4=Left): "))
        Column=int(input("What column will you place the front of your ship in? "))
        Row=int(input("What row will you place the front of your ship in? "))
        ShipPos1=(((Row*10)-10)+Column)-1
        if ShipType==1 and ShipDirection==1:
            ShipPos2=ShipPos1+10
            ShipPos3=ShipPos1+20
            PTG[ShipPos1]="▲"
            PTG[ShipPos2]="█"
            PTG[ShipPos3]="▼"
            RoundTwoBattleships=RoundTwoBattleships-1
            RoundTwoMenu()
        if ShipType==1 and ShipDirection==2:
            ShipPos2=ShipPos1-1
            ShipPos3=ShipPos1-2
            PTG[ShipPos1]="►"
            PTG[ShipPos2]="■"
            PTG[ShipPos3]="◄"
            RoundTwoBattleships=RoundTwoBattleships-1
            RoundTwoMenu()
        if ShipType==1 and ShipDirection==3:
            ShipPos2=ShipPos1-10
            ShipPos3=ShipPos1-20
            PTG[ShipPos1]="▼"
            PTG[ShipPos2]="█"
            PTG[ShipPos3]="▲"
            RoundTwoBattleships=RoundTwoBattleships-1
            RoundTwoMenu()
        if ShipType==1 and ShipDirection==4:
            ShipPos2=ShipPos1+1
            ShipPos3=ShipPos1+2
            PTG[ShipPos1]="◄"
            PTG[ShipPos2]="■"
            PTG[ShipPos3]="►"
            RoundTwoBattleships=RoundTwoBattleships-1
            RoundTwoMenu()
        if ShipType==2 and ShipDirection==1:
            ShipPos2=ShipPos1+10
            PTG[ShipPos1]="┴"
            PTG[ShipPos2]="║"
            RoundTwoCruisers=RoundTwoCruisers-1
            RoundTwoMenu()
        if ShipType==2 and ShipDirection==2:
            ShipPos2=ShipPos1-1
            PTG[ShipPos1]="├"
            PTG[ShipPos2]="═"
            RoundTwoCruisers=RoundTwoCruisers-1
            RoundTwoMenu()
        if ShipType==2 and ShipDirection==3:
            ShipPos2=ShipPos1-10
            PTG[ShipPos1]="┬"
            PTG[ShipPos2]="║"
            RoundTwoCruisers=RoundTwoCruisers-1
            RoundTwoMenu()
        if ShipType==2 and ShipDirection==4:
            ShipPos2=ShipPos1+1
            PTG[ShipPos1]="┤"
            PTG[ShipPos2]="═"
            RoundTwoCruisers=RoundTwoCruisers-1
            RoundTwoMenu()
        if ShipType==3:
            PTG[ShipPos1]="±"
            RoundTwoDestroyers=RoundTwoDestroyers-1
            RoundTwoMenu()

def PlayerOneDefeatMenu():
    print(" ")
    print("PLAYER ONE was defeated!")
    print("Congratulations, PLAYER TWO!")
    print(" ")
    print("END")
    time.sleep(999)

def PlayerTwoDefeatMenu():
    print(" ")
    print("PLAYER TWO was defeated!")
    print("Congratulations, PLAYER ONE!")
    print(" ")
    print("END")
    time.sleep(999)

MainMenu()
