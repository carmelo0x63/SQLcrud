#!/usr/bin/env python
#
# author: mellowizAThotmailDOTcom
# date: 2015/07/23

# Import some modules
from __future__ import print_function	# print() as a function not as a statement
import argparse	# Parser for command-line options, arguments and sub-commands
import os.path	# Common pathname manipulations
import sys	# System-specific parameters and functions
import sqlite3	# DB-API 2.0 interface for SQLite databases

# Version number
__version__ = 1.0

def main():
	parser = argparse.ArgumentParser(description='Python interface to SQLITE3 database, version {version}.'.format(version=__version__))
	parser.add_argument('dbName', metavar='<dbName>', help='Database Name')
	parser.add_argument('tName', metavar='<tName>', help='Table Name')
	actionsgrp= parser.add_mutually_exclusive_group()
	actionsgrp.add_argument('-c', '--create', action='store_true', help='Create record')
	actionsgrp.add_argument('-d', '--delete', action='store_true', help='Delete record')
	actionsgrp.add_argument('-p', '--print', action='store_true', help='Print whole database')
	actionsgrp.add_argument('-r', '--read', action='store_true', help='Read record')
	parser.add_argument('-v', '--values', nargs=9, help='In association with -a')
	parser.set_defaults(print=True)
	parser.add_argument('-V', '--version', action='version', version='%(prog)s {version}'.format(version=__version__))

	# In case of no arguments print help message then exit
	if len(sys.argv)==1:
		parser.print_help()
		sys.exit(1)
	else:
		args = parser.parse_args() # else parse command line

	# Finally invoke the add/delete/print functions
	print("[+] DEBUG:: All arguments =", args)
#	print("[+] DEBUG:: DB Name is =", args.dbName)
#	print("[+] DEBUG:: Action Add is =", args.add)
#	print("[+] DEBUG:: Action Print is =", args.print)
#	print("[+] DEBUG:: Action Delete is =", args.delete)

	if not os.path.isfile(args.dbName):
		print("[+] ERROR: file \"{dbN}\" doesn't exist!".format(dbN=args.dbName))
		sys.exit(2)

	if args.create:
		createRecord(args.dbName,args.tName,args.values)
	elif args.delete:
		delRecord(args.dbName,args.tName)
	else: # "print" is the default action anyway
		printDB(args.dbName,args.tName)

def createRecord(dbName,tName,values):
	print("[+] You've chosen to ADD a record to DB={db}, table={t}".format(db='example.db', t=tName))
	print("[+] DEBUG:: VALUES =", values)
	if values[0] == 'None':
		values[0] = 'null'
	print("[+] DEBUG:: VALUES =", values)
	r1 = tuple(values)
	conn = sqlite3.connect(dbName)
	c = conn.cursor()
	c.execute('INSERT INTO {t} VALUES {r}'.format(t=tName,r=r1))
	conn.commit()
	conn.close()

def delRecord(dbName,tName):
	print("[+] You've chosen to DEL a record from DB={db}, table={t}".format(db='example.db', t=dbName))

def printDB(dbName,tName):
	print("[+] You've chosen to PRINT/DUMP DB={db}, table={t}".format(db=dbName, t=tName))
	conn = sqlite3.connect(dbName)
	c = conn.cursor()
	for row1 in c.execute('SELECT * FROM ' + tName):
		print(row1)

#	print(c.fetchone())
#	print(c.fetchall())
	conn.close()

if __name__ == '__main__':
	main()
