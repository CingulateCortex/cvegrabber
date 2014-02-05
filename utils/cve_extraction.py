import urllib3
from bs4 import BeautifulSoup
import re
from color_class import bcolors

class cve_extraction:

    def vuln_details(self,cveid):
        url = "http://www.cvedetails.com/cve/" + cveid
        http = urllib3.PoolManager()
        r= http.request('GET', url)
        color = bcolors()
        soup = BeautifulSoup(r.data)

        table = soup.find('table' , {'id' : 'cvssscorestable'})
        #cvs = table.find('th', text= 'CVSS Score')
        #x= cvs.findNext('td')
        area = []
        cells = []
        cell2 = []

        print color.HEADER+soup.title.text+ color.ENDC

        for row in table.findAll("tr"):
            cells += row.findAll("th")
            cell2 += row.findAll("td")


        for item in range(len(cells)-2):
            area = cells[item].find(text=True)
            text = cell2[item].find(text=True)
            print color.WARNING + "[+] " + color.ENDC + color.OKBLUE + area + color.ENDC + " : " + text