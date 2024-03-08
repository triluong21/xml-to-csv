from src.elementTreeLib import convertXmlUsingEtree
from src.xmlToDictLib import convertXmlUsingToDict
from src.unTangleLib import convertXmlUsingUnTangle

# Create CSV file with element Tree
outputFileName = "elementtree"
convertXmlUsingEtree(outputFileName)

outputFileName = "xmltodict"
convertXmlUsingToDict(outputFileName)

outputFileName = "untangle"
convertXmlUsingUnTangle(outputFileName)

