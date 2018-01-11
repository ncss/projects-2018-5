import re

class Node:
    def __init__(self):
        pass


class TextNode(Node):
    def __init__(self, statement):
        self.text = statement

class ExprNode(Node):
    reg = re.compile(r'^\{\{ +(.+) +\}\}')
    def __init__(self, statement, context):
        self.parse(statement)
        self.context = context

    def parse(self, statement):
        self.expression = ExprNode.reg.search(statement).group(1)

    def translate(self):
        if self.expression not in self.context:
            raise Exception("Expression is not in the context")
        else:
            translation = eval(self.context[self.expression])
        return translation
        

class IncNode(Node):
    reg = re.compile(r'^\{\% +include +(.+)\%\}')
    def __init__(self, statement, context):
        self.parse(statement)
        self.context = context
        
    def parse(self, statement):
        self.filename = IncNode.reg.search(statement).group(1)

class IfNode(Node):
    reg = re.compile(r'^\{\% +if +(.+) +\%\}')
    def __init__(self, statement, context):
        self.block = GroupNode(False)
        self.parse(statement)
        self.context = context

    def parse(self, statement):
        self.condition = IfNode.reg.search(statement).group(1)

class ForNode(Node):
    reg = re.compile(r'^\{\% +for +(.+) +in +(.+) +\%\}')
    def __init__(self, statement, context):
        self.block = GroupNode(False)
        self.parse(statement)
        self.context = context

    def parse(self, statement):
        self.variable = ForNode.reg.search(statement).group(1)
        self.iterable = ForNode.reg.search(statement).group(2)

class GroupNode(Node):
    def __init__(self, isRoot, context = {}):
        self.children = []
        self.isRoot = isRoot
        self.context = context

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
