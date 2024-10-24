import pandas as pd


def modifying_data(data):

    df = pd.read_csv(data)

    df.drop('Id', axis=1, inplace=True)

    print('Before Encoding: ')
    print(df.head())

    zoning_encoded = pd.get_dummies(df['MSZoning'], prefix='MSZoning', dtype=int)

    df = pd.concat([df, zoning_encoded], axis=1)

    df.drop('MSZoning', axis=1, inplace=True)

    print('After Encoding: ')
    print(df.head())

    return df

