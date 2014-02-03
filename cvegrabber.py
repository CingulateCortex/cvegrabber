import urllib3
from bs4 import BeautifulSoup
import re
from utils.generic import generic
from utils.cve_extraction import cve_extraction




a = cve_extraction()

a.vuln_details()


