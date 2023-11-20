class Song:
    lyrics=[]
    
    def __init__(self,lyrics):
        self.lyrics=lyrics
    
    def sing_me_a_song(self):
        l=self.lyrics
        for i in l:
            print(i)
            
s1=Song(["Happy Birthday to you", "You were born in a zoo", "all the animals like you", "may god bless you"])
print("Song 1:")
s1.sing_me_a_song()
s2=Song(["vande mataram", "Vande mataram", "sujalam, suphalam ", "sasya shamalam mataram"])
print("\nSong 2:")
s2.sing_me_a_song()
