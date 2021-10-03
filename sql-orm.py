from sqlalchemy import(
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from our local host "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Artist" table:
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# create a class-based model for the "Album" table:
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

# create a class-based model for the "Track" table:
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))    
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declartive_base subclass
base.metadata.create_all(db)


# query 1 - select all records from the 'Artist' table:
# SELECT everything FROM "Artist"; - PostgreSQL command
# cursor.execute('SELECT * FROM "Artist"') - psycopg2 command
# select_query = artist_table.select() - SQLAlchemyExpression command
""" SQLAlchemy ORM command
artists = session.query(Artist)
for artist in artists:
    print(artist.ArtistId, artist.Name, sep=" | ")
"""

# query 2 - select only the 'Name' collumn from the 'Artist' table:
# SELECT "Name" FROM "Artist";
# cursor.execute('SELECT "Name" FROM "Artist"') - psycopg2 command
# select_query = artist_table.select().with_only_columns([artist_table.c.Name]) - SQLAlchemyExpression command
""" SQLAlchemy ORM command
artists = session.query(Artist)
for artist in artists:
    print(artist.Name)
"""

# query 3 - select only 'Queen' from the 'Artist' table:
# SELECT * FROM "Artist" WHERE "Name" = 'Queen'; - PostgreSQL command
# cursor.execute('SELECT * from "Artist" WHERE "Name"= %s', ["Queen"]) - psycopg2 command
# select_query = artist_table.select().where(artist_table.c.Name == "Queen") - SQLAlchemyExpression command
""" SQLAlchemy ORM command
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep=" | ")
"""

# query 4 - select only by "ArtistId" #51 from the "Artist" table:
# SELECT * FROM "Artist" WHERE "ArtistId" = 51; - PostgreSQL command
# cursor.execute('SELECT * from "Artist" WHERE "ArtistId"= %s', [51]) - psycopg2 command
# select_query = artist_table.select().where(artist_table.c.ArtistId == 51) - SQLAlchemyExpression command
""" SQLAlchemy ORM command
artist = session.query(Artist).filter_by(ArtistId=51).first()
print(artist.ArtistId, artist.Name, sep=" | ")
"""

# query 5 - select only the albums with "ArtistId" #51 on the "Album" table:
# SELECT * FROM "Album" WHERE "ArtistId" = 51; - PostgreSQL command
# cursor.execute('SELECT * from "Album" WHERE "ArtistId"=%s', [51]) - psycopg2 command
# select_query = album_table.select().where(album_table.c.ArtistId == 51) - SQLAlchemyExpression command
""" SQLAlchemy ORM command
albums = session.query(Album).filter_by(ArtistId=51)
for album in albums:
    print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")
"""

# query 6 - select all tracks where the composer is Queen from the "Track" table:
# SELECT * FROM "Track" WHERE "Composer" = 'Queen'; - PostgreSQL command
# cursor.execute('SELECT * from "Track" WHERE "Composer"=%s', ['Queen']) - psycopg2 command
# select_query = track_table.select().where(track_table.c.Composer == "Queen") - SQLAlchemyExpression command
# """ SQLAlchemy ORM command
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId, 
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
# """
