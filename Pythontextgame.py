print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Play dead."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	elif bear == "3":
		print "Smart choice, you must have read the bear manual! The bear sniffs you and quickly runs away."
		print "1. Continue down the corridor."
	else:
		print "The bear is swallowed by a dragon, which in turn...burns your face off."
		exit()
		
		
	survive = raw_input("> ")
		
	if survive == "1":
		print "You enter a large room with a red button in the middle of the room and a door to the left and right."
		print "1. Press the button."
		print "2. Enter the left door."
		print "3. Enter the right door."
	else:
		print "You fall on a stalagmite"
		exit()
		
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "Nothing happens...The button must be broken."
		print "1. You fix the red button "
	elif choice == "2":
		print "You walk through the door into open space, bring your space helmet next time."
	elif choice == "3":
		print "You find an armoury with a door at the back of the room."
		print "2. Explore the room."
	else:
		print "A sinkhole eats you."
		exit()
		
	choice1 = raw_input("> ")
	
	if choice1 == "1":
		print "The button is fixed."
		print "1. Press the fixed button."
	elif choice1 == "2":
		print "You rummage through the armoury and find a sword, shield, spear, and staff with a glowing crystal attached to the top of it."
		print "You only have room to take one item, type in the item you want. Keywords are 'sword', 'shield, 'spear', and 'staff'"
	else:
		print "You slip on a banana and break your skull."
		exit()
		
	choice2 = raw_input("> ")
	
	if choice2 == "1":
		print "You press the red button.\n.\n.\nA whole opens in the ceiling and a laser gun floats down into your hands."
		print "1. Blast a hole in the wall"
	elif choice2 in ['sword', 'shield', 'spear', 'staff']:
		print "You picked up a %s." % choice2
		print "2. Enter the door at the end of the room."
	else:
		print "Aliens abduct you and you live the rest of your life on Mars."
		exit()
	choice3 = raw_input("> ")
		
	if choice3 == "1":
		print "You blast a hole in the wall and the whole room collapses on you. \n Game Over."
		exit()
	elif choice3 == "2":
		print "You open the door and enter a dark room. \n There is a gargantuan spider with fangs dripping venom poised to attack. \nDo you 'run', 'fight', or 'play dead'?"
	else:
		print "Because you did %s you fall asleep and never wake up. Game Over." % choice3
		exit()
		
	choice4 = raw_input("> ")
	
	if choice4 == "run":
		print "Nope, never %s from a spider!" % choice4
		exit()
	elif choice4 == "fight":
		print "You fight valiantly, however it is enough.\n You have broken your %s and the spider is poised over you with his fangs..." % choice2
		print "1. Try to break a fang"
		print "2. Try to reason with the spider."
	elif choice4 == "play dead":
		print "The spider doesn't buy it, he eviscerates you."
		exit()
	else:
		print "A ninja appears and makes quick work of the spider...and you."
		exit()
	
	end_game = raw_input("> ")
	
	if end_game == "1":
		print "You manage to break a fang and dodge his attack! \n You plunge his own fang into his hairy head. \n The spider is vanquished you win!"
	elif end_game == "2":
		print "You try to reason with the spider, he is unimpressed. You are gored by a fang. At least it was a quick death...Game Over."
		exit()
	else:
		print "%s didn't work...The spider spits venom in your eyes and your skull disintegrates." % end_game
		exit()
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck."
		
else:
	print "You stumble around and fall on a knife and die. Good job!"
	
