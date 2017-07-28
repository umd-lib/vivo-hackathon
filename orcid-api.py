#!/usr/bin/env python3

import requests
import sys
import json
import os

OAUTH_TOKEN = os.getenv('ORCID_OAUTH_TOKEN', None)
BASEURL = "https://pub.sandbox.orcid.org/v2.0/"
HEADERS = {
    "Authorization": "Bearer {0}".format(OAUTH_TOKEN),
    "Accept": "application/json"
    }


def print_header():
    '''Print a header to stdout'''
    title = "| QUERY ORCID |"
    bar = "=" * len(title)
    print("\n".join([" ", bar, title, bar]))


def pretty_print_json(text):
    '''Take a string and return pretty json string'''
    j = json.loads(text)
    pretty_dump = json.dumps(
        j, sort_keys=True, indent=4, separators=(',', ': ')
        )
    return pretty_dump


def main():
    if OAUTH_TOKEN is None:
	print("You must set ORCID_OAUTH_TOKEN environment variable.")
        sys.exit(1)
    uri = BASEURL + sys.argv[1]
    print("Querying {0}...".format(uri))
    response = requests.get(uri, headers=HEADERS)
    print("Response: {0}".format(response.status_code))
    print(pretty_print_json(response.text))


if __name__ == "__main__":
    main()
