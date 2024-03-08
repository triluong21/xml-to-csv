from src.elementTreeLib import convertXmlUsingEtree
from src.xmlToDictLib import convertXmlUsingToDict

# Create CSV file with element Tree
outputFileName = "elementtree"
convertXmlUsingEtree(outputFileName)

outputFileName = "xmltodict"
convertXmlUsingToDict(outputFileName)

