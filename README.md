# 👁️ LogiVision AI — Autonomous Dark Store Infrastructure Engine

LogiVision AI is a real-time, edge-integrated supply chain control center engineered for ultra-fast fulfillment dark stores. The platform marries high-speed computer vision hardware processing with cognitive LLM logic to automatically audit inventory packages, evaluate regional compliance constraints, and optimize courier route dispatches instantly under changing urban conditions.

---

## 🚀 Core Features

- **Automated Edge-Camera Audit Desk**: Real-time parallel barcode scanning using OpenCV and ZXing modules directly through local hardware webcams.
- **Global Inventory Cross-Referencing**: Instantly reverse-lookups parsed SKU data against live international product catalogs via Open Food Facts & UPCitemdb API channels.
- **Cognitive Supply-Chain Decision System**: Evaluates real-time localized variables (metro traffic density, weather anomalies, vehicle profiles) using OpenAI's client model infrastructure to coordinate dynamic route recovery models.
- **Target Regional Localization**: Translates automated customer arrival updates into multiple regional languages (Hindi, Telugu, Kannada, Tamil, English) on the fly.

---

## 🛠️ System Architecture & Script Modules

The project is structured with strict modular isolation to maximize telemetry speed and keep development clean:

1. **`app.py`**: The central Streamlit control room user interface. Handles the layout configuration presentation grid, metrics display cards, and localized sidebar controls.
2. **`vision_engine.py`**: Controls the local camera asset, decodes barcode frame matrices, and handles global database API queries.
3. **`decision_orchestrator.py`**: The AI cognitive routing hub. Structures the multi-layered operations prompts and connects seamlessly with OpenAI's backend.
4. **`requirements.txt`**: Manages all local system dependencies and package environments.

---

## 📦 Local Installation & Setup

Follow these steps to run the complete platform locally on your machine:

### 1. Clone the Architecture
```bash
git clone [https://github.com/DarshithRaj/LogiVision-AI-Core.git](https://github.com/DarshithRaj/LogiVision-AI-Core.git)
cd LogiVision-AI-Core
