#!/usr/bin/env python3

import requests
import sys
import json

BASEURL = "https://pub.sandbox.orcid.org/v2.0/"
HEADERS = {
    "Authorization": "Bearer 19fcc56c-e696-49cc-82eb-7ddef7e4a0de",
    "Accept": "application/json"
    }


def print_header():
    '''Print a header to stdout'''
    title = "| QUERY ORCID |"
    bar = "=" * len(title)
    print("\n".join([" ", bar, title, bar]))


def pretty_print_json(text):
    '''take a string and print pretty json'''
    j = json.loads(text)
    pretty_dump = json.dumps(
        j, sort_keys=True, indent=4, separators=(',', ': ')
        )
    print(pretty_dump)


def main():
    uri = BASEURL + sys.argv[1]
    print("Querying {0}...".format(uri))
    response = requests.get(uri, headers=HEADERS)
    print("Response: {0}".format(response.status_code))
    pretty_print_json(response.text)


if __name__ == "__main__":
    main()