from Player import Player
import os
from LevelOne import LevelOne
from LevelFour import LevelFour
from LevelTwo import LevelTwo


# find the finish room in the list
def where_is_finish(_rooms):
    for room in _rooms:
        if room.finish:
            return room


# check if you finished the level
def end(_player, _rooms):
    finish_room = where_is_finish(_rooms)
    if _player.pos == finish_room.cords:
        return True
    else:
        return False


def press_key_to_continue():
    input("Press enter to continue...")
    os.system('clear')


def level_number(lvl):
    num = ""
    if lvl == 1:
        num = "One"
    elif lvl == 2:
        num = "Two"
    elif lvl == 3:
        num = "Three"
    elif lvl == 4:
        num = "Four"
    return f"___Level {num}___"


# Level one init
level = LevelOne()
level_rooms = level.level_one_rooms()
level_keys = []

# Start
print("___The maze___")
press_key_to_continue()

# Level 1
level_num = 4
print(level_number(level_num))
press_key_to_continue()
while level_num != 5:
    # level 2
    if level_num == 2:
        level = LevelTwo()
        level_rooms = level.level_two_rooms()
        level_keys = level.level_two_keys(level_rooms[4])
        os.system('clear')
        print(level_number(level_num))
        press_key_to_continue()
    # level 3
    elif level_num == 3:
        pass
    # level 4
    elif level_num == 4:
        level = LevelFour()
        level_rooms = level.level_four_rooms()
        level_keys = level.level_four_keys(level_rooms[19], level_rooms[11], level_rooms[3])
        os.system('clear')
        print(level_number(level_num))
        press_key_to_continue()

    player = Player(0, 0, level_rooms, level_keys)

    loop = True
    while loop:
        player.decision()
        os.system('clear')
        if end(player, level_rooms):
            level_num += 1
            break
    input("You have finished this level!")
print("Congratulations! You have won the game :)")




