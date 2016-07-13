class ListNode(object):
    parent = None
    myList = []


class ObjectNode(object):
    parent = None
    data = {}


def AddComplexObject(node, lastNode, objName=""):
    node.parent = lastNode
    if isinstance(lastNode, ListNode):
        lastNode.myList.append(node)
    elif isinstance(lastNode, ObjectNode):
        lastNode.data[objName] = node

def strOrNumber(strValue):
    if strValue.isdigit():
        return int(strValue)
    else:
        return strValue


def main():
    f = open("testInput.txt")
    latestNode = ListNode()
    latestItem = ""
    itemName = ""
    for bob in f:
        for ch in bob:
            if ch is "[":
                tempNode = ListNode()
                AddComplexObject(tempNode, latestNode)
                latestNode = tempNode
            elif ch is "{":
                tempNode = ObjectNode()
                AddComplexObject(tempNode, latestNode, itemName)
                latestNode = tempNode
            elif ch is "]":
                latestNode.myList.append(latestItem)
                latestItem = ""
                latestNode = latestNode.parent
            elif ch is "}":
                latestNode.data[itemName] = latestItem
                latestItem = ""
                latestNode = latestNode.parent
            elif ch is ":":
                itemName = latestItem
                latestItem = ""
            elif ch is ",":
                if isinstance(latestNode, ListNode) and latestItem is not "":
                    latestNode.myList.append(strOrNumber(latestItem))
                    latestItem = ""
                elif isinstance(latestNode, ObjectNode) and latestItem is not "":
                    latestNode.data[itemName] = strOrNumber(latestItem)
                    latestItem = ""
                    itemName = ""
            else:
                if ch is not "\"" and ch is not "\n":
                    latestItem += ch

        print("{0}, {1}".format(bob, str(latestNode)))


if __name__ == "__main__":
    main()
