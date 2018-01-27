# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:23:14 2018

@author: navya
"""

from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start:", tag)
        for k,v in (attrs):
            print("->", k,">",v )

    def handle_endtag(self, tag):
        print ("End:", tag)

    def handle_startendtag(self, tag, attrs):
        print ("Empty:", tag)
        for k,v in (attrs):
            print("->", k,">",v )
for i in range(int(input())):
    parser=MyHTMLParser()
    parser.feed(input())
    
    