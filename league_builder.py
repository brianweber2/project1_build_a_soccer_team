'''
Author: Brian Weber
Date Created: November 19, 2016
Revision: 1.0
Title: Build a Soccer League
Description: You have volunteered to be the Coordinator for your town’s youth
soccer league. As part of your job you need to divide the 18 children who have
signed up for the league into three even teams - Dragons, Sharks and Raptors. 
In years past, the teams have been unevenly matched, so this year you are doing
your best to fix that. For each child, you will have the following information:
Name, height (in inches), whether or not they have played soccer before, and 
their guardians’ names. You'll take a list of these children, divide them into
teams and output a text file listing the three teams and the players on them. 
There are three main tasks you'll need to complete to get this done:

1. In your Python program, read the data from the supplied CSV file. Store that
   data in an appropriate data type so that it can be used in the next task.

2. Create logic that can iterate through all 18 players and assign them to 
   teams such that each team has the same number of players. The number of 
   experienced players on each team should also be the same.

3. Finally, the program should output a text file named -- teams.txt -- that 
   contains the league roster listing the team name, and each player on the 
   team including the player's information: name, whether they've played soccer 
   before and their guardians' names.
'''

# Import libraries to be used
import csv

# Define functions
def read_csv(filename):
	with open(filename, newline='') as csvfile:
		player_reader = csv.DictReader(csvfile, delimiter=',')
		player_data = list(player_reader)
	return player_data
		


if __name__ == "__main__":
	# Read CSV file. Output is a list of dictionaries
	player_data = read_csv("soccer_players.csv")

	# Separate experienced and non-experienced players
	exp_players = []
	no_exp_players = []
	for row in player_data:
		if row['Soccer Experience'] == 'YES':
			exp_players.append(row)
		else:
			no_exp_players.append(row)

	# Split up inexperienced and experienced players onto their teams
	no_exp1 = no_exp_players[:3]
	no_exp2 = no_exp_players[3:6]
	no_exp3 = no_exp_players[6:9]
	exp1 = exp_players[:3]
	exp2 = exp_players[3:6]
	exp3 = exp_players[6:9]
	sharks = no_exp1 + exp1
	dragons = no_exp2 + exp2
	raptors = no_exp3 + exp3

	# Create text file named "teams.txt"
	with open("teams.txt", "w") as file:
		file.write("Sharks\n")
		for player in sharks:
			file.write("{Name}, {Soccer Experience}, "
				"{Guardian Name(s)}\n".format(**player))
		file.write("\nDragons\n")
		for player in dragons:
			file.write("{Name}, {Soccer Experience}, "
				"{Guardian Name(s)}\n".format(**player))
		file.write("\nRaptors\n")
		for player in raptors:
			file.write("{Name}, {Soccer Experience}, "
				"{Guardian Name(s)}\n".format(**player))

	### Extra Credit ###
	# Add team name to dictionary 
	for player in sharks:
		player["Team Name"] = "Sharks"
	for player in dragons:
		player["Team Name"] = "Dragons"
	for player in raptors:
		player["Team Name"] = "Raptors"

	new_player_data = sharks + dragons + raptors

	# Create 18 text files ("welcome" letters)
	for player in new_player_data:
		file_name = "_".join(player["Name"].lower().split()) + ".txt"
		with open(file_name, "w") as file:
			file.write("Dear {Guardian Name(s)},\n\n".format(**player))
			file.write("Your child, {Name}, has been selected to play on\n"
				"the {Team Name}! The {Team Name} first practice is on \n"
				"Saturday, November 26, 2016 at 10:00am. Can't wait to see\n"
				"{Name} there!\n".format(**player))
			file.write("\nSincerely,\n\nYour Soccer League")