import requests
import re
import argparse
import sys

__author__ = 'Scott Reese'

datas = {
    "links": {
        "matches":[],
        "pattern": "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    },
    "emails": {
        "matches":[],
        "pattern": "[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    },
    "phone_numbers": {
        "matches":[],
        "pattern": "[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]"
    }
}

def fetch_html(link):
    """Returns the html text
    Parameters
    ----------
    link : String
    Returns
    -------
    String
    """
    r = requests.get(link)
    return r.text

def extract_data(site_data):
    """Data is extracted based upon the global datas dict
    Parameters
    ----------
    Nothing
    Returns
    -------
    Nothing
    """
    for data_type in datas.values():
        matches = re.findall(data_type["pattern"], site_data)
        for i, match in enumerate(matches):
            if match.endswith("></script>"):
                matches[i] = match[0:match.index("></script>")]
        data_type["matches"] = list(set(matches))

def print_data():
    """Data is printed from the global datas object
    Parameters
    ----------
    Nothing
    Returns
    -------
    Nothing
    """
    for key in datas.keys():
        print("\n{} found:\n".format(key))
        for data in datas[key]["matches"]:
            print(data)

def create_parser():
    """Returns an arg parser
    Parameters
    ----------
    Nothing
    Returns
    -------
    argument parser object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Website to extract data from')

    return parser

def main(args):
    parser = create_parser()

    if not args:
        parser.print_usage()
        sys.exit(1)
    
    parsed_args = parser.parse_args(args)
    site_data = fetch_html(parsed_args.url)
    extract_data(site_data)
    print_data()

if __name__ == '__main__':
    main(sys.argv[1:])