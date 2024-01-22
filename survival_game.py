import random

# PART A (10 points)

#########################################################################

class Member:
    '''
    Purpose: Represents a player in the game with their name and their
        social status.
    Instance variables:
        self.name: The player's name.
        self.socialStatus: The player's social status, which is initialized
            at 5.
    Methods:
        __init__: Initializes the instance variables
        updateStatus: Adds or subtracts 1 from the player's social status. The
            player's social status cannot go below 1 or above 10. The greater
            the number of the player's social status the more odds that player
            will be voted out.
        __repr__: Overrides the repr() method and outputs a string defining
            the name and the social status of a player.
    '''
    def __init__(self, name):
        self.name = name
        self.socialStatus = 5
    def updateStatus(self):
        self.socialStatus += random.choice([-1,1])
        if self.socialStatus < 1:
            self.socialStatus = 1
        elif self.socialStatus > 10:
            self.socialStatus = 10
    def __repr__(self):
        return f"Name: {self.name}, Social Status: {self.socialStatus}"

class Tribe:
    '''
    Purpose: Creates a tribe with their name and all the players within the
        said tribe. All playes within the tribe will have a name and a social
        status.
    Instance variables:
        self.tribeName: The tribe's name.
        self.members: An empty list later used for storing all the player names
            and assigned social status within the tribe.
    Methods:
        __init__: Initializes the instance variables
        updateStatusForAll: Updates every players' social status using the
            updateStatus method in the Member class.
    '''
    def __init__(self, tribeName, playerNames):
        self.tribeName = tribeName
        self.members = []
        for member in playerNames:
            mem = Member(member)
            self.members.append(mem)
    def updateStatusForAll(self):
        for member in self.members:
            member.updateStatus()
#########################################################################


# PART B (20 points)
#########################################################################


class Game:
    '''
    Purpose: Makes a survivor game that will be computer driven with random
        choices made by the computer.
    Instance variables:
        self.redTribe: Stores the redTribe that was passed in.
        self.blueTribe: Stores the blueTribe that was passed in.
        self.merge: Creates an initial tribe named Merge with no members in it.
    Methods:
        __init__: Initializes the instance variables
        challengeWinner: If two tribes are still in the game then one tribe
            will be randomly chosen to be the winner of the challenge and all
            the members in the winning tribe will be immune in the voting
            round. If both tribes merged and became one then one person within
            the merged group will be chosen to be the winner of the challenge
            and that one person will be immune during the voting round.
        getOdds: Makes a list of the names of all the people within a group and
            multiplies the amount of times their names appear in the list
            respective to their social status.
        vote: If there are two teams still in the game then the non-immune team
            will have a player voted out, which is decided by a random choice
            picked from the getOdds list created for the non-immune group. If
            there is only one team in the game then one of the non-immune
            players will be voted out, which is decided by a random choice
            picked from the getOdds list created for the merged group excluding
            the immune player's name.
        playSurvivor: Runs four rounds of the Tribe vs. Tribe Phase, which will
            run four challenges and votes to eliminate 4 players collectively.
            Then it will merge the two groups to create one group of 8 members.
            In the Merged Tribe Phase, the players within the one tribe will go
            through 6 challenges and vote outs until there are 2 members left.
            In the Winner Phase, one of the two members will be voted out and
            the winner of the competition will be outputted.
    '''
    def __init__(self, redTribe, blueTribe):
        self.redTribe = redTribe
        self.blueTribe = blueTribe
        self.merge = Tribe('Merge', [])

    def challengeWinner(self):
        if len(self.merge.members) > 0:
            members_object = random.choice(self.merge.members)
            return members_object.name
        else:
            return random.choice(['Red Tribe','Blue Tribe'])

    def getOdds(self, tribe):
        tribe_odds = []
        for player in tribe.members:
            tribe_odds += ([player.name]*player.socialStatus)
        return tribe_odds

    def vote(self, tribe, immune):
        tribe_odds = self.getOdds(tribe)
        vote_out = random.choice(tribe_odds)
        while vote_out == immune:
            vote_out = random.choice(tribe_odds)
        new_tribe = []
        for player in tribe.members:
            if vote_out != player.name:
                new_tribe.append(player)
        tribe.members = new_tribe
        return vote_out

    def playSurvivor(self):
        #Tribe vs. Tribe Phase
        for i in range(4):
            tribe_victor = self.challengeWinner()
            if tribe_victor == 'Red Tribe':
                print('Red Tribe wins the challenge!')
                player_out = self.vote(self.blueTribe, '')
                print(player_out+' voted out of the Blue Tribe\n')
            else:
                print('Blue Tribe wins the challenge!')
                player_out = self.vote(self.redTribe, '')
                print(player_out+' voted out of the Red Tribe\n')
            self.redTribe.updateStatusForAll()
            self.blueTribe.updateStatusForAll()
        #Merged Tribe Phase
        self.merge.members = self.redTribe.members + self.blueTribe.members
        for i in range(6):
            immune_winner = self.challengeWinner()
            print(immune_winner+' wins the challenge!')
            player_vote_out = self.vote(self.merge, immune_winner)
            print(player_vote_out+' voted out of the Merged Tribe\n')
            self.merge.updateStatusForAll()
        #Winner Phase
        self.vote(self.merge, '')
        winner = self.merge.members[0].name
        print('The sole survivor is '+ winner)

#########################################################################
#
# def main():
#      redTribeNames = ["Isaac", "Arunima", "Nakul", "Micah", "David", "Alice"]
#      blueTribeNames = ["Tarik", "Ian", "Charley", "Demond", "Abdourahman", "Vin"]
#      redTribe = Tribe("Red Tribe", redTribeNames)
#      blueTribe = Tribe("Blue Tribe", blueTribeNames)
#      simulation = Game(redTribe, blueTribe)
#      simulation.playSurvivor()
#
#
#     # names = ["Isaac", "Arunima", "Nakul", "Micah", "David", "Alice",
#     #         "Tarik", "Ian", "Charley", "Demond", "Abdourahman", "Vin"]
#     # redTribeNames = []
#     #
#     # while len(redTribeNames) < 6:
#     #     randName = random.choice(names)
#     #     redTribeNames.append(randName)
#     #     names.remove(randName)
#     #
#     # blueTribeNames = names
#     #
#     # # UNCOMMENT THE FOLLOWING TO CREATE TRIBES AND TEST THE SIMULATION
#     # redTribe = Tribe("Red Tribe", redTribeNames)
#     # blueTribe = Tribe("Blue Tribe", blueTribeNames)
#     #
#     # simulation = Game(redTribe, blueTribe)
#     # simulation.playSurvivor()
#
# if __name__ == '__main__':
#     main()
