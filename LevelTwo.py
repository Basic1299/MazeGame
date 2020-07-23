from Room import Room
from Key import Key


class LevelTwo(object):
    @staticmethod
    def level_two_rooms():
        room_1 = Room(1, 0, 0, door_w=True, is_r_w=True)
        room_2 = Room(2, -1, 0, door_e=True, is_r_e=True, door_w=True, is_r_w=True)
        room_3 = Room(3, -2, 0, door_e=True, is_r_e=True, door_n=True, is_r_n=True,
                      door_w=True, is_r_w=True, door_n_locked=True, color_n="red")
        room_4 = Room(4, -3, 0, door_e=True, is_r_e=True, door_n=True, is_r_n=True)
        room_5 = Room(5, -3, -1, door_s=True, is_r_s=True, key=True, key_color="red")
        room_6 = Room(6, -2, -1, door_s=True, is_r_s=True, door_e=True, is_r_e=True,
                      door_n=True, is_r_n=True, color_s="red")
        room_7 = Room(7, -2, -2, door_s=True, is_r_s=True)
        room_8 = Room(8, -1, -1, door_w=True, is_r_w=True, door_n=True, is_r_n=True,
                      door_e=True, is_r_e=True)
        room_9 = Room(9, 0, -1, door_w=True, is_r_w=True)
        room_10 = Room(10, -1, -2, door_s=True, is_r_s=True, door_n=True, is_r_n=True)
        room_11 = Room(11, -1, -3, door_s=True, is_r_s=True, finish=True)

        return [room_1, room_2, room_3, room_4, room_5, room_6, room_7, room_8, room_9, room_10,
                room_11]

    @staticmethod
    def level_two_keys(room_5):
        key_1 = Key(room_5, "north", 3, "red")

        return [key_1]

