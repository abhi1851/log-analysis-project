#!/usr/bin/env python3

import psycopg2

DBNAME = "news"


# Find most popular three articles of all time
def article():
    print("\n\nThe top three articles of all time --")
    
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        print("Unable to connect database")
        
    c = db.cursor()
    c.execute("""
        SELECT title, count(*) as views
        FROM articles a, log l
        WHERE a.slug=substring(l.path, 10)
        GROUP BY title
        ORDER BY views DESC LIMIT 3;
        """)
    posts = c.fetchall()
    db.close()
    print("%s \n %s \n%s" % (posts[0], posts[1], posts[2]))


# Find most popular author of all time
def author():
    print("\n\nThe most popular author of all time --")

    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        print("Unable to connect database")
        
    c = db.cursor()
    c.execute("""
        SELECT authors.name , count(*) as views
        FROM authors, log, articles
        WHERE authors.id = articles.author
        AND log.status = '200 OK'
        AND articles.slug = substring(log.path,10)
        GROUP BY authors.name
        ORDER BY views DESC LIMIT 1;
        """)
    posts = c.fetchall()
    db.close()
    print(posts[0])


# Find the most percentage of errors in a day
def log():
    print("\n\nHighest percentage of 404 errors --")
    
    try:
        db = psycopg2.connect(database=DBNAME)
    except:
        print("Unable to connect database")
        
    c = db.cursor()
    c.execute("""

               SELECT to_char(fourohfours.day, 'MM/DD/YYYY'),
                 round(
                   (fourohfours.totals*1.0 / request_totals.totals*1.0)*100, 2)
                 as percentage
               FROM fourohfours, request_totals
               WHERE fourohfours.day = request_totals.day
                and
                (fourohfours.totals*1.0 / request_totals.totals*1.0)*100 > 1
               ORDER BY percentage desc;
           """)
    posts = c.fetchone()
    db.close()
    print("%s -- %s%%" % (posts[0], posts[1]))


if __name__ == "__main__":
    article()
    author()
    log()
