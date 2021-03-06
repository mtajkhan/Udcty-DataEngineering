# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS tb_songplay;"
user_table_drop = "DROP TABLE IF EXISTS tb_user;"
song_table_drop = "DROP TABLE IF EXISTS tb_song;"
artist_table_drop = "DROP TABLE IF EXISTS tb_artist;"
time_table_drop = "DROP TABLE IF EXISTS tb_time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS tb_songplay (
start_time TIMESTAMP NOT NULL,
user_id INTEGER NOT NULL,
level VARCHAR,
song_id VARCHAR,
artist_id VARCHAR,
session_id INTEGER,
location VARCHAR, 
user_agent VARCHAR
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS tb_user (
userId VARCHAR PRIMARY KEY, 
firstName VARCHAR NOT NULL, 
lastName VARCHAR NOT NULL, 
gender VARCHAR, 
level VARCHAR
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS tb_song (
song_id VARCHAR PRIMARY KEY,
title VARCHAR NOT NULL,
artist_id VARCHAR NOT NULL, 
year INT, 
duration FLOAT
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS tb_artist (
artist_id VARCHAR PRIMARY KEY, 
artist_name VARCHAR NOT NULL, 
artist_location VARCHAR, 
artist_latitude VARCHAR,  
artist_longitude VARCHAR
);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS tb_time (
start_time TIMESTAMP PRIMARY KEY,
hour INT,
day INT, 
weekofyear INT, 
month INT,
year INT,
weekday INT
);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO tb_songplay (
start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
) 
VALUES (
%s, %s, %s, %s, %s, %s, %s, %s
);
""")

user_table_insert = ("""INSERT INTO tb_user (
userId, firstName, lastName, gender, level
) 
VALUES (
%s, %s, %s, %s, %s
)
ON CONFLICT(
userId
)
DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
INSERT INTO tb_song (
song_id,title,artist_id,year, duration
) 
VALUES (
%s, %s, %s, %s, %s
)
ON CONFLICT(
song_id
) 
DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO tb_artist (
artist_id,artist_name,artist_location,artist_latitude,artist_longitude
) 
VALUES (
%s, %s, %s, %s, %s
)
ON CONFLICT(
artist_id
) 
DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO tb_time (
start_time, hour, day, weekofyear, month, year, weekday
) 
VALUES (
%s, %s, %s, %s, %s, %s, %s
)
ON CONFLICT(
start_time
) 
DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, s.artist_id 
FROM tb_song s 
JOIN tb_artist a 
ON s.artist_id = a.artist_id 
WHERE s.title = %s AND a.artist_name = %s AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]



