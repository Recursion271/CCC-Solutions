numberofplayers = int(input("Number of players: "))
starplayers = 0
for i in range(numberofplayers):
    numberofpoints = int(input("Number of points"))
    numberoffouls = int(input("Number of fouls"))
    numberofstars = numberofpoints * 5 - numberoffouls *3
    if numberofstars > 40:
        starplayers = starplayers + 1
if starplayers == numberofplayers:
    print(str(starplayers)+"+")
else: 
    print(starplayers)
