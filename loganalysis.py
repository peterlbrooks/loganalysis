#!/usr/bin/env python3
# Access the news db to print out 3 reports

# Could have put all logic in this file but wanted to seperate out
#   the data model / methods.

from loganalysisdb import topArticles, topAuthors, topErrors
from datetime import datetime

# Print out a serices of reports
# For each report:
#   - print the header
#   - loop through the data results
#   - for each record returned, print out the data


# Print out top viewed articles
articles = topArticles()
print("\n\033[4mTop Articles\033[0m")
for title, num in articles:
    print(""" "%s" - %d views """ % (title, num))


# Print out top viewed authors
authors = topAuthors()
print("\n\033[4mTop Authors\033[0m")
for name, num in authors:
    print(""" "%s" - %d views """ % (name, num))


# Print out articles with a high rate of errors
# Note: date from topErrors is a string. If it was a date then
#   could have used d = datetime.strftime(date, '%B %d, %Y') and
#   print out d
errors = topErrors()
print("\n\033[4mMost Errors\033[0m")
for date, percent in errors:
    print(" %s - %.2f%% errors" % (date, percent))

print("")
