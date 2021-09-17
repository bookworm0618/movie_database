from models import (Base, session,
                    Book, engine)

import datetime
import csv
import time

def menu():
    while True:
        print('''
            \nRecently Watched Movies
            \r1) Add movie
            \r2) View all movies
            \r3) Search for a movie
            \r4) Movie analysis
            \r5) Exit ''')
        choice = input('What is your wish oh wise one? ')

        if choice in ['1','2','3','4','5']:
            return choice
        else:
            input('''
                    \rPlease choose one of the options above.
                    \rA number from 1-5.
                    \rPress enter to try again
                ''')


def app():
    app_running = True
    while app_running:
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            print('Bye bye bye bye bye')
            app_running = False




if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # add_csv()
    # app()

    for movie in session.query(Movie):
        print(movie)
