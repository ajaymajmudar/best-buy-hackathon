import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin

class PriceFeatures(TransformerMixin):
    def __init__(self, 
        ret_col = "retail_price", 
        pro_col = "promo_price", 
        com_col = "competitor_price"
        ):
        self.ret_col = ret_col
        self.pro_col = pro_col
        self.com_col = com_col
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_copy = X.copy()
        X_copy["real_price"] = X_copy[self.pro_col].apply(lambda x: float(x) if x != "?" else np.nan)
        X_copy["real_price"] = X_copy["real_price"].fillna(X_copy[self.ret_col])
        X_copy[self.com_col] = X_copy[self.com_col].apply(lambda x: float(x) if x != "?" else np.nan)
        X_copy["price_com_diff"] = X_copy["real_price"] - X_copy[self.com_col]
        X_copy["price_com_diff_pct"] = X_copy["real_price"] / X_copy[self.com_col] - 1
        X_copy["promo_cleaned"] = X_copy[self.pro_col].apply(lambda x: float(x) if x != "?" else np.nan)
        X_copy['comp_cleaned'] = X_copy[self.com_col].apply(lambda x: float(x) if x != "?" else np.nan)
        X_copy['has_comp'] = np.where(X_copy['comp_cleaned'].isnull(), 0, 1)
        X_copy['has_promo'] = np.where(X_copy['promo_cleaned'].isnull(), 0, 1)
        return X_copy
    

