from files.pawns import *


class Game:

    def __init__(self):

        self.state = 'standby'

        self.busy = {}
        self.round = 'white'
        self.winner = None
        self.nb_moves = 0
        self.recent_moves = []

        self.start_time = 0
        self.last_time = 0
        self.white_time = 0
        self.black_time = 0

        self.check_from_white = 0
        self.check_from_black = 0

        # create and place all pieces
        self.white_pawn_0 = Pawn()
        self.busy[self.white_pawn_0] = [(0, 1), 'white']

        self.white_pawn_1 = Pawn()
        self.busy[self.white_pawn_1] = [(0, 1), 'white']
        self.white_pawn_1.move((1, 1), self.busy)
        self.white_pawn_1.dead_position = (909, 156)

        self.white_pawn_2 = Pawn()
        self.busy[self.white_pawn_2] = [(0, 1), 'white']
        self.white_pawn_2.move((2, 1), self.busy)
        self.white_pawn_2.dead_position = (909, 226)

        self.white_pawn_3 = Pawn()
        self.busy[self.white_pawn_3] = [(0, 1), 'white']
        self.white_pawn_3.move((3, 1), self.busy)
        self.white_pawn_3.dead_position = (909, 296)

        self.white_pawn_4 = Pawn()
        self.busy[self.white_pawn_4] = [(0, 1), 'white']
        self.white_pawn_4.move((4, 1), self.busy)
        self.white_pawn_4.dead_position = (909, 366)

        self.white_pawn_5 = Pawn()
        self.busy[self.white_pawn_5] = [(0, 1), 'white']
        self.white_pawn_5.move((5, 1), self.busy)
        self.white_pawn_5.dead_position = (909, 436)

        self.white_pawn_6 = Pawn()
        self.busy[self.white_pawn_6] = [(0, 1), 'white']
        self.white_pawn_6.move((6, 1), self.busy)
        self.white_pawn_6.dead_position = (909, 506)

        self.white_pawn_7 = Pawn()
        self.busy[self.white_pawn_7] = [(0, 1), 'white']
        self.white_pawn_7.move((7, 1), self.busy)
        self.white_pawn_7.dead_position = (909, 576)

        ##############################

        self.black_pawn_0 = Pawn()
        self.busy[self.black_pawn_0] = [(0, 1), 'black']
        self.black_pawn_0.move((0, 6), self.busy)
        self.black_pawn_0.dead_position = (109, 86)
        self.black_pawn_0.black()

        self.black_pawn_1 = Pawn()
        self.busy[self.black_pawn_1] = [(0, 1), 'black']
        self.black_pawn_1.move((1, 6), self.busy)
        self.black_pawn_1.dead_position = (109, 156)
        self.black_pawn_1.black()

        self.black_pawn_2 = Pawn()
        self.busy[self.black_pawn_2] = [(0, 1), 'black']
        self.black_pawn_2.move((2, 6), self.busy)
        self.black_pawn_2.dead_position = (109, 226)
        self.black_pawn_2.black()

        self.black_pawn_3 = Pawn()
        self.busy[self.black_pawn_3] = [(0, 1), 'black']
        self.black_pawn_3.move((3, 6), self.busy)
        self.black_pawn_3.dead_position = (109, 296)
        self.black_pawn_3.black()

        self.black_pawn_4 = Pawn()
        self.busy[self.black_pawn_4] = [(0, 1), 'black']
        self.black_pawn_4.move((4, 6), self.busy)
        self.black_pawn_4.dead_position = (109, 366)
        self.black_pawn_4.black()

        self.black_pawn_5 = Pawn()
        self.busy[self.black_pawn_5] = [(0, 1), 'black']
        self.black_pawn_5.move((5, 6), self.busy)
        self.black_pawn_5.dead_position = (109, 436)
        self.black_pawn_5.black()

        self.black_pawn_6 = Pawn()
        self.busy[self.black_pawn_6] = [(0, 1), 'black']
        self.black_pawn_6.move((6, 6), self.busy)
        self.black_pawn_6.dead_position = (109, 506)
        self.black_pawn_6.black()

        self.black_pawn_7 = Pawn()
        self.busy[self.black_pawn_7] = [(0, 1), 'black']
        self.black_pawn_7.move((7, 6), self.busy)
        self.black_pawn_7.dead_position = (109, 566)
        self.black_pawn_7.black()

        ##############################
        ##############################

        self.white_rook_0 = Rook()
        self.busy[self.white_rook_0] = [(0, 0), 'white']

        self.white_rook_1 = Rook()
        self.busy[self.white_rook_1] = [(0, 0), 'white']
        self.white_rook_1.move((7, 0), self.busy)
        self.white_rook_1.dead_position = (979, 576)
        self.white_rook_1.has_moved = False

        ##############################

        self.black_rook_0 = Rook()
        self.busy[self.black_rook_0] = [(0, 0), 'black']
        self.black_rook_0.move((0, 7), self.busy)
        self.black_rook_0.dead_position = (39, 86)
        self.black_rook_0.black()
        self.black_rook_0.has_moved = False

        self.black_rook_1 = Rook()
        self.busy[self.black_rook_1] = [(0, 0), 'black']
        self.black_rook_1.move((7, 7), self.busy)
        self.black_rook_1.dead_position = (39, 576)
        self.black_rook_1.black()
        self.black_rook_1.has_moved = False

        ##############################
        ##############################

        self.white_knight_0 = Knight()
        self.busy[self.white_knight_0] = [(1, 0), 'white']

        self.white_knight_1 = Knight()
        self.busy[self.white_knight_1] = [(1, 0), 'white']
        self.white_knight_1.move((6, 0), self.busy)
        self.white_knight_1.dead_position = (979, 506)

        ##############################

        self.black_knight_0 = Knight()
        self.busy[self.black_knight_0] = [(1, 0), 'black']
        self.black_knight_0.move((1, 7), self.busy)
        self.black_knight_0.dead_position = (39, 156)
        self.black_knight_0.black()

        self.black_knight_1 = Knight()
        self.busy[self.black_knight_1] = [(1, 0), 'black']
        self.black_knight_1.move((6, 7), self.busy)
        self.black_knight_1.dead_position = (39, 506)
        self.black_knight_1.black()

        ##############################
        ##############################

        self.white_bishop_0 = Bishop()
        self.busy[self.white_bishop_0] = [(2, 0), 'white']

        self.white_bishop_1 = Bishop()
        self.busy[self.white_bishop_1] = [(2, 0), 'white']
        self.white_bishop_1.move((5, 0), self.busy)
        self.white_bishop_1.dead_position = (979, 436)

        ##############################

        self.black_bishop_0 = Bishop()
        self.busy[self.black_bishop_0] = [(2, 0), 'black']
        self.black_bishop_0.move((2, 7), self.busy)
        self.black_bishop_0.dead_position = (39, 226)
        self.black_bishop_0.black()

        self.black_bishop_1 = Bishop()
        self.busy[self.black_bishop_1] = [(2, 0), 'black']
        self.black_bishop_1.move((5, 7), self.busy)
        self.black_bishop_1.dead_position = (39, 436)
        self.black_bishop_1.black()

        ##############################
        ##############################

        self.white_queen = Queen()
        self.busy[self.white_queen] = [(3, 0), 'white']

        ##############################

        self.black_queen = Queen()
        self.busy[self.black_queen] = [(3, 0), 'black']
        self.black_queen.move((3, 7), self.busy)
        self.black_queen.dead_position = (39, 296)
        self.black_queen.black()

        ##############################
        ##############################

        self.white_king = King()
        self.busy[self.white_king] = [(4, 0), 'white']

        ##############################

        self.black_king = King()
        self.busy[self.black_king] = [(4, 0), 'black']
        self.black_king.move((4, 7), self.busy)
        self.black_king.dead_position = (39, 366)
        self.black_king.black()
        self.black_king.has_moved = False

        #############################
        #############################

        self.all_pieces = [self.white_pawn_0, self.white_pawn_1, self.white_pawn_2, self.white_pawn_3,
                           self.white_pawn_4, self.white_pawn_5, self.white_pawn_6, self.white_pawn_7,
                           self.white_rook_0, self.white_rook_1, self.white_knight_0, self.white_knight_1,
                           self.white_bishop_0, self.white_bishop_1, self.white_queen, self.white_king,
                           self.black_pawn_0, self.black_pawn_1, self.black_pawn_2, self.black_pawn_3,
                           self.black_pawn_4, self.black_pawn_5, self.black_pawn_6, self.black_pawn_7,
                           self.black_rook_0, self.black_rook_1, self.black_knight_0, self.black_knight_1,
                           self.black_bishop_0, self.black_bishop_1, self.black_queen, self.black_king]

    def all_possibilities(self, color=None):
        if color is None:
            color = self.round
        all_possibilities = []
        for piece in self.busy:
            if piece.color == color:
                for possibilities in piece.show_possibilities(self):
                    if possibilities not in all_possibilities:
                        all_possibilities.append(possibilities)
        return all_possibilities
