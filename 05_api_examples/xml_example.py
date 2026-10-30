import xml.etree.ElementTree as ET

xml_data = '''
<person>
    <name>Anna</name>
    <age>24</age>
    <address>
        <street>Saarstraße 123</street>
        <city>Mainz</city>
        <postalCode>55122</postalCode>
    </address>
    <hobbies>
        <hobby>Lesen</hobby>
        <hobby>Radfahren</hobby>
        <hobby>Schwimmen</hobby>
    </hobbies>
</person>
'''

root = ET.fromstring(xml_data)

name = root.find('name').text
age = root.find('age').text
city = root.find('./address/city').text  
first_hobby = root.findall('./hobbies/hobby')[0].text

print(f"Name: {name}")
print(f"Alter: {age}")
print(f"Stadt: {city}")
print(f"Erstes Hobby: {first_hobby}")
