import pygame
# from copy import copy

# create an board with the coordinates of the squares
table = [[(264, 86),  (334, 86),  (404, 86),  (474, 86),  (544, 86),  (614, 86),  (684, 86),  (754, 86)],
         [(264, 156), (334, 156), (404, 156), (474, 156), (544, 156), (614, 156), (684, 156), (754, 156)],
         [(264, 226), (334, 226), (404, 226), (474, 226), (544, 226), (614, 226), (684, 226), (754, 226)],
         [(264, 296), (334, 296), (404, 296), (474, 296), (544, 296), (614, 296), (684, 296), (754, 296)],
         [(264, 366), (334, 366), (404, 366), (474, 366), (544, 366), (614, 366), (684, 366), (754, 366)],
         [(264, 436), (334, 436), (404, 436), (474, 436), (544, 436), (614, 436), (684, 436), (754, 436)],
         [(264, 506), (334, 506), (404, 506), (474, 506), (544, 506), (614, 506), (684, 506), (754, 506)],
         [(264, 576), (334, 576), (404, 576), (474, 576), (544, 576), (614, 576), (684, 576), (754, 576)]]

# generate the points of possibilities image
possible_move_image = pygame.image.load('files/assets/possible_move.png')
possible_move_image = pygame.transform.scale(possible_move_image, (60, 60))
possible_move_rect = possible_move_image.get_rect()


def all_values(busy):
    return [v[0] for v in busy.values()]


def find_key(value, busy):
    for k, v in busy.items():
        if v[0] == value:
            return k


def find_piece_color(coordinates, busy):
    values = [v for v in busy.values()]
    for value in values:
        if value[0] == coordinates:
            return value[1]


def all_possibilities(game, color):
    all_the_possibilities = []
    for piece in game.busy:
        if piece.color != color:
            if piece.type != 'king':
                for possibilities in piece.show_possibilities(game):
                    if possibilities not in all_the_possibilities:
                        all_the_possibilities.append(possibilities)
    return all_the_possibilities


# create an object for each type of pieces
class Pawn(pygame.sprite.Sprite):

    def __init__(self):
        super(Pawn, self).__init__()
        self.type = "pawn"
        self.image = pygame.image.load('files/assets/white_pawn.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'white'
        self.rect = self.image.get_rect()
        self.rect.x = table[0][1][0]
        self.rect.y = table[0][1][1]
        self.position = (0, 1)
        self.is_alive = True
        self.dead_position = (909, 86)
        self.just_took_his_double_step = False

    def black(self):
        self.image = pygame.image.load('files/assets/black_pawn.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'black'

    def move(self, case, busy):
        self.rect.x = table[case[0]][case[1]][0]
        self.rect.y = table[case[0]][case[1]][1]
        busy[self][0] = case
        self.position = case

    def show_possibilities(self, game):
        busy = game.busy
        possibilities = []
        if self.color == 'white' and self.rect.x != table[0][7][0]:
            if not (self.position[0], self.position[1] + 1) in all_values(busy):
                possibilities.append((self.position[0], self.position[1] + 1))
                if self.position[1] == 1 and not (self.position[0], self.position[1] + 2) in all_values(busy):
                    possibilities.append((self.position[0], self.position[1] + 2))
            if self.rect.y != table[0][0][1] and (self.position[0] - 1, self.position[1] + 1) in all_values(busy):
                if find_piece_color((self.position[0] - 1, self.position[1] + 1), busy) == 'black':
                    possibilities.append((self.position[0] - 1, self.position[1] + 1))
            if self.rect.y != table[7][0][1] and (self.position[0] + 1, self.position[1] + 1) in all_values(busy):
                if find_piece_color((self.position[0] + 1, self.position[1] + 1), busy) == 'black':
                    possibilities.append((self.position[0] + 1, self.position[1] + 1))
            # for the "take by the way"
            if self.rect.x == table[0][4][0]:
                if self.position[0] > 0 and (self.position[0] - 1, self.position[1]) in all_values(busy) and \
                        find_key((self.position[0] - 1, self.position[1]), busy).color != self.color and \
                        find_key((self.position[0] - 1, self.position[1]), busy).type == "pawn" and \
                        find_key((self.position[0] - 1, self.position[1]), busy).just_took_his_double_step:
                    possibilities.append((self.position[0] - 1, self.position[1] + 1))
                if self.position[0] < 7 and (self.position[0] + 1, self.position[1]) in all_values(busy) and \
                        find_key((self.position[0] + 1, self.position[1]), busy).color != self.color and \
                        find_key((self.position[0] + 1, self.position[1]), busy).type == "pawn" and \
                        find_key((self.position[0] + 1, self.position[1]), busy).just_took_his_double_step:
                    possibilities.append((self.position[0] + 1, self.position[1] + 1))
        elif self.rect.x != table[0][0][0]:
            if not (self.position[0], self.position[1] - 1) in all_values(busy):
                possibilities.append((self.position[0], self.position[1] - 1))
                if self.position[1] == 6 and not (self.position[0], self.position[1] - 2) in all_values(busy):
                    possibilities.append((self.position[0], self.position[1] - 2))
            if self.rect.y != table[0][0][1] and (self.position[0] - 1, self.position[1] - 1) in all_values(busy):
                if find_piece_color((self.position[0] - 1, self.position[1] - 1), busy) == 'white':
                    possibilities.append((self.position[0] - 1, self.position[1] - 1))
            if self.rect.y != table[7][0][1] and (self.position[0] + 1, self.position[1] - 1) in all_values(busy):
                if find_piece_color((self.position[0] + 1, self.position[1] - 1), busy) == 'white':
                    possibilities.append((self.position[0] + 1, self.position[1] - 1))
            # for the "take by the way"
            if self.rect.x == table[0][3][0]:
                if self.position[0] > 0 and (self.position[0] - 1, self.position[1]) in all_values(busy) and \
                        find_key((self.position[0] - 1, self.position[1]), busy).color != self.color and \
                        find_key((self.position[0] - 1, self.position[1]), busy).type == "pawn" and \
                        find_key((self.position[0] - 1, self.position[1]), busy).just_took_his_double_step:
                    possibilities.append((self.position[0] - 1, self.position[1] - 1))
                if self.position[0] < 7 and (self.position[0] + 1, self.position[1]) in all_values(busy) and \
                        find_key((self.position[0] + 1, self.position[1]), busy).color != self.color and \
                        find_key((self.position[0] + 1, self.position[1]), busy).type == "pawn" and \
                        find_key((self.position[0] + 1, self.position[1]), busy).just_took_his_double_step:
                    possibilities.append((self.position[0] + 1, self.position[1] - 1))
        return possibilities


class Rook(pygame.sprite.Sprite):

    def __init__(self):
        super(Rook, self).__init__()
        self.type = "rook"
        self.image = pygame.image.load('files/assets/white_rook.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'white'
        self.rect = self.image.get_rect()
        self.rect.x = table[0][0][0]
        self.rect.y = table[0][0][1]
        self.position = (0, 0)
        self.is_alive = True
        self.dead_position = (979, 86)
        self.has_moved = False

    def black(self):
        self.image = pygame.image.load('files/assets/black_rook.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'black'

    def move(self, case, busy):
        self.rect.x = table[case[0]][case[1]][0]
        self.rect.y = table[case[0]][case[1]][1]
        busy[self][0] = case
        self.position = case
        self.has_moved = True

    def show_possibilities(self, game):
        busy = game.busy
        possibilities = []
        i = 1
        while not (self.position[0] + i, self.position[1]) in all_values(busy) and self.position[0] + i < 8:
            possibilities.append((self.position[0] + i, self.position[1]))
            i += 1
        if (self.position[0] + i, self.position[1]) in all_values(busy) and \
                find_piece_color((self.position[0] + i, self.position[1]), busy) != self.color:
            possibilities.append((self.position[0] + i, self.position[1]))
        i = 1
        while not (self.position[0] - i, self.position[1]) in all_values(busy) and self.position[0] - i > -1:
            possibilities.append((self.position[0] - i, self.position[1]))
            i += 1
        if (self.position[0] - i, self.position[1]) in all_values(busy) and \
                find_piece_color((self.position[0] - i, self.position[1]), busy) != self.color:
            possibilities.append((self.position[0] - i, self.position[1]))
        i = 1
        while not (self.position[0], self.position[1] + i) in all_values(busy) and self.position[1] + i < 8:
            possibilities.append((self.position[0], self.position[1] + i))
            i += 1
        if (self.position[0], self.position[1] + i) in all_values(busy) and \
                find_piece_color((self.position[0], self.position[1] + i), busy) != self.color:
            possibilities.append((self.position[0], self.position[1] + i))
        i = 1
        while not (self.position[0], self.position[1] - i) in all_values(busy) and self.position[1] - i > -1:
            possibilities.append((self.position[0], self.position[1] - i))
            i += 1
        if (self.position[0], self.position[1] - i) in all_values(busy) and \
                find_piece_color((self.position[0], self.position[1] - i), busy) != self.color:
            possibilities.append((self.position[0], self.position[1] - i))
        return possibilities


class Knight(pygame.sprite.Sprite):

    def __init__(self):
        super(Knight, self).__init__()
        self.type = "knight"
        self.image = pygame.image.load('files/assets/white_knight.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'white'
        self.rect = self.image.get_rect()
        self.rect.x = table[1][0][0]
        self.rect.y = table[1][0][1]
        self.position = (1, 0)
        self.is_alive = True
        self.dead_position = (979, 156)

    def black(self):
        self.image = pygame.image.load('files/assets/black_knight.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'black'

    def move(self, case, busy):
        self.rect.x = table[case[0]][case[1]][0]
        self.rect.y = table[case[0]][case[1]][1]
        busy[self][0] = case
        self.position = case

    def show_possibilities(self, game):
        busy = game.busy
        possibilities = [(self.position[0] - 2, self.position[1] - 1), (self.position[0] - 2, self.position[1] + 1),
                         (self.position[0] + 2, self.position[1] - 1), (self.position[0] + 2, self.position[1] + 1),
                         (self.position[0] - 1, self.position[1] - 2), (self.position[0] + 1, self.position[1] - 2),
                         (self.position[0] - 1, self.position[1] + 2), (self.position[0] + 1, self.position[1] + 2)]
        if self.position[0] <= 1:
            possibilities.remove((self.position[0] - 2, self.position[1] - 1))
            possibilities.remove((self.position[0] - 2, self.position[1] + 1))
            if self.position[0] == 0:
                possibilities.remove((self.position[0] - 1, self.position[1] - 2))
                possibilities.remove((self.position[0] - 1, self.position[1] + 2))
        elif self.position[0] >= 6:
            possibilities.remove((self.position[0] + 2, self.position[1] - 1))
            possibilities.remove((self.position[0] + 2, self.position[1] + 1))
            if self.position[0] == 7:
                possibilities.remove((self.position[0] + 1, self.position[1] - 2))
                possibilities.remove((self.position[0] + 1, self.position[1] + 2))
        if self.position[1] <= 1:
            if (self.position[0] - 1, self.position[1] - 2) in possibilities:
                possibilities.remove((self.position[0] - 1, self.position[1] - 2))
            if (self.position[0] + 1, self.position[1] - 2) in possibilities:
                possibilities.remove((self.position[0] + 1, self.position[1] - 2))
            if self.position[1] == 0:
                if (self.position[0] - 2, self.position[1] - 1) in possibilities:
                    possibilities.remove((self.position[0] - 2, self.position[1] - 1))
                if (self.position[0] + 2, self.position[1] - 1) in possibilities:
                    possibilities.remove((self.position[0] + 2, self.position[1] - 1))
        elif self.position[1] >= 6:
            if (self.position[0] - 1, self.position[1] + 2) in possibilities:
                possibilities.remove((self.position[0] - 1, self.position[1] + 2))
            if (self.position[0] + 1, self.position[1] + 2) in possibilities:
                possibilities.remove((self.position[0] + 1, self.position[1] + 2))
            if self.position[1] == 7:
                if (self.position[0] - 2, self.position[1] + 1) in possibilities:
                    possibilities.remove((self.position[0] - 2, self.position[1] + 1))
                if (self.position[0] + 2, self.position[1] + 1) in possibilities:
                    possibilities.remove((self.position[0] + 2, self.position[1] + 1))
        while len([p for p in possibilities if p in all_values(busy) and find_piece_color(p, busy) == self.color]) > 0:
            for p in possibilities:
                if p in all_values(busy) and find_piece_color(p, busy) == self.color:
                    possibilities.remove(p)
        return possibilities


class Bishop(pygame.sprite.Sprite):

    def __init__(self):
        super(Bishop, self).__init__()
        self.type = "bishop"
        self.image = pygame.image.load('files/assets/white_bishop.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'white'
        self.rect = self.image.get_rect()
        self.rect.x = table[2][0][0]
        self.rect.y = table[2][0][1]
        self.position = (2, 0)
        self.is_alive = True
        self.dead_position = (979, 226)

    def black(self):
        self.image = pygame.image.load('files/assets/black_bishop.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'black'

    def move(self, case, busy):
        self.rect.x = table[case[0]][case[1]][0]
        self.rect.y = table[case[0]][case[1]][1]
        busy[self][0] = case
        self.position = case

    def show_possibilities(self, game):
        busy = game.busy
        possibilities = []
        i = 1
        while not (self.position[0] + i, self.position[1] + i) in all_values(busy) and self.position[0] + i < 8 \
                and self.position[1] + i < 8:
            possibilities.append((self.position[0] + i, self.position[1] + i))
            i += 1
        if (self.position[0] + i, self.position[1] + i) in all_values(busy) and \
                find_piece_color((self.position[0] + i, self.position[1] + i), busy) != self.color:
            possibilities.append((self.position[0] + i, self.position[1] + i))
        i = 1
        while not (self.position[0] + i, self.position[1] - i) in all_values(busy) and self.position[0] + i < 8 \
                and self.position[1] - i > -1:
            possibilities.append((self.position[0] + i, self.position[1] - i))
            i += 1
        if (self.position[0] + i, self.position[1] - i) in all_values(busy) and \
                find_piece_color((self.position[0] + i, self.position[1] - i), busy) != self.color:
            possibilities.append((self.position[0] + i, self.position[1] - i))
        i = 1
        while not (self.position[0] - i, self.position[1] + i) in all_values(busy) and self.position[0] - i > -1 \
                and self.position[1] + i < 8:
            possibilities.append((self.position[0] - i, self.position[1] + i))
            i += 1
        if (self.position[0] - i, self.position[1] + i) in all_values(busy) and \
                find_piece_color((self.position[0] - i, self.position[1] + i), busy) != self.color:
            possibilities.append((self.position[0] - i, self.position[1] + i))
        i = 1
        while not (self.position[0] - i, self.position[1] - i) in all_values(busy) and self.position[0] - i > -1 \
                and self.position[1] - i > -1:
            possibilities.append((self.position[0] - i, self.position[1] - i))
            i += 1
        if (self.position[0] - i, self.position[1] - i) in all_values(busy) and \
                find_piece_color((self.position[0] - i, self.position[1] - i), busy) != self.color:
            possibilities.append((self.position[0] - i, self.position[1] - i))
        return possibilities


class Queen(pygame.sprite.Sprite):

    def __init__(self):
        super(Queen, self).__init__()
        self.type = "queen"
        self.image = pygame.image.load('files/assets/white_queen.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'white'
        self.rect = self.image.get_rect()
        self.rect.x = table[3][0][0]
        self.rect.y = table[3][0][1]
        self.position = (3, 0)
        self.is_alive = True
        self.dead_position = (979, 296)

    def black(self):
        self.image = pygame.image.load('files/assets/black_queen.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'black'

    def move(self, case, busy):
        self.rect.x = table[case[0]][case[1]][0]
        self.rect.y = table[case[0]][case[1]][1]
        busy[self][0] = case
        self.position = case

    def show_possibilities(self, game):
        return Rook.show_possibilities(self, game) + Bishop.show_possibilities(self, game)


class King(pygame.sprite.Sprite):

    def __init__(self):
        super(King, self).__init__()
        self.type = "king"
        self.image = pygame.image.load('files/assets/white_king.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'white'
        self.rect = self.image.get_rect()
        self.rect.x = table[4][0][0]
        self.rect.y = table[4][0][1]
        self.position = (4, 0)
        self.is_alive = True
        self.dead_position = (979, 366)
        self.has_moved = False

    def black(self):
        self.image = pygame.image.load('files/assets/black_king.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.color = 'black'

    def move(self, case, busy):
        self.rect.x = table[case[0]][case[1]][0]
        self.rect.y = table[case[0]][case[1]][1]
        busy[self][0] = case
        self.position = case
        self.has_moved = True

    def show_possibilities(self, game):
        busy = game.busy
        possibilities = [(self.position[0] - 1, self.position[1] - 1), (self.position[0] - 1, self.position[1]),
                         (self.position[0] - 1, self.position[1] + 1), (self.position[0], self.position[1] - 1),
                         (self.position[0], self.position[1] + 1), (self.position[0] + 1, self.position[1] - 1),
                         (self.position[0] + 1, self.position[1]), (self.position[0] + 1, self.position[1] + 1)]
        if self.position[0] == 0:
            possibilities.remove((self.position[0] - 1, self.position[1] - 1))
            possibilities.remove((self.position[0] - 1, self.position[1]))
            possibilities.remove((self.position[0] - 1, self.position[1] + 1))
        elif self.position[0] == 7:
            possibilities.remove((self.position[0] + 1, self.position[1] - 1))
            possibilities.remove((self.position[0] + 1, self.position[1]))
            possibilities.remove((self.position[0] + 1, self.position[1] + 1))
        if self.position[1] == 0:
            if (self.position[0] - 1, self.position[1] - 1) in possibilities:
                possibilities.remove((self.position[0] - 1, self.position[1] - 1))
            if (self.position[0], self.position[1] - 1) in possibilities:
                possibilities.remove((self.position[0], self.position[1] - 1))
            if (self.position[0] + 1, self.position[1] - 1) in possibilities:
                possibilities.remove((self.position[0] + 1, self.position[1] - 1))
        elif self.position[1] == 7:
            if (self.position[0] - 1, self.position[1] + 1) in possibilities:
                possibilities.remove((self.position[0] - 1, self.position[1] + 1))
            if (self.position[0], self.position[1] + 1) in possibilities:
                possibilities.remove((self.position[0], self.position[1] + 1))
            if (self.position[0] + 1, self.position[1] + 1) in possibilities:
                possibilities.remove((self.position[0] + 1, self.position[1] + 1))
        while len([p for p in possibilities if p in all_values(busy) and find_piece_color(p, busy) == self.color]) > 0:
            for p in possibilities:
                if p in all_values(busy) and find_piece_color(p, busy) == self.color:
                    possibilities.remove(p)
        if not self.has_moved:
            if not (self.position[0] + 1, self.position[1]) in all_values(busy) and \
                    not (self.position[0] + 2, self.position[1]) in all_values(busy) and \
                    (self.position[0] + 3, self.position[1]) in all_values(busy) and \
                    find_key((self.position[0] + 3, self.position[1]), busy).type == 'rook' and \
                    not find_key((self.position[0] + 3, self.position[1]), busy).has_moved and \
                    not self.position in all_possibilities(game, self.color) and \
                    not (self.position[0] + 1, self.position[1]) in all_possibilities(game, self.color) and \
                    not (self.position[0] + 2, self.position[1]) in all_possibilities(game, self.color) and \
                    not (self.position[0] + 3, self.position[1]) in all_possibilities(game, self.color):
                possibilities.append((self.position[0] + 2, self.position[1]))
            if not (self.position[0] - 1, self.position[1]) in all_values(busy) and \
                    not (self.position[0] - 2, self.position[1]) in all_values(busy) and \
                    not (self.position[0] - 3, self.position[1]) in all_values(busy) and \
                    (self.position[0] - 4, self.position[1]) in all_values(busy) and \
                    find_key((self.position[0] - 4, self.position[1]), busy).type == 'rook' and \
                    not find_key((self.position[0] - 4, self.position[1]), busy).has_moved and \
                    not self.position in all_possibilities(game, self.color) and \
                    not (self.position[0] - 1, self.position[1]) in all_possibilities(game, self.color) and \
                    not (self.position[0] - 2, self.position[1]) in all_possibilities(game, self.color) and \
                    not (self.position[0] - 3, self.position[1]) in all_possibilities(game, self.color) and \
                    not (self.position[0] - 4, self.position[1]) in all_possibilities(game, self.color):
                possibilities.append((self.position[0] - 2, self.position[1]))
        return possibilities
