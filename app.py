from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd
import json, os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model
model = load_model("model/crop_disease_model.h5", compile=False)

# Load class indices
with open("model/class_indices.json") as f:
    class_indices = json.load(f)

idx_to_class = {v: k for k, v in class_indices.items()}

# Load fertilizer data
fert_df = pd.read_csv("fertilizer_data/fertilizer_recommendations.csv")
fert_df = fert_df.applymap(lambda x: x.strip().lower() if isinstance(x, str) else x)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["image"]
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        img = image.load_img(path, target_size=(224, 224))
        img = image.img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        pred = model.predict(img)
        idx = np.argmax(pred)
        confidence = round(float(np.max(pred)) * 100, 2)

        label = idx_to_class[idx]
        crop, disease = label.lower().split("___")

        fert = fert_df[
            (fert_df["crop"] == crop) &
            (fert_df["disease"] == disease)
        ]

        if not fert.empty:
            fert = fert.iloc[0]
            pesticide = fert["pesticide"]
            dosage = fert["dosage_ml_per_l"]
            notes = fert["precautions"]
        else:
            pesticide = dosage = notes = "N/A"

        result = {
            "crop": crop.title(),
            "disease": disease.replace("_", " ").title(),
            "confidence": confidence,
            "pesticide": pesticide,
            "dosage": dosage,
            "notes": notes
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
        app.run()   #debug=False, use_reloader=False
 