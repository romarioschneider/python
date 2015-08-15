#!/usr/bin/python3

import sys
import xml.sax.saxutils

def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = 'lightgreen'
            elif count % 2:
                color = 'white'
            else:
                color = 'lightyellow'
            print_line(line, color, maxwidth)
            count += 1
        except EOFError:
            break
    print_end()
    
def process_options():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print("usage:\n {0} [maxwidth=int] [format=str] < infile.csv > outfile.html".format(sys.argv[0]))
        return (None, None)
    elif (sys.argv) == 1:
        
    
def print_start():
    print("<table border='1'>")
        
def print_end():
     print("</table>")
        
def print_line(line, color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                field = xml.sax.saxutils.escape(field)
                if len(field) <= maxwidth:
                    print("<td>{0}</td>".format(field))
                else:
                    print("<td>{0:.{1}} ...".format(field, maxwidth))
    print("</tr>")
        
def extract_fields(line):
    fields = list()
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:
                quote = c
            elif quote == c:
                 quote = None
            else:
                field += c
            continue
            
        if quote is None and c == ",":
            fields.append(field)
            field = ""
        else:
            field += c
    if field:
        fields.append(field)
        
    return fields
    
main()