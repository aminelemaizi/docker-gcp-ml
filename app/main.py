# this is just a dummy example,
# focus on how we load and write data from and to the bucket

# importing the necessary libraries
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from google.cloud import storage


# function to load train data from the bucket
def load_train_data():
    storage_client = storage.Client()
    train_file = open("train_iris.csv", "wb")
    # the 'gs://iris_ml_bucket/iris.csv' represents the bucket file path 
    storage_client.download_blob_to_file("gs://iris_ml_bucket/iris.csv", train_file)
    train_file.close()

# training our dummy model and saving it as a pickle
def train_model():
    data = pd.read_csv("train_iris.csv")
    X = data.drop(columns=['Id', 'Species'])
    le = LabelEncoder()
    y = le.fit_transform(data['Species'])
    dt = DecisionTreeClassifier()
    dt.fit(X, y)
    filename = "model.pkl"
    with open(filename, 'wb') as file:
        pickle.dump(dt, file)
        file.close()

# write the saved model to the bucket
def save_model():
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('iris_ml_bucket')
    blob = bucket.blob("trained_model.pkl")
    blob.upload_from_filename('model.pkl')


if __name__ == "__main__":
    load_train_data()
    train_model()
    save_model()
