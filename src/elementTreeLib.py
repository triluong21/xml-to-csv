from xml.etree import ElementTree
import csv

# Parse XML file
xml = ElementTree.parse("inputDataFiles/catalogs.xml")

# Output CSV
csvFile = open("outputDataFiles/etreecsv.csv", "w", encoding="utf-8")
csvFileWriter = csv.writer(csvFile)

# Add csv header line
csvFileWriter.writerow(["AUTHOR", "TITLE", "GENRE", "PRICE", "PUBLISH DATE", "DESCRIPTION"])

# Write each row
for book in xml.findall("book"):
    if(book):
        author = book.find("author")
        title = book.find("title")
        genre = book.find("genre")
        price = book.find("price")
        publish_date = book.find("publish_date")
        description = book.find("description")
        # Put texts in list and write csv data line
        csvLineList = [author.text,
                       title.text,
                       genre.text,
                       price.text,
                       publish_date.text,
                       description.text]
        csvFileWriter.writerow(csvLineList)

# Close csv file
csvFile.close()        
