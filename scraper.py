import requests
import re
import argparse
import sys
from bs4 import BeautifulSoup

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
    },
    "images": {
        "matches":[],
        "pattern": ""
    },
    "a_tags": {
        "matches": [],
        "pattern": ""
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
    site_data : String
    """
    for data_type in datas.values():
        if data_type["pattern"] != "":
            matches = re.findall(data_type["pattern"], site_data)
            for i, match in enumerate(matches):
                if match.endswith("></script>"):
                    matches[i] = match[0:match.index("></script>")]
            data_type["matches"] = list(set(matches))

def soup_links(site_data):
    """Data is extracted using Beautiful Soup
    Parameters
    ----------
    site_data : String
    """
    soup = BeautifulSoup(site_data, 'html.parser')
    img_list = list(set([link.get('src') for link in soup.find_all("img")]))
    img_list = rem_duplicates(img_list)
    datas["images"]["matches"] = img_list

    a_tags = list(set([link.get('href') for link in soup.find_all("a")]))
    a_tags = rem_duplicates(a_tags)
    datas["a_tags"]["matches"] = a_tags

def rem_duplicates(pre_list):
    """Items from the Beautiful Soup are filtered out by a master list
    Parameters
    ----------
    pre_list : list
    Returns
    -------
    result : list
    """
    result = []
    master_list = datas["links"]["matches"] + datas["emails"]["matches"] + datas["phone_numbers"]["matches"]
    for master in master_list:
        for item in pre_list:
            if master not in item:
                result.append(item)
    return result

def print_data():
    """Data is printed from the global datas object"""
    for key in datas.keys():
        print("\n{} found:\n".format(key))
        for data in datas[key]["matches"]:
            print(data)

def create_parser():
    """Returns an arg parser"""

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
    soup_links(site_data)
    print_data()

if __name__ == '__main__':
    main(sys.argv[1:])