#!/usr/bin/env python3

import requests
import datetime

URL = "http://api.open-notify.org/iss-now.json"

def main():
    iss  = requests.get(URL).json()

    # print(iss)

    longitude = iss["iss_position"]["longitude"]
    latitude = iss["iss_position"]["latitude"]
    
    ts = iss["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts)

    print("The ISS is at: ","At time: ", {ts}, "longitude: ", {longitude}, "latitude: ", {latitude})

if __name__ == "__main__":
    main()
