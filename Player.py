class Player(object):
    def __init__(self, x, y, rooms, keys):
        self.pos = [x, y]
        self.rooms = rooms
        self.keys = keys
        self.roomNum = 0

    # this is going to mark each room you enter by numbers
    def number_for_room(self, room, room_num):
        if room.showNumber == 0:
            room.showNumber = room_num + 1
            self.roomNum += 1
        return room.showNumber

    def decision(self):
        room = self.where_am_i(self.pos)
        print(f"{self.number_for_room(room, self.roomNum)}.room")
        room.draw_room("￿")
        self.move(input("Write [up, down, left, right] to move or [take] to take keys\n>").lower().strip(), self.pos)

    @staticmethod
    def wall_info():
        input("There is the wall.")

    # Move between the rooms
    def move(self, option, pos):
        room = self.where_am_i(pos)
        if option == "up":
            if room.doorN:
                if not room.doorNisLocked:
                    self.pos[1] -= 1
                else:
                    self.write_locked()
            else:
                self.wall_info()
        elif option == "right":
            if room.doorE:
                if not room.doorEisLocked:
                    self.pos[0] += 1
                else:
                    self.write_locked()
            else:
                self.wall_info()
        elif option == "down":
            if room.doorS:
                if not room.doorSisLocked:
                    self.pos[1] += 1
                else:
                    self.write_locked()
            else:
                self.wall_info()
        elif option == "left":
            if room.doorW:
                if not room.doorWisLocked:
                    self.pos[0] -= 1
                else:
                    self.write_locked()
            else:
                self.wall_info()

        elif option == "take":
            if self.is_here_key(self.pos):
                room = self.where_am_i(self.pos)
                key = self.what_key(self.pos)
                if room.key:
                    room.key = False
                    self.unlock_door(key)
                    input(f"The {key.color} key was taken!")
                else:
                    input("Nothing to take.")
            else:
                input("Nothing to take.")

    def unlock_door(self, key):
        for room in self.rooms:
            if key.roomWhereToUnlockDoor == room.number:
                self.which_door(key.door, room)

    @staticmethod
    def which_door(door, room):
        if door == "north":
            room.doorNisLocked = False
        elif door == "south":
            room.doorSisLocked = False
        elif door == "east":
            room.doorEisLocked = False
        elif door == "west":
            room.doorWisLocked = False

    def is_here_key(self, pos):
        for key in self.keys:
            if key.cords == pos:
                return True
        return False

    def what_key(self, pos):
        for key in self.keys:
            if key.cords == pos:
                return key

    @staticmethod
    def write_locked():
        input("The door is locked! Find the right key.")

    # locate the room where you are right now by cords
    def where_am_i(self, pos):
        for room in self.rooms:
            if room.cords == pos:
                return room

