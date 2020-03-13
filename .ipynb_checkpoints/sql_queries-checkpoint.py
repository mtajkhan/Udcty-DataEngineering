# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS tb_songplay"
user_table_drop = "DROP TABLE IF EXISTS tb_user"
song_table_drop = "DROP TABLE IF EXISTS tb_song"
artist_table_drop = "DROP TABLE IF EXISTS tb_artist"
time_table_drop = "DROP TABLE IF EXISTS tb_time"

# CREATE TABLES

songplay_table_create = ("""
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS tb_user (userId varchar, firstName varchar, lastName varchar, gender varchar, level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS tb_song (song_id varchar,title varchar,artist_id varchar, year int, duration float);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS tb_artist (artist_id varchar, artist_name varchar, artist_location varchar, artist_latitude varchar,  artist_longitude varchar);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS tb_time (timestamp timestamp,hour int,day int, weekofyear int, month int,year int,weekday int);""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""INSERT INTO tb_user (userId, firstName, lastName, gender, level) VALUES (%s, %s, %s, %s, %s)""")

song_table_insert = ("""INSERT INTO tb_song (song_id,title,artist_id,year, duration) VALUES (%s, %s, %s, %s, %s)""")

artist_table_insert = ("""INSERT INTO tb_artist (artist_id,artist_name,artist_location,artist_latitude,artist_longitude) VALUES (%s, %s, %s, %s, %s)""")


time_table_insert = ("""INSERT INTO tb_time (timestamp, hour, day, weekofyear, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

# create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

