# read data
from sklearn.datasets import load_boston
import pandas as pd
Boston = load_boston()
print(Boston.data.shape)
Boston.info()
type(Boston)
boston = pd.DataFrame(Boston.data)
boston.head()


