import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import pandas as pd

# Load the trained model
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    messagebox.showerror("Error", "Model file not found. Please run train_model.py first.")
    raise SystemExit

# Load dataset to get symptom names
df = pd.read_csv('training_data.csv')
df = df.dropna(axis=1, how='all')

# Extract symptom columns (all except 'prognosis')
symptoms = [col for col in df.columns if col != 'prognosis']

# Create main window
root = tk.Tk()
root.title("Chronic Disease Prediction using Machine Learning")
root.geometry("700x500")
root.configure(bg="#F0F4F8")

# Title label
title_label = tk.Label(
    root,
    text="Chronic Disease Prediction using Machine Learning",
    font=("Helvetica", 18, "bold"),
    bg="#F0F4F8",
    fg="#333"
)
title_label.pack(pady=20)

# Instruction label
inst_label = tk.Label(
    root,
    text="Select up to 5 symptoms to predict the disease:",
    font=("Helvetica", 12),
    bg="#F0F4F8",
    fg="#333"
)
inst_label.pack(pady=10)

# Dropdowns for symptom selection
symptom_vars = [tk.StringVar() for _ in range(5)]
dropdowns = []
for i in range(5):
    label = tk.Label(root, text=f"Symptom {i+1}:", bg="#F0F4F8", fg="#333")
    label.pack()
    cb = ttk.Combobox(root, textvariable=symptom_vars[i], values=symptoms, width=50)
    cb.pack(pady=5)
    dropdowns.append(cb)

# Prediction label
result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 14, "bold"),
    bg="#F0F4F8",
    fg="#00529B"
)
result_label.pack(pady=20)

# Prediction function
def predict_disease():
    selected_symptoms = [var.get() for var in symptom_vars if var.get()]
    if not selected_symptoms:
        messagebox.showwarning("Input Error", "Please select at least one symptom.")
        return

    # Create input vector
    input_data = pd.DataFrame([[1 if symptom in selected_symptoms else 0 for symptom in symptoms]],
                              columns=symptoms)

    # Predict
    prediction = model.predict(input_data)[0]
    result_label.config(text=f"Predicted Disease: {prediction}")

# Predict button
predict_button = tk.Button(
    root,
    text="Predict",
    command=predict_disease,
    font=("Helvetica", 12, "bold"),
    bg="#007ACC",
    fg="white",
    padx=20,
    pady=10
)
predict_button.pack(pady=10)

# Run the app
root.mainloop()
