![Project Logo](assets/openai-tts-logo.png)

# OpenAI Text-to-Speech (TTS) App

## 📌 Project Overview
This is a **Gradio-based Text-to-Speech (TTS) application** powered by **OpenAI's TTS API**. It allows users to input text and convert it into **natural-sounding speech** using different voice models.

## 🚀 Features
- Convert text into speech using OpenAI's **TTS models** (`tts-1`, `tts-1-hd`).
- Choose from **6 voice options**: `alloy`, `echo`, `fable`, `onyx`, `nova`, and `shimmer`.
- **Secure API Key Input** (hidden for security).
- **Instant Speech Generation** with playback in the browser.
- **Gradio UI** for an interactive user experience.

## 🛠️ Technologies Used
- **Python**
- **Gradio** (for UI)
- **OpenAI API** (for text-to-speech conversion)
- **Tempfile** (for managing audio files)

## 📂 Project Structure
```
├── tts_app.py             # Main Python script for running the TTS app
├── requirements.txt       # Required dependencies
├── README.md              # Documentation
└── .gitignore             # Ignore unnecessary files
```

## 🔧 Installation & Setup
### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/OpenAI-TTS.git
cd OpenAI-TTS
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python tts_app.py
```

The **Gradio interface** will launch, allowing you to enter text and generate speech!

## 🎤 How It Works
1. Enter your **OpenAI API Key**.
2. Select a **TTS Model** (`tts-1` or `tts-1-hd`).
3. Choose a **Voice** from the available options.
4. Enter text and click **Generate Speech**.
5. Listen to the generated speech in the output audio player.

## 🖼️ Example Gradio UI
*(Insert Screenshot Here)*

## 🛠️ Troubleshooting
- Ensure you have a valid **OpenAI API Key**.
- Check that your **internet connection** is active.
- If issues persist, check the **console logs** for errors.

## 📜 License
This project is **open-source** under the **MIT License**.

## 🤝 Contributing
Contributions are welcome! If you have improvements, please submit a pull request.

## 📬 Contact
For any questions or collaborations:
- **GitHub**: [@your-username](https://github.com/your-username)
- **Email**: your-email@example.com

---
### ⭐ If you find this project useful, please give it a star! ⭐

