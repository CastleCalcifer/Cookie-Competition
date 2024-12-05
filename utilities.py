def parseVote(ranking:str) -> int:
    if ranking == "1st":
        return 5
    elif ranking == "2nd":
        return 4
    elif ranking == "3rd":
        return 3
    elif ranking == "4th":
        return 2
    else:
        return 1