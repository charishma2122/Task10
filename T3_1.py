import random # Imports the random module to generate random ratings.
#Three classes are defined: Audio, Playlist, and AudioManager.
# Audio represents an audio file with attributes like URL, name, and ratings.
class Audio:
    def __init__(self, url, name): # passing the url and name
        # Assigning url ,name and initializing the ratings variables
        self.url = url
        self.name = name
        self.ratings = []


    def add_rating(self, rating): # defining a function for rating
        self.ratings.append(rating)

    def get_average_rating(self): # function to calculate the average ratings
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings) # returing the output by calcluating the average
# Playlist represents a collection of audio files categorized by genre.
class Playlist:
    def __init__(self, name, genre): #  assigning name, genere
        self.name = name
        self.genre = genre
        self.audio_files = []
        self.ratings = []

    def add_audio(self, audio): # adding a function to audio
        self.audio_files.append(audio)

    def add_rating(self, rating): # a
        self.ratings.append(rating)

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class User:
    def __init__(self, name):
        self.name = name
  # AudioManager manages audio files and playlists.
class AudioManager:
    def __init__(self):
        self.users = []
        self.audios = []
        self.playlists = []

#class contains methods to add ratings, calculate average ratings, search by name, and manage audio and playlist functionalities.
    def create_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def create_audio(self, url, name):
        audio = Audio(url, name)
        self.audios.append(audio)
        return audio

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def add_audio_to_playlist(self, playlist, audio):
        playlist.add_audio(audio)

    def add_rating_to_audio(self, audio, rating):
        audio.add_rating(rating)

    def add_rating_to_playlist(self, playlist, rating):
        playlist.add_rating(rating)

    def search_audio_by_name(self, name):
        return [audio for audio in self.audios if audio.name.lower() == name.lower()]

    def search_playlist_by_name(self, name):
        return [playlist for playlist in self.playlists if playlist.name.lower() == name.lower()]

# Function to generate random ratings for demonstration
def generate_random_ratings(): # generates random ratings (1-5) for demonstration purposes.
    return random.randint(1, 5)

# Function to display average ratings for audios and playlists
def display_average_ratings(audio_manager):
    for audio in audio_manager.audios:
        print(f"Average rating for {audio.name}: {audio.get_average_rating()}")

    for playlist in audio_manager.playlists:
        print(f"Average rating for {playlist.name}: {playlist.get_average_rating()}")

if __name__ == "__main__":
    audio_manager = AudioManager()

    # Creating 3 users
    for i in range(1, 4):
        user_name = input(f"Enter name for User {i}: ")
        audio_manager.create_user(user_name)
    # Creating audio and playlists
    audio_name = input("Enter audio name: ")
    audio_url = input("Enter audio URL: ")
    audio = audio_manager.create_audio(audio_url, audio_name)
#  Prompts users to input data step by step to create audio and playlists, add audio files to playlists, rate them, and perform searches.
    playlist_name = input("Enter playlist name: ")
    playlist_genre = input("Enter playlist genre: ")
    playlist = audio_manager.create_playlist(playlist_name, playlist_genre)

    audio_manager.add_audio_to_playlist(playlist, audio)

    # Adding random ratings ,
    for i in range(3):  # 3 random ratings
        rand_rating = generate_random_ratings()
        audio_manager.add_rating_to_audio(audio, rand_rating)
        audio_manager.add_rating_to_playlist(playlist, rand_rating)
    # Displaying average ratings
display_average_ratings(audio_manager)
