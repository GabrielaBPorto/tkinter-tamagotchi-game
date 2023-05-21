class animalFriend:
	def __init__(self, initname = 'Bob', initanimal='dog',
				 initage="0"):
		self.name = initname
		self.animal = initanimal
		self.age = initage
		self.hunger = 100
		self.tired = 0
		self.happiness = 0

	def getName(self):
		return(self.name)

	def getAnimal(self):
		return(self.animal)

	def getAge(self):
		return(self.age)

	def feed(self):
		if(self.hunger == 100):
			print("Your pet is not hungry")
		else:
			self.hunger+=10
			print(self.name, "is less hungry")

	def sleep(self, hours = 3):
		if(self.tired<= 0):
			print("Your pet is not tired")
		else:
			i = 0
			while(i<hours and self.tired != 100):
				self.tired-=10
				self.hunger-=10
				i+=1
			print(self.name, "has slept for", hours, "hours")

	def play(self):
		if(self.happiness == 100):
			print("Your pet is too happy, it doesnt want to play anymore")
		elif(self.tired >= 90):
			print("Your pet is too tired to play")
		elif(self.hunger == 0 or self.hunger <=20):
			print("Your pet is too hungry to play")
		else:
			self.happiness+=10
			self.tired+=10
			self.hunger-=10

	def giveStatus(self):
		print("Name:", self.name)
		print("Is ", self.animal)
		print("Is ", self.age, "years old")
		print("Belly", self.hunger)
		print("Tired", self.tired)
		print("Happiness", self.happiness)

name = input("What is the name of your pet?\n")
animal = input("What kinda of pet it is?\n")
age = input("How old is your pet? \n")

first = animalFriend(name, animal,age)
entrada = input("You can feed, put to sleep or play with your pet.\nS for sleep.\nF for feed.\nP for play.\nE for exit.\nST will give you the status\n")

while entrada != "E":
	if(entrada == "S"):
		sleeptime = input("How many hours do you want him to sleep?\n")
		if(sleeptime == str(0)):
			first.sleep()
		else:
			first.sleep(int(sleeptime))
	elif(entrada == "F"):
		first.feed()
	elif(entrada == "P"):
		first.play()
	elif(entrada == "ST"):
		first.giveStatus()
	entrada = input("What do you want to do now\n")

print("End game")
