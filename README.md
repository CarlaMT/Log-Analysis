# Log Analysis

Program written connects to the database by utilizing SQL queries to analyze the log data. Reports are printed based on the analysis of the database answering three questions about the site's user activity.
The report answer the following questions:

-   What are the most popular three articles of all time?
-   Who are the most popular article authors of all time?
-   On which days did more than 1% of requests lead to errors?


## Installation
### Virtual Machine

The data acquired for this project utilized a virtual machine. To run it, three installations are required on your computer, which can be installed as follows:.

-   Install [VirtualBox 5.1.34](https://www.virtualbox.org/wiki/Changelog-5.1#v34)
-   Install [Vagrant](https://www.vagrantup.com/downloads.html)
-   Download the VM Configuration - Vagrant takes a configuration file called `Vagrantfile` that tells it how to start your Linux VM. [Download the Vagrantfile here.](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f73b_vagrantfile/vagrantfile) Put this file into a new directory (folder) on your computer. Using your terminal, change directory (with the `cd` command) to that directory, then run `vagrant up.
### Start Virtual Machine

-   cd vagrant  \- opens vagrant subdirectory
-   vagrant up  \- installs PostgreSQL database
-   vagrant ssh - logs into the VM

### Database
Log Analysis data from database to download and initialize:

-   Download [data](https://drive.google.com/open?id=1l00nYzLtiDZ2e9Q5jgav1cbPk8ZeCH6K)
-   Unzip newsdata.sql and move into the vagrant directory.
-   To load the data, cd into the vagrant directory, and type the command psql -d news -f newsdata.sql to initialize the database.
- 
### Running Reports

Once installation is complete: python newsdb.py

### Views
Single queries were used in by creating views to the database.  Here are the view commands created.

```
CREATE VIEW quest1 AS 
SELECT articles.title, COUNT
(log.id) AS views
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views DESC
LIMIT 3;

CREATE VIEW auths AS
SELECT name,
VIEW FROM authors,
quest WHERE authors.id = quest.author
ORDER BY view DESC;

CREATE VIEW errors AS
SELECT time::timestamptz::date,
count(*) AS errors
FROM log
WHERE not status ='200 OK'
GROUP BY time::timestamptz::date;
CREATE VIEW:


CREATE VIEW error_percentages AS
SELECT errors.time, errors.errors/count(*)::float AS errorperc
FROM errors, log
WHERE errors.time =log.time::timestamptz::date
GROUP BY errors.time, errors.errors
HAVING errors.errors/count(*)::float > .01
ORDER BY errorperc DESC;
```



