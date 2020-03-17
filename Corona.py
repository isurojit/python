import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


html = urllib.request.urlopen('https://www.worldometers.info/coronavirus/').read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('title')
for tag in tags:
   result = tag
for lines in result:
    line = lines.split()
print('############################################################################################################################')
print('####        ###         ###       ###         ###    ######  ###        ### ######### ###   ###     ### ##### ###        ###')
print('####  #########  #####  ###  ###  ###  #####  ###  #  #####  ###  ####  #### ####### ##### #### ### ### ##### ### ##########')
print('####  #########  #####  ###       ###  #####  ###  ###  ###  ###        ##### ##### ###### ####     ### ##### ###        ###')
print('####  #########  #####  ###  ##  ####  #####  ###  ####  ##  ###  ####  ###### ### ####### #### ## #### ##### ########## ###')
print('####        ###         ###  ###  ###         ###  #####     ###  ####  #######   #######   ### ### ###       ###        ###')
print('############################################################################################################################\n')
print('\n LIVE UPDATES  :-\n')

print('\n************************************\n')
print('\n************************************\n')
print('TOTAL CASES TILL NOW :-- \n',line[3])
print('TOTAL DEATHS TILL NOW :-- \n',line[6])
print('\n************************************\n')
print('\n************************************\n')

print('PLEASE STAY SAFE & FOLLOW WHAT YOUR GOVERMENT & HEALTH OFFICIAL SAYS. THIS BAD TIME WILL PAST SOON. TAKE CARE OF ELDERS.')
print('-made by Surojit Manna')
print('Live Update Web Crawling From - World Meters')
