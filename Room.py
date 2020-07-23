from colorama import Fore, Back, Style


class Room(object):
    def __init__(self, number, x, y, door_n=False, door_e=False, door_s=False, door_w=False,
                 is_r_n=False, is_r_e=False, is_r_s=False, is_r_w=False, door_n_locked=False,
                 door_e_locked=False, door_s_locked=False, door_w_locked=False, key=False, finish=False,
                 key_color="", color_n="", color_w="", color_e="", color_s=""):

        self.number = number
        self.cords = [x, y]
        self.doorN = door_n
        self.doorE = door_e
        self.doorS = door_s
        self.doorW = door_w
        self.isRoomN = is_r_n
        self.isRoomE = is_r_e
        self.isRoomS = is_r_s
        self.isRoomW = is_r_w
        self.doorNisLocked = door_n_locked
        self.doorEisLocked = door_e_locked
        self.doorSisLocked = door_s_locked
        self.doorWisLocked = door_w_locked
        self.key = key
        self.finish = finish
        self.showNumber = 0
        self.keyColor = key_color
        self.colorN = color_n
        self.colorW = color_w
        self.colorE = color_e
        self.colorS = color_s

    def draw_room(self, wall_sign):
        north = wall_sign
        south = wall_sign
        east = wall_sign
        west = wall_sign
        if self.doorN:
            north = "-"
        if self.doorS:
            south = "-"
        if self.doorE:
            east = "|"
        if self.doorW:
            west = "|"

        self._draw_graphic(north, south, east, west, wall_sign)

    @staticmethod
    def set_color(color):
        if color == "red":
            return Fore.RED
        elif color == "blue":
            return Fore.BLUE
        elif color == "green":
            return Fore.GREEN
        else:
            return Fore.WHITE

    # prints how room looks
    def _draw_graphic(self, north, south, east, west, wall_sign):
        # North side
        if north == "-":
            print(f"{wall_sign*6} {self.set_color(self.colorN)}{north*4}{Style.RESET_ALL} {wall_sign*6} ")
        else:
            print(f"{wall_sign*7}{north * 4}{wall_sign*7} ")

        # West and east sides
        for x in range(0, 6):
            if not self.key:
                if x == 2 or x == 3:
                    print(f"{self.set_color(self.colorW)}{west} {Style.RESET_ALL}               "
                          f"{self.set_color(self.colorE)}{east} {Style.RESET_ALL} ")
                else:
                    print(f"{wall_sign}                {wall_sign} ")
            else:
                if x == 2:
                    print(f"{self.set_color(self.colorW)}{west} {Style.RESET_ALL}               "
                          f"{self.set_color(self.colorE)}{east} {Style.RESET_ALL} ")
                elif x == 3:
                    print(f"{west}      {self.set_color(self.keyColor)}key{Style.RESET_ALL}       {east} ")
                else:
                    print(f"{wall_sign}                {wall_sign} ")

        # South side
        if south == "-":
            print(f"{wall_sign * 6} {self.set_color(self.colorS)}{south * 4}{Style.RESET_ALL} {wall_sign * 6} ")
        else:
            print(f"{wall_sign * 7}{south * 4}{wall_sign * 7} ")










