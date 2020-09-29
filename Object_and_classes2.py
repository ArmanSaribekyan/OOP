# Задача 2

class Album:
    album_name = ''
    group = ''
    track_list = ''

    def get_tracks(self, album):
        for tracks in album:
            tracks.show()

    def add_track(self, album, track_name, track_duration):
        New_track = Track(track_name, track_duration)
        album.track_list.append(New_track)

    def get_duration(self, album):
        num_ = 0
        for tracks in album:
            num_ += tracks.track_duration
        print(f'Длительность альбома: {num_} минут')


class Track:
    def __init__(self, track_name, track_duration):
        self.track_name = track_name
        self.track_duration = int(track_duration)   # minute

    def show(self):
        print(f'{self.track_name} - {self.track_duration} min')

track_1 = Track('Revolt', 4)
track_2 = Track('Hurricane', 5)
track_3 = Track('Feel', 4)

# track_1.show()
# track_2.show()
# track_3.show()

track_4 = Track('Anti-Social', 3)
track_5 = Track('Haunt me', 4)
track_6 = Track('The Guilty Party', 5)

# track_4.show()
# track_5.show()
# track_6.show()

album_1 = Album()
album_1.album_name = 'You Are We'
album_1.group = 'While She Sleeps'
album_1.track_list = [track_1, track_2, track_3]

album_2 = Album()
album_2.album_name = 'You Are We'
album_2.group = 'While She Sleeps'
album_2.track_list = [track_4, track_5, track_6]

# album_1.add_track(album_1, 'You Are We', 5)
#
# album_1.get_tracks(album_1.track_list)

album_1.get_duration(album_1.track_list)
album_2.get_duration(album_2.track_list)