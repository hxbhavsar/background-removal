# Background Removal App

A Streamlit web application for removing backgrounds from images with additional blur effects.

## Features

- 🖼️ Upload images (PNG, JPG, JPEG)
- 🎯 Automatic background removal
- 🌫️ Adjustable blur effect
- 💾 Download processed images
- 📱 Mobile-friendly interface

## Prerequisites

- Python 3.11 (Required for compatibility with rembg)
- Homebrew (for macOS users)

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/background-removal.git
cd background-removal
```

2. **Create and activate virtual environment**
```bash
python3.11 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

1. **Run the application**
```bash
streamlit run app.py
```

2. **Access the web interface**
- Open your browser and go to `http://localhost:8501`
- Upload an image using the sidebar
- Adjust blur radius if desired
- Download the processed image

## Project Structure
```
background-removal/
├── README.md
├── requirements.txt
├── app.py
└── .gitignore
```

## Common Issues & Solutions

1. **rembg installation issues**
```bash
pip install --no-cache-dir rembg[gpu]
# or for CPU only
pip install --no-cache-dir rembg
```

2. **onnxruntime issues**
```bash
pip install onnxruntime-cpu
```

## Technical Details

- Maximum file size: 20MB
- Supported formats: PNG, JPG, JPEG
- Image processing: rembg library
- Interface: Streamlit
- Blur effect: PIL ImageFilter

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.