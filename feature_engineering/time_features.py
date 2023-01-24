import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

class TimeFeatures(TransformerMixin):
    def __init__(self, time_column, time_format='%Y-%m-%d'):
        self.time_column = time_column
        self.time_format = time_format
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_copy = X.copy()
        cal = calendar()
        dt_series = pd.to_datetime(X[self.time_column], format=self.time_format)
        cal = calendar()
        holidays = cal.holidays(start=dt_series.min(), end=dt_series.max())
        X_copy["holidays"] = dt_series.isin(holidays).astype(int)
        X_copy['year'] = dt_series.dt.year
        X_copy['month'] = dt_series.dt.month
        X_copy['day'] = dt_series.dt.day
        X_copy['dayofweek'] = dt_series.dt.dayofweek
        X_copy["weekofyear"] = dt_series.dt.isocalendar().week
        X_copy["quarter"] = dt_series.dt.quarter
        X_copy["is_weekend"] = X_copy["dayofweek"].apply(lambda x: 1 if x in [5,6] else 0)
        return X_copy

