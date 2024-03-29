import os
import math
from datetime import datetime


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def convert_time(datetime_ts):
    return datetime \
        .fromtimestamp(datetime_ts) \
        .strftime("%d/%m/%Y, %H:%M:%S")


PATH = "F:\\Output"

for i in os.listdir(PATH):
    file_path = os.path.join(PATH, i)
    size = os.path.getsize(file_path)
    datetime_ts = os.path.getctime(file_path)
    date = convert_time(datetime_ts)
    print(i, " - ", date, " - ", convert_size(size))
