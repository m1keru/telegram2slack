import json
import time
import datetime
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("file", help="exported from Telegram Json File")
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

result = []
with open(args.file) as json_file:
    data = json.load(json_file)
    channel = data['name']
    messages = data['messages']
    for msg in messages:
        __date = int(time.mktime(
            datetime.datetime.strptime(msg['date'], "%Y-%m-%dT%H:%M:%S").timetuple()))
        try:
            __from = msg['from']
        except KeyError as e:
            __from = 'Unknown'
        try:
            __text = msg['text'] if msg['text'] != '' else "No text"
        except KeyError as e:
            __text = 'No text'
        #result.append([date, channel, _from, msg['text']])
        print("\"%s\"|\"%s\"|\"%s\"|\"%s\"" % (__date, channel, __from, __text ))
