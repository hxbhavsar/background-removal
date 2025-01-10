# Image Background Remover

A Streamlit web application that removes backgrounds from images using the rembg library and allows for custom blur effects.

## Features

- 🖼️ Upload images in PNG, JPG, or JPEG format
- 🎯 Automatic background removal
- 🌫️ Adjustable blur effect
- 💾 Download processed images
- 📱 Mobile-friendly interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hxbhavsar/background-removal.git
cd background-removal
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and go to `http://localhost:8501`

3. Use the application:
   - Upload an image using the sidebar
   - Adjust blur radius if desired
   - Download the processed image

## Limitations

- Maximum file size: 20MB
- Supported formats: PNG, JPG, JPEG
- Processing time may vary based on image size and complexity

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
