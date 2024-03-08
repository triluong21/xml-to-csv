import untangle
import csv
from src.formatString import formatLongText

def convertXmlUsingUnTangle(outputFilename) -> None:
    # Parse XML file
    with open("inputDataFiles/catalogs.xml") as xmlFile:
        xml = untangle.parse(xmlFile.read())

    # Output CSV
    outputFilePath = f'outputDataFiles/{outputFilename}.csv'
    csvFile = open(outputFilePath, "w", newline="", encoding="utf-8")
    csvFileWriter = csv.writer(csvFile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Add csv header line
    csvFileWriter.writerow(["ID", "AUTHOR", "TITLE", "GENRE", "PRICE", "PUBLISH DATE", "DESCRIPTION"])

    # Write each row
    for book in xml.catalog.book:
        if(book):
            id = book['id']
            author = book.author.cdata
            title = book.title.cdata
            genre = book.genre.cdata
            price = book.price.cdata
            publish_date = book.publish_date.cdata
            description = formatLongText(book.description.cdata)
            # Put texts in list and write csv data line
            csvLineList = [id,
                           author,
                           title,
                           genre,
                           price,
                           publish_date,
                           description]
            
            csvFileWriter.writerow(csvLineList)

    # Close csv file
    csvFile.close()        
