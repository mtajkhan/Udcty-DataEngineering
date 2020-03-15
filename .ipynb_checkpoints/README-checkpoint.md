#**Sparkify: Postgres Music Database**

**Business Requirement**

Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. 

To achieve the above goal Postgres database is required to be designed to optimize queries on song play analysis.

**Current Status**

Currently, Sparkify don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

**Design Requirement**
    * Define fact and dimension tables for a star schema for a particular analytic focus
    * Build an ETL pipeline using Python that transfers data from files in two local directories into these tables in Postgres using Python and SQL


###**Database Details**

####Schema:

**Dim Tables**
    * **tb_user:** App users
    * **tb_song:** Available songs in the app
    * **tb_artist:**Details of artists of the songs
    * **tb_time:** tb_songplay start time broken down into various time units

**Fact Tables**
    * **tb_songplay:** Details of songs played via app 

###Project Design

####Overall Design:

ETL Pipeline is created to auto ingest multiple file(s) within a directory as well as sub directories, parsed as needed and stored into the specific tables in the desired schema's.

The Database Design is carried out with star schema structure keeping in mind the ease and efficient use for analytics team as requested. The database can be queried for analytical work loads optimally as well as intuitively.

####Tools required for execution:
    * **Jupyter Lab:** For updating, testing and interactive execution of the srcipts
    * **Python Shell:** To execute ETL pipelines (.py files)

####Scripts/Notebook details:
    * **create_tables.py:** Drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts
    * **sql_queries.py:** Contains all your sql queries, and is imported into create_tables.py, etl.ipynb, etl.py 
    * **etl.ipynb:**Reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
    * **etl.py:** Reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook
    * **test.ipynb:**Displays the first few rows of each table to let you check your database
