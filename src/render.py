from game2dboard import Board


# from src.pre_proc import *


class Visualize():

    def __init__(self, p_map, actions: list):
        self.p_map = p_map
        # Add the Flag to the End of the Map!
        self.p_map += 'D'
        self.actions = actions
        self.start = False
        self.step = 0
        self.board_len = min(63 // 3, len(p_map))
        self.board = Board(2, self.board_len)
        self.board.on_key_press = self.onkey
        self.board.title = 'Super Mario!'
        self.board.on_timer = self.ontimer
        self.board.start_timer(263)

    def fill_board(self):
        # Fill the Game Board!
        for x, cell in enumerate(self.p_map[self.step:self.board_len + self.step]):
            # L Cells Are on The Top of the Map!
            if 'L' in cell:
                self.board[0][x % self.board_len] = cell
            # Other Cells Are on the Middle of the Map!
            else:
                self.board[1][x % self.board_len] = cell

        # Jump Action (Player Image Should Show on the Top of the Map)!
        if self.action == '1':
            self.board[0][0] = 'pj'
        # Sit Action (Player Image Should Show on the Bottom of the Map)!
        elif self.action == '2':
            self.board[1][0] = 'pm'
        # Move Forward Action (Player Image Should Show on the Middle of the Map)!
        else:
            self.board[1][0] = 'p'

    def ontimer(self):
        # The Rendering isn't Started Yet!
        if not self.start:
            return
        # End of the Rendering!
        if self.step == len(self.actions):
            exit(0)
        # Clear the Board for the New Step!
        self.board.clear()
        # Get the Action of this Step!
        self.action = self.actions[self.step - 1]
        # Move Forward if This is the First Step!
        if self.step == 0:
            self.action = '0'

        # Fill the Game Board!
        self.fill_board()

        # Increase the Step!
        self.step += 1

    def onkey(self, key):
        if key == "Return":
            self.start = True


    def render(self):
        self.board.show()
