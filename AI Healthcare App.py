import tkinter as tk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from flask import Flask, request, jsonify
import threading
import json
import speech_recognition as sr  # Placeholder for voice input

# Flask App
app = Flask(__name__)

@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    data = request.json
    symptoms = data.get('symptoms', '')
    # Dummy recommendation logic
    recommendation = f"Recommended Medication for {symptoms}: Example Medicine"
    return jsonify({'recommendation': recommendation})

def run_flask():
    app.run(port=5000)

# Tkinter App
class PatientVisitApp:
    def __init__(self, root):
        self.root = root
        root.title('Patient Visit Recorder')

        # Setup GUI elements
        self.create_widgets()
        self.setup_plot()

    def create_widgets(self):
        # User Authentication
        self.username_label = tk.Label(self.root, text='Username:')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text='Password:')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text='Login', command=self.authenticate_user)
        self.login_button.pack()

        self.label = tk.Label(self.root, text='Enter Symptom:')
        self.label.pack()
        self.symptom_entry = tk.Entry(self.root)
        self.symptom_entry.pack()

        self.submit_button = tk.Button(self.root, text='Get Recommendation', command=self.submit_data)
        self.submit_button.pack()

        self.recommendation_label = tk.Label(self.root, text='')
        self.recommendation_label.pack()

        self.voice_button = tk.Button(self.root, text='Speak Symptom', command=self.record_voice)
        self.voice_button.pack()

        self.language_var = tk.StringVar(value='en')
        self.language_dropdown = tk.OptionMenu(self.root, self.language_var, 'en', 'es', 'fr', command=self.change_language)
        self.language_dropdown.pack()

    def setup_plot(self):
        # Create a Matplotlib figure
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Symptom Trends")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Frequency")

        # Create a canvas to display the figure
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

    def authenticate_user(self):
        # Dummy authentication
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == 'user' and password == 'password':
            messagebox.showinfo("Login", "Login successful")
        else:
            messagebox.showerror("Login", "Invalid credentials")

    def submit_data(self):
        symptom = self.symptom_entry.get()
        response = requests.post('http://localhost:5000/recommendation', json={'symptoms': symptom})
        recommendation = response.json().get('recommendation', 'No recommendation available')
        self.recommendation_label.config(text=recommendation)
        
        # Update plot with dummy data
        self.ax.clear()
        self.ax.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r-')
        self.ax.set_title("Updated Symptom Trends")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Frequency")
        self.canvas.draw()

    def record_voice(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.voice_button.config(text="Listening...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                self.symptom_entry.delete(0, tk.END)
                self.symptom_entry.insert(0, text)
                self.voice_button.config(text="Speak Symptom")
            except sr.UnknownValueError:
                self.voice_button.config(text="Error")
                messagebox.showerror("Voice Input", "Could not understand audio")
            except sr.RequestError:
                self.voice_button.config(text="Error")
                messagebox.showerror("Voice Input", "Error connecting to speech recognition service")

    def change_language(self, language):
        # Placeholder for localization
        if language == 'en':
            self.label.config(text='Enter Symptom:')
            self.submit_button.config(text='Get Recommendation')
            self.voice_button.config(text='Speak Symptom')
        elif language == 'es':
            self.label.config(text='Ingrese Síntoma:')
            self.submit_button.config(text='Obtener Recomendación')
            self.voice_button.config(text='Hablar Síntoma')
        elif language == 'fr':
            self.label.config(text='Entrez le Symptôme:')
            self.submit_button.config(text='Obtenir Recommandation')
            self.voice_button.config(text='Parler Symptôme')

# Run Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Run Tkinter app
if __name__ == '__main__':
    root = tk.Tk()
    app = PatientVisitApp(root)
    root.mainloop()
