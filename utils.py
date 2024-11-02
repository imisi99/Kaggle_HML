import pandas as pd
import numpy as np


def modifying_data(data):
    df = pd.read_csv(data)

    print('data before processing...')
    print(df.head())
    # Drop 'Id' column
    df = df.drop(columns=['Id'])

    # Convert 'NA' values in specific columns to np.nan
    missing_value_cols = [
        'Alley', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1',
        'BsmtFinType2', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual',
        'GarageCond', 'PoolQC', 'Fence', 'MiscFeature'
    ]
    for col in missing_value_cols:
        df[col] = df[col].replace('NA', np.nan)

    # Using the median to fill NaNs in numerical columns
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        median = df[col].median()
        df[col] = df[col].fillna(median)

    # Drop unused columns
    drop_columns = [
        'Street', 'Alley', 'LandContour', 'LandSlope', 'Condition1', 'Condition2',
        'YearRemodAdd', 'RoofStyle', 'RoofMatl', 'Exterior2nd', 'MasVnrType',
        'Foundation', 'BsmtExposure', 'BsmtFinType2', 'BsmtFinSF2', 'Heating',
        'HeatingQC', 'CentralAir', 'Electrical', 'LowQualFinSF', 'KitchenQual',
        'Functional', 'FireplaceQu', 'GarageYrBlt', 'GarageArea', 'GarageQual',
        'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch',
        '3SsnPorch', 'ScreenPorch', 'PoolQC', 'MiscVal', 'MoSold', 'YrSold',
        'SaleType', 'SaleCondition', 'MSZoning', 'MSSubClass', 'LotShape', 'Utilities', 'LotConfig',
        'Neighborhood', 'BldgType', 'HouseStyle', 'Exterior1st', 'ExterQual',
        'ExterCond', 'BsmtQual', 'BsmtCond', 'BsmtFinType1', 'GarageType',
        'GarageFinish', 'Fence', 'MiscFeature'
    ]
    df = df.drop(columns=drop_columns, errors='ignore')

    print("Data after preprocessing:")
    print(df.head())

    return df
