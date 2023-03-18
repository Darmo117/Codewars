import sqlite3

with sqlite3.connect('/tmp/movies.db') as db:
    db.execute("""\
    CREATE TABLE MOVIES (
        name TEXT NOT NULL,
        year INT NOT NULL,
        rating INT NOT NULL
    )""")
    db.execute("""
    INSERT INTO MOVIES(name, year, rating)
    VALUES ("Rise of the Planet of the Apes", 2011, 77),
    ("Dawn of the Planet of the Apes", 2014, 91),
    ("Alien", 1979, 97),
    ("Aliens", 1986, 98),
    ("Mad Max", 1979, 95),
    ("Mad Max 2: The Road Warrior", 1981, 100)
    """)
