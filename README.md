# StegoGuard
# StegoGuard

StegoGuard is an AI-powered system for **steganography detection and threat prevention** in digital images.  
It can **detect hidden data, extract it, sanitize malicious payloads, and securely transmit images** using advanced deep learning models.

---

## 🚀 Features
- ✅ **Image Steganography Detection** – Uses CNN-based models (UNet, StegoNet) to detect hidden data.
- ✅ **Malware & Threat Prevention** – Sanitizes suspicious images before processing.
- ✅ **Data Extraction** – Retrieves embedded data from stego images.
- ✅ **Secure Transmission** – Encrypts and transmits images safely.
- ✅ **End-to-End Flask API** – Exposes detection & extraction endpoints.
- ✅ **Modular Design** – Easy to extend for new steganography techniques.

---

## 📂 Project Structure

SmartStegoGuard/
│
├── client/ # Frontend (if applicable)
├── docs/ # Documentation & research papers
├── ml_models/ # Pre-trained deep learning models
├── server/
│ ├── app/
│ │ ├── models/ # Model definitions
│ │ ├── routes/ # Flask routes (detect, extract, sanitize, etc.)
│ │ ├── services/ # Helper services
│ │ ├── utils/ # Utility functions
│ │ ├── init.py
│ │ └── models.py
│ ├── uploads/ # Uploaded images (ignored in Git)
│ └── requirements.txt # Python dependencies
└── run.sh # Script to run the app


**Install Dependencies**
pip install -r requirements.txt

**Run the Flask Server**
python server/app.py

**The server will start at:**
👉 http://127.0.0.1:5000
