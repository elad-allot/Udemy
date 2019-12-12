import pandas as pd
from PandasBootCamp.csv_files import get_path_for_file as get_path

titanic = pd.read_csv(get_path("titanic.csv"))

# print(titanic)

# print(titanic.head(n=10))
# print(titanic.tail(n=10))

# print(titanic.index)
# print(titanic.columns)
# titanic_info = titanic.info()

# print(titanic.shape)
print(titanic.describe())
# print(titanic.min())
# print(bla)
# print(type(titanic))
#
# print(titanic.to_dict(orient="index"))


# titanic.sort_values()
