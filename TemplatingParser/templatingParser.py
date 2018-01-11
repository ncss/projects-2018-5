# Team 971 is best & IFI sucks
import re


class Node:
    def __init__(self):
        pass

    def render(self):
        pass


class GroupNode(Node):
    def __init__(self):
        self._children = []

    def addChild(self, child):
        self._children.append(child)


fileBlob = ""
tokenList = []
with open("template.html") as file:
    fileBlob = file.read()


def addBlock(searchObj):
    tokenList.append(fileBlob[:searchObj.start()])
    tokenList.append(fileBlob[searchObj.start():searchObj.end()])
    return fileBlob[searchObj.end():]


while fileBlob != "":
    exprSearch = re.search(r"{{.*?}}", fileBlob)
    pySearch = re.search(r"{%.*?%}", fileBlob)
    if exprSearch is not None and pySearch is not None:
        if exprSearch.start() < pySearch.start():
            fileBlob = addBlock(exprSearch)
        else:
            fileBlob = addBlock(pySearch)
    elif exprSearch is not None:
        fileBlob = addBlock(exprSearch)
    elif pySearch is not None:
        fileBlob = addBlock(pySearch)
    else:
        tokenList.append(fileBlob)
        fileBlob = ""
print(tokenList)
