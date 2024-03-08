
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
