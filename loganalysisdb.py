# Log analysis database calls

import psycopg2

# All SQL updated per review feedback, thanks!

# Select path subquery added so as to not do SUBSTR on all rows
# rginally (on purpose) was checking for path = slug%, now just
# checking for path whose status is OK
# Runs quick!
articleSQL = """
    SELECT title, num
    FROM articles,
        (SELECT path, count(*) as num
        FROM log
        WHERE status = '200 OK'
        GROUP BY path) as agglog
    WHERE slug=SUBSTR(path,10,length(slug))
    ORDER BY num DESC
    LIMIT 3;"""

# 1st subquery returns a table of slugs and the author name of each slug
# 2nd subquery returns the count of each path
# Outer select  joins the author name and count using slug and path
# Runs quick!
authorSQL = """
    SELECT name, sum(num) as total
    FROM
        (SELECT slug, name
        FROM articles, authors
        WHERE articles.author = authors.id) as sluginfo,

        (SELECT path, count(*) as num
        FROM log
        WHERE status = '200 OK'
        GROUP BY path) as loginfo
    WHERE slug = SUBSTR(path,10)
    GROUP BY name ORDER BY total desc;"""


# 1st subquery gets the count of all requests per day
# 2nd subquery gets the count of all successful request per day
# Outer select calculates the percent of error requests per day
# Note: results is a string. If used "SELECT tot.date as date"
#   rather than to_char, results would be in date format and have to
#   convert in loganalysis.py python rather than DB as is done here
errorSQL = """
    SELECT to_char(tot.date,'FMMonth FMDD, YYYY') as date,
    round(err.num*100/tot.num::numeric,2) as percent
    FROM
        (SELECT date(time) as date, count(*) as num
        FROM log
        GROUP BY date(time)) as tot,

        (SELECT date(time) as date, count(*) as num
        FROM log
        WHERE status != '200 OK'
        GROUP BY date(time)) as err
    WHERE tot.date = err.date AND err.num*100/tot.num > 1.0
    ORDER BY percent DESC;"""


# added in recommended helper
def get_query_results(query):
        db = psycopg2.connect(database="news")
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result


# Find top viewed articles
def topArticles():
    return get_query_results(articleSQL)


# Find top viewed authors
def topAuthors():
    return get_query_results(authorSQL)


# Find top dates that have viewing errors
def topErrors():
    return get_query_results(errorSQL)
