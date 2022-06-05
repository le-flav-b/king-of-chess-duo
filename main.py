# KING OF CHESS DUO
import time
from files.game import Game
from files.pawns import *
pygame.init()
# python -m pip install pygame

# not successful:
#  promotion
#  can't be check by yourself

# define the text font
clock_font = pygame.font.SysFont('impact', 25)
winner_font = pygame.font.SysFont('arialblack', 35)
details_font = pygame.font.SysFont('timesnewroman', 20)
thanks_font = pygame.font.SysFont('verdana', 28)
continue_font = pygame.font.SysFont('monospace', 15)

# generate the game window with its background
pygame.display.set_caption('King of Chess Duo')
pygame.display.set_icon(pygame.image.load('files/assets/icon.png'))
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('files/assets/background.png')

# generate play button, banner, and statistics rectangle
play_button = pygame.image.load('files/assets/play_button2.png')
play_button = pygame.transform.scale(play_button, (250, 88))
play_button_rect = play_button.get_rect()
play_button_rect.x, play_button_rect.y = 415, 360

music_on_button = pygame.image.load('files/assets/music_on.png')
music_on_button = pygame.transform.scale(music_on_button, (60, 60))
music_rect = music_on_button.get_rect()
music_rect.x, music_rect.y = 940, 10

music_off_button = pygame.image.load('files/assets/music_off.png')
music_off_button = pygame.transform.scale(music_off_button, (60, 60))

sound_on_button = pygame.image.load('files/assets/sound_on.png')
sound_on_button = pygame.transform.scale(sound_on_button, (60, 60))
sound_rect = sound_on_button.get_rect()
sound_rect.x, sound_rect.y = 1010, 10

sound_off_button = pygame.image.load('files/assets/sound_off.png')
sound_off_button = pygame.transform.scale(sound_off_button, (60, 60))

banner = pygame.image.load('files/assets/banner.png')
banner = pygame.transform.scale(banner, (400, 400))

rectangle = pygame.image.load('files/assets/rectangle.png')
rectangle = pygame.transform.scale(rectangle, (400, 500))
rectangle.set_alpha(225)

# generate the background music and all the sounds
background_music = pygame.mixer.Sound('files/assets/background_music.wav')
background_music.set_volume(0.2)
background_music.fadeout(1000)
press_play = pygame.mixer.Sound('files/assets/press_play.wav')
press_play.set_volume(0.6)
press_settings = pygame.mixer.Sound('files/assets/click.wav')
press_settings.set_volume(0.6)
victory = pygame.mixer.Sound('files/assets/victory.wav')
victory.set_volume(0.8)
stalemate = pygame.mixer.Sound('files/assets/stalemate.wav')
stalemate.set_volume(0.7)
white_move = pygame.mixer.Sound('files/assets/white_move.wav')
white_move.set_volume(0.5)
black_move = pygame.mixer.Sound('files/assets/black_move.wav')
black_move.set_volume(0.5)
check = pygame.mixer.Sound('files/assets/check.wav')
check.set_volume(0.6)


# function to find if we are stalemate by 3 times the same series of moves
def find_3_repetitions(a_list):
    a_list_copy = a_list.copy()
    if len(a_list_copy) >= 12:
        while len(a_list_copy) % 6 != 0:
            del a_list_copy[0]
        for i in range(len(a_list_copy) // 6 - 1):
            end_of_list = a_list_copy[len(a_list_copy) - (12 + 6 * i):]
            if end_of_list[:4 + 2 * i] == end_of_list[4 + 2 * i:8 + 4 * i] == end_of_list[8 + 4 * i:]:
                return True
    return False


# create and initialize a game
game = Game()

selected = None
counter = 0
music_on = True
sound_on = True
# overall game loop
running = True
print('\nGAME OPENING')
background_music.play(119, 0, 1000)
while running:

    # apply background
    screen.blit(background, (-100, 0))

    # apply images of pieces
    for piece in game.all_pieces:
        if piece.is_alive:
            screen.blit(piece.image, piece.rect)
        else:
            screen.blit(piece.image, piece.dead_position)

    # apply images of settings buttons
    if music_on:
        screen.blit(music_on_button, music_rect)
    else:
        screen.blit(music_off_button, music_rect)
    if sound_on:
        screen.blit(sound_on_button, sound_rect)
    else:
        screen.blit(sound_off_button, sound_rect)

    if game.state == 'playing':

        total_time = round(time.time() - game.start_time)
        clock = clock_font.render(str(total_time // 60) + ' min ' + str(total_time % 60) + ' sec ', True,
                                  (255, 150, 150))
        screen.blit(clock, (10, 10))

        # display a point on each squares where the selected pawn can move
        if selected is not None:
            for coordinates in selected.show_possibilities(game):
                possible_move_rect.x = table[coordinates[0]][coordinates[1]][0]
                possible_move_rect.y = table[coordinates[0]][coordinates[1]][1]
                screen.blit(possible_move_image, possible_move_rect)

        # if the user interacts
        for event in pygame.event.get():

            # if the user clicks on a piece
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_coordinates = pygame.mouse.get_pos()
                mouse_case = ((mouse_coordinates[1] - 79)//70, (mouse_coordinates[0] - 260)//70)

                # select the clicked piece
                if game.white_pawn_0.rect.collidepoint(event.pos) and game.white_pawn_0.is_alive\
                        and game.round == 'white':
                    selected = game.white_pawn_0
                elif game.white_pawn_1.rect.collidepoint(event.pos) and game.white_pawn_1.is_alive\
                        and game.round == 'white':
                    selected = game.white_pawn_1
                elif game.white_pawn_2.rect.collidepoint(event.pos) and game.white_pawn_2.is_alive\
                        and game.round == 'white':
                    selected = game.white_pawn_2
                elif game.white_pawn_3.rect.collidepoint(event.pos) and game.white_pawn_3.is_alive\
                        and game.round == 'white':
                    selected = game.white_pawn_3
                elif game.white_pawn_4.rect.collidepoint(event.pos) and game.white_pawn_4.is_alive\
                        and game.round == 'white':
                    selected = game.white_pawn_4
                elif game.white_pawn_5.rect.collidepoint(event.pos) and game.white_pawn_5.is_alive\
                        and game.round == 'white':
                    selected = game.white_pawn_5
                elif game.white_pawn_6.rect.collidepoint(event.pos) and game.white_pawn_6.is_alive\
                        and game.round == 'white':
                    selected = game.white_pawn_6
                elif game.white_pawn_7.rect.collidepoint(event.pos) and game.white_pawn_7.is_alive\
                        and game.round == 'white':
                    selected = game.white_pawn_7
                elif game.white_rook_0.rect.collidepoint(event.pos) and game.white_rook_0.is_alive\
                        and game.round == 'white':
                    selected = game.white_rook_0
                elif game.white_rook_1.rect.collidepoint(event.pos) and game.white_rook_1.is_alive\
                        and game.round == 'white':
                    selected = game.white_rook_1
                elif game.white_knight_0.rect.collidepoint(event.pos) and game.white_knight_0.is_alive\
                        and game.round == 'white':
                    selected = game.white_knight_0
                elif game.white_knight_1.rect.collidepoint(event.pos) and game.white_knight_1.is_alive\
                        and game.round == 'white':
                    selected = game.white_knight_1
                elif game.white_bishop_0.rect.collidepoint(event.pos) and game.white_bishop_0.is_alive\
                        and game.round == 'white':
                    selected = game.white_bishop_0
                elif game.white_bishop_1.rect.collidepoint(event.pos) and game.white_bishop_1.is_alive\
                        and game.round == 'white':
                    selected = game.white_bishop_1
                elif game.white_queen.rect.collidepoint(event.pos) and game.white_queen.is_alive\
                        and game.round == 'white':
                    selected = game.white_queen
                elif game.white_king.rect.collidepoint(event.pos) and game.white_king.is_alive\
                        and game.round == 'white':
                    selected = game.white_king
                elif game.black_pawn_0.rect.collidepoint(event.pos) and game.black_pawn_0.is_alive\
                        and game.round == 'black':
                    selected = game.black_pawn_0
                elif game.black_pawn_1.rect.collidepoint(event.pos) and game.black_pawn_1.is_alive\
                        and game.round == 'black':
                    selected = game.black_pawn_1
                elif game.black_pawn_2.rect.collidepoint(event.pos) and game.black_pawn_2.is_alive\
                        and game.round == 'black':
                    selected = game.black_pawn_2
                elif game.black_pawn_3.rect.collidepoint(event.pos) and game.black_pawn_3.is_alive\
                        and game.round == 'black':
                    selected = game.black_pawn_3
                elif game.black_pawn_4.rect.collidepoint(event.pos) and game.black_pawn_4.is_alive\
                        and game.round == 'black':
                    selected = game.black_pawn_4
                elif game.black_pawn_5.rect.collidepoint(event.pos) and game.black_pawn_5.is_alive\
                        and game.round == 'black':
                    selected = game.black_pawn_5
                elif game.black_pawn_6.rect.collidepoint(event.pos) and game.black_pawn_6.is_alive\
                        and game.round == 'black':
                    selected = game.black_pawn_6
                elif game.black_pawn_7.rect.collidepoint(event.pos) and game.black_pawn_7.is_alive\
                        and game.round == 'black':
                    selected = game.black_pawn_7
                elif game.black_rook_0.rect.collidepoint(event.pos) and game.black_rook_0.is_alive\
                        and game.round == 'black':
                    selected = game.black_rook_0
                elif game.black_rook_1.rect.collidepoint(event.pos) and game.black_rook_1.is_alive\
                        and game.round == 'black':
                    selected = game.black_rook_1
                elif game.black_knight_0.rect.collidepoint(event.pos) and game.black_knight_0.is_alive\
                        and game.round == 'black':
                    selected = game.black_knight_0
                elif game.black_knight_1.rect.collidepoint(event.pos) and game.black_knight_1.is_alive\
                        and game.round == 'black':
                    selected = game.black_knight_1
                elif game.black_bishop_0.rect.collidepoint(event.pos) and game.black_bishop_0.is_alive\
                        and game.round == 'black':
                    selected = game.black_bishop_0
                elif game.black_bishop_1.rect.collidepoint(event.pos) and game.black_bishop_1.is_alive\
                        and game.round == 'black':
                    selected = game.black_bishop_1
                elif game.black_queen.rect.collidepoint(event.pos) and game.black_queen.is_alive\
                        and game.round == 'black':
                    selected = game.black_queen
                elif game.black_king.rect.collidepoint(event.pos) and game.black_king.is_alive\
                        and game.round == 'black':
                    selected = game.black_king

                # move if a piece is selected and the user clicks on a square where he can go
                elif selected is not None and mouse_case in selected.show_possibilities(game):
                    move = chr(65 + selected.position[0]) + str(selected.position[1] + 1) + '  ->  ' +\
                            chr(65 + mouse_case[0]) + str(mouse_case[1] + 1)
                    print(move, end='    ')
                    game.recent_moves.append(move)

                    # to can eat
                    if mouse_case in all_values(game.busy):
                        find_key(mouse_case, game.busy).is_alive = False
                        del game.busy[find_key(mouse_case, game.busy)]
                        game.recent_moves = []

                    # to do the "take by the way"
                    elif mouse_case[1] == 5 and selected in game.all_pieces[:8] and (mouse_case[0], mouse_case[1] - 1)\
                            in all_values(game.busy) and find_key((mouse_case[0], mouse_case[1] - 1), game.busy) in\
                            game.all_pieces[16:24]:
                        find_key((mouse_case[0], mouse_case[1] - 1), game.busy).is_alive = False
                        del game.busy[find_key((mouse_case[0], mouse_case[1] - 1), game.busy)]
                    elif mouse_case[1] == 2 and selected in game.all_pieces[16:24] and\
                            (mouse_case[0], mouse_case[1] + 1) in all_values(game.busy) and\
                            find_key((mouse_case[0], mouse_case[1] + 1), game.busy) in game.all_pieces[:8]:
                        find_key((mouse_case[0], mouse_case[1] + 1), game.busy).is_alive = False
                        del game.busy[find_key((mouse_case[0], mouse_case[1] + 1), game.busy)]

                    # to do the castling
                    if selected == game.white_king and not selected.has_moved or selected == game.black_king\
                            and not selected.has_moved:
                        if selected == game.white_king:
                            if mouse_case == (2, 0):
                                if not game.white_rook_0.has_moved:
                                    game.white_rook_0.move((3, 0), game.busy)
                            elif mouse_case == (6, 0):
                                if not game.white_rook_1.has_moved:
                                    game.white_rook_1.move((5, 0), game.busy)
                        elif mouse_case == (2, 7):
                            if not game.black_rook_0.has_moved:
                                game.black_rook_0.move((3, 7), game.busy)
                        elif mouse_case == (6, 7):
                            if not game.black_rook_1.has_moved:
                                game.black_rook_1.move((5, 7), game.busy)

                    # to check if the pawn just took his double step
                    if selected in game.all_pieces[:8] + game.all_pieces[16:24]:
                        if selected.color == 'white' and selected.position[1] == 1 and mouse_case[1] == 3 or\
                                selected.color == 'black' and selected.position[1] == 6 and mouse_case[1] == 4:
                            selected.just_took_his_double_step = True

                    # to move
                    selected.move(mouse_case, game.busy)

                    # to check if someone is check
                    if game.round == 'white' and game.black_king.position in game.all_possibilities() or\
                            game.round == 'black' and game.white_king.position in game.all_possibilities():
                        print('check !')
                        if sound_on:
                            check.play()
                        if game.round == 'white':
                            game.check_from_white += 1
                        else:
                            game.check_from_black += 1
                    else:
                        print()

                    # to pass to the next round
                    if game.round == 'white':
                        if sound_on:
                            white_move.play()
                        game.white_time += time.time() - game.last_time
                        game.round = 'black'
                        # to do the "take by the way"
                        for piece in game.all_pieces[16:24]:
                            piece.just_took_his_double_step = False
                        game.nb_moves += 1
                    else:
                        if sound_on:
                            black_move.play()
                        game.black_time += time.time() - game.last_time
                        game.round = 'white'
                        # to do the "take by the way"
                        for piece in game.all_pieces[:8]:
                            piece.just_took_his_double_step = False
                    game.last_time = time.time()
                    selected = None

                # if the user changes the settings
                elif music_rect.collidepoint(event.pos):
                    if music_on:
                        music_on = False
                        background_music.set_volume(0)
                        print('--- music off ---')
                    else:
                        music_on = True
                        background_music.set_volume(0.2)
                        print('--- music on ---')
                    press_settings.play()
                elif sound_rect.collidepoint(event.pos):
                    if sound_on:
                        sound_on = False
                        print('--- sound off ---')
                    else:
                        sound_on = True
                        print('--- sound on ---')
                    press_settings.play()

                else:
                    selected = None

            # if the user leave
            elif event.type == pygame.QUIT:
                running = False

        # if there is a winner or stalemate
        # TODO: if we could be check ourselves we should have replaced the "not alive" by the comments
        # if find_3_repetitions(game.recent_moves) or len(game.all_possibilities()) == 0:
        if find_3_repetitions(game.recent_moves) or not game.white_king.is_alive or not game.black_king.is_alive:

            # play music for the winner
            background_music.stop()
            # if sound_on and (game.black_king.position in game.all_possibilities('white') or game.black_king.position\
            #                 in game.all_possibilities('black'))
            if sound_on and (not game.white_king.is_alive or not game.black_king.is_alive):
                victory.play()
            elif sound_on:
                stalemate.play()

            if not game.black_king.is_alive:  # if game.black_king.position in game.all_possibilities('white')
                print('\nWHITE PLAYER WON !')
                game.winner = 'White'
            elif not game.white_king.is_alive:  # if game.black_king.position in game.all_possibilities('black')
                print('\nBLACK PLAYER WON !')
                game.winner = 'Black'
            else:
                print('\nSTALEMATE !')
            game.state = 'statistics'
            print('consultation of statistics...')

    elif game.state == 'standby':
        screen.blit(clock_font.render('0 min 0 sec', True, (255, 150, 150)), (10, 10))
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, (340, 120)) #365 145

        # if the user interacts
        for event in pygame.event.get():

            # if the user click on the play button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    if sound_on:
                        press_play.play()
                    game.state = 'playing'
                    print('\n\nstart of the game\n')
                    game.start_time = time.time()
                    game.last_time = time.time()

                # if the user changes the settings
                if music_rect.collidepoint(event.pos):
                    if music_on:
                        music_on = False
                        background_music.set_volume(0)
                        print('--- music off ---')
                    else:
                        music_on = True
                        background_music.set_volume(0.2)
                        print('--- music on ---')
                    press_settings.play()
                elif sound_rect.collidepoint(event.pos):
                    if sound_on:
                        sound_on = False
                        print('--- sound off ---')
                    else:
                        sound_on = True
                        print('--- sound on ---')
                    press_settings.play()

            # if the user leave
            elif event.type == pygame.QUIT:
                running = False

    else:
        screen.blit(clock, (10, 10))
        screen.blit(rectangle, (340, 110))

        if game.winner is not None:
            text_winner = winner_font.render(game.winner + ' player Won !', True, (255, 28, 28))
            screen.blit(text_winner, (363, 150))

        else:
            text_winner = winner_font.render('Stalemate !', True, (255, 0, 0))
            screen.blit(text_winner, (428, 150))

        text_nb_moves = details_font.render('number of move to finish :  ' + str(game.nb_moves), True, (0, 0, 0))
        screen.blit(text_nb_moves, (385, 230))

        text_time_total = details_font.render('total playing time :  ' + str(total_time // 60) + ' min ' +
                                              str(total_time % 60) + ' sec ', True, (0, 0, 0))
        screen.blit(text_time_total, (385, 290))
        text_time_white = details_font.render('white playing time :  ' + str(round(game.white_time // 60)) + ' min ' +
                                              str(round(game.white_time % 60)) + ' sec ', True, (0, 0, 0))
        screen.blit(text_time_white, (385, 320))
        text_time_black = details_font.render('black playing time :  ' + str(round(game.black_time // 60)) + ' min ' +
                                              str(round(game.black_time % 60)) + ' sec ', True, (0, 0, 0))
        screen.blit(text_time_black, (385, 350))

        text_check_white = details_font.render('number of check from white :  ' + str(game.check_from_white),
                                               True, (0, 0, 0))
        screen.blit(text_check_white, (385, 410))
        text_check_black = details_font.render('number of check from black :  ' + str(game.check_from_black),
                                               True, (0, 0, 0))
        screen.blit(text_check_black, (385, 440))

        text_thanks = thanks_font.render('thanks for playing !', True, (22, 166, 55))
        screen.blit(text_thanks, (402, 490))

        counter += 1
        if 0 <= counter % 40 <= 28:
            screen.blit(continue_font.render('..press space to continue..', True, (0, 0, 255)), (415, 560))

        # if the user interacts
        for event in pygame.event.get():

            # if the user finished viewing statistics
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    game = Game()
                    game.state = 'standby'
                    print('game over')
                    background_music.play(119, 0, 1000)

            # if the user changes the settings
            if event.type == pygame.MOUSEBUTTONDOWN:
                if music_rect.collidepoint(event.pos):
                    if music_on:
                        music_on = False
                        background_music.set_volume(0)
                        print('--- music off ---')
                    else:
                        music_on = True
                        background_music.set_volume(0.2)
                        print('--- music on ---')
                    press_settings.play()
                elif sound_rect.collidepoint(event.pos):
                    if sound_on:
                        sound_on = False
                        print('--- sound off ---')
                    else:
                        sound_on = True
                        print('--- sound on ---')
                    press_settings.play()

            # if the user leave
            elif event.type == pygame.QUIT:
                running = False

    # update screen
    pygame.display.flip()

pygame.quit()
print('\n\nGAME CLOSING')
