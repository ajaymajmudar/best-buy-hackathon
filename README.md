# best-buy-project-week

Please view slide deck for presentation of problem statement, EDA process, feature engineering, model selection, model refinement, and model results!

Repo structure

```
.
├── EDA_Best_Buy.ipynb
├── modeling-final.ipynb
└── feature_engineering
    ├── inventory_features.py
    ├── price_features.py
    └── time_features.py
```

`feature_engineering/*`: Folder containing sklearn's transformer classes that are used for data pipeline, enable easy contribution of team members. Within each file, the class inherited from `sklearn.base.TransformerMixin` then define `fit()` and `transform` method.

`EDA_Best_Buy.ipynb`: The EDA_Best_Buy files contains the exploratory Data Analysis to discover the relationships between time, price, inventory, category of items.

`modeling-final.ipynb`: Contain our final models, including:
    - Import library and data
    - Add feature - Data enrichment using sklearn's pipeline
    - Formulating the regression problem: Define the `labels` dataset of shape `(num_cutoff_day * num_sku, 7)`. Cutoff days are every Monday in the last 1 year. Also we cut the train-valid-test datasets by date so that there are no information leakage.
    - Feature engineering: Calculate features for the training data. We are carefull to use only data in the pass of the cutoff_day.
    - Modeling: Model training and tuning based on the train and valid set (data up to `2022-07-31`).
    - Evaluate model performance: Calculate RMSE of the models on the test set (data from Best Buy's `Validation_Data.xlsx` - after `2022-08-01`).
