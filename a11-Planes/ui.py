from exception import PlaneException


class UI:
    def __init__(self, player, computer, moveplayer, movecomputer):
        self._player = player
        self._computer = computer
        self._move_player = moveplayer
        self._move_computer = movecomputer

    def start(self):
        print("Welcome to Planes!")
        print("Your board")
        print(str(self._player))
        print("Computer`s board")
        print(str(self._computer))
        i = 0
        while i < 3:
            #computer introduces the planes
            try:
                i += 1
                self._move_computer.set_plane()
                #self._computer.show_planes()
            except PlaneException as ve:
                i -= 1
        #print(str(self._computer))

        i = 0
        while i < 3:
            try:
                #player introduces the planes
                move = input("Enter plane cabin: ")
                orient = input("Enter orientation: ")
                self._move_player.set_plane(move, orient)
                #self._player.show_planes()
                i += 1
            except PlaneException as ve:
                print(str(ve))

        """
        #used to spare the player from introducing the planes from the keyboard
        #print(str(self._player))
        self._move_player.set_plane('B3', 'N')
        self._move_player.set_plane('H3', 'E')
        self._move_player.set_plane('E8', 'N')
        """
        player_turn = True
        while len(self._player._planes_crushed) < 3 and len(self._computer._planes_crushed) < 3:
            try:
                if player_turn:
                    #player makes a move
                    move = input("Enter move: ")
                    if len(move) == 2:
                        if 'A' <= move[0] <= 'J' and '1' <= move[1] <= '9':
                            self._move_player.move(move)
                            print("Computer`s board: ")
                            print(str(self._computer))
                        else:
                            raise PlaneException("Not a valid cell!")
                    elif len(move) == 3:
                        if 'A' <= move[0] <= 'J' and move[1] == '1' and move[1] == '0':
                            self._move_player.move(move)
                            print("Computer`s board: ")
                            print(str(self._computer))
                        else:
                            raise PlaneException("Not a valid cell!")
                    else:
                        raise PlaneException("Not a valid cell!")
                else:
                    #computer makes a move (the move is printed out)
                    row, col = self._move_computer.move()
                    if col == 9:
                        square = chr(65 + row) + chr(49) + chr(48)
                    else:
                        square = chr(65 + row) + chr(49 + col)
                    print("Computer moves at:", square)
                    print("Your board: ")
                    print(str(self._player))
                player_turn = not player_turn
            except PlaneException as ve:
                print(str(ve))

        if player_turn:
            print("You LOST!")
        else:
            print("You WON!")
