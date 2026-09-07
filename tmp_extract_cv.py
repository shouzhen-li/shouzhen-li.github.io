import zipfile
import xml.etree.ElementTree as ET

path = r'd:\个人主页\minimal-academic-homepage-main\李守真履历.docx'
with zipfile.ZipFile(path) as z:
    root = ET.fromstring(z.read('word/document.xml'))

ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
texts = []
for p in root.findall('.//w:p', ns):
    s = ''.join((t.text or '') for t in p.findall('.//w:t', ns)).strip()
    if s:
        texts.append(s)

for i, s in enumerate(texts, 1):
    print(f'{i}: {s}')
