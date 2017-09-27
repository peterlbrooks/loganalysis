#!/usr/bin/env python3
# access the news db to print out 3 reports

from loganalysisdb import topArticles, topAuthors, topErrors
from datetime import datetime

# print out a serices of reports
# for each report:
#   - print the header
#   - loop through the data results
#   - for each record returned, print out the data


# print out top viewed articles
articles = topArticles()
print("\n\033[4mTop Articles\033[0m")
for title, num in articles:
    print(""" "%s" - %d views """ % (title, num))


# print out top viewed authors
authors = topAuthors()
print("\n\033[4mTop Authors\033[0m")
for name, num in authors:
    print(""" "%s" - %d views """ % (name, num))


# print out articles with a high rate of errors
errors = topErrors()
print("\n\033[4mMost Errors\033[0m")
for date, percent in errors:
    d = datetime.strftime(date, '%B %d, %Y')
    print(" %s - %.2f%% errors" % (d, percent))

print("")
