#!/usr/bin/python37all
import cgi,json
data = cgi.FieldStorage()

input_width=data.getvalue('width')
input_length=data.getvalue('length')
input_size={}
input_size={'width':input_width, 'length':input_length}

previous_size={}
with open('pagesize.txt', 'r') as pagesize:
    previous_size=json.load(pagesize)

with open('pagecheck.txt', 'r') as pagecheck:
    page_there=json.load(pagecheck)


if page_there==1:
    #START SCANNING
    if input_width is not None:
        with open('pagesize.txt', 'w') as pagesize:
            json.dump(input_size,pagesize)
        with open('scancheck.txt', 'w') as scancheck:
            json.dump(1,scancheck)
        print('Content-type: text/html\n\n')
        print('<html>')
        print('<meta http-equiv="refresh" content="30">')
        print("<body style='background-color:powderblue;text-align:center'>")
        print('<br><br>')
        print('<font size="10">')
        print('Scanning...<br>')
        print('<font size="6">')
        print('Latest Scan:<br>')
        print("<img src='\scan.jpg'>")
        print('<font size="4">')
        print('<br>Width (in.): ' + input_width + '<br>')
        print('Length (in.): '+input_length+ '<br><br>')
        print('<font size="5">')
        print('Your scan will be ready shortly!')
        print('</body>')
        print('</form>')
        print('</html>')

    else:
        with open('scancheck.txt', 'w') as scancheck:
            json.dump(1,scancheck)
        print('Content-type: text/html\n\n')
        print('<html>')
        print('<meta http-equiv="refresh" content="30">')
        print("<body style='background-color:powderblue;text-align:center'>")
        print('<br><br>')
        print('<font size="10">')
        print('Scanning...<br>')
        print('<font size="6">')
        print('Latest Scan:<br>')
        print("<img src='\scan.jpg'>")
        print('<font size="4">')
        print('<br>Width (in.): ' + previous_size['width'] + '<br>')
        print('Length (in.): '+previous_size['length']+ '<br><br>')
        print('<font size="5">')
        print('Your scan will be ready shortly!')
        print('</body>')
        print('</form>')
        print('</html>')
else:
    #SHOW NO PAGE THERE
    if input_width is not None:
        with open('pagesize.txt', 'w') as pagesize:
            json.dump(input_size,pagesize)
        width=input_width
        length=input_length
    else:
        width=previous_size['width']
        length=previous_size['length']
    print('Content-type: text/html\n\n')
    print('<html>')
    print("<body style='background-color:powderblue;text-align:center'>")
    print('<form action="/cgi-bin/finalp.cgi" method="POST">')
    print('<br><br><br><br><br><br><br><br><br><br>')
    print('<font size="10">')
    print("There's no page there!<br>")
    print('<font size="4">')
    print('<br>Width (in.): ' + width + '<br>')
    print('Length (in.): '+length+ '<br><br><nr>')
    print('<font size="5">')
    print('Put a page down and try again!<br>')
    print('<input type="submit" value="Try Again"/>')
    print('</body>')
    print('</form>')
    print('</html>')



    #print('<form action="/cgi-bin/finalp.cgi" method="POST">')
    #print('Input page size:<br><br>')
    #print('Width (in.): &nbsp<input type="text" name="width"><br>')
    #print('Length (in.): <input type="text" name="length"><br><br>')
    #print('<input type="submit" value="Scan"/>')
