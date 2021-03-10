class GamePiece:
    """Creates game piece object"""
    def __init__(self):
        self._piece = "None"
        self._player = "None"
        self._pos = "None"
        self._piece_name = "None"

    def get_piece(self):
        return self._piece

    def get_player(self):
        return self._player

    def get_pos(self):
        return self._pos

    def get_piece_name(self):
        return self._piece_name

    def set_piece(self, piece_name):
        self._piece = piece_name

    def set_player(self, player):
        self._player = player

    def set_pos(self, new_pos):
        self._pos = new_pos


class General(GamePiece):
    """Creates general game piece inheriting properties from parent game piece class."""
    def __init__(self, player, x_coor, y_coor, piece_name):
        self._piece = "General"
        self._player = player
        self._pos = [x_coor, y_coor]
        self._piece_name = piece_name


class Guard(GamePiece):
    """Creates general game piece inheriting properties from parent game piece class."""
    def __init__(self, player, x_coor, y_coor, piece_name):
        self._piece = "Guard"
        self._player = player
        self._pos = [x_coor, y_coor]
        self._piece_name = piece_name


class Soldier(GamePiece):
    """Creates general game piece inheriting properties from parent game piece class."""
    def __init__(self, player, x_coor, y_coor, piece_name):
        self._piece = "Soldier"
        self._player = player
        self._pos = [x_coor, y_coor]
        self._piece_name = piece_name


class Cannon(GamePiece):
    """Creates general game piece inheriting properties from parent game piece class."""
    def __init__(self, player, x_coor, y_coor, piece_name):
        self._piece = "Cannon"
        self._player = player
        self._pos = [x_coor, y_coor]
        self._piece_name = piece_name


class Horse(GamePiece):
    """Creates general game piece inheriting properties from parent game piece class."""
    def __init__(self, player, x_coor, y_coor, piece_name):
        self._piece = "Horse"
        self._player = player
        self._pos = [x_coor, y_coor]
        self._piece_name = piece_name


class Elephant(GamePiece):
    """Creates general game piece inheriting properties from parent game piece class."""
    def __init__(self, player, x_coor, y_coor, piece_name):
        self._piece = "Elephant"
        self._player = player
        self._pos = [x_coor, y_coor]
        self._piece_name = piece_name


class Chariot(GamePiece):
    """Creates general game piece inheriting properties from parent game piece class."""
    def __init__(self, player, x_coor, y_coor, piece_name):
        self._piece = "Chariot"
        self._player = player
        self._pos = [x_coor, y_coor]
        self._piece_name = piece_name


def get_coords(pos):
    """Converts algebraic notation to numerical coordinates."""
    x = 0
    y = 0
    if pos[0] == 'a':
        x = 0
    elif pos[0] == 'b':
        x = 1
    elif pos[0] == 'c':
        x = 2
    elif pos[0] == 'd':
        x = 3
    elif pos[0] == 'e':
        x = 4
    elif pos[0] == 'f':
        x = 5
    elif pos[0] == 'g':
        x = 6
    elif pos[0] == 'h':
        x = 7
    elif pos[0] == 'i':
        x = 8

    if pos[1] == '1' and len(pos) == 2:
        y = 0
    elif pos[1] == '2':
        y = 1
    elif pos[1] == '3':
        y = 2
    elif pos[1] == '4':
        y = 3
    elif pos[1] == '5':
        y = 4
    elif pos[1] == '6':
        y = 5
    elif pos[1] == '7':
        y = 6
    elif pos[1] == '8':
        y = 7
    elif pos[1] == '9':
        y = 8
    elif pos[1] == '1' and pos[2] == '0':
        y = 9
    coordinates = [x, y]
    return coordinates


class JanggiGame:
    """Class responsible for creating the game and initializing the board, it
    communicates with all of the game piece classes."""

    def __init__(self):
        """Initializes the game board and places all the pieces for both teams
        in the appropriate starting positions, and sets the initial player
        turn to blue's turn."""

        # First board is just for my visualization and keeping track of pieces, thus why it is not a private variable.
        # "Real Board" is the board where the actual class getters are being called to confirm piece types and player
        # possesion of individual pieces where types of are their own class.

        self.board = [ ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"]]

        self._real_board = [ ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"],
                       ["---", "---", "---", "---", "---", "---", "---", "---", "---"]]
        self._player_turn = "blue"
        self._game_state = "UNFINISHED"
        self._check_red = "None"
        self._check_blue = "None"
        self._blue_gen_pos = "None"
        self._red_gen_pos = "None"

        # Below is a setup of the board with the initial piece placements of players: Red and Blue.

        RG1 = General("red", 4, 1, "RG1")               # Initializing both Generals and their board placement
        BG1 = General("blue", 4, 8, "BG1")
        self.board[1][4] = RG1.get_piece_name()
        self.board[8][4] = BG1.get_piece_name()
        self._real_board[1][4] = RG1
        self._real_board[8][4] = BG1
        self._blue_gen_pos = [4, 1]
        self._red_gen_pos = [4, 8]

        RS1 = Soldier("red", 0, 3, "RS1")               # Initializing all soldiers and their board placement
        RS2 = Soldier("red", 2, 3, "RS2")
        RS3 = Soldier("red", 4, 3, "RS3")
        RS4 = Soldier("red", 6, 3, "RS4")
        RS5 = Soldier("red", 8, 3, "RS5")
        self.board[3][0] = RS1.get_piece_name()
        self.board[3][2] = RS2.get_piece_name()
        self.board[3][4] = RS3.get_piece_name()
        self.board[3][6] = RS4.get_piece_name()
        self.board[3][8] = RS5.get_piece_name()
        self._real_board[3][0] = RS1
        self._real_board[3][2] = RS2
        self._real_board[3][4] = RS3
        self._real_board[3][6] = RS4
        self._real_board[3][8] = RS5

        BS1 = Soldier("blue", 0, 6, "BS1")
        BS2 = Soldier("blue", 2, 6, "BS2")
        BS3 = Soldier("blue", 4, 6, "BS3")
        BS4 = Soldier("blue", 6, 6, "BS4")
        BS5 = Soldier("blue", 8, 6, "BS5")
        self.board[6][0] = BS1.get_piece_name()
        self.board[6][2] = BS2.get_piece_name()
        self.board[6][4] = BS3.get_piece_name()
        self.board[6][6] = BS4.get_piece_name()
        self.board[6][8] = BS5.get_piece_name()
        self._real_board[6][0] = BS1
        self._real_board[6][2] = BS2
        self._real_board[6][4] = BS3
        self._real_board[6][6] = BS4
        self._real_board[6][8] = BS5

        RA1 = Guard("red", 3, 0, "RA1")                 # Initializing all guards and their board placement
        RA2 = Guard("red", 5, 0, "RA2")
        BA1 = Guard("blue", 3, 9, "BA1")
        BA2 = Guard("blue", 5, 9, "BA2")
        self.board[0][3] = RA1.get_piece_name()
        self.board[0][5] = RA2.get_piece_name()
        self.board[9][3] = BA1.get_piece_name()
        self.board[9][5] = BA2.get_piece_name()
        self._real_board[0][3] = RA1
        self._real_board[0][5] = RA2
        self._real_board[9][3] = BA1
        self._real_board[9][5] = BA2

        RE1 = Elephant("red", 1, 0, "RE1")              # Initializing all elephants and their board placement
        RE2 = Elephant("red", 6, 0, "RE2")
        BE1 = Elephant("blue", 1, 9, "BE1")
        BE2 = Elephant("blue", 6, 9, "BE2")
        self.board[0][1] = RE1.get_piece_name()
        self.board[0][6] = RE2.get_piece_name()
        self.board[9][1] = BE1.get_piece_name()
        self.board[9][6] = BE2.get_piece_name()
        self._real_board[0][1] = RE1
        self._real_board[0][6] = RE2
        self._real_board[9][1] = BE1
        self._real_board[9][6] = BE2

        RT1 = Chariot("red", 0, 0, "RT1")               # Initializing all chariots and their board placement
        RT2 = Chariot("red", 8, 0, "RT2")
        BT1 = Chariot("blue", 8, 9, "BT1")
        BT2 = Chariot("blue", 8, 9, "BT2")
        self.board[0][0] = RT1.get_piece_name()
        self.board[0][8] = RT2.get_piece_name()
        self.board[9][0] = BT1.get_piece_name()
        self.board[9][8] = BT2.get_piece_name()
        self._real_board[0][0] = RT1
        self._real_board[0][8] = RT2
        self._real_board[9][0] = BT1
        self._real_board[9][8] = BT2

        RH1 = Horse("red", 2, 0, "RH1")                 # Initializing all horses and their board placement
        RH2 = Horse("red", 7, 0, "RH2")
        BH1 = Horse("blue", 2, 9, "BH1")
        BH2 = Horse("blue", 7, 9, "BH2")
        self.board[0][2] = RH1.get_piece_name()
        self.board[0][7] = RH2.get_piece_name()
        self.board[9][2] = BH1.get_piece_name()
        self.board[9][7] = BH2.get_piece_name()
        self._real_board[0][2] = RH1
        self._real_board[0][7] = RH2
        self._real_board[9][2] = BH1
        self._real_board[9][7] = BH2

        RC1 = Cannon("red", 1, 2, "RC1")                #  Initializing all cannons and their board placement
        RC2 = Cannon("red", 7, 2, "RC2")
        BC1 = Cannon("blue", 1, 7, "BC1")
        BC2 = Cannon("blue", 7, 7, "BC2")
        self.board[2][1] = RC1.get_piece_name()
        self.board[2][7] = RC2.get_piece_name()
        self.board[7][1] = BC1.get_piece_name()
        self.board[7][7] = BC2.get_piece_name()
        self._real_board[2][1] = RC1
        self._real_board[2][7] = RC2
        self._real_board[7][1] = BC1
        self._real_board[7][7] = BC2

    def show_board(self):
        """Prints a visual representation of the current state of the board."""
        for row in self.board:
            print(*row)

    def show_real_board(self):
        for row in self._real_board:
            print(*row)

    def get_game_state(self):
        """Returns the current game state, being UNFINISHED, BLUE_WON, or RED_WON"""
        return self._game_state

    def is_in_check(self, player):
        """Returns true if the respective player is in check, returns false otherwise."""
        if player == 'blue' and self._check_blue == "Yes":
            return True
        elif player == 'red' and self._check_red == "Yes":
            return True
        else:
            return False

    def make_move(self, start, end):
        """Moves the game piece object on the board of depending on the game piece,
        returns False if move is invalid"""

        if self._real_board[get_coords(start)[1]][get_coords(start)[0]] == "---":
            return False

        blue_gen_x = self._blue_gen_pos[0]
        blue_gen_y = self._blue_gen_pos[1]
        red_gen_x = self._red_gen_pos[0]
        red_gen_y = self._red_gen_pos[1]

        start_coords = get_coords(start)
        start_x = start_coords[0]
        start_y = start_coords[1]
        start_piece_pos = self.board[start_y][start_x]
        start_piece = self._real_board[start_y][start_x]
        start_piece_type = start_piece.get_piece()
        start_player = start_piece.get_player()

        end_coords = get_coords(end)
        end_x = end_coords[0]
        end_y = end_coords[1]
        end_piece_pos = self.board[end_y][end_x]
        end_piece = self._real_board[end_y][end_x]

        blue_fort = ['d8', 'd9', 'd10', 'e8', 'e9', 'e10', 'f8', 'f9', 'f10']
        red_fort = ['d1', 'd2', 'd3', 'e1', 'e2', 'e3', 'f1', 'f2', 'f3']
        blue_illegal = ['d9', 'e8', 'f9', 'e10']
        red_illegal = ['e1', 'd2', 'e3', 'f2']
        horse_moves = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
        elephant_moves = [[2, 3], [3, 2], [3, -2], [2, -3], [-2, -3], [-3, -2], [-3, 2], [-2, 3]]
        checks_red = ['c1', 'c2', 'c3', 'd1', 'd2', 'd3', 'd4', 'e1', 'e2', 'e3', 'e4', 'f1', 'f2',
                      'f3', 'f4', 'g1', 'g2', 'g3']

        if start_piece == '---':                                       # This block returns False if wrong turn/wrong piece/
            return False                                               # game is already won.
        elif start_piece.get_player() != self._player_turn:
            return False
        elif self._game_state != "UNFINISHED":
            return False

        if end_piece != '---':
            if start_piece.get_player() == end_piece.get_player():     # Returns false is destination is friendly piece.
                return False

        if start_player == 'blue' and start == end:
            self._player_turn = 'red'
            return True
        if start_player == 'red' and start == end:
            self._player_turn = 'blue'
            return True

################################################################################### Soldiers ###########################

        if start_player == 'blue' and start_piece_type == "Soldier":
            if (end_y == start_y) and (end_x - 1 != start_x) and (end_x + 1 != start_x):
                return False
            elif (end_x == start_x) and (end_y - start_y != -1):
                return False
            elif (end_x - start_x > 1) or (end_y - start_y > 1):
                return False
            else:
                self.board[end_y][end_x] = start_piece.get_piece_name()
                self.board[start_y][start_x] = '---'
                self._real_board[end_y][end_x] = start_piece
                self._real_board[start_y][start_x] = '---'
                check_pos_x = red_gen_x - end_x
                check_pos_y = red_gen_y - end_y
                if end in checks_red:                                   # checks if soldier placement puts red in check.
                    if check_pos_x == 0 and check_pos_y == -1:
                        self._check_red = 'Yes'
                    elif check_pos_y == 0 and check_pos_x == 1:
                        self._check_red = 'Yes'
                    elif check_pos_y == 0 and check_pos_x == -1:
                        self._check_red = 'Yes'
                    elif (end == 'd3' or end == 'f3') and self._red_gen_pos == [4, 1]:
                        self._check_red = 'Yes'
                    elif (end == 'e2') and (self._red_gen_pos == [3, 0] or self._red_gen_pos == [5, 0]):
                        self._check_red = 'Yes'
                self._player_turn = 'red'
                return True

        if start_player == 'red' and start_piece_type == "Soldier":
            if (end_y == start_y) and (end_x - 1 != start_x) and (end_x + 1 != start_x):
                return False
            elif (end_x == start_x) and (end_y - start_y != 1):
                return False
            elif (end_x - start_x > 1) or (end_y - start_y > 1):
                return False
            else:
                self.board[end_y][end_x] = start_piece.get_piece_name()
                self.board[start_y][start_x] = '---'
                self._real_board[end_y][end_x] = start_piece
                self._real_board[start_y][start_x] = '---'
                self._player_turn = 'blue'
                return True

########################################################################################## Generals ####################

        if start_player == 'blue' and start_piece_type == 'General':
            if end not in blue_fort:
                return False
            if (end_x - start_x > 1) or (end_y - start_y > 1) or (end_x - start_x < -1) or (end_y - start_y < -1):
                return False
            if (start in blue_illegal) and (end in blue_illegal):               # Prevents wrong diagonal movement.
                return False
            else:
                self.board[end_y][end_x] = start_piece.get_piece_name()
                self.board[start_y][start_x] = '---'
                self._real_board[end_y][end_x] = start_piece
                self._real_board[start_y][start_x] = '---'
                self._blue_gen_pos = [end_x, end_y]
                self._player_turn = 'red'
                return True

        if start_player == 'red' and start_piece_type == 'General':
            if end not in red_fort:
                return False
            if (end_x - start_x > 1) or (end_y - start_y > 1) or (end_x - start_x < -1) or (end_y - start_y < -1):
                return False
            if (start in red_illegal) and (end in red_illegal):
                return False
            else:
                self.board[end_y][end_x] = start_piece.get_piece_name()
                self.board[start_y][start_x] = '---'
                self._real_board[end_y][end_x] = start_piece
                self._real_board[start_y][start_x] = '---'
                self._red_gen_pos = [end_x, end_y]
                self._player_turn = 'blue'
                return True


########################################################################################### Guards ####################

        if start_player == 'blue' and start_piece_type == 'Guard':
            if end not in blue_fort:
                return False
            if (end_x - start_x > 1) or (end_y - start_y > 1) or (end_x - start_x < -1) or (end_y - start_y < -1):
                return False
            if (start in blue_illegal) and (end in blue_illegal):
                return False
            else:
                self.board[end_y][end_x] = start_piece.get_piece_name()
                self.board[start_y][start_x] = '---'
                self._real_board[end_y][end_x] = start_piece
                self._real_board[start_y][start_x] = '---'
                self._player_turn = 'red'
                return True

        if start_player == 'red' and start_piece_type == 'Guard':
            if end not in red_fort:
                return False
            if (end_x - start_x > 1) or (end_y - start_y > 1) or (end_x - start_x < -1) or (end_y - start_y < -1):
                return False
            if (start in red_illegal) and (end in red_illegal):
                return False
            else:
                self.board[end_y][end_x] = start_piece.get_piece_name()
                self.board[start_y][start_x] = '---'
                self._real_board[end_y][end_x] = start_piece
                self._real_board[start_y][start_x] = '---'
                self._player_turn = 'blue'
                return True


############################################################################## Chariots (blue) ####################

        if start_player == 'blue' and start_piece_type == 'Chariot':
            x_diff = end_x - start_x
            y_diff = end_y - start_y
            blocked = None
            if (x_diff != 0) and (y_diff != 0):
                return False
            elif y_diff < 0:
                range_y = (abs(y_diff))
                for i in range(1, range_y):
                    temp_y = start_y - i
                    temp_pos = self.board[temp_y][start_x]
                    if temp_pos != '---':
                        blocked = True
                        break
                if blocked == True:
                    return False
            elif y_diff > 0:
                for i in range(1, y_diff):
                    temp_pos = self.board[start_y + i][start_x]
                    if temp_pos != '---':
                        blocked = True
                        break
                if blocked == True:
                    return False
            elif x_diff < 0:
                range_x = (abs(x_diff))
                for i in range(1, range_x):
                    temp_x = start_x - i
                    temp_pos = self.board[start_y][temp_x]
                    if temp_pos != '---':
                        blocked = True
                        break
                if blocked == True:
                    return False
            elif x_diff > 0:
                for i in range(1, x_diff):
                    temp_pos = self.board[start_y][start_x + i]
                    if temp_pos != '---':
                        blocked = True
                        break
                if blocked == True:
                    return False

            self.board[end_y][end_x] = start_piece.get_piece_name()
            self.board[start_y][start_x] = '---'
            self._real_board[end_y][end_x] = start_piece
            self._real_board[start_y][start_x] = '---'
            self._player_turn = 'red'
            return True


#################################################################################   Chariots (red) ####################

        if start_player == 'red' and start_piece_type == 'Chariot':
            x_diff = end_x - start_x
            y_diff = end_y - start_y
            blocked = None
            if (x_diff != 0) and (y_diff != 0):
                return False
            elif y_diff < 0:
                range_y = (abs(y_diff))
                for i in range(1, range_y):
                    temp_y = start_y - i
                    temp_pos = self.board[temp_y][start_x]
                    if temp_pos != '---':
                        blocked = True
                        break
                if blocked == True:
                    return False
            elif y_diff > 0:
                for i in range(1, y_diff):
                    temp_pos = self.board[start_y + i][start_x]
                    if temp_pos != '---':
                        blocked = True
                        break
                if blocked == True:
                    return False
            elif x_diff < 0:
                range_x = (abs(x_diff))
                for i in range(1, range_x):
                    temp_x = start_x - i
                    temp_pos = self.board[start_y][temp_x]
                    if temp_pos != '---':
                        blocked = True
                        break
                if blocked == True:
                    return False
            elif x_diff > 0:
                for i in range(1, x_diff):
                    temp_pos = self.board[start_y][start_x + i]
                    if temp_pos != '---':
                        blocked = True
                        break
                if blocked == True:
                    return False

            self.board[end_y][end_x] = start_piece.get_piece_name()
            self.board[start_y][start_x] = '---'
            self._real_board[end_y][end_x] = start_piece
            self._real_board[start_y][start_x] = '---'
            self._player_turn = 'blue'
            return True

################################################################################# Horses (blue) ########################

        if start_player == 'blue' and start_piece_type == 'Horse':
            x_diff = end_x - start_x
            y_diff = end_y - start_y
            move_pos = [x_diff, y_diff]
            if (y_diff > 2) or (y_diff < -2) or (x_diff > 2) or (x_diff < -2):
                return False
            elif move_pos not in horse_moves:
                return False
            elif ((x_diff == -1) or (x_diff == 1)) and (y_diff == 2):
                if self.board[start_y + 1][start_x] != '---':
                    return False
            elif ((x_diff == -1) or (x_diff == 1)) and (y_diff == -2):
                if self.board[start_y - 1][start_x] != '---':
                    return False
            elif ((y_diff == -1) or (y_diff == 1)) and (x_diff == 2):
                if self.board[start_y][start_x + 1] != '---':
                    return False
            elif ((y_diff == -1) or (y_diff == 1)) and (x_diff == -2):
                if self.board[start_y][start_x - 1] != '---':
                    return False

            self.board[end_y][end_x] = start_piece.get_piece_name()
            self.board[start_y][start_x] = '---'
            self._real_board[end_y][end_x] = start_piece
            self._real_board[start_y][start_x] = '---'
            self._player_turn = 'red'
            return True

################################################################################# Horses (red) ########################

        if start_player == 'red' and start_piece_type == 'Horse':
            x_diff = end_x - start_x
            y_diff = end_y - start_y
            move_pos = [x_diff, y_diff]
            if (y_diff > 2) or (y_diff < -2) or (x_diff > 2) or (x_diff < -2):
                return False
            elif move_pos not in horse_moves:
                return False
            elif ((x_diff == -1) or (x_diff == 1)) and (y_diff == 2):
                if self.board[start_y + 1][start_x] != '---':
                    return False
            elif ((x_diff == -1) or (x_diff == 1)) and (y_diff == -2):
                if self.board[start_y - 1][start_x] != '---':
                    return False
            elif ((y_diff == -1) or (y_diff == 1)) and (x_diff == 2):
                if self.board[start_y][start_x + 1] != '---':
                    return False
            elif ((y_diff == -1) or (y_diff == 1)) and (x_diff == -2):
                if self.board[start_y][start_x - 1] != '---':
                    return False

            self.board[end_y][end_x] = start_piece.get_piece_name()
            self.board[start_y][start_x] = '---'
            self._real_board[end_y][end_x] = start_piece
            self._real_board[start_y][start_x] = '---'
            self._player_turn = 'blue'
            return True


################################################################################# Elephants (blue) ######################

        if start_player == 'blue' and start_piece_type == 'Elephant':
            x_diff = end_x - start_x
            y_diff = end_y - start_y
            mov_pos = [x_diff, y_diff]
            if mov_pos not in elephant_moves:
                return False
            elif x_diff == 2 and y_diff == -3:
                if self.board[start_y - 1][start_x] != '---' or self.board[start_y - 2][start_x + 1] != '---':
                    return False
            elif x_diff == 3 and y_diff == -2:
                if self.board[start_y][start_x + 1] != '---' or self.board[start_y - 1][start_x + 2] != '---':
                    return False
            elif x_diff == 3 and y_diff == 2:
                if self.board[start_y][start_x + 1] != '---' or self.board[start_y + 1][start_x + 2] != '---':
                    return False
            elif x_diff == 2 and y_diff == 3:
                if self.board[start_y + 1][start_x] != '---' or self.board[start_y + 2][start_x + 1] != '---':
                    return False
            elif x_diff == -2 and y_diff == 3:
                if self.board[start_y + 1][start_x] != '---' or self.board[start_y + 2][start_x - 1] != '---':
                    return False
            elif x_diff == -3 and y_diff == 2:
                if self.board[start_y][start_x - 1] != '---' or self.board[start_y + 1][start_x - 2] != '---':
                    return False
            elif x_diff == -3 and y_diff == -2:
                if self.board[start_y ][start_x - 1] != '---' or self.board[start_y - 1][start_x - 2] != '---':
                    return False
            elif x_diff == -2 and y_diff == -3:
                if self.board[start_y - 1][start_x] != '---' or self.board[start_y - 2][start_x - 1] != '---':
                    return False

            self.board[end_y][end_x] = start_piece.get_piece_name()
            self.board[start_y][start_x] = '---'
            self._real_board[end_y][end_x] = start_piece
            self._real_board[start_y][start_x] = '---'
            self._player_turn = 'red'
            return True


################################################################################# Elephants (red) ######################

        if start_player == 'red' and start_piece_type == 'Elephant':
            x_diff = end_x - start_x
            y_diff = end_y - start_y
            mov_pos = [x_diff, y_diff]
            if mov_pos not in elephant_moves:
                return False
            elif x_diff == 2 and y_diff == -3:
                if self.board[start_y - 1][start_x] != '---' or self.board[start_y - 2][start_x + 1] != '---':
                    return False
            elif x_diff == 3 and y_diff == -2:
                if self.board[start_y][start_x + 1] != '---' or self.board[start_y - 1][start_x + 2] != '---':
                    return False
            elif x_diff == 3 and y_diff == 2:
                if self.board[start_y][start_x + 1] != '---' or self.board[start_y + 1][start_x + 2] != '---':
                    return False
            elif x_diff == 2 and y_diff == 3:
                if self.board[start_y + 1][start_x] != '---' or self.board[start_y + 2][start_x + 1] != '---':
                    return False
            elif x_diff == -2 and y_diff == 3:
                if self.board[start_y + 1][start_x] != '---' or self.board[start_y + 2][start_x - 1] != '---':
                    return False
            elif x_diff == -3 and y_diff == 2:
                if self.board[start_y][start_x - 1] != '---' or self.board[start_y + 1][start_x - 2] != '---':
                    return False
            elif x_diff == -3 and y_diff == -2:
                if self.board[start_y ][start_x - 1] != '---' or self.board[start_y - 1][start_x - 2] != '---':
                    return False
            elif x_diff == -2 and y_diff == -3:
                if self.board[start_y - 1][start_x] != '---' or self.board[start_y - 2][start_x - 1] != '---':
                    return False

            self.board[end_y][end_x] = start_piece.get_piece_name()
            self.board[start_y][start_x] = '---'
            self._real_board[end_y][end_x] = start_piece
            self._real_board[start_y][start_x] = '---'
            self._player_turn = 'blue'
            return True


################################################################################# Cannons (blue) ######################

        if start_player == 'blue' and start_piece_type == 'Cannon':
            x_diff = end_x - start_x
            y_diff = end_y - start_y
            illegal = None
            if x_diff != 0 and y_diff != 0:
                return False
            elif x_diff == 1 or y_diff == 1 or x_diff == -1 or y_diff == -1:
                return False
            elif y_diff < 0:
                blocks = 0
                y_range = abs(y_diff)
                for i in range(1, y_range):
                    temp_pos = self._real_board[start_y - i][start_x]
                    if temp_pos != '---':
                        blocks += 1
                        if temp_pos.get_piece() == 'Cannon':
                            illegal = True
                if blocks > 1 or illegal == True:
                    return False
            elif y_diff > 0:
                blocks = 0
                for i in range(1, y_diff):
                    temp_pos = self._real_board[start_y + i][start_x]
                    if temp_pos != '---':
                        blocks += 1
                        if temp_pos.get_piece() == 'Cannon':
                            illegal = True
                if blocks > 1 or illegal == True:
                    return False
            elif x_diff < 0:
                blocks = 0
                x_range = abs(x_diff)
                for i in range(1, x_range):
                    temp_pos = self._real_board[start_y][start_x - i]
                    if temp_pos != '---':
                        blocks += 1
                        if temp_pos.get_piece() == 'Cannon':
                            illegal = True
                if blocks > 1 or illegal == True:
                    return False
            elif x_diff > 0:
                blocks = 0
                for i in range(1, x_diff):
                    temp_pos = self._real_board[start_y][start_x + i]
                    if temp_pos != '---':
                        blocks += 1
                        if temp_pos.get_piece() == 'Cannon':
                            illegal = True
                    if blocks > 1 or illegal == True:
                        return False

            self.board[end_y][end_x] = start_piece.get_piece_name()
            self.board[start_y][start_x] = '---'
            self._real_board[end_y][end_x] = start_piece
            self._real_board[start_y][start_x] = '---'
            self._player_turn = 'red'
            return True


################################################################################# Cannons (red) ######################

        if start_player == 'red' and start_piece_type == 'Cannon':
            x_diff = end_x - start_x
            y_diff = end_y - start_y
            illegal = None
            if x_diff != 0 and y_diff != 0:
                return False
            elif x_diff == 1 or y_diff == 1 or x_diff == -1 or y_diff == -1:
                return False
            elif y_diff < 0:
                blocks = 0
                y_range = abs(y_diff)
                for i in range(1, y_range):
                    temp_pos = self._real_board[start_y - i][start_x]
                    if temp_pos != '---':
                        blocks += 1
                        if temp_pos.get_piece() == 'Cannon':
                            illegal = True
                if blocks > 1 or illegal == True:
                    return False
            elif y_diff > 0:
                blocks = 0
                for i in range(1, y_diff):
                    temp_pos = self._real_board[start_y + i][start_x]
                    if temp_pos != '---':
                        blocks += 1
                        if temp_pos.get_piece() == 'Cannon':
                            illegal = True
                if blocks > 1 or illegal == True:
                    return False
            elif x_diff < 0:
                blocks = 0
                x_range = abs(x_diff)
                for i in range(1, x_range):
                    temp_pos = self._real_board[start_y][start_x - i]
                    if temp_pos != '---':
                        blocks += 1
                        if temp_pos.get_piece() == 'Cannon':
                            illegal = True
                if blocks > 1 or illegal == True:
                    return False
            elif x_diff > 0:
                blocks = 0
                for i in range(1, x_diff):
                    temp_pos = self._real_board[start_y][start_x + i]
                    if temp_pos != '---':
                        blocks += 1
                        if temp_pos.get_piece() == 'Cannon':
                            illegal = True
                    if blocks > 1 or illegal == True:
                        return False

            self.board[end_y][end_x] = start_piece.get_piece_name()
            self.board[start_y][start_x] = '---'
            self._real_board[end_y][end_x] = start_piece
            self._real_board[start_y][start_x] = '---'
            self._player_turn = 'blue'
            return True



game = JanggiGame()
game.show_real_board()
print(" ")
game.show_board()
print(game.make_move('a7', 'b7'))
game.show_board()
print(game.make_move('c4', 'b4'))
game.show_board()
print(game.make_move('b8', 'b4'))
game.show_board()
print(game.make_move('a4', 'a5'))
game.show_board()
print(game.make_move('b4', 'b8'))
game.show_board()
print(game.make_move('a5', 'b5'))
game.show_board()
print(game.make_move('b8', 'b5'))
game.show_board()
print(game.make_move('a1', 'a6'))
game.show_board()
print(game.make_move('a10', 'a6'))
game.show_board()
print(game.make_move('i1', 'i3'))
game.show_board()
print(game.make_move('g7', 'h7'))
game.show_board()
print(game.make_move('g4', 'h4'))
game.show_board()
