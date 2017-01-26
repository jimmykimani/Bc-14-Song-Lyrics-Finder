import cmd
import click
from views import Lyrics
class AppRun(cmd.Cmd):
    '''Name of the program'''
    prompt = "Enter find  <query> to search for song name or artist:"

    def do_find(self, query):
        '''
        The do_find commmand  enables a user to view a list of songs
        based on the query ie Find drake
        '''
        if(query == ""):
            print('"Please, input a Song name or Artist Name!!"')
        else:
             lyric.song_find(query)

    def do_view(self, query):
        '''
        This command enables a user to view a list of sings based
        onthe Track id where by the user inputs the id of the track to view
        Lyrics
        '''
        lyric.song_view(query)

    def do_save(self, query):
        '''
        This command enables a user to save lyrics of a certain song based on its id
        to the local database
        '''
        if(song == ""):
            print('"Sorry, Your Song is either already in the database or no song found"')
        else:
            (model.save_lyrics(song, save = True))
            print("Success! Song saved.")


    def do_clear(self, query):
        '''
        Formats the lyrics database
        '''
        click.echo('Do you wish to continue?,This song will be deleted [y/n]\n')
        c ==click.getchar()
        if c =='y':
            clear()
            click.echo('Song Lyrics Deleted Succesfully')
        elif c == 'n':
            click.echo('Aborted Deletion')
        else:
            click.echo('Invalid Input')


        lyric.song_clear(query)

    def do_0(self):
        ''' Normal termination exits with 0'''
        # Exit
        return True


if __name__ == '__main__':
    lyric=Lyrics()
    try:
        AppRun().cmdloop()

    except KeyboardInterrupt:
           pass
