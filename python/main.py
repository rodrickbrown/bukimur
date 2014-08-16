import random
class Player(object):
    tiles = []

    def __init__(self, name):
        self.name = name

    def getTiles(self):
        return None

    def setTiles(self, tiles):
        self.tiles.extend(tiles)

    def getPlayerName(self):
        return self.name


class Rummikub(object):
    decks = [0,1]
    colors = ["red", "blue", "black", "orange"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    jokers = ["black", "red"]

    bag = []

    def __init__(self, players):
        self.players = players
        print('----- Intialzing game with {0} players -----'.format(players))

        for deck in self.decks:
            for color in self.colors:
                for number in self.numbers:
                    self.bag.append({"deck":deck, "color":color, "number":number})
        [ self.bag.append(joker) for joker in self.jokers ]

    def dealTiles(self, n):
        tiles = []
        for c in range(n):
            tiles.append(self.bag.pop(random.randint(0, len(self.bag)-1)))

        return tiles

if __name__ == '__main__':
    game = Rummikub(1)
    player = Player('rodrick')

    print("Size of bag is now {0}".format(len(game.bag)))
    print("Dealing 1 tile to {0}".format(player.getPlayerName()))
    myTiles = game.dealTiles(1)
    for tiles in myTiles: print(tiles)
    print("Size of bag is now {0}".format(len(game.bag)))
    print("Dealing 1 tile to {0}".format(player.getPlayerName()))
    myTiles = game.dealTiles(1)
    for tiles in myTiles: print(tiles)
    print("Size of bag is now {0}".format(len(game.bag)))

