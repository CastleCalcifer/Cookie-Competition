def parseVote(ranking:str) -> int:
    if ranking == "1st":
        return 4
    elif ranking == "2nd":
        return 3
    elif ranking == "3rd":
        return 2
    else:
        return 1