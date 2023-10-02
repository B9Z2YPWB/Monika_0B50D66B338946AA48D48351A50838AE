''' Implement a class called Player that represents a cricket player.
The Player class should have a method called play() which prints "the player is playing cricket."
Override the play() method in each derived class to print "The Batsman is batting" and "The Bowler is bowling", respectively.
Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.'''


# Define the base class Player
class Player:
  def play(self):
    print("The player is playing cricket")

#Define the derived class Batsman 
class Batsman(Player):
  def play(self):
    print("The Batsman is batting.")

#Define the derived class Bowler
class Bowler(Player):
  def play(self):
    print("The Bowler is bowling.")

#Create objects of Batsman and Bowler classes
batsman=Batsman()
bowler=Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()