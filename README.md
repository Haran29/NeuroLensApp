# NeuroLens

> A full-stack platform for exploring audio, speech, and signal-based insights through a mobile application and Python-powered analysis backend.

NeuroLens combines an Expo/React Native frontend with a FastAPI backend to support multimodal data collection, processing, and analysis. The project is designed for assistive technology, experimentation, and research-oriented workflows involving speech, audio, and sensor data.

> **Project status:** NeuroLens is under active development. Some functionality may require additional configuration, platform permissions, or a development build.

## ✨ Features

- Cross-platform mobile frontend powered by Expo and React Native
- File-based navigation with Expo Router
- Audio and speech-related functionality
- Bluetooth device integration through `react-native-ble-plx`
- Firebase client and Firebase Admin SDK integration
- FastAPI backend for application and analysis services
- Audio feature extraction using libraries such as Librosa and Parselmouth
- Speech-to-text support through OpenAI Whisper
- Machine-learning workflows using PyTorch, scikit-learn, XGBoost, SHAP, and SciPy
- Cloud Build configuration for deployment workflows

## 🏗️ Architecture

```text
NeuroLensApp/
├── frontend/
│   └── NeuroLens/       # Expo / React Native mobile application
├── backend/              # FastAPI and machine-learning backend
├── cloudbuild.yaml       # Cloud Build configuration
└── README.md
```

The application is split into two primary components:

| Component | Technologies | Purpose |
| --- | --- | --- |
| Frontend | TypeScript, Expo, React Native, Firebase | Mobile user experience, navigation, audio interaction, and device connectivity |
| Backend | Python, FastAPI, PyTorch, scikit-learn | API services, data processing, audio analysis, and machine-learning workflows |

## 🧰 Technology Stack

### Frontend

- TypeScript
- React Native
- Expo SDK 54
- Expo Router
- React Navigation
- Firebase
- Axios
- Expo Audio and speech packages
- React Native Bluetooth Low Energy
- React Native Reanimated
- React Native Web

### Backend

- Python
- FastAPI
- Uvicorn
- Firebase Admin SDK
- SQLAlchemy
- Pydantic
- NumPy
- pandas
- SciPy
- PyTorch
- scikit-learn
- XGBoost
- SHAP
- Librosa
- SoundFile
- Parselmouth
- OpenAI Whisper

## ✅ Prerequisites

Install the following before getting started:

- Node.js and npm
- Python 3.10 or newer
- Git
- Expo tooling and the platform tools required for your target device
- Android Studio for Android development, or Xcode for iOS development
- FFmpeg-compatible system support for audio processing

Depending on the features you use, you may also need:

- A physical Android or iOS device
- Bluetooth hardware
- Platform-specific microphone, Bluetooth, and media permissions
- An Expo development build rather than Expo Go

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/Haran29/NeuroLensApp.git
cd NeuroLensApp
```

The frontend and backend run independently, so use separate terminal windows.

### 1. Start the backend

#### macOS / Linux

```bash
cd backend

python3 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

uvicorn main:app --reload
```

#### Windows PowerShell

```powershell
cd backend

python -m venv venv
.\venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

uvicorn main:app --reload
```

The development server runs at:

```text
http://localhost:8000
```

### 2. Start the frontend

Open another terminal:

```bash
cd frontend/NeuroLens
npm install
npm start
```

Expo will display available options for opening the application on a development build, emulator, simulator, web browser, or connected device.

You can also use the project scripts directly:

```bash
npm run android
npm run ios
npm run web
npm run lint
npm run build
```

> Native functionality such as Bluetooth, microphone access, and some audio features may require a development build and additional platform configuration. Follow the relevant Expo and React Native platform setup instructions for your environment.

## ⚙️ Configuration

Configuration values should be provided through environment variables or local configuration files appropriate for each environment.

Before running the complete application, review:

- Firebase client configuration in the frontend
- Firebase Admin credentials for the backend
- Backend service configuration
- Local API connection settings
- Native permissions for microphone, Bluetooth, and media access

Do not commit private keys, service-account files, API keys, or other secrets to the repository.

## 📁 Project Documentation

Additional documentation is available in the component directories:

- [Backend README](backend/README.md)
- [Frontend README](frontend/NeuroLens/README.md)

## 🧪 Development Notes

### Frontend linting

```bash
cd frontend/NeuroLens
npm run lint
```

### Backend development server

```bash
cd backend
uvicorn main:app --reload
```

The backend automatically reloads when Python source files change during development.

## 🛠️ Contributing

Contributions and improvements are welcome.

A typical contribution workflow is:

1. Create a feature branch.
2. Make focused changes.
3. Run the relevant frontend or backend checks.
4. Update documentation when behavior or setup changes.
5. Open a pull request with a clear description of the changes.

Please avoid committing generated files, credentials, local environments, or device-specific configuration.

## 🗺️ Suggested Future Work

Potential areas for future development include:

- Expanded API and component documentation
- Automated frontend and backend testing
- Reproducible model and dataset management
- Improved production deployment documentation
- More detailed Bluetooth and audio setup guides
- Screenshots or demonstrations of supported workflows

## 📄 License

No license has been specified for this repository yet. Until a license is added, usage and redistribution rights remain subject to the repository owner's rights.
