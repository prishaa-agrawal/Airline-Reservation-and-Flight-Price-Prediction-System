import xgboost as xgb
import os
import json
import numpy as np

model_path = "models/price_model.json"
if os.path.exists(model_path):
    bst = xgb.Booster()
    bst.load_model(model_path)
    print(f"Model loaded from {model_path}")
    
    # Try predicting with various shapes
    for i in [3, 4, 5]:
        print(f"Testing with {i} features...")
        try:
            X = np.random.rand(1, i)
            d = xgb.DMatrix(X)
            p = bst.predict(d)
            print(f"  Success: {p}")
        except Exception as e:
            print(f"  Failure: {e}")
else:
    print("Model file not found!")
