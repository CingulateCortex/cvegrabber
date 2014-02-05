import urllib3
from bs4 import BeautifulSoup
import re
from utils.generic import generic
from utils.cve_extraction import cve_extraction
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-s', help ='Search CVE Id in database')
#CVE-2006-5135

result = parser.parse_args()
print result
if result.s:
    a = cve_extraction()
    a.vuln_details(result.s)


