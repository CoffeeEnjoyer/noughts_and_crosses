import pygame

pygame.init()

turn = "o"
knots = []
crosses = []
spacing = 31
s = spacing

knot = pygame.image.load('knot.png')
cross = pygame.image.load('cross.png')
win = pygame.image.load('win_screen.png')
winning = ""


def if_win(list1):

    l = len(list1)
    list3 = list1
    list1 = tuple(list1[l - 1])
# ify poziome
    if tuple([list1[0] + s, list1[1]]) in list3 and tuple([list1[0] + 2*s, list1[1]]) in list3:
        if tuple([list1[0] + 3*s, list1[1]]) in list3 and tuple([list1[0] + 4*s, list1[1]]) in list3:
            return True
    if tuple([list1[0] - s, list1[1]]) in list3 and tuple([list1[0] - 2 * s, list1[1]]) in list3:
        if tuple([list1[0] - 3 * s, list1[1]]) in list3 and tuple([list1[0] - 4 * s, list1[1]]) in list3:
            return True
    if tuple([list1[0] + s, list1[1]]) in list3 and tuple([list1[0] + 2*s, list1[1]]) in list3:
        if tuple([list1[0] + 3*s, list1[1]]) in list3 and tuple([list1[0] - s, list1[1]]) in list3:
            return True
    if tuple([list1[0] + s, list1[1]]) in list3 and tuple([list1[0] + 2*s, list1[1]]) in list3:
        if tuple([list1[0] - 2*s, list1[1]]) in list3 and tuple([list1[0] - s, list1[1]]) in list3:
            return True
    if tuple([list1[0] - s, list1[1]]) in list3 and tuple([list1[0] - 2*s, list1[1]]) in list3:
        if tuple([list1[0] - 3*s, list1[1]]) in list3 and tuple([list1[0] + s, list1[1]]) in list3:
            return True


# ify pionowe
    if tuple([list1[0], list1[1] + s]) in list3 and tuple([list1[0], list1[1] + 2*s]) in list3:
        if tuple([list1[0], list1[1] + 3*s]) in list3 and tuple([list1[0], list1[1] + 4*s]) in list3:
            return True
    if tuple([list1[0], list1[1] - s]) in list3 and tuple([list1[0], list1[1] - 2*s]) in list3:
        if tuple([list1[0], list1[1] - 3*s]) in list3 and tuple([list1[0], list1[1] - 4*s]) in list3:
            return True
    if tuple([list1[0], list1[1] + s]) in list3 and tuple([list1[0], list1[1] + 2*s]) in list3:
        if tuple([list1[0], list1[1] + 3*s]) in list3 and tuple([list1[0], list1[1] - s]) in list3:
            return True
    if tuple([list1[0], list1[1] + s]) in list3 and tuple([list1[0], list1[1] + 2*s]) in list3:
        if tuple([list1[0], list1[1] - 2*s]) in list3 and tuple([list1[0], list1[1] - s]) in list3:
            return True
    if tuple([list1[0], list1[1] - s]) in list3 and tuple([list1[0], list1[1] - 2*s]) in list3:
        if tuple([list1[0], list1[1] - 3*s]) in list3 and tuple([list1[0], list1[1] + s]) in list3:
            return True

# ify ukośne
    if tuple([list1[0] + s, list1[1] + s]) in list3 and tuple([list1[0] + 2 * s, list1[1] + 2*s]) in list3:
        if tuple([list1[0]+3*s, list1[1]+3*s]) in list3 and tuple([list1[0]+4*s, list1[1]+4*s]) in list3:
            return True
    if tuple([list1[0] - s, list1[1] - s]) in list3 and tuple([list1[0] - 2 * s, list1[1] - 2*s]) in list3:
        if tuple([list1[0] - 3*s, list1[1]-3*s]) in list3 and tuple([list1[0]-4*s, list1[1]-4*s]) in list3:
            return True
    if tuple([list1[0] + s, list1[1] + s]) in list3 and tuple([list1[0] + 2 * s, list1[1] + 2*s]) in list3:
        if tuple([list1[0] + 3*s, list1[1] + 3*s]) in list3 and tuple([list1[0] - s, list1[1] -s]) in list3:
            return True
    if tuple([list1[0] + s, list1[1] + s]) in list3 and tuple([list1[0] + 2 * s, list1[1] + 2*s]) in list3:
        if tuple([list1[0] - 2*s, list1[1] - 2*s]) in list3 and tuple([list1[0] - s, list1[1] -s]) in list3:
            return True
    if tuple([list1[0] - s, list1[1] - s]) in list3 and tuple([list1[0] - 2*s, list1[1] - 2*s]) in list3:
        if tuple([list1[0] - 3*s, list1[1] - 3*s]) in list3 and tuple([list1[0] + s, list1[1] +s]) in list3:
            return True

        # ify ukośne 2
    if tuple([list1[0] + s, list1[1] - s]) in list3 and tuple([list1[0] + 2 * s, list1[1] - 2 * s]) in list3:
        if tuple([list1[0] + 3 * s, list1[1] - 3 * s]) in list3 and tuple([list1[0] + 4*s, list1[1]-4*s]) in list3:
            return True
    if tuple([list1[0] - s, list1[1] + s]) in list3 and tuple([list1[0] - 2 * s, list1[1] + 2 * s]) in list3:
        if tuple([list1[0] - 3 * s, list1[1] + 3 * s]) in list3 and tuple([list1[0] - 4*s, list1[1]+4*s]) in list3:
            return True
    if tuple([list1[0] + s, list1[1] - s]) in list3 and tuple([list1[0] + 2 * s, list1[1] - 2 * s]) in list3:
        if tuple([list1[0] + 3 * s, list1[1] + 3 * s]) in list3 and tuple([list1[0] - s, list1[1] + s]) in list3:
            return True
    if tuple([list1[0] + s, list1[1] - s]) in list3 and tuple([list1[0] + 2 * s, list1[1] - 2 * s]) in list3:
        if tuple([list1[0] - 2 * s, list1[1] + 2 * s]) in list3 and tuple([list1[0] - s, list1[1] + s]) in list3:
            return True
    if tuple([list1[0] - s, list1[1] + s]) in list3 and tuple([list1[0] - 2 * s, list1[1] + 2 * s]) in list3:
        if tuple([list1[0] - 3 * s, list1[1] + 3 * s]) in list3 and tuple([list1[0] + s, list1[1] - s]) in list3:
            return True


# screen
height = 600
width = 1200
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
margin1 = 10
margin2 = 10




pygame.display.set_caption("O and X")

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
gridcolour = 0, 170, 30


#game loop
running = True
while running:

    screen.fill((60, 60, 60))

    width = screen.get_width()
    height = screen.get_height()

    corner = [(width - margin1 - (width - margin1) % spacing), (height - margin2 - (height - margin2) % spacing)]

    # grid
    line1 = margin1
    line2 = margin2
    while line1 <= width:
        pygame.draw.line(screen, gridcolour, [line1, 0], [line1, height], 1)
        line1 += spacing

    while line2 <= height:
        pygame.draw.line(screen, gridcolour, [0, line2], [width, line2], 1)
        line2 += spacing

    for kn in range(len(knots)):
        screen.blit(knot, knots[kn])

    for cs in range(len(crosses)):
        screen.blit(cross, crosses[cs])

    if winning != "":
        screen.blit(pygame.transform.scale(win, (750, 310)), ((width - 750)/2, (height - 310)/2))
        if winning == "knots":
            screen.blit(pygame.transform.scale(knot, (310, 310)), ((width - 750)/2, (height - 310)/2))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    winning = ""
                    knots = []
                    crosses = []
                    turn = "o"
                if event.type == pygame.QUIT:
                    running = False
        else:
            screen.blit(pygame.transform.scale(cross, (310, 310)), ((width - 750) / 2, (height - 310) / 2))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    winning = ""
                    knots = []
                    crosses = []
                    turn = "o"
                if event.type == pygame.QUIT:
                    running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = tuple(map(lambda x, y: x - (x-y)%spacing, pygame.mouse.get_pos(), [margin1, margin2]))

            list3 = knots + crosses
            if pos not in list3 and margin1 <= pos[0] < tuple(corner)[0] and margin2 <= pos[1] < tuple(corner)[1]:

                if turn == "o":
                    knots.append(pos)
                    if if_win(knots):
                        winning = "knots"

                    turn = "x"

                else:
                    crosses.append(pos)
                    if if_win(crosses):
                        winning = "crosses"

                    turn = "o"

    pygame.display.update()
