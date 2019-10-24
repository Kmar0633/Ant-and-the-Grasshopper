Game=["[]","G",".",".",".","a",".",".","a",".","a",".","[***]"]
#Game=["[]","G",".",".","[***]"]
Food=["[","*","*","*","]"]
Nest=["[","]"]
Commands=["WALK L", "DROP" ,"QUIT" ,"WALK R" , "PICK UP" , "HOP L" , "HOP R"]
Grasshopper="G"
Pos_of_G=Game.index("G")

Ant_Attack="Arrgh!! An Ant attacked you. Game over."
Game_Screen=" ".join(Game)
Num_elem=len(Game)
Pos=Num_elem-1
print(Game_Screen)

while True:
	Command=(input("> ")).upper()
	if Command=="WALK L":
		Pos_of_G=Pos_of_G-1		
		if Game[Pos_of_G]==".":
			Game[Pos_of_G]=Game[Pos_of_G+1]
			Game[Pos_of_G+1]="."
			print(" ".join(Game))
		elif Game[Pos_of_G]!="." and Game[Pos_of_G]!="a":
			Pos_of_G=(Pos_of_G*0)+1
			print(" ".join(Game))

		elif Game[Pos_of_G]=="a":
			print(Ant_Attack)
			break
		
	if Command=="WALK R":
		Pos_of_G=Pos_of_G+1
		if Game[Pos_of_G]==".":
			
			Game[Pos_of_G]=Game[Pos_of_G-1]
			Game[Pos_of_G-1]="."
			print(" ".join(Game))
		elif Pos_of_G==12:
			Pos_of_G=Pos_of_G-1
			Game[Pos_of_G]=Grasshopper
			print(" ".join(Game))
			
		elif Game[Pos_of_G]=="a":
			print(Ant_Attack)
			break
		
	if Command=="HOP L":
		Pos_of_G=Pos_of_G-2
		if Game[Pos_of_G]==".":
			
			Game[Pos_of_G]=Game[Pos_of_G+2]
			Game[Pos_of_G+2]="."
			print(" ".join(Game))

		elif Game[Pos_of_G]=="a":
			print(Ant_Attack)
			break
			
		elif Game[Pos_of_G]!="." or Game[Pos_of_G]!="a":
			Pos_of_G=(Pos_of_G*0)+1
			Game[1]=Grasshopper
			Game[2]="."
			
			print(" ".join(Game))
		
	if Command=="HOP R":
		Pos_of_G=Pos_of_G+2
		if Pos_of_G>=Pos:
			Pos_of_G=Pos-1
		
			Game[Pos]="".join(Food)
			print(" ".join(Game))
		
		elif Game[Pos_of_G]=="." and Pos_of_G<Pos:
			
			Game[Pos_of_G]=Game[Pos_of_G-2]
			Game[Pos_of_G-2]="."
	
			print(" ".join(Game))
		elif Game[Pos_of_G]=="a":
			print(Ant_Attack)
			break

	if Command=="PICK UP":
	
		if Game[Pos_of_G]=="G*" or Game[Pos_of_G+1]=="[]" or Game[Pos_of_G+1]=="a" or Game[Pos_of_G+1]==".":
			print("Cannot pick up food")	
		elif (Game[Pos_of_G+1]=="[***]" or Game[Pos_of_G+1]=="[**]" or Game[Pos_of_G+1]=="[*]") and Grasshopper=="G":
			Food.remove("*")
			Game[Pos]=str("".join(Food))
			Game[Pos_of_G]="G*"
			Grasshopper="G*"
			print(" ".join(Game))
	
	if Command=="QUIT":
		print("Goodbye Grasshopper!")
		break
	if Command=="DROP":
		
		if (Game[Pos_of_G-1]=="[**]" or Game[Pos_of_G-1]=="[*]" or Game[Pos_of_G-1]=="[]") and Game[Pos_of_G]=="G*":
			Nest.insert(1,"*")
			Game[0]=str("".join(Nest))
			Game[Pos_of_G]="G"
			Grasshopper="G"
			print(" ".join(Game))
			
			No_of_food=Nest.count("*")
			if No_of_food==3:
				print("Congratulations Grasshopper, you now have enough food to last the winter!")
				break
		elif Game[Pos_of_G]=="G" or Game[Pos_of_G-1]=="." or "a":
			print("Cannot drop food")
            
	if Command not in Commands:
		print("Invalid command")
		
		
