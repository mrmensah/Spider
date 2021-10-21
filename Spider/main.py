# importing the libraries
from bs4 import BeautifulSoup
import requests

#Function to check for presence of renewable energy
def isRenewableEnergyPresent(sentence, word1, word2):
    # print(sentence)
    s = sentence.split(" ")

    for i in s:
        for j in s:
            if (i == word1 or j == word2):
                print(sentence)
                return True
    return False


# the url
url = 'https://www.energy.gov/funding-financing-energy-projects'
theURL = requests.get(url)

# Get the website's HTML page
soup = BeautifulSoup(theURL.text, 'html.parser')
energy = 'Energy'
renewable = "Renewable"
# create file for the links
sites = open("sites.txt", "w+")

# find all links
for link in soup.find_all('a'):
    linkContent = link.getText()
    if (isRenewableEnergyPresent(linkContent, renewable, energy) == True):
        site = link.get('href')
        print(site)
        sites.write(site + '\n') # Write urls to file
    else:
        print("No possible renewable energy grants available")

sites.close() #close the file

# send the sites file to email
