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
    <li>tb_songplay: Details of songs played via app </li>
</ul>


