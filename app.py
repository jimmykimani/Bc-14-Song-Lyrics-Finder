#!/usr/bin/env python
"""
Discovr is A Command Line Application for Finding Lyrics for a particular song using an API

Usage:
    my_app find <query_string>
    my_app view <song_id>
    my_app save <song_id>
    my_app delete <song_id>
    my_app (-i | --interactive)
    my_app (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

"""

import sys
import cmd
from tabulate import tabulate
from docopt import docopt, DocoptExit

def docopt_cmd(func):
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyApp (cmd.Cmd):
    intro = 'Welcome to Discovr!' \
        + ' (type help for a list of commands.)'
    prompt = '(Discovr) '
    file = None

    @docopt_cmd
    def do_find(self, search_parameters):
        """ Shows a list of songs searched by the user"""
        results = view.find_song(search_parameters)

        table_headers=['Song ID', 'Song Title','Artist']
        '''table[]'''

        for i in range(len(results)):
            song_id = results[i]['result']['id']
            title = results[i]['result']['title']
            artist = results[i]['result']['primary_artist']['name']

            table.append([song_id, title, artist])


            '''' click.echo(tabulate(table, table_headers,
                             tablefmt="fancy_grid"), fg='green')'''

    @docopt_cmd
    def do_view(self, song_id):
        """View song lyrics bases on song id"""
        lyrics=view.get_song(song_id)['lyrics']
        ""

    @docopt_cmd
    def do_save(self, song_id):
        """Store song lyrics based on id locally"""
        view.save_song(song_id)
        lyrics=view.get_song_by_id(song_id)['lyrics']

    @docopt_cmd
    def do_delete(self, line):
        """Deletes song lyrics bases on song id locally"""

        lyrics=view.get_song_by_id(song_id)['lyrics']


    def do_q(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyApp().cmdloop()

print(opt)
