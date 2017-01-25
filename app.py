import cmd
import click
from views import Lyrics

class AppRun(cmd.Cmd):
    '''Name of the program'''
    prompt = "Welcome to Discovr>>"

    def do_find(self, query):
        '''
        The do_find commmand  enables a user to view a list of songs
        based on the query ie Find drake
        ''''
        if(query == ""):
            print('"Sorry, You did not input a Song name or Artist Name"')
        else:
             lyric.song_find(query)

    def do_view(self, query):
        '''
        This command enables a user to view a list of sings based
        onthe Track id where by the user inputs the id of the trackto view
        Lyrics
        '''
        lyric.song_view(query)

    def do_save(self, query):
        '''
        This is for saving the lyrics of a certain song based on its id
        to the local database

        '''
        lyric.song_save(query)


    def do_cls(self, arg):
        click.clear()

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
