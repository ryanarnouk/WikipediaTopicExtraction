import xml.etree.ElementTree as ET
import codecs 
import re

tree = ET.parse('simplewiki-20170201-pages-articles-multistream.xml')
root = tree.getroot()
path = 'articles//'
url = '{http://www.mediawiki.org/xml/export-0.10/}page'
file = path + "articles.txt"

def is_ascii(s): 
    return all(ord(c) < 128 for c in s)

for i, page in enumerate(root.findall(url)): 
    for p in page: 
        r_tag = "{http://www.mediawiki.org/xml/export-0.10/}revision"
        if p.tag == r_tag: 
            for x in p: 
                tag = "{http://www.mediawiki.org/xml/export-0.10/}text"
                if x.tag == tag: 
                    text = x.text
                    if not text == None: 
                        text = text[:text.find("==")]
                        text = re.sub(r"{{.*}}","",text)
                        text = re.sub(r"\[\[File:.*\]\]","",text)
                        text = re.sub(r"\[\[Image:.*\]\]","",text)
                        text = re.sub(r"\n: \'\'.*","",text)
                        text = re.sub(r"\n!.*","",text)
                        text = re.sub(r"^:\'\'.*","",text)
                        text = re.sub(r"&nbsp","",text)
                        text = re.sub(r"http\S+","",text)
                        text = re.sub(r"\d+","",text)   
                        text = re.sub(r"\(.*\)","",text)
                        text = re.sub(r"Category:.*","",text)
                        text = re.sub(r"\| .*","",text)
                        text = re.sub(r"\n\|.*","",text)
                        text = re.sub(r"\n \|.*","",text)
                        text = re.sub(r".* \|\n","",text)
                        text = re.sub(r".*\|\n","",text)
                        text = re.sub(r"{{Infobox.*","",text)
                        text = re.sub(r"{{infobox.*","",text)
                        text = re.sub(r"{{taxobox.*","",text)
                        text = re.sub(r"{{Taxobox.*","",text)
                        text = re.sub(r"{{ Infobox.*","",text)
                        text = re.sub(r"{{ infobox.*","",text)
                        text = re.sub(r"{{ taxobox.*","",text)
                        text = re.sub(r"{{ Taxobox.*","",text)
                        text = re.sub(r"\* .*","",text)
                        text = re.sub(r"<.*>","",text)
                        text = re.sub(r"\n","",text)  
                        text = re.sub(r"\!|\"|\#|\$|\%|\&|\'|\(|\)|\*|\+|\,|\-|\.|\/|\:|\;|\<|\=|\>|\?|\@|\[|\\|\]|\^|\_|\`|\{|\||\}|\~"," ",text)
                        text = re.sub(r" +"," ",text)
                        text = text.replace(u'\xa0', u' ')
                            
                        if not text == None and not text == "" and len(text) > 150 and is_ascii(text):
                            append = '\n' + text + '\n'
                            appendFile = open(file, 'a')
                            appendFile.write(append)
                            print(text)
                            print('\n=========================================\n')
