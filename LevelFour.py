from Room import Room
from Key import Key


class LevelFour(object):
    @staticmethod
    def level_four_rooms():
        room_1 = Room(1, 0, 0, door_e=True, is_r_e=True)
        room_2 = Room(2, 1, 0, door_w=True, is_r_w=True, door_n=True, is_r_n=True, door_s=True, is_r_s=True,
                      door_n_locked=True, color_n="green")
        room_3 = Room(3, 1, -1, door_s=True, is_r_s=True, door_n=True, is_r_n=True, color_s="green")
        room_4 = Room(4, 0, -1, door_n=True, is_r_n=True, key=True, key_color="blue")
        room_5 = Room(5, 0, -2, door_s=True, is_r_s=True, door_e=True, is_r_e=True)
        room_6 = Room(6, 1, -2, door_w=True, is_r_w=True, door_s=True, is_r_s=True)
        room_7 = Room(7, -1, -2, door_s=True, is_r_s=True)
        room_8 = Room(8, -1, -1, door_n=True, is_r_n=True, door_w=True, is_r_w=True)
        room_9 = Room(9, -2, -1, door_w=True, is_r_w=True, door_s=True, is_r_s=True, door_e=True, is_r_e=True)
        room_10 = Room(10, -2, 0, door_n=True, is_r_n=True, door_e=True, is_r_e=True)
        room_11 = Room(11, -1, 0, door_w=True, is_r_w=True, door_s=True, is_r_s=True)
        room_12 = Room(12, -3, 0, door_n=True, is_r_n=True, key=True, key_color="green")
        room_13 = Room(13, -3, -1, door_s=True, is_r_s=True, door_e=True, is_r_e=True, door_n=True, is_r_n=True)
        room_14 = Room(14, -3, -2, door_s=True, is_r_s=True, door_e=True, is_r_e=True)
        room_15 = Room(15, -2, -2, door_w=True, is_r_w=True, door_n=True, is_r_n=True, door_n_locked=True,
                       color_n="blue")
        room_16 = Room(16, -1, 1, door_n=True, is_r_n=True, door_e=True, is_r_e=True)
        room_17 = Room(17, 0, 1, door_w=True, is_r_w=True, door_e=True, is_r_e=True, color_e="red")
        room_18 = Room(18, 1, 1, door_w=True, is_r_w=True, door_n=True, is_r_n=True, door_e=True, is_r_e=True,
                       door_w_locked=True, color_w="red")
        room_19 = Room(19, 2, 1, door_w=True, is_r_w=True, door_s=True, is_r_s=True)
        room_20 = Room(20, 0, 2, door_e=True, is_r_e=True, key=True, key_color="red")
        room_21 = Room(21, 1, 2, door_w=True, is_r_w=True, door_e=True, is_r_e=True)
        room_22 = Room(22, 2, 2, door_w=True, is_r_w=True, door_n=True, is_r_n=True)
        room_23 = Room(23, -2, -3, door_s=True, is_r_s=True, finish=True)

        return [room_1, room_2, room_3, room_4, room_5, room_6, room_7, room_8, room_9, room_10,
                room_11, room_12, room_13, room_14, room_15, room_16, room_17, room_18, room_19,
                room_20, room_21, room_22, room_23]

    @staticmethod
    def level_four_keys(room_20, room_12, room_4):
        key_1 = Key(room_20, "west", 18, "red")
        key_2 = Key(room_12, "north", 2, "green")
        key_3 = Key(room_4, "north", 15, "blue")

        return [key_1, key_2, key_3]
