import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

def train_model():
    df = pd.read_csv('datasets/cancer_diagnosis_data.csv')
    df["Gender"] = df["Gender"].replace({"Male": 1, "Female": 0})
    df["Biopsy_Result"] = df["Biopsy_Result"].replace({"Positive": 1, "Negative": 0})
    df["Treatment"] = df["Treatment"].replace({"Surgery": 0, "Radiation Therapy": 1, "Chemotherapy": 2})
    df["Response_to_Treatment"] = df["Response_to_Treatment"].replace({"No Response": 0, "Complete Response": 1, "Partial Response": 2})

    X = df[["Age", "Gender", "Tumor_Size(cm)", "Biopsy_Result", "Treatment", "Response_to_Treatment"]]
    y = df["Survival_Status"]

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    # Save the trained model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

def predict(input_data):
    # Load the trained model
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model.predict(input_data).tolist()

