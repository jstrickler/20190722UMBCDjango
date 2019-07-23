#!/usr/bin/env python

import sqlite3


with sqlite3.connect('music/music.db') as music_conn:
    cur = music_conn.cursor()

    cur.execute("""
    select * from bands_Band
    """)

    for row in cur.fetchall():
        print(row)


    cur.execute("""
    select * from bands_Member
    """)

    for row in cur.fetchall():
        print(row)

    # cur.execute("""
    # select * from bands_Member m join bands_Genre g on b.genre = g.id
    # """)
    #
    # for row in cur.fetchall():
    #     print(row)
