import pandas as pd
def func(num):
    return pd.DataFrame({'col1':[i for i in range(num)],'col2':['main' for i in range(num)]})