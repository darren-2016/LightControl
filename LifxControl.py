############################################################
# LIFX Controller
# Application for remote control of LIFX LED lighting
#
# D.J.Draper 2018

import sys
import requests
import authorisation
import time

WHITE = "white"
RED = "red"
ORANGE = "orange"
YELLOW = "yellow"
CYAN = "cyan"
GREEN = "green"
BLUE = "blue"
PURPLE = "purple"
PINK = "pink"


token = authorisation.token

headers = { "Authorization" : "Bearer %s" % token,
}



def switchOn():
    payload = {
        "power": "on",
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)


def switchOff():
    payload = {
        "power": "off",
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)


def setColour(colour):
    payload = {
        "color" : colour,
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)


def setBrightness(brightness):
    print "Brightness = " + str(brightness)
    payload = {
        "brightness" : brightness,
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)


def breath():
    payload = {
        "period": 2,
        "cycles": 5,
        "color": "green",
    }

    response = requests.post('https://api.lifx.com/v1/lights/all/effects/breathe', data=payload, headers=headers)


def main(argv):
    response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)

    print response.status_code

    print response.url

    print response.text

    switchOn()

    setColour(BLUE)

    breath()


    #setBrightness(0.0)

    switchOn()
    for b in range(1, 10):
        c = float(b/10.0)
        setBrightness(c)
        time.sleep(1)
        print c



################################################################################
# Main entry point
#
if __name__ == "__main__":
    main(sys.argv[1:])
