import pandas as pd
import xml.etree.ElementTree as ET
import lxml

tree = ET.parse("patinfo.xml")
root = tree.getroot()

df = pd.read_xml('patinfo.xml')
print(df)