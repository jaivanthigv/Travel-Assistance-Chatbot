# 🌍 AI Travel Assistant Chatbot

An intelligent travel assistant chatbot that helps users with travel-related queries such as booking flights, finding hotels, checking travel information, and answering common travel questions.

This project uses **Machine Learning and Natural Language Processing (NLP)** to understand user queries and provide appropriate responses.

---

## 🚀 Features

* ✈️ Flight booking assistance
* 🏨 Hotel booking support
* ❌ Booking cancellation help
* ❓ Travel FAQ responses
* 🤖 Intent classification using Machine Learning
* 🌐 Web interface using Streamlit

---

## 🧠 Technologies Used

* Python
* Scikit-learn
* NumPy
* Streamlit
* JSON
* Pickle

---

## 📂 Project Structure

```
AI-travel-assistant-chatbot
│
├── data
│   └── intents.json
│
├── models
│   ├── chat_model.pkl
│   └── vectorizer.pkl
│
├── src
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── app.py
└── webapp.py
```

---

## ⚙️ Installation

1. Clone the repository

```
git clone https://github.com/yourusername/ai-travel-assistant-chatbot.git
```

2. Navigate to the project folder

```
cd ai-travel-assistant-chatbot
```

3. Install required libraries

```
pip install numpy scikit-learn streamlit
```

---

## ▶️ Run the Project

### Train the model

```
python src/train.py
```

### Run the chatbot (terminal version)

```
python app.py
```

### Run the web application

```
python -m streamlit run webapp.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 💡 How It Works

1. User enters a travel-related query.
2. The text is converted into numerical features using **CountVectorizer**.
3. A **Logistic Regression model** predicts the intent.
4. The chatbot returns a response based on the detected intent.

---

## 📌 Future Improvements

* Add real-time flight APIs
* Integrate weather information
* Add travel recommendation system
* Improve NLP using advanced models like transformers

---

## 👩‍💻 Author

**Jaivanthi Venkatasan**

B.Tech Artificial Intelligence & Data Science
Passionate about AI, Machine Learning, and Generative AI.

---

## ⭐ If you like this project

Please consider giving it a **star ⭐ on GitHub**.
