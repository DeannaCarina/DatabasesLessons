from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our local host "chinook" database
db = create_engine("postgresql:///chinook")
# three slashes means database hosted locally within our workspace environment

meta = MetaData(db)

# create a variable for the "Artist" table:
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create a variable for the "Album" table:
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create a variable for the "Track" table:
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", String, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    # query 1 - select all records from the 'Artist' table:
    # SELECT everything FROM "Artist"; - PostgreSQL command
    # cursor.execute('SELECT * FROM "Artist"') - psycopg2 command
    # select_query = artist_table.select()



    # query 2 - select only the 'Name' collumn from the 'Artist' table:
    # SELECT "Name" FROM "Artist";
    # cursor.execute('SELECT "Name" FROM "Artist"') - psycopg2 command
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])


    # query 3 - select only 'Queen' from the 'Artist' table:
    # SELECT * FROM "Artist" WHERE "Name" = 'Queen'; - PostgreSQL command
    # cursor.execute('SELECT * from "Artist" WHERE "Name"= %s', ["Queen"]) - psycopg2 command
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # query 4 - select only by "ArtistId" #51 from the "Artist" table:
    # SELECT * FROM "Artist" WHERE "ArtistId" = 51; - PostgreSQL command
    # cursor.execute('SELECT * from "Artist" WHERE "ArtistId"= %s', [51]) - psycopg2 command
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)


    # query 5 - select only the albums with "ArtistId" #51 on the "Album" table:
    # SELECT * FROM "Album" WHERE "ArtistId" = 51; - PostgreSQL command
    # cursor.execute('SELECT * from "Album" WHERE "ArtistId"=%s', [51]) - psycopg2 command
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)


    # query 6 - select all tracks where the composer is Queen from the "Track" table:
    # SELECT * FROM "Track" WHERE "Composer" = 'Queen'; - PostgreSQL command
    # cursor.execute('SELECT * from "Track" WHERE "Composer"=%s', ['Queen']) - psycopg2 command
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
