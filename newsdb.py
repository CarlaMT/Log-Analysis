#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import Python DB API for PSQL

import psycopg2

# Set Database Name

DBNAME = 'news'


def connectDatabase(query):
    """This function connects to database in DBNAME, executes the 'query',
    then return 'result'
    """

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result
    print 'Can not connect to the database'


# Create function to find top three articles

def get_articles():
    """
    This function will return the three
    most popular articles of all time.
    """


query = """
        SELECT * FROM quest1;
"""
results = connectDatabase(query)
print '1.  What are the most popular three articles of all time?'
for result in results:
    print(result[0], result[1])


# Create function to find top three authors

def get_authors():
    """
    This function will return the three
    most popular authors of all time.
    """


query = """
     SELECT * FROM auths;
"""
results = connectDatabase(query)
print '\n'
print '2.  What are the most popular three authors of all time?'
for result in results:
    print(result[0], result[1])


# Create function to locate more than 1% of requests leading to errors

def errpc():
    """
    This function will locate more than 1%
    of requests that lead to errors.
    """


query = """
     SELECT * FROM error_percentages;
"""
results = connectDatabase(query)
print '\n'
print '3. On which day did more than 1% of requests lead to errors?'
for result in results:
    print(result[0], result[1])
