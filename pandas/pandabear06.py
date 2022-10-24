#!/usr/bin/env python3

"""Alta 3 | EGranillo | converting from json to csv"""

import pandas

def main():

    # create a dataframe from json
    df = pandas.red_json("5movies.json")

    # send dataframe to csv
    df.to_csv("5movies-translated-from-json.csv")

if __name__ == "__main__":
    main()

