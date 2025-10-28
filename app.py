import joblib
import re
from pathlib import Path 
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from flask import Flask, request, jsonify, render_template


# 1. Initialize Flask app and Load Resources:

app = Flask(__name__)


# Ensure templates directory exists and is configured

# --- FIX 1: Robust Pathing for MLOps ---
BASE_DIR = Path(__file__).parent 
MODEL_PATH = BASE_DIR / 'models' / 'sentiment_model.pkl'
VECTORIZER_PATH = BASE_DIR / 'models' / 'vectorizer.pkl'
# --- End Robust Pathing Fix ---

# Download NLTK stopwords (only if needed)
try:
    nltk.data.find('corpora/stopwords')
except nltk.downloader.DownloadError:
    nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Load the trained model and vectorizer using robust paths
try:
    MODEL = joblib.load(MODEL_PATH) 
    vectorizer_obj = joblib.load(VECTORIZER_PATH)
    
    # Check if the loaded object is actually a vectorizer or just a matrix
    if hasattr(vectorizer_obj, 'transform'):
        VECTORIZER = vectorizer_obj
        print("Models and Vectorizer loaded successfully using robust paths!")
    else:
        print(f"ERROR: Vectorizer file contains {type(vectorizer_obj)} instead of a vectorizer object.")
        print("The vectorizer.pkl file needs to be regenerated with the actual TfidfVectorizer object.")
        MODEL = None
        VECTORIZER = None
except Exception as e:
    print(f"CRITICAL ERROR: Failed to load models. Check paths: {MODEL_PATH} and {VECTORIZER_PATH}. Error: {e}")
    MODEL = None
    VECTORIZER = None


# 2. Preprocessing Function:
def preprocess_txt(txt):
    if not isinstance(txt, str):
        return ""
    txt = txt.lower()
    txt = re.sub(r'[^\w\s]', '', txt)
    tokens = txt.split()
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [stemmer.stem(word) for word in tokens]
    return " ".join(tokens)

# 3. Prediction Function:
# 3. Prediction Function:
def predict_sentiment(raw_text):
    if not MODEL or not VECTORIZER:
        raise Exception("Prediction error: Model or vectorizer not available.")
    
    # Check if vectorizer has transform method
    if not hasattr(VECTORIZER, 'transform'):
        raise Exception("Prediction error: Vectorizer is not properly configured.")
        
    cleaned_text = preprocess_txt(raw_text)
    
    try:
        text_vectorized = VECTORIZER.transform([cleaned_text])
        
        # Get prediction and probabilities
        prediction = MODEL.predict(text_vectorized)[0] 
        prediction_proba_array = MODEL.predict_proba(text_vectorized)[0] 
        
        # Convert to standard Python types
        scalar_prediction = int(prediction) 
        sentiment_label = "Positive" if scalar_prediction == 1 else "Negative"
        positive_probability = float(prediction_proba_array[1]) 
        
        return sentiment_label, positive_probability
        
    except Exception as e:
        raise Exception(f"Prediction error during transformation or prediction: {str(e)}")

# 4. Flask Routes:
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if MODEL is None or VECTORIZER is None:
        return jsonify({'error': 'Prediction service is unavailable: The vectorizer model file is corrupted and needs to be regenerated. Please retrain the model.'}), 500
        
    text_input = request.form.get('text_input', '')

    if not text_input:
        return jsonify({'Error': 'Please enter some text for Analysis.'}), 200

    try:
        sentiment, probability = predict_sentiment(text_input)
        return render_template('index.html', prediction=sentiment, 
                               confidence=f"{probability*100:.2f}%")
    except Exception as e:
        app.logger.error(f"Prediction failed: {e}")
        if "not fitted" in str(e).lower():
            return jsonify({'Error': 'Model configuration error: The vectorizer needs to be retrained. Please regenerate the model files.'}), 500
        else:
            return jsonify({'Error': 'An error occurred during prediction. Check server logs.'}), 500

# 5. Run the Application:
if __name__ == '__main__':
    app.run(debug=True)