import random


class Dice:

    def __init__(self, num_players, num_rounds, num_dices):
        self.num_players = num_players
        self.num_rounds = num_rounds
        self.num_dices = num_dices
        self.value = random.randint(1, 6)
        self.dic = {}
        self.list = []

    def game(self):
        for i in range(self.num_rounds):
            for k in range(self.num_dices):
                self.value = random.randint(1, 6)
                self.list.append(self.value)
            for j in range(self.num_players):
                guess = int(input('Try guessing the number player' + str(j) + str(' ')))
                if guess not in self.list:
                    if j in self.dic.keys():
                        self.dic[j] -= 1
                    else:
                        self.dic[j] = -1
                elif guess in self.list:
                    n = self.list.count(guess)
                    if j in self.dic.keys():
                        self.dic[j] += n
                    else:
                        self.dic[j] = n

            print(self.list)
            self.list.clear()

    def __str__(self):
        return str(self.dic)


def main():
    nPlayers = int(input('How many players? '))
    nRounds = int(input('How many rounds? '))
    nDices = int(input('How many dices will be used? '))
    game = Dice(nPlayers, nRounds, nDices)
    game.game()

    print(game)


main()
