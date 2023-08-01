#!/usr/bin/env python3
# Initialize an SQL database using 'sqlite3' module
# author: Carmelo C
# email: carmelo.califano@gmail.com
# history:
#  2023-07-19: 1.0 initial version

import sqlite3
DBNAME = 'ipam.db'
conn = sqlite3.connect(DBNAME)

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE ipam_db
        (rowid integer primary key, first_added text, last_modified text, host_name text, ip_address text, port integer, group text, notes text)''');

# Insert a row of data
c.execute("INSERT INTO ipam_db VALUES (1, '20230719', '20230719', 'raspi1', '192.0.2.54', '513', 'RasPis', 'Raspberry Pi v. 1 model B')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

