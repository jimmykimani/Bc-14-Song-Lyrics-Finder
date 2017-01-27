
"""
    usage:
        song_find <query>
        song_view <track_number>
        song_save <track_id>
        clear
        quit
    Options:
        -h, --help  Show this screen and exit

"""
import cmd
import click
from colorama import Fore, Back, Style
from views import Lyrics
class AppRun(cmd.Cmd):
    '''Name of the program'''
    prompt = Fore.GREEN + "Welcome to Discovr (enter help for more)-->"

    def do_find(self, query):
        '''
        The do_find commmand  enables a user to view a list of songs
        based on the query ie Find drake
        '''
        print  lyric.song_find(query)




    def do_view(self, query):
        '''
        This command enables a user to view a list of sings based
        onthe Track id where by the user inputs the id of the track to view
        Lyrics
        '''
        print lyric.song_view(query)

    def do_save(self, query):
        '''
        This command enables a user to save lyrics of a certain song based on its id
        to the local database
        '''

        print(lyric.save_lyrics(query))



    def do_clear(self, line):
        clear=raw_input ( Fore.RED + " Warning!!! Song database will be cleared [y/n]: ")
        if clear=='y':
          print Fore.CYAN + ("#### Database cleared Succesfully ####")
        else:
          print Fore.CYAN + ("### Aborted ###")

    def do_quit(self, arg):
        """Usage: quit"""
        print Fore.CYAN + ("######### Goodbye! :( ")
        exit()


if __name__ == '__main__':
    lyric=Lyrics()
    try:
        AppRun().cmdloop()

    except KeyboardInterrupt:
           pass
