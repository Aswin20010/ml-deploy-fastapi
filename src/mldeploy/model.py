import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent / "iris_model.pkl"


def train_and_save_model():
    """Train a simple Logistic Regression model on Iris dataset and save it."""
    iris = load_iris()
    X, y = iris.data, iris.target
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)


def load_model():
    """Load the trained model, train and save if not exists."""
    if not MODEL_PATH.exists():
        train_and_save_model()
    return joblib.load(MODEL_PATH)
