#!/usr/bin/env python3

import os
import os.path
import re
import json

PATH = "/mnt/fileshare"
FILENAME_PATTERN = re.compile(r"([^_]+)_([^_]+)_([^_]+).tr")

entries = []
for root,dirnames,filenames in os.walk(PATH):
    if len(filenames) == 0:
        continue
    for filename in filenames:
        match = FILENAME_PATTERN.match(filename)
        if not match:
            continue
        server_path = "/".join(root.split("/")[3:])
        entry = {}
        entry["lang"] = match.group(1)
        entry["resource"] = match.group(2)
        entry["book"] = match.group(3)
        entry["download_url"] = f"http://source.walink.org/bttr-source/{server_path}/{filename}"
        entries.append(entry)

print(json.dumps(entries))
