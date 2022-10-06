from board import ComputerBoard, PlayerBoard
from move import MovePlayer, MoveComputer
from ui import UI


player = PlayerBoard(10, 10)
computer = ComputerBoard(10, 10)


# 2. Start the service to work with the selected repository
moveplayer = MovePlayer(player, computer)
movecomputer = MoveComputer(player, computer)

# 3. Start the UI with the initialized services
ui = UI(player, computer, moveplayer, movecomputer)

# 4. Start the program
ui.start()
