class Key(object):
    def __init__(self, room, door, room_door_locked, color):
        # room number where the key lays
        self.roomNumber = room.number
        # room number where are door to unlock with this key
        self.roomWhereToUnlockDoor = room_door_locked
        # specific door in the room (north, south, west, east)
        self.door = door
        self.cords = room.cords
        self.color = color