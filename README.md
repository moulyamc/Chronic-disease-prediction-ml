# 🧬 Chronic Disease Prediction using Machine Learning  

This project predicts the **risk of chronic diseases** based on patient symptoms and health data using a **Gaussian Naive Bayes** machine learning model.  

It includes:  
- 🧠 A **machine learning model** trained on medical data  
- 🧩 A **Tkinter graphical user interface (GUI)** for symptom-based prediction  
- 📊 A clear, simple workflow for users and reviewers to understand and run easily  

## 🚀 Project Overview  

This system helps users predict diseases by selecting symptoms from dropdown menus.  
The model was trained using a dataset containing multiple diseases and their associated symptoms.  

After training, the model can predict diseases such as:  
- Diabetes  
- Migraine  
- GERD  
- Tuberculosis  
- Hypertension  
- Typhoid  
- Hepatitis, and more!  

## 🧠 Machine Learning Details  

- **Algorithm used:** Gaussian Naive Bayes  
- **Libraries:** scikit-learn, pandas, numpy, matplotlib, seaborn  
- **Dataset:** Training dataset (`training_data.csv`) with symptoms and corresponding diseases  
- **Output model:** `model.pkl` — a serialized trained model file  

During testing, the model achieved:
Accuracy: 1.00  
Precision: 1.00  
Recall: 1.00  

## 🖥️ Graphical User Interface  

The GUI allows users to:  
- Select up to **5 symptoms** from dropdown menus  
- Click the **Predict** button  
- Instantly see the **predicted disease** below  

## ⚙️ How to Run the Project  

### 1️⃣ Clone this repository
```bash
git clone https://github.com/moulyamc/Chronic-disease-prediction-ml.git
cd Chronic-disease-prediction-ml
```

2️⃣ Install dependencies
Make sure Python 3.x is installed, then run:
```bash
pip install -r requirements.txt
```

3️⃣ Train the model
This will create model.pkl automatically:
```bash
python train_model.py
```

4️⃣ Run the GUI
```bash
python gui_app.py
```

5️⃣ Use the app
- Select symptoms
- Click Predict
- View the predicted disease on screen

## 📂 Project Structure
```bash
Chronic-disease-prediction-ml/
│
├── gui_app.py              # Tkinter GUI for user input and prediction
├── train_model.py          # Script for model training and saving model.pkl
├── training_data.csv       # Dataset used to train the Naive Bayes model
├── model.pkl               # Saved trained model (auto-generated after training)
├── requirements.txt        # Required Python libraries
├── README.md               # Project documentation
│
└── venv/                   # (Optional) Virtual environment folder
```









