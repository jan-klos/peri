#!/bin/bash

rm /home/pi/peridb.db
touch /home/pi/peridb.db
sqlite3 /home/pi/peridb.db < create_table.sql