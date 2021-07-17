class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @staticmethod
    def find_room(room, rooms):
        for r in rooms:
            if r.number == room:
                return r
        return False

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.find_room(room_number, self.rooms)
        if room:
            room_index = self.rooms.index(room)
            self.rooms[room_index].take_room(people)
            self.guests += people

    def free_room(self, room_number):
        room = self.find_room(room_number, self.rooms)
        if room:
            self.guests -= room.guests
            room_index = self.rooms.index(room)
            self.rooms[room_index].free_room()

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms)}\n" \
               f"Taken rooms: {', '.join(taken_rooms)}"
