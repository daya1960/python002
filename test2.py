from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import HiveContext
from pyspark.sql import Row


DATA_FILE = "/Users/christophe/PROJECTS/dataffirm/Dataffirm/lastfm-dataset-1K/userid-timestamp-artid-artname-traid-traname.tsv"

APP_NAME = "pyspark test 2"


def main(sc):
    sqlContext = HiveContext(sc)
    raw_data = sc.textFile(DATA_FILE)
    tsv_data = raw_data.map(lambda l: l.split("\t"))
    df_tsv = tsv_data.map(lambda p: Row(
        userid=p[0],
        timestamp=p[1],
        musicbrainz_artist_id=p[2],
        artist_name=p[3],
        musicbrainz_track_id=p[4],
        track_name=p[5])).toDF()
    df_tsv.write.format("orc").saveAsTable("music")
    query = sqlContext.sql("""
         select track_name, artist_name, count(track_name) as value_occurrence from music
         group by track_name, artist_name
         ORDER BY `value_occurrence` DESC
         limit 100
    """)
    # query.show(100)
    query.write.csv('test_2.csv')


if __name__ == "__main__":
    conf = SparkConf().setAppName(APP_NAME)
    conf = conf.setMaster("local[*]")
    sc = SparkContext(conf=conf)
    main(sc)

'''
Result:
+--------------------+--------------------+----------------+
|          track_name|         artist_name|value_occurrence|
+--------------------+--------------------+----------------+
|  Such Great Heights|  The Postal Service|            3992|
|Love Will Tear Us...|        Boy Division|            3663|
|        Karma Police|           Radiohead|            3534|
|Supermassive Blac...|                Muse|            3483|
|     Soul Meets Body| Death Cab For Cutie|            3479|
|          Heartbeats|           The Knife|            3156|
|           Starlight|                Muse|            3060|
|    Rebellion (Lies)|         Arcade Fire|            3048|
|          Gimme More|      Britney Spears|            3004|
| When You Were Young|         The Killers|            2998|
|                Evil|            Interpol|            2989|
|       Love Lockdown|          Kanye West|            2950|
|            Teardrop|      Massive Attack|            2948|
|I Will Follow You...| Death Cab For Cutie|            2947|
| Time Is Running Out|                Muse|            2945|
|             Banquet|          Bloc Party|            2906|
|Neighborhood #1 (...|         Arcade Fire|            2826|
|          All I Need|           Radiohead|            2696|
|      Nothing Better|  The Postal Service|            2670|
|        Chasing Cars|         Snow Patrol|            2667|
|               Creep|           Radiohead|            2651|
|             15 Step|           Radiohead|            2647|
|           Heartless|          Kanye West|            2644|
|                Nude|           Radiohead|            2639|
|           Womanizer|      Britney Spears|            2635|
|               Crazy|      Gnarls Barkley|            2603|
|            Reckoner|           Radiohead|            2588|
|     Time To Pretend|                Mgmt|            2584|
|    Paranoid Android|           Radiohead|            2568|
|       The Scientist|            Coldplay|            2563|
|I Bet You Look Go...|      Arctic Monkeys|            2557|
|          Wonderwall|               Oasis|            2519|
|  Fake Plastic Trees|           Radiohead|            2490|
|  She'S Lost Control|        Joy Division|            2447|
|Neighborhood #3 (...|         Arcade Fire|            2444|
|Jigsaw Falling In...|           Radiohead|            2420|
|        Viva La Vida|            Coldplay|            2387|
|All These Things ...|         The Killers|            2385|
|Welcome To Heartb...|          Kanye West|            2376|
|   Enjoy The Silence|        Depeche Mode|            2369|
|The District Slee...|  The Postal Service|            2365|
|         Take Me Out|     Franz Ferdinand|            2355|
|Amazing (Feat. Yo...|          Kanye West|            2354|
|          Slow Hands|            Interpol|            2344|
|                Kids|                Mgmt|            2333|
|          Heartbeats|       José González|            2333|
|    Somebody Told Me|         The Killers|            2318|
|  Wish You Were Here|          Pink Floyd|            2314|
|          Obstacle 1|            Interpol|            2313|
|                Maps|     Yeah Yeah Yeahs|            2311|
|       Bodysnatchers|           Radiohead|            2294|
|           New Slang|           The Shins|            2281|
|  Knights Of Cydonia|                Muse|            2280|
|Map Of The Proble...|                Muse|            2276|
|Everything In Its...|           Radiohead|            2275|
|            Hysteria|                Muse|            2264|
|Paranoid (Feat. M...|          Kanye West|            2261|
|    Caring Is Creepy|           The Shins|            2247|
|              Clocks|            Coldplay|            2246|
|      House Of Cards|           Radiohead|            2243|
|        Paper Planes|              M.I.A.|            2240|
|       Hide And Seek|         Imogen Heap|            2239|
|         Don'T Panic|            Coldplay|            2232|
|        Say You Will|          Kanye West|            2229|
|Smells Like Teen ...|             Nirvana|            2229|
|        No Surprises|           Radiohead|            2227|
|        Golden Skans|             Klaxons|            2226|
|          Blue Light|          Bloc Party|            2216|
|             Fix You|            Coldplay|            2215|
|          Hallelujah|        Jeff Buckley|            2210|
|  Staring At The Sun|     Tv On The Radio|            2209|
|      Coldest Winter|          Kanye West|            2201|
|          No Cars Go|         Arcade Fire|            2195|
|Smile Like You Me...|         The Killers|            2182|
|            Float On|        Modest Mouse|            2178|
|               Rehab|       Amy Winehouse|            2167|
|            Bad News|          Kanye West|            2163|
|              Yellow|            Coldplay|            2158|
|       Electric Feel|                Mgmt|            2155|
|            Fidelity|      Regina Spektor|            2119|
|         Summer Skin| Death Cab For Cutie|            2115|
|                Hurt|         Johnny Cash|            2114|
|Une Année Sans Lu...|         Arcade Fire|            2111|
|             Wake Up|         Arcade Fire|            2108|
|Pinocchio Story (...|          Kanye West|            2107|
|             Robocop|          Kanye West|            2106|
|See You In My Nig...|          Kanye West|            2092|
|         Scar Tissue|Red Hot Chili Pep...|            2091|
|Weird Fishes/Arpeggi|           Radiohead|            2089|
|Exit Music (For A...|           Radiohead|            2088|
|         Clark Gable|  The Postal Service|            2088|
|        Say It Right|       Nelly Furtado|            2080|
|    Brand New Colony|  The Postal Service|            2076|
|               Angel|      Massive Attack|            2071|
|         Piece Of Me|      Britney Spears|            2071|
|  How To Save A Life|            The Fray|            2064|
|  Stairway To Heaven|      Dread Zeppelin|            2062|
|           Videotape|           Radiohead|            2061|
|       Street Lights|          Kanye West|            2051|
|                 Run|         Snow Patrol|            2048|
+--------------------+--------------------+----------------+

'''
