import re
import sys
import fileinput

#Argument for directory path:  link_sanitizer.py <file>
san_file = sys.argv[1]

#this takes the file, inplace corrects fileinput from adding a line.
#Regexes ip addresses and replaces . with [.]
for line in fileinput.input(san_file, inplace=1):
    #The ^ and $ at begiining and end of search makes only exact matches acceptable
    ip_san = re.sub(r"^(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})$",r"\1[.]\2[.]\3[.]\4",line.rstrip())
    print(ip_san)

#this replaces http with hxxp
for line in fileinput.input(san_file, inplace=1):
    http_san = re.sub('http','hxxp',line.rstrip(),flags=re.I)
    print(http_san)