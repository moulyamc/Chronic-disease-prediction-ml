# 🧬 Chronic Disease Prediction using Machine Learning  

This project predicts the **risk of chronic diseases** based on patient symptoms using a **Gaussian Naive Bayes** machine learning model and provides a **Tkinter-based GUI** for easy interaction.  

## ✨ Features  

- 🧠 Machine Learning–based disease prediction  
- 🧩 User-friendly GUI built using Tkinter  
- 📊 Trained on a dataset with 130+ symptoms and 40+ diseases  
- 💾 Saves trained model automatically (`model.pkl`)  
- ⚡ Quick predictions with clean and simple interface  

## 🧰 Tech Stack  

- **Language:** Python 🐍  
- **Libraries:**  
  - scikit-learn  
  - pandas  
  - numpy  
  - matplotlib  
  - seaborn  
  - tkinter 

## 📂 Project Structure
```bash
Chronic-disease-prediction-ml/
│
├── gui_app.py              # Tkinter GUI for disease prediction
├── train_model.py          # Trains and saves model.pkl
├── training_data.csv       # Dataset for training
├── model.pkl               # Saved trained model (after running train_model.py)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
``` 

## ⚙️ Installation / Setup Instructions  

### 1️⃣ Clone this repository
```bash
git clone https://github.com/moulyamc/Chronic-disease-prediction-ml.git
cd Chronic-disease-prediction-ml
```

### 2️⃣ Install dependencies
Make sure Python 3.x is installed, then run:
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model
This will create model.pkl automatically:
```bash
python train_model.py
```

### 4️⃣ Run the GUI
```bash
python gui_app.py
```

### 5️⃣ Use the app
- Select symptoms
- Click Predict
- View the predicted disease on screen

## 📊 Results
After training, the model achieved perfect classification on the dataset:
```bash
Accuracy: 1.00  
Precision: 1.00  
Recall: 1.00  
```

## 👩‍💻 Author
Moulya M C
