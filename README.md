# 🎬 IMDB Movie Review Sentiment Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19-orange?style=for-the-badge&logo=tensorflow)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-LSTM-blueviolet?style=for-the-badge)

### Deep Learning-based Sentiment Analysis using LSTM and TensorFlow

Predict whether an IMDB movie review is **Positive 😊** or **Negative 😞** using a trained LSTM neural network.

🚀 **Live Demo:** https://imdb-movie-review-sentiment--analysis.streamlit.app/

</div>

---

# 📖 Overview

This project is an end-to-end **Natural Language Processing (NLP)** application that classifies movie reviews into **Positive** or **Negative** sentiments.

The model is built using **TensorFlow/Keras**, trained on the **IMDB Movie Review Dataset**, and deployed using **Streamlit Cloud**.

The project demonstrates the complete Deep Learning workflow:

- Data preprocessing
- Tokenization
- Sequence Padding
- LSTM Model
- Model Training
- Model Evaluation
- Streamlit Deployment

---

# ✨ Features

- 🎬 Predict sentiment of movie reviews
- 🤖 Deep Learning model using LSTM
- 📝 Text preprocessing pipeline
- ⚡ Real-time predictions
- 📊 Confidence score
- 🚀 Streamlit Web App
- 💾 Saved trained model
- 📦 Production-ready project structure

---

# 📊 Dataset

**Dataset:** IMDB Movie Reviews

- Total Reviews: **50,000**
- Positive Reviews: **25,000**
- Negative Reviews: **25,000**

Dataset Characteristics

- Balanced Dataset
- Binary Classification
- English Movie Reviews

---

# 🧠 Model Architecture

```
Input Review
      │
      ▼
Text Cleaning
      │
      ▼
Tokenizer
      │
      ▼
Sequence Padding
      │
      ▼
Embedding Layer
      │
      ▼
LSTM Layer
      │
      ▼
Dense Layer
      │
      ▼
Sigmoid Activation
      │
      ▼
Positive / Negative
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| TensorFlow | Deep Learning |
| Keras | Model Building |
| NumPy | Numerical Computing |
| Pandas | Data Analysis |
| Scikit-Learn | Data Processing |
| NLTK | NLP |
| Streamlit | Web Application |
| Pickle | Model Serialization |

---

# 📂 Project Structure

```
IMDB-Movie-Review-Sentiment-Analysis
│
├── Notebook/
│   └── IMDB_Sentiment_Analysis.ipynb
│
├── Models/
│   ├── imdb_lstm.keras
│   ├── tokenizer.pkl
│   └── label_encoder.pkl
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
└── LICENSE
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/mdzaheerjk/IMDB-Movie-Review-Sentiment-Analysis.git
```

Move inside the project

```bash
cd IMDB-Movie-Review-Sentiment-Analysis
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

# 🌐 Live Demo

👉 https://imdb-movie-review-sentiment--analysis.streamlit.app/

---

# 📸 Application Screenshots

## Home Page

> Add screenshot here

```
images/home.png
```

---

## Prediction Result

> Add screenshot here

```
images/prediction.png
```

---

# 📈 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | ~89% |
| Precision | High |
| Recall | High |
| F1 Score | High |

> **Note:** Replace these values with your actual evaluation metrics if available.

---

# 🔍 Prediction Pipeline

```
User Review
      │
      ▼
Text Cleaning
      │
      ▼
Tokenizer
      │
      ▼
Padding
      │
      ▼
LSTM Model
      │
      ▼
Probability Score
      │
      ▼
Positive / Negative
```

---

# 📚 Notebook

The notebook contains:

- Exploratory Data Analysis
- Text Preprocessing
- Tokenization
- Sequence Generation
- LSTM Model
- Model Training
- Model Evaluation
- Saving Model
- Prediction

---

# 📦 Dependencies

```
TensorFlow
Streamlit
NumPy
Pandas
Scikit-Learn
NLTK
Pickle
```

Install all packages

```bash
pip install -r requirements.txt
```

---

# 🔮 Future Improvements

- ✅ GRU Model
- ✅ Bidirectional LSTM
- ✅ Attention Mechanism
- ✅ BERT Fine-Tuning
- ✅ Transformer Models
- ✅ Docker Deployment
- ✅ FastAPI Backend
- ✅ CI/CD Pipeline
- ✅ Explainable AI (LIME/SHAP)

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Mohammed Zaheeruddin

**AI/ML Engineer | Deep Learning | NLP | Generative AI**

GitHub

https://github.com/mdzaheerjk

LinkedIn

https://www.linkedin.com/in/mdzaheerjk

---

# ⭐ Support

If you found this project helpful, please consider:

⭐ Star this repository

🍴 Fork the repository

🐛 Report issues

💡 Suggest new features

---

<div align="center">

## ⭐ If you like this project, don't forget to Star the repository!

Made with ❤️ by **Mohammed Zaheeruddin**

</div>
