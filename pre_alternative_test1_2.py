#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine

DATA_FILE = "./lastfm-dataset-1K/userid-timestamp-artid-artname-traid-traname.tsv"


def main():

    dataffirm_db = create_engine('sqlite:///dataffirm_db.db')

    chunksize = 19150868
    chunks = pd.read_csv(DATA_FILE,
                         chunksize=chunksize,
                         header=None,
                         names=['userid', 'timestamp', 'musicbrainz_artist_id',
                                'artist_name', 'musicbrainz_track_id', 'track_name'],
                         sep='\t',
                         iterator=True,
                         encoding='utf-8',
                         error_bad_lines=False)
    for chunk in chunks:
        chunk.to_sql('musictable', dataffirm_db, if_exists='append')
    df = pd.read_sql_query('select count(*) from musictable', dataffirm_db)
    print(df)


if __name__ == "__main__":
    main()
