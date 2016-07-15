class ListNode(object):
    parent = None
    myList = []


class ObjectNode(object):
    parent = None
    data = {}


def str_or_number(str_value):
    if str_value[0:1] == "-" and str_value[1:].isdigit():
        return int(str_value)
    if str_value.isdigit():
        return int(str_value)
    else:
        return str_value.strip("\"")


def count_items(node_to_start, string_to_avoid):
    totalCount = 0
    if isinstance(node_to_start, ListNode):
        for item in node_to_start.myList:
            if isinstance(item, int):
                totalCount += item
            elif isinstance(item, ListNode) or isinstance(item, ObjectNode):
                totalCount += count_items(item, string_to_avoid)
    elif isinstance(node_to_start, ObjectNode):
        if string_to_avoid not in node_to_start.data.values():
            for key, value in node_to_start.data.iteritems():
                if isinstance(value, int):
                    totalCount += value
                elif isinstance(value, ListNode) or isinstance(value, ObjectNode):
                    totalCount += count_items(value, string_to_avoid)
    return totalCount


def main():
    f = open("realInput.txt")
    for bob in f:
        latestNode = ""
        latestItem = ""
        itemName = ""
        rootItem = None

        for ch in bob.strip():
            if ch is "[":
                tempNode = ListNode()
                tempNode.myList = []
                tempNode.parent = latestNode
                if isinstance(latestNode, ListNode):
                    latestNode.myList.append(tempNode)
                elif isinstance(latestNode, ObjectNode):
                    latestNode.data[itemName] = tempNode
                if rootItem is None:
                    rootItem = tempNode
                latestNode = tempNode
            elif ch is "{":
                tempNode = ObjectNode()
                tempNode.data = {}
                tempNode.parent = latestNode
                if isinstance(latestNode, ListNode):
                    latestNode.myList.append(tempNode)
                elif isinstance(latestNode, ObjectNode):
                    latestNode.data[itemName] = tempNode
                if rootItem is None:
                    rootItem = tempNode
                latestNode = tempNode
            elif ch is "]":
                if latestItem != "":
                    latestNode.myList.append(str_or_number(latestItem))
                    latestItem = ""
                latestNode = latestNode.parent
            elif ch is "}":
                if latestItem != "":
                    latestNode.data[itemName] = str_or_number(latestItem)
                    latestItem = ""
                latestNode = latestNode.parent
            elif ch is ":":
                itemName = latestItem
                latestItem = ""
            elif ch is ",":
                if isinstance(latestNode, ListNode) and latestItem is not "":
                    latestNode.myList.append(str_or_number(latestItem))
                    latestItem = ""
                elif isinstance(latestNode, ObjectNode) and latestItem is not "":
                    latestNode.data[itemName] = str_or_number(latestItem)
                    latestItem = ""
                    itemName = ""
            else:
                if ch is not "\"" and ch is not "\n":
                    latestItem += ch

        print("count={0}, {1}, {2}".format(count_items(rootItem, "red"), str(rootItem), str(latestNode)))


if __name__ == "__main__":
    main()
