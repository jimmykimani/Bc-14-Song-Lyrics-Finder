import cmd
import click
from views import Lyrics

class AppRun(cmd.Cmd):
    prompt = "Welcome to Discovr>>"

    def do_find(self, query):
        if(query == ""):
            print('"Sorry, You did not input a Song name or Artist Name"')
        else:
             lyric.song_find(query)

    def do_view(self, query):
        lyric.song_view(query)


    def do_cls(self, arg):
        click.clear()

    def do_q(self):
        # Exit
        return True


if __name__ == '__main__':
    lyric=Lyrics()
    try:
        AppRun().cmdloop()

    except KeyboardInterrupt:
           pass
