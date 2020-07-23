from Room import Room


class LevelOne(object):
    @staticmethod
    def level_one_rooms():
        room_1 = Room(1, 0, 0, door_e=True, is_r_e=True)
        room_2 = Room(2, 1, 0, door_w=True, is_r_w=True, door_s=True, is_r_s=True)
        room_3 = Room(3, 1, 1, door_n=True, is_r_n=True, door_e=True, is_r_e=True)
        room_4 = Room(4, 2, 1, door_w=True, is_r_w=True, door_n=True, is_r_n=True,
                      door_e=True, is_r_e=True)
        room_5 = Room(5, 2, 0, door_s=True, is_r_s=True)
        room_6 = Room(6, 3, 1, door_w=True, is_r_w=True, door_s=True, is_r_s=True)
        room_7 = Room(7, 3, 2, door_n=True, is_r_n=True, door_s=True, is_r_s=True)
        room_8 = Room(8, 3, 3, door_n=True, is_r_n=True, finish=True)

        return [room_1, room_2, room_3, room_4, room_5, room_6, room_7, room_8]

