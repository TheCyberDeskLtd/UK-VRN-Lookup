#Created by The Cyber Desk Ltd with the purpose of making vehicle lookups more efficient.

import requests
from requests.structures import CaseInsensitiveDict
import json
import webbrowser
import os
import random
import sys

print (r"""\

                                                         _________________________   
                    /\\      _____          _____       |   |     |     |    | |  \  
     ,-----,       /  \\____/__|__\_    ___/__|__\___   |___|_____|_____|____|_|___\ 
  ,--''---:---`--, /  |  _     |     `| |      |      `| |                    | |    \
 ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)''   `--(o)(o)--------------(o)--''  
`````````````````````````````````````````````````````````````````````````````````````

There's a great joke below. Have a wonderful day!

    """)

jokes = ['Who can drive all of their customers away and still make money? Taxi Drivers',
         'What did the tornado say to the car? Want to go for a spin?',
         'What car brand does baby Yoda drive? Toyoda',
         'A man in New York drove his Benz into a wall. He wanted to see how the Mercedes Bends',
         'What do you call a Ford Fiesta without fuel? Ford Siesta',
         'What happens when a frog’s car breaks down? It gets toad away',
         'A frog’s car broke down in the middle of the road. He had to jump-start it again',
         'My 8 years old daughter asked if I can make a car out of spaghetti. I wish you saw the look on her face when I drive pasta.',
         'Which snake species are found on cars? Windscreen vipers',
         'Snakes used to drive cars in the past. Ana-Honda is was their favorite car brand.'
         ]

print(random.choice(jokes))

print(" ")

def mainpart():

    return again()

def again():
    while True:
        vrn = input('Enter the VRN:')

        if len(sys.argv) > 1:

            opt = str(sys.argv[1])

        else :
            opt = ''

        url = "https://beta.check-mot.service.gov.uk/trade/vehicles/mot-tests?registration=" + vrn

        headers = CaseInsensitiveDict()
        headers["x-api-key"] = ""

        resp = requests.get(url, headers=headers)

        if resp.status_code == 200:
            
            datas = json.loads(resp.text)

            print(" ")
            print (datas[0]["make"] + ',' + datas[0]["model"] + ',' + datas[0]["primaryColour"])
            print(" ")

            #print(datas[0]["motTests"][0]["motTestNumber"])
            #print(resp['make'])
            if opt != 's':
                
                f = open('C:\\Temp\\vehicles.html','w')

                html_page = """<html><h1><ul><li>""" + 'Make/Brand: ' + datas[0]["make"] + '<li>' + 'Model: ' + datas[0]["model"] + '<li>' + 'Colour: ' + datas[0]["primaryColour"] + """</h1>
                <iframe id="if1" width="100%" height="1000" style="visibility:visible" src="https://www.bing.com/images/search?q=""" + datas[0]["make"] + ' ' + datas[0]["model"] + ' ' + datas[0]["primaryColour"] + """&form=HDRSC3&first=1&tsc=ImageHoverTitle"></iframe>
                </html>"""

                f.write(html_page)
                f.close()

                webbrowser.open('C:\\Temp\\vehicles.html')

                return again ()
            else :
                return again()
    
        else :

            print ("VRN not found. Please try again.")

            return again()

mainpart()
