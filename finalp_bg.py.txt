import ultrasonic as u
import main

while True:
        try:

                with open(pagecheck.txt) as f: f.write(u.detect_page())

                with open(scancheck.txt) as f:
                        x = int(f.read())
                        if x:
                                with open(pagesize.txt) as f:
                                        data = f.read()
                                main.main(data["width"],data["length"])
                                f[0] = 0
        except:
                pass
