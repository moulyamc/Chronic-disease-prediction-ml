# Chronic Disease Prediction using Machine Learning

This project predicts diseases based on user-selected symptoms using a **Gaussian Naive Bayes** machine-learning model.  
It includes a **Tkinter graphical interface (GUI)** that allows users to select symptoms and instantly see the predicted disease.

---

## Features
- Uses a pre-trained **Naive Bayes model (model.pkl)**  
- **Tkinter GUI** for easy disease prediction  
- Dataset: 4920 records, 132 features, 41 possible diseases  
- Clean, simple, and reproducible training script (`train_model.py`)

---

## How It Works
1. `train_model.py` trains a Naive Bayes model using `training_data.csv`
2. The model is saved as `model.pkl`
3. `gui_app.py` loads this model and predicts disease based on selected symptoms

---

## Run Instructions

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the GUI**
   ```bash
   python gui_app.py
   ```

3. *(Optional)* **Retrain the model**
   ```bash
   python train_model.py
   ```

---

## Output
When you run `gui_app.py`, a window titled  
**“Chronic Disease Prediction using Machine Learning”** opens.  
Select symptoms from dropdowns → click **Predict** → see the predicted disease instantly.

---

## Dependencies
See `requirements.txt` for the complete list.

---

## License
This project is for educational and research purposes.
