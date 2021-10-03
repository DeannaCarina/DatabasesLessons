import psycopg2

# connect to chinook database:
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database:
cursor = connection.cursor()

# query 1 - select all records from the 'Artist' table:
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - select only the 'Name' collumn from the 'Artist' table:
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only 'Queen' from the 'Artist' table:
# cursor.execute('SELECT * from "Artist" WHERE "Name"= %s', ["Queen"])

# query 4 - select only by "ArtistId" #51 from the "Artist" table:
# cursor.execute('SELECT * from "Artist" WHERE "ArtistId"= %s', [51])

# query 5 - select only the albums with "ArtistId" #51 on the "Album" table:
# cursor.execute('SELECT * from "Album" WHERE "ArtistId"=%s', [51])

# query 6 - select all tracks where the composer is Queen from the "Track" table:
# cursor.execute('SELECT * from "Track" WHERE "Composer"=%s', ['Queen'])

# fetch the results (multiple):
results = cursor.fetchall()

# fetch the result (single):
# results = cursor.fetchone()

# close the connection:
connection.close()

# print results:
for result in results:
    print(result)
