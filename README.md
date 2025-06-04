```markdown
# 🌸 Iris Flower Classifier

A simple web application built using **Django** and **Scikit-learn** that predicts the type of Iris flower based on four input features. This project uses a machine learning model trained on the Iris dataset to classify the flower as either **Versicolor** or **Virginica** (Setosa is excluded in this version).

---

## 🔍 Overview

This application demonstrates how machine learning models can be integrated into Django web applications. It includes:

- A trained classification model using `scikit-learn`
- A Django-powered web interface to input flower measurements
- A prediction displayed on the UI
- Styling using basic HTML and optional CSS frameworks like Tailwind

---

## 🧠 Machine Learning Model

The model is trained using the famous Iris dataset. Only two classes are used:

- **Versicolor**
- **Virginica**

### Features used:

- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

### Preprocessing:
- Feature scaling using `StandardScaler`
- Model trained with `Logistic Regression`
- Serialized using `joblib`

---

## 🚀 How It Works

1. User enters the 4 flower measurements in the form.
2. The Django backend takes the input and scales it using a fitted `StandardScaler`.
3. The ML model makes a prediction.
4. The result is displayed on the web page.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/iris-flower-classifier.git
cd iris-flower-classifier
````

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python manage.py runserver
```

---

## 🌐 Usage

1. Navigate to `http://127.0.0.1:8000/`
2. Enter the flower's sepal and petal measurements
3. Click **Predict**
4. View the predicted flower class (Versicolor or Virginica)

---

## 📷 Screenshots

Coming soon...

---

## 🛠 Technologies Used

* Python
* Django
* Scikit-learn
* HTML/CSS (Django templates)
* Joblib

---

## 🧑‍💻 Author

**Naeem Ahmed**
Full Stack Developer (Django + Flutter)
[GitHub](https://github.com/naeemahmed02) | [LinkedIn](#)

---

## 📜 License

This project is licensed under the MIT License.

```
```
