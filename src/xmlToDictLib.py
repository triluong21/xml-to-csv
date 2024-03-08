import xmltodict
import csv
from src.formatString import formatLongText

def convertXmlUsingToDict(outputFilename) -> None:
    # Parse XML file
    with open("inputDataFiles/catalogs.xml") as xmlFile:
        xml = xmltodict.parse(xmlFile.read())

    # Output CSV
    outputFilePath = f'outputDataFiles/{outputFilename}.csv'
    csvFile = open(outputFilePath, "w", newline="", encoding="utf-8")
    csvFileWriter = csv.writer(csvFile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Add csv header line
    csvFileWriter.writerow(["ID", "AUTHOR", "TITLE", "GENRE", "PRICE", "PUBLISH DATE", "DESCRIPTION"])

    # Write each row
    for book in xml["catalog"]["book"]:
        if(book):
            id = book["@id"]
            author = book["author"]
            title = book["title"]
            genre = book["genre"]
            price = book["price"]
            publish_date = book["publish_date"]
            description = formatLongText(book["description"])
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
