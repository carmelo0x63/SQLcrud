#!/usr/bin/env python3
#
# author: carmelo.califano@gmail.com
# date: 2020-05-06

import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE urldb
        (rowid integer primary key, first_added text, last_modified text, short_name text, url text, userid text, password text, category text, notes text)''');

# Insert a row of data
#c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
c.execute("INSERT INTO urldb VALUES (1, '20200506', '20200506', 'Google', 'https://www.google.com/', 'user1', 'passwd1', 'search engine', 'gmail drive calendar')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

