#!/usr/bin/env python
import json
import time
import datetime
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--file", help="exported from Telegram Json File", required=True)
parser.add_argument("--slack_chat_name", help="name for the Slack chat", required=True)
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit()

result = []
with open(args.file) as json_file:
    data = json.load(json_file)
    channel = args.slack_chat_name
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
        try:
            __text = str(__text).replace('\n', ' ').replace('\r', '')
        except:
            __text = 'non-utf string'
        print("\"%s\"|\"%s\"|\"%s\"|\"%s\"" % (__date, channel, __from, __text ))
