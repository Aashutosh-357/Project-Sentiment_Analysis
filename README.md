# 🧠 MLOps Portfolio Project: Sentiment Analysis MVP

![Status](https://img.shields.io/badge/status-Deployed-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--learn-87%25%20Accuracy-orange?logo=scikit-learn)

---

## 🚀 Overview

This **Minimum Viable Product (MVP)** demonstrates an end-to-end **Machine Learning Operations (MLOps)** lifecycle by deploying a trained sentiment analysis model via a robust **Flask API** and a simple web interface. 
The primary goal of this project is to showcase production readiness, robust dependency management, and preparedness for containerization and cloud deployment.

### Problem Solved
This tool quickly analyzes and classifies text input (e.g., customer reviews, feedback) as either positive or negative, providing an instant sentiment score and showcasing a deployed, working ML pipeline.

---

## ✨ Features

* **End-to-End MLOps Pipeline:** Demonstrates training, serialization, and deployment of an ML model.
* **Production-Ready API:** Uses **Flask** served by **Gunicorn** for a performant and scalable API.
* **Robust Preprocessing:** Includes stop word removal and Porter stemming.
* **High Accuracy:** Utilizes a **Logistic Regression** classifier achieving approximately **87% accuracy** on the IMDB reviews dataset.
* **Reproducibility:** Strict dependency management via `requirements.txt` and environment isolation using Python `venv`.
* **Live Deployment:** The application is live and accessible via a modern PaaS.

---

## 🌐 Live Demo

The application is deployed and can be tested live at the link below:

* **Live Deployment Link:** [https://project-sentiment-analysis.onrender.com](https://project-sentiment-analysis.onrender.com)

---

## 🛠️ Tech Stack

This project leverages key tools for building a production-grade machine learning application.

* **Primary Language:** Python (3.8+)
* **ML Frameworks:** Scikit-Learn, NumPy
* **Web Framework:** Flask
* **Production Server:** Gunicorn
* **Deployment:** Render (PaaS)
* **Dependency Management:** `requirements.txt`

---

## 📦 Installation & Local Setup

Follow these steps to get a local copy up and running on your machine.

### Prerequisites

* **Python** version 3.8 or higher.
* **Git** for cloning the repository.

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Aashutosh-357/Project-Sentiment-Analysis
    cd Project-Sentiment-Analysis
    ```

2.  **Create and Activate Virtual Environment**
    ```bash
    # Create the venv
    python3 -m venv venv

    # Activate the venv (Linux/macOS)
    source venv/bin/activate
    
    # Activate the venv (Windows)
    # .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    Install all required libraries, ensuring the correct `scikit-learn` version for model compatibility.
    ```bash
    python -m pip install -r requirements.txt
    ```

4.  **Run the Application**
    Start the Flask server using the Python executable inside your active virtual environment.
    ```bash
    python app.py
    ```
    The application will be accessible locally at `http://127.0.0.1:5000/`.

---

## 🎯 Usage

Once the server is running, the main interface is the web page at `/` where you can input text.

### Example Interaction

You can use a tool like **`curl`** or **Postman** to hit the prediction API endpoint (`/predict`).

```bash
# Example API call to the local server
curl -X POST [http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict) \
     -H "Content-Type: application/json" \
     -d '{"text": "This movie was absolutely phenomenal and the acting was superb!"}'
````

**Expected JSON Response:**

```json
{
  "text": "This movie was absolutely phenomenal and the acting was superb!",
  "prediction": "Positive",
  "probability": 0.957
}
```

-----

## 🗂️ Project Structure

The repository follows a clean structure focusing on production readiness:

```
Project-Sentiment-Analysiss/
├── models/                   # Contains serialized ML assets (model.pkl, vectorizer.pkl)
├── app.py                    # Main Flask application and API entry point
├── templates/                # HTML files for the simple web interface
├── requirements.txt          # Defines all dependencies for reproducibility
├── Procfile                  # Gunicorn configuration for production deployment
└── README.md
```

-----

## 🤝 Contributing

We love your input\! While this is primarily a portfolio project, feel free to fork the repository and submit a pull request if you find a bug or have a suggestion for improvement.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'feat: Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.


-----

## 🐛 Bug Reports and Feature Requests

If you encounter any issues or have a suggestion, please open an issue on the GitHub repository.

-----

## 👥 Authors and Contact

This project was developed and is maintained by:

  * **Ashutosh Kumar Rai** - *Developer & Maintainer*
      * GitHub: [github.com/Aashutosh-357](https://www.google.com/search?q=https://github.com/Aashutosh-357/)
      * LinkedIn: [linkedin.com/in/ashutoshkr135/](https://www.google.com/search?q=https://linkedin.com/in/ashutoshkr135/)
      * Email: ashutoshkumarrai77@gmail.com

**Acknowledgments**

  * Inspired by classic NLP tutorials and best practices in MLOps deployment.

-----
