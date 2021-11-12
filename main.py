print("Input your games, write print to list all the games")
games = []
while True:
    game = input()
    if game == "print":
        print(games)
        break
    else:
        games.append(game)
