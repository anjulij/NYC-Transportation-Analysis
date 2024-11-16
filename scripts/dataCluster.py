import pandas as pd


def dataCleaner():
    # This data frame takes the columns we need to analyize within the k-means method, ridership, latitude and longitude.
    df = pd.read_csv("NYC-Public-Transport-Analysis/data/samples/mta_subway_sample.csv", usecols=['ridership', 'latitude', 'longitude'])

    df.to_csv("NYC-Public-Transport-Analysis/data/samples/reduced_data.csv")
