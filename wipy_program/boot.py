import machine
from network import WLAN
from ws2812 import WS2812
import time
wlan = WLAN(mode=WLAN.STA) # get current object, without changing the mode

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('wifi', auth=(WLAN.WPA2, 'password'), timeout=5000)
    print('Network Found..')

    while not wlan.isconnected():
        chain = WS2812(ledNumber=5)
        data = [
            (0, 0, 255),
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            ]
        chain.show(data)
        time.sleep(0.1)
        chain = WS2812(ledNumber=5)
        data = [
            (0, 0, 0),
            (0, 0, 255),
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            ]
        chain.show(data)
        time.sleep(0.1)
        chain = WS2812(ledNumber=5)
        data = [
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 255),
            (0, 0, 0),
            (0, 0, 0),
            ]
        chain.show(data)
        time.sleep(0.1)
        chain = WS2812(ledNumber=5)
        data = [
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 255),
            (0, 0, 0),
            ]
        chain.show(data)
        time.sleep(0.1)
        chain = WS2812(ledNumber=5)
        data = [
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 0),
            (0, 0, 255),
            ]
        chain.show(data)
        time.sleep(0.1)
