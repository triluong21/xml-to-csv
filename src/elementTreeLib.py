from xml.etree import ElementTree
import csv

def convertXmlToCsv(outputFilename) -> None:
    # Parse XML file
    xml = ElementTree.parse("inputDataFiles/catalogs.xml")

    # Output CSV
    outputFilePath = f'outputDataFiles/{outputFilename}.csv'
    csvFile = open(outputFilePath, "w", newline="", encoding="utf-8")
    csvFileWriter = csv.writer(csvFile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

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
            description = formatLongText(book.find("description").text)
            
            # Put texts in list and write csv data line
            csvLineList = [author.text,
                        title.text,
                        genre.text,
                        price.text,
                        publish_date.text,
                        description]
            
            csvFileWriter.writerow(csvLineList)

    # Close csv file
    csvFile.close()        

def formatLongText(inputString: str) -> str:
    workTextString1 = ""
    workTextString2 = ""

    endLineList = inputString.split("\n")
    for textString in endLineList:
        workTextString1 = f'{workTextString1} {textString}'

    tabStringList = workTextString1.split("\t")
    for textString in tabStringList:
       workTextString2 = f'{workTextString2} {textString}'
    
    return f"'{workTextString2}'"
