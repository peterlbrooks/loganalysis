# Log analysis database calls

import psycopg2


# Find top viewed articles
def topArticles():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    # Join articles, log tables on slug, path columns. Results are the title
    #   and count of top viewed articles
    cursor.execute("SELECT title, count(*) as num FROM articles,log WHERE slug=SUBSTR(path,10,length(slug)) GROUP BY title ORDER BY num DESC LIMIT 10;")
    results = cursor.fetchall()
    db.close()
    return results


# Find top viewed authors
def topAuthors():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    # 1. Create a subquery named subq that joins authors, articles tables on
    #   author (author and id columns, respectively).
    #   Results are the name and slug. This creates a table of  articles and
    #   the author for each articles.
    # 2. Join log and the subquery results using slug. Results are the author
    #   and count of top viewed articles.
    cursor.execute("SELECT name, count(*) as num FROM log,(SELECT name, slug ,authors.id FROM authors, articles WHERE author = authors.id) as subq WHERE slug=SUBSTR(path,10,length(slug)) GROUP BY name  ORDER BY num DESC LIMIT 10;")
    results = cursor.fetchall()
    db.close()
    return results


# Find top dates that have viewing errors
def topErrors():
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    # Create two subqueries.
    # 1. Subquery named tot creates a table of dates and total view counts.
    # 2. Subquery named err creates a table of dates and a count of view
    #   errors for the date.
    # 3. Join the above two subqueries in order to calculate the percent of
    #   views with errors
    #   (subquery err view count / subquery tot view count)
    # 4. Results are a table of dates and error percentages that are more
    #   than a l.0%
    cursor.execute("SELECT tot.date as date, round(err.num*100/tot.num::numeric,2) as percent FROM (SELECT date(time) as date, count(*) as num FROM log GROUP BY date(time)) as tot, (SELECT date(time) as date, count(*) as num FROM log WHERE status != '200 OK' GROUP BY date(time)) as err WHERE tot.date = err.date AND err.num*100/tot.num > 1.0 ORDER BY percent DESC;")
    results = cursor.fetchall()
    db.close()
    return results
