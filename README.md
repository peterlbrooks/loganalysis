# loganalysis
Udacity Full Stack course - Log Analysis Program

Run 3 reports against a web log database
    1. Show the top requested articles
    2. Show the top requested authors
    3. Show the top requests that resulted in web errors

Environment:
    - Python
    - PosgreSQL
    - Key libraries: psycopg2

This python program will run in the vagrant VM environment. It is assumed
that you have vagrant installed, else see: https://www.vagrantup.com/docs/installation/

Prep:
    1. Navigate to your vagrant folder
    2. Create a "loganalysis" folder in the vagrant directory
    3. Download these files to the loganalysis folder
    4. Unzip the news.sql file into the vangrant folder

Setup
    1. Start up the vagrant VM, "vagrant up"
    2. SSH to the vagrant VM, "vagrant ssh" (small case)
    3. In vagrant, "cd /vagrant" to go to vagrant directory (need the slash)
    4. Start postgres: "psql"
    5. Create the news database: "create database news;"
    6. Exist psql via :"\q"
    4. Create the news db via: "psql -d news -f newsdata.sql"

To run the program:
    1. "cd loganalysis" to get to loganalysis directory
    2. "python loganalysis.py" to run the reports!
    3. "exit" when done to log out of vagrant
