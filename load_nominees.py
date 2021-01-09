# import sqlite module
import sqlite3

# Reading a file is always the same
# open (with mode, r (default), w, a)
# read/write
# close

# create file object
f = open("awards.csv")

# readlines (into a list)
lines = f.readlines()

# close file handle
f.close()

# connect to database
conn = sqlite3.connect('conference.sqlite')

# create cursor object
c = conn.cursor()

# for each line in the lines list (each line in file)
for line in lines:
    # split into a list of values
    vals = line.split(",")
    # print(vals)

    # map to local variables for sanity (strip leading/trailing whitespace)
    nominee_name = vals[0].strip().replace('"','')
    nominee_desc = vals[1].strip().replace('"','')
    nominee_img = vals[2].strip().replace('"','')
    nominee_votes = vals[3].strip().replace('"','')

    # print(nominee_name);
    # print(nominee_desc);
    # print(nominee_img);
    # print(nominee_votes);

    # Create tuple for insertion - immutable
    nominee = (nominee_name, nominee_desc, nominee_img, nominee_votes)

    print(nominee)

    # Insert a row of data (DML insert, update, delete)
    c.execute('INSERT INTO nominees (nominee_name, nominee_desc, nominee_img, nominee_votes) VALUES (?, ?, ? , ?)', nominee)

conn.commit()

conn.close()