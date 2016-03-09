#!/usr/bin/env python
# description: collection of Python modules to Create, Read and Delete records
#              in a database. Update not available for the moment.
#              Currently based on SQLite3.
# author: mellowizAThotmailDOTcom
# date (ISO 8601): 2015-08-07

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
	parser.set_defaults(print=True)

	parser.add_argument('dbName', metavar='<dbName>', help='Database Name')
	parser.add_argument('tName', metavar='<tName>', help='Table Name')
	parser.add_argument('-V', '--version', action='version', version='%(prog)s {version}'.format(version=__version__))

	actionsgrp = parser.add_mutually_exclusive_group()
	actionsgrp.add_argument('-c', '--create', action='store_true', help='Create record')
	actionsgrp.add_argument('-d', '--delete', action='store_true', help='Delete record')
	actionsgrp.add_argument('-p', '--print', action='store_true', help='Print whole database')
	actionsgrp.add_argument('-r', '--read', action='store_true', help='Read record')

	valuesgrp = parser.add_mutually_exclusive_group()
	valuesgrp.add_argument('-v', '--values', nargs=8, help='In association with create')
	valuesgrp.add_argument('-i', '--index', nargs=1, help='In association with delete/read')

	# In case of no arguments print help message then exit
	if len(sys.argv)==1:
		parser.print_help()
		sys.exit(1) # no arguments
	else:
		args = parser.parse_args() # else parse command line

	# Finally invoke the actual functions
	print("[+] DEBUG:: All arguments =", args) # remove in final version

	if not os.path.isfile(args.dbName):
		print("[+] ERROR: file \"{dbN}\" doesn't exist!".format(dbN=args.dbName))
		sys.exit(2) # database file doesn't exist

	# The following arguments/functions are mutually exclusive
	if args.create:
		createRecord(args.dbName, args.tName, args.values)
	elif args.delete:
		delRecord(args.dbName, args.tName, args.index)
	elif args.read:
		readRecord(args.dbName, args.tName, args.index)
	else: # "print" is the default action anyway
		printDB(args.dbName, args.tName)

def createRecord(dbName, tName, values):
	print("[+] You've chosen to ADD a record to DB={db}, table={t}".format(db=dbName, t=tName))
	print("[+] DEBUG:: VALUES =", values) # remove in final version
	record1 = '\"' + '\", \"'.join(values) + '\"'
	print("[+] DEBUG:: record1 =", record1) # remove in final version
	conn = sqlite3.connect(dbName)
	c = conn.cursor()
	print('[+] DEBUG:: command > INSERT INTO {t} VALUES (null, {r})'.format(t=tName, r=record1)) # remove in final version
	c.execute('INSERT INTO {t} VALUES (null, {r})'.format(t=tName, r=record1))
	conn.commit()
	conn.close()

def delRecord(dbName, tName, index):
	index1 = index[0]
	print("[+] You've chosen to DELETE a record from DB={db}, table={t}, index={i}".format(db=dbName, t=dbName, i=index1))
	conn = sqlite3.connect(dbName)
	c = conn.cursor()
	print('[+] DEBUG:: command > DELETE FROM {t} WHERE rowid = {idx}'.format(t=tName, idx=index1)) # remove in final version
	c.execute('DELETE FROM {t} WHERE rowid = {idx}'.format(t=tName, idx=index1))
	conn.commit()
	conn.close()

def readRecord(dbName, tName, index):
	index1 = index[0]
	print("[+] You've chosen to READ a record from DB={db}, table={t}, index={i}".format(db=dbName, t=dbName, i=index1))
	conn = sqlite3.connect(dbName)
	c = conn.cursor()
	print('[+] DEBUG:: command > SELECT * FROM {t} WHERE rowid = {idx};'.format(t=tName, idx=index1)) # remove in final version
	c.execute('SELECT * FROM {t} WHERE rowid = {idx};'.format(t=tName, idx=index1))
	print(c.fetchone())
	conn.close()

def printDB(dbName, tName):
	print("[+] You've chosen to PRINT/DUMP all of DB={db}, table={t}".format(db=dbName, t=tName))
	conn = sqlite3.connect(dbName)
	c = conn.cursor()
	for row1 in c.execute('SELECT * FROM ' + tName):
		print(row1)
	conn.close()

if __name__ == '__main__':
	main()
