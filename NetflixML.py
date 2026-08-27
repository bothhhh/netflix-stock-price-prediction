'''
*******************************
Author: Limpanhaboth Yin, Megatron Stafford, Kevin Thomas
u3301989, u3307724, u3296126 Assessment 1(a) 19/ 05/2026
Programming: Netflix Stock Price Prediction Application
*******************************
'''

import tkinter as tk
import pickle
import numpy as np


class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Netflix Stock Price Prediction")
        self.main_window.geometry("650x750")
        self.model = pickle.load(open("NetflixStockPredictionModel.pkl", "rb"))

        # Min and Max values
        self.ranges = {
            "Open": (1, 700),
            "High": (1, 705),
            "Low": (1, 695),
            "Volume": (1000000, 100000000)
        }

        self.sliders = {}
        self.value_labels = {}
        self.create_widgets()

        self.main_window.mainloop()

    def update_value(self, feature, value):
        self.value_labels[feature].config(text=f"Current Value: {float(value):.2f}")

    def create_widgets(self):
        title = tk.Label(self.main_window, text="Netflix Stock Price Prediction", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        for feature, values in self.ranges.items():
            frame = tk.Frame(self.main_window)
            frame.pack(pady=10)

            label = tk.Label(frame, text=feature, font=("Arial", 11, "bold"))
            label.pack()

            min_val, max_val = values

            slider = tk.Scale(frame, from_=min_val, to=max_val, orient="horizontal", resolution=0.01,
                              length=400, command=lambda value, f=feature: self.update_value(f, value))
            slider.pack()

            value_label = tk.Label(frame, text=f"Current Value: {slider.get():.2f}", font=("Arial", 10))
            value_label.pack()

            # Min/Max label UNDER slider
            range_label = tk.Label(frame, text=f"Min:{min_val}     Max:{max_val}", font=("Arial", 9))
            range_label.pack()

            # Save slider and label
            self.sliders[feature] = slider
            self.value_labels[feature] = value_label

        predict_btn = tk.Button(self.main_window, text="Predict Closing Price", command=self.predict_price,
                                bg="#2845bd", fg="white", font=("Arial", 12, "bold"))
        predict_btn.pack(pady=20)

        self.result = tk.StringVar()

        result_label = tk.Label(self.main_window, textvariable=self.result, font=("Arial", 14))
        result_label.pack(pady=10)

    def predict_price(self):
        open1 = self.sliders['Open'].get()
        high = self.sliders['High'].get()
        low = self.sliders['Low'].get()
        volume = self.sliders['Volume'].get()

        sample_data = np.array([[open1, high, low, volume]])
        prediction = self.model.predict(sample_data)

        self.result.set(f"Predicted Netflix Closing Price: ${prediction[0]:.2f}")

if __name__ == "__main__":
    my_gui = MyGUI()