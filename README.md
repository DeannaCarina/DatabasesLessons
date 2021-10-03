To download sample sql database "Chinook":
wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql


Error fix due to Gitpod change:
If you get the following error after typing psql in the terminal:
psql: error: could not connect to server: No such file or directory
Please use the following command in the terminal to set an environment variable needed for it to work:
set_pg
And then try the psql command again
You will need to do this each time you return to your Gitpod workspace for the Database Management Systems videos.

To view, or list, any databases in our environment, we can type \l. (when the postgres=# is in the CLI)

To create a new database: 

CREATE DATABASE {database name}; - in this case 'chinook'
check with \l

To change to a difference database:
\c {name of database to switch to}; - in this case 'chinook', but could be 'postgres' or anything else

To install downloaded sample database:
\i {filepath/filename}; - in this case 'Chinook_PostgreSql.sql' (no filepath as in main repo)

To exit the database CLI:
\q

If in the standard workspace terminal (and not in the database):
psql -d {database name} - in this case 'chinook'

To check all files and tables were installed correctly:
\dt

Example commands:
To retrieve all data from the 'Artist' table:
SELECT * FROM "Artist"; (single quote will throw syntax error)

To exit a search press 'q' in the CLI (not to be confused with \q!)

SELECT "Name" FROM "Artist";

SELECT * FROM "Artist" WHERE "Name" = 'Queen'; (Notice single quotes on value to be searched for)

SELECT * FROM "Artist" WHERE "ArtistId" = 51; (No quotes needed for integer)

SELECT * FROM "Album" WHERE "ArtistId" = 51;
In this example, first collumn is the primary key ID, third collumn is the Foreign Key ID

SELECT * FROM "Track" WHERE "Composer" = 'Queen';