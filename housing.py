import os
import tarfile
import pandas as pd
import numpy as np
import hashlib
from matplotlib import pyplot as plt
from six.moves import urllib
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from pandas.tools.plotting import scatter_matrix
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()

'''housing.hist(bins=50, figsize=(20,15)) ADAT ÁBRÁZOLÁS
plt.show()''' 

train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42) #test set készítése

housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)

housing = strat_train_set.copy()

housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1) #a házak elhelyezkedése ábrázolva
plt.show()

housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,            #házak árai ábrázolva
            s=housing["population"]/100, label="population", figsize=(10,7),    #
            c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,)   #
plt.legend()
plt.show()

corr_matrix = housing.corr()                                            #összefüggések vizsgálata
corr_matrix["median_house_value"].sort_values(ascending=False)          #
                                                                        #
attributes = ["median_house_value", "median_income", "total_rooms",     #
"housing_median_age"]                                                   #  
scatter_matrix(housing[attributes], figsize=(12, 8))                    #

housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

imputer = Imputer(strategy="median") #hiányzó adatok kiegészítése

housing_num = housing.drop("ocean_proximity", axis=1)
imputer.fit(housing_num)
X = imputer.transform(housing_num)

housing_tr = pd.DataFrame(X, columns=housing_num.columns) #numpy array to pandas dataFrame

encoder = LabelEncoder() #szöveg számmá alakítás
housing_cat = housing["ocean_proximity"]
housing_cat_encoded = encoder.fit_transform(housing_cat)
encoder = OneHotEncoder() 
housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1,1))

housing_cat_1hot.toarray()
