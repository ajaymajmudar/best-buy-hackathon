import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin

class InventoryFeatures(TransformerMixin):
    def __init__(self,
        inv_col="inventory"
        ):
        self.inv_col = inv_col

    def fit(self, X, y=None):
        self.inv_status = X[self.inv_col].unique()
        return self

    def transform(self, X):
        X_copy = X.copy()
        for status in self.inv_status:
            X_copy[f"inv_{status.lower()}"] = X_copy[self.inv_col].apply(lambda x: 1 if x == status else 0)
        return X_copy