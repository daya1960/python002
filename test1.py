from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SQLContext
from pyspark.sql import Row


DATA_FILE = "./lastfm-dataset-1K/userid-timestamp-artid-artname-traid-traname.tsv"

APP_NAME = "pyspark test 1"


def toto():
    print("TOTO")


def main(sc):
    sqlContext = SQLContext(sc)
    raw_data = sc.textFile(DATA_FILE)
    tsv_data = raw_data.map(lambda l: l.split("\t"))
    row_data = tsv_data.map(lambda p: Row(
        userid=p[0],
        timestamp=p[1],
        musicbrainz_artist_id=p[2],
        artist_name=p[3],
        musicbrainz_track_id=p[4],
        track_name=p[5]))
    interactions_df = sqlContext.createDataFrame(row_data)
    interactions_df.registerTempTable("music")
    tcp_interactions = sqlContext.sql("""
         select count(userid) from music
             """)
    tcp_interactions.show()
    '''
    +-------------+
    |count(userid)|
    +-------------+
    |     19150868|
    +-------------+
    '''    
    tcp_interactions = sqlContext.sql("""
         select userid, track_name, count(*) from music group by userid, track_name
    """)
    tcp_interactions.write.csv('test_1.csv')


if __name__ == "__main__":
    conf = SparkConf().setAppName(APP_NAME)
    conf = conf.setMaster("local[*]")
    sc = SparkContext(conf=conf)
    main(sc)

