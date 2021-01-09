# import sqlite module
import sqlite3

# connect to database
conn = sqlite3.connect('conference.sqlite')

# create cursor object
c = conn.cursor()

# drop table (if exists, otherwise error)
c.execute('''DROP TABLE nominees''')

# create table
c.execute('''CREATE TABLE nominees
(nominee_id INTEGER PRIMARY KEY AUTOINCREMENT,
 nominee_name TEXT NOT NULL,
 nominee_desc TEXT NOT NULL,
 nominee_img TEXT NOT NULL,
 nominee_votes INT DEFAULT 0)''')

# commit changes (if in transaction)
conn.commit()

# release resource
conn.close()
