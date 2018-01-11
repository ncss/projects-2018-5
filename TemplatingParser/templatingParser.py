import re


class Node:
    def __init__(self):
        pass


class TextNode(Node):
    def __init__(self, text):
        self.content = text


class ExprNode(Node):
    def __init__(self, expression):
        self.content = expression


class IncNode(Node):
    def __init__(self, content):
        self.content = content


class IfNode(Node):
    def __init__(self, statement):
        self.block = GroupNode(False)
        self.content = statement


class ForNode(Node):
    def __init__(self, statement):
        self.block = GroupNode(False)
        self.content = statement


class GroupNode(Node):
    def __init__(self, isRoot):
        self.children = []
        self.isRoot = isRoot

    def addChild(self, child):
        self.children.append(child)

    def parse(self, tokenSplit):
        tokenList = tokenSplit
        while tokenList != []:
            if re.match(r"{{.*?}}", tokenList[0]) is not None:
                # Expression node
                self.addChild(ExprNode(tokenList.pop(0)))
            elif re.match(r"{% if.*%}", tokenList[0]) is not None:
                # If node
                node = IfNode(tokenList.pop(0))
                self.addChild(node)
                node.block.parse(tokenList)
            elif re.match(r"{% end if[ ]*%}", tokenList[0]) is not None:
                # NOTE: end if is dropped.
                if self.isRoot:
                    raise SyntaxError("Unmatched end if token")
                tokenList.pop(0)
                return None
            elif re.match(r"{% for.+in.+%}", tokenList[0]) is not None:
                # For node
                node = ForNode(tokenList.pop(0))
                self.addChild(node)
                node.block.parse(tokenList)
            elif re.match(r"{% end for[ ]*%}", tokenList[0]) is not None:
                if self.isRoot:
                    raise SyntaxError("Unmatched end for token")
                tokenList.pop(0)
                return None
            elif re.match(r"{% include[ ].*%}", tokenList[0]) is not None:
                self.addChild(IncNode(tokenList.pop(0)))
            elif re.match(r"{%.*%}", tokenList[0]) is not None:
                raise SyntaxError("Unknown token")
            else:
                self.addChild(TextNode(tokenList.pop(0)))

        if not self.isRoot:
            raise SyntaxError("Missing closing For or If token")


def splitFile(fileLocation):

    fileBlob = ""
    tokenList = []
    with open(fileLocation) as file:
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
    return tokenList


# TODO: GroupNode with parse function, other node types with appropriate constructors.
root = GroupNode(True)
root.parse(splitFile("../TestCase2.Moana"))


def printNodeContent(nodes):
    for i in nodes:
        print(i.content, end="")
        if type(i) is IfNode or type(i) is ForNode:
            printNodeContent(i.block.children)


printNodeContent(root.children)
