### SQLite CRUD application

Collection of Python modules to Create, Read and Delete records in a database.
**NOTE**: based on SQLite3, database is local in current implementation.

```
$ ./sqlcrud.py
usage: sqlcrud.py [-h] [-c | -d | -p | -r]
                  [-v VALUES VALUES VALUES VALUES VALUES VALUES VALUES VALUES VALUES]
                  [-V]
                  <dbName> <tName>

Python interface to SQLITE3 database, version 1.0.

positional arguments:
  <dbName>              Database Name
  <tName>               Table Name

optional arguments:
  -h, --help            show this help message and exit
  -c, --create          Create record
  -d, --delete          Delete record
  -p, --print           Print whole database
  -r, --read            Read record
  -v VALUES VALUES VALUES VALUES VALUES VALUES VALUES VALUES VALUES, --values VALUES VALUES VALUES VALUES VALUES VALUES VALUES VALUES VALUES
                        In association with -a
  -V, --version         show program's version number and exit
```
