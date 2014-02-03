import urllib3
from bs4 import BeautifulSoup
import re


class cve_extraction:

    def vuln_details(self):
        url = "http://www.cvedetails.com/cve/CVE-2006-5135/"
        http = urllib3.PoolManager()
        r= http.request('GET', url)

        soup = BeautifulSoup(r.data)

        table = soup.find('table' , {'id' : 'cvssscorestable'})
        #cvs = table.find('th', text= 'CVSS Score')
        #x= cvs.findNext('td')
        area = []
        cells = []
        cell2 = []
        for row in table.findAll("tr"):
            cells += row.findAll("th")
            cell2 += row.findAll("td")


        for item in range(len(cells)-2):
            area = cells[item].find(text=True)
            text = cell2[item].find(text=True)
            print area + " : " + text