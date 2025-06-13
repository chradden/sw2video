# 🎨📽️ Colorize & Animate – Alte Fotos lebendig machen

Diese App verwandelt alte Schwarz-Weiß-Bilder in kolorierte Videos mit lebensechter Bewegung – direkt im Browser.

> Entwickelt mit: Python · Streamlit · DeOldify · First-Order-Motion-Model

---

## 🚀 Installation in GitHub Codespaces (oder lokal)

### 1. Projekt klonen und öffnen

```bash
git clone https://github.com/dein-benutzername/colorize-animate-app.git
cd colorize-animate-app


### 2. Starte deinen Codespace (oder aktiviere lokal dein venv)

pip install -r requirements.txt


### 3. Setup-Skripte ausführen (nur beim ersten Mal)

python setup_deoldify.py
python setup_firstorder.py

Diese Befehle laden: 
- das DeOldify-Farbmodell (300mb)
- das First-Order-Animationsmodell inkl. Demo-Video (200mb)


### 4. App starten

streamlit run app.py

Dann öffnet sich im Browser die App unter localhost:8501 (oder Codespace-Link)



### Projektstruktur

.
├── app.py
├── requirements.txt
├── colorizer.py
├── animator.py
├── setup_deoldify.py
├── setup_firstorder.py
├── .devcontainer/
│   └── devcontainer.json
└── first-order-model/
    └── ... (automatisch erstellt)
