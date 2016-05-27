#simple script to scrape BL contacts off the Boston Logic website after downloading list to html
import csv
from bs4 import BeautifulSoup
#import urllib.request 

#need this for downloading the file using urllib.request (see above)
#urllib.request.urlretrieve('http://www.eplacehomes.com/admin/marketing_lists/11850.html?search_type=contacts','eplace_landlords.html')

#open the file -- using python -- no libraries 
f = open('list.html','r')

#open the file in BeautifulSoup
soup = BeautifulSoup(f,'html.parser')

#pull out the simple table structure
#table = soup.find('table') #table = soup.find('table', attrs={'class': 'collapse shadow BCSDTable'})
table = soup.find('table', attrs={'class': 'search_report_results marketing_table'})
#create an array that is a list of rows
list_of_rows = []

##go into each row and get the cells
for row in table.findAll('tr'):
	# create an array that contains the cells in one row
	list_of_cells = []
	# for each row, pull out the cells
	for cell in row.findAll('td'):		
		#get the text from the cell only, none of the html
		text = cell.text
		#add this text to the array
		list_of_cells.append(text)
	#add the specific row information to the list of all rows	
	list_of_rows.append(list_of_cells)

#create the csv file for download and write the rows to it
outfile = open("./ll_symposium.csv","a")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
