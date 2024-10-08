
###1 XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # Initialize count of attributes
    count = len(node.attrib)  # Count attributes of the current node
    # Recursively count attributes for all child nodes
    for child in node:
        count += get_attr_number(child)  # Add child attributes count
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
  

###2 XML2 - Find the Maximum Depth
