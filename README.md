# Dataffirm
Part A 
Create a list of user IDs, along with the number of distinct songs each user has played. 

  - Run Test_1.py
      Result: in 'test_1.csv'
      
    |count(userid)|
    
    |     19150868|  
    

  Alternative solution:
  First:
  - Run pre_alternative_test1_2.py
  
      Result: creation of dataffirm_db.db
      
      Remark: with a Total Lines input: 19,150,868, the test is showing some missing "rows": 19098862
  - Run alternative_test1.py - change path db_path = "/Users/csbailleul/Documents/Test_Automation/pyspark/dataffirm_db.db"
      Result: in user_track_count.txt

Part B 
Create a list of the 100 most popular songs (artist and title) in the dataset, with the number of times 
each was played. 

  - Run Test_2.py
  
      Result: in 'test_2.csv' and comment in Test_2.py
      
  Alternative solution:
  
  if not executed once:
  
    First:
    
    - Run pre_alternative_test1_2.py - change path for db_path = "/Users/csbailleul/Documents/Test_Automation/pyspark/dataffirm_db.db"
    
        Result: creation of dataffirm_db.db (similar to create table dataffirm (userid text, timestamp text, musicbrainz_artist_id text, artist_name text, musicbrainz_track_id text, track_name text))
        
  - Run alternative_test2.py
  
      Result: in 100_ref.txt
      
      Remark: slightly different results to Test_2.py


Part C 
Say we define a user’s “session” of Last.fm usage to be comprised of one or more songs played by that  user, where each song is started within 20 minutes of the previous song’s start time. Create a list of the top 10 longest sessions, with the following information about each session: userid, timestamp of first and last songs in the session, and the list of songs played in the session (in order of play).

- Lack of time.
p y t h o n   2   t e s t i n g  
 