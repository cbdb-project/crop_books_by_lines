## description
Compare the field names and the orders of field names between csv files and MS Access files

The separator for csv is "\t"

## env and dependency
python 2.7

pyodbc

## basic usage
1. put your csv files to ./text
2. create a ODBC link to your MS Access file, default name is *new_lease*
3. run compare.py

## tips
1. When the Access table field names include non-English characters, it might triggle a bug in pyodbc. When it happens, the program will print "please run it again". Please just run this py file again
2. pyodbc works better in python 2 than 3 in my own experiment
