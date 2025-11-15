# 🌸 **Iris Flower Classification – Machine Learning Project**

This project is an end-to-end Machine Learning application that classifies **Iris flower species** based on four input features:

* **Sepal Length (cm)**
* **Sepal Width (cm)**
* **Petal Length (cm)**
* **Petal Width (cm)**

The model predicts one of the following species:

* **Iris-setosa**
* **Iris-versicolor**
* **Iris-virginica**

This project includes:

* Data preprocessing
* Model training
* Model evaluation
* Saving ML model
* Streamlit web application
* Ready-to-use test values

---

## 📁 **Project Structure**

```
Iris-Classification/
│── Iris.csv
│── train_model.py
│── app.py
│── iris_model.pkl
│── scaler.pkl
│── README.md
│── requirements.txt
```

---

## 📦 **Requirements**

Install all required libraries:

```bash
pip install numpy pandas scikit-learn streamlit joblib
```

---

## 🧠 **1. Model Training (`train_model.py`)**

This script:

✔ Reads `Iris.csv`
✔ Preprocesses the data
✔ Splits into train/test
✔ Trains RandomForestClassifier
✔ Evaluates accuracy
✔ Saves model & scaler (`iris_model.pkl` and `scaler.pkl`)

Run training:

```bash
python train_model.py
```

After running, you will see accuracy and model files will be created.

---

## 🖥 **2. Streamlit Application (`app.py`)**

This web app allows users to enter flower measurements and get a prediction instantly.

Run the application:

```bash
streamlit run app.py
```

Open the link shown in the terminal to use the app.

---

## 🌼 **3. Test Values for Prediction**

### ✔ Setosa

```
SepalLength: 5.1
SepalWidth: 3.5
PetalLength: 1.4
PetalWidth: 0.2
```

### ✔ Versicolor

```
SepalLength: 6.0
SepalWidth: 2.9
PetalLength: 4.5
PetalWidth: 1.5
```

### ✔ Virginica

```
SepalLength: 6.5
SepalWidth: 3.0
PetalLength: 5.8
PetalWidth: 2.2
```

---

## 📊 **4. Model Details**

* Algorithm: **RandomForestClassifier**
* Accuracy: ~97%–100%
* Dataset size: **150 rows**
* Classes: **3**

---

## 🚀 Deployment Options

You can deploy this app on:

* **Streamlit Cloud** (easiest)
* **Render.com** (free)
* **Heroku**
* **AWS EC2 / Azure VM**
* **Docker**

---

## 📝 **5. How to Contribute**

Feel free to:

* Add new ML models
* Improve UI design
* Convert app into API using FastAPI
* Add visualizations

---

## ❤️ **6. Author**

**Srinivas**
Iris Flower Classification – ML Project
Built using Python, Scikit-learn, and Streamlit
