# Log Analysis Project
### This project is a database log analysis project for udacity Full Stack Nanodegree 1.

This program runs three reports to answer the following questions-

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Pre-reqiusites

You need to have some specific software installed and running in your computer. Download and intall it from the links below (if you don't have it installed)
- Download and install [Python3](https://www.python.org/downloads/).
- Download and run [virtual box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
- Download and run [vagrant](https://www.vagrantup.com/). 
- Download the SQL file here([newssdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip))
 
## Quick Start
First you must have the PostgreSQL newsdata.sql database running from the FSND virtual machine. 
- From the `vagrant` directory,run `vagrant up`.
- SSH to the virtual machine with `vagrant ssh`.
- Connect to the `psql` database with `psql -d news`
- We'll need to create two database views for the reporting tool to work properly:
```
CREATE view fourohfours as
  SELECT date_trunc('day', time) "day", count(status) as totals
  FROM log
  WHERE status = '404 NOT FOUND'
  GROUP by day;

CREATE view request_totals as
  SELECT date_trunc('day', time) "day", count(status) as totals
  FROM log
  GROUP by day;
```
- After creating the views, you should run *newsdatadb.py*
using the command `python3 newsdatadb,py` 
- hurrah!!! The program gives the answer.


## Example Output

```
The top three articles of all time --
('Candidate is jerk, alleges rival', 338647)
 ('Bears love berries, alleges bear', 253801)
('Bad things gone, say good people', 170098)


The most popular author of all time --
[('Ursula La Multa', 507594)]


Highest percentage of 404 errors --
07/17/2016 -- 2.26%
```