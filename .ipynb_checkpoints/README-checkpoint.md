<h1><b>Sparkify: Postgres Music Database </b></h1>

<b>Business Requirement</b>

Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. 

To achieve the above goal Postgres database is required to be designed to optimize queries on song play analysis.

<b>Current Status</b>

Currently, Sparkify don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

<b>Design Requirement</b>

<ul>
    <li>Define fact and dimension tables for a star schema for a particular analytic focus</li>
    <li>Build an ETL pipeline using Python that transfers data from files in two local directories into these tables in Postgres using Python and SQL</li>
</ul>

<h3><b>Database Details</b></h3>

<h4>Schema:</h4>

<b>Dim Tables</b>
<ul>
    <li><b>tb_user:</b> App users</li>
    <li><b>tb_song:</b> Available songs in the app</li>
    <li><b>tb_artist:</b>Details of artists of the songs</li>
    <li><b>tb_time:</b> tb_songplay start time broken down into various time units</li>
</ul>

<b>Fact Tables</b>
<ul>    
    <li><b>tb_songplay:</b> Details of songs played via app </li>
</ul>

<h3>Project Design</h3>

<h4>Overall Design:</h4>

ETL Pipeline is created to auto ingest multiple file(s) within a directory as well as sub directories, parsed as needed and stored into the specific tables in the desired schema's.

The Database Design is carried out with star schema structure keeping in mind the ease and efficient use for analytics team as requested. The database can be queried for analytical work loads optimally as well as intuitively.

<h4>Tools required for execution:</h4>
<ul>
    <li><b>Jupyter Lab:</b> For updating, testing and interactive execution of the srcipts</li>
    <li><b>Python Shell:</b> To execute ETL pipelines (.py files)</li>
</ul>

<h4>Scripts/Notebook details:</h4>
<ul>
    <li><b>create_tables.py:</b> Drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts</li>
    <li><b>sql_queries.py:</b> Contains all your sql queries, and is imported into create_tables.py, etl.ipynb, etl.py </li>
    <li><b>etl.ipynb:</b>Reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.</li>
    <li><b>etl.py:</b> Reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook</li>
    <li><b>test.ipynb:</b>Displays the first few rows of each table to let you check your database</li>
</ul>