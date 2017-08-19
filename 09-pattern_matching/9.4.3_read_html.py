'''
Parse abstracts from PubMed HTML pages.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 9.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
# Python2 Fixed in Python3
import urllib.request as urllib2
import re

pmid = '18235848'
url = 'http://www.ncbi.nlm.nih.gov/pubmed?term=%s' % pmid
handler = urllib2.urlopen(url)
html = handler.read()
# added for python 3
html = html.decode('utf-8')

title_regexp = re.compile('<h1>.{5,400}</h1>')
title_text = title_regexp.search(html)
abstract_regexp = re.compile('<h3>Abstract</h3><div class=""><p><AbstractText>.{20,3000}</AbstractText></p></div>')
abstract_text = abstract_regexp.search(html)

print(url)
print('TITLE:', title_text.group())
print('ABSTRACT:', abstract_text.group())
