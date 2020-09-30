# Задача 2

class Album:

    def __init__(self, group, album_name, track_list):
        self.group = group
        self.album_name = album_name
        self.track_list = track_list

    def get_tracks(self, album):
        for tracks in album:
            print(tracks)

    def add_track(self, album, track_name, track_duration):
        new_track = Track(track_name, track_duration)
        album.track_list.append(new_track)

    def get_duration(self, album):
        num_ = 0
        for tracks in album:
            num_ += tracks.track_duration
        print(f'Длительность альбома: {num_} минут')

    def __str__(self):
        tracks = ''
        for track in self.track_list:
            tracks += f'\n\t{str(track)}'
        return f'Name group: {self.group}\nName album: {self.album_name}\n'\
               f'Tracks:{tracks}'



class Track:

    def __init__(self, track_name, track_duration):
        self.track_name = track_name
        self.track_duration = int(track_duration)   # minute

    def __str__(self):
        return f'{self.track_name} - {self.track_duration} min'

    def __lt__(self, other):
        return self.track_duration < other.track_duration


track_1 = Track('Revolt', 4)
track_2 = Track('Hurricane', 5)
track_3 = Track('Feel', 4)

# print(track_1)

track_4 = Track('Anti-Social', 3)
track_5 = Track('Haunt me', 4)
track_6 = Track('The Guilty Party', 5)

# print(track_4)

album_1 = Album('While She Sleeps', 'You Are We', [track_1, track_2, track_3])
album_2 = Album('While She Sleeps', 'So What?', [track_4, track_5, track_6])

# album_1.add_track(album_1, 'You Are We', 5)
#
# album_1.get_tracks(album_1.track_list)

album_1.get_duration(album_1.track_list)
album_2.get_duration(album_2.track_list)

# print(track_1 < track_5)

print(album_1)