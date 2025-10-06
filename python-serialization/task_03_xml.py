#!/usr/bin/python
"""
serialize and deserialize using XML
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    """
    root = ET.Element("data")
    for k, v in dictionary.items():
        child = ET.SubElement(root, k)
        child.text = str(v)
    ET.ElementTree(root).write(filename,
                               encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    back = {child.tag: child.text for child in root}
    return back
