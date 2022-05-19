#!/usr/bin/env python3

import sys
from pwn import log, time

log.info("Starting...")
try:
    file_for_read = sys.argv[1]
    file_for_write = sys.argv[2]
except:
    log.info("Give 2 arguments!")
    log.info("Example: python3 clean_cupp.py words.spanish words.spanish.fix")
    exit()
with open(file_for_read, 'r') as read_file, open(file_for_write, 'w') as write_file:
    p = log.progress(f"Reading {file_for_read}, writing in {file_for_write}")
    time.sleep(1.0)
    for word in read_file:
        if "`" in word:
            p.status(f"Find an ` in {word}")
            word = word.replace("a`", "á")
            word = word.replace("e`", "é")
            word = word.replace("i`", "í")
            word = word.replace("o`", "ó")
            word = word.replace("u`", "ú")
        if word != "'#''#''#'":
            p.status(f"{word} is not '#''#''#'")
            if "'#'" in word:
                p.status(f"Find an '#' in {word}")
                word = word.replace("'#'","#")
            write_file.write(word)
    p.success("Finish!")
