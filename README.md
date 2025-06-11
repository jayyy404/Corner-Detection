# 🟩 Corner Detection System

## 📷 Overview

**Corner Detection** is a Python-based computer vision tool that leverages the Harris Corner Detection algorithm to identify and visualize corners in images. This system is ideal for feature extraction, object recognition, and image matching tasks in research and development.

---

## ✨ Features

- **Automatic Grayscale Conversion:** Prepares your image for analysis.
- **Gradient Visualization:** See the image gradients (`Ix`, `Iy`) for deeper insight.
- **Noise Reduction:** Gaussian blur for robust corner detection.
- **Harris Response Calculation:** Visualizes both the raw and thresholded Harris response.
- **Non-Maximum Suppression:** Ensures only the most significant corners are detected.
- **Interactive Scaling:** Choose your output image size for easy viewing.
- **Visual Output:** Detected corners are highlighted directly on your image.

---

## 🚀 Quick Start

### 1. **Install Requirements**

```sh
pip install opencv-python numpy matplotlib
```

### 2. **Add Your Image**

Place your image (e.g., `sample4.jpg`) in the project directory.

### 3. **Run the Program**

```sh
python main.py
```

### 4. **Follow the Prompts**

- Enter your desired scale (e.g., `1` for 100%, `0.5` for 50%, `2` for 200%).
- The program will display:
  - Gradient images (`Ix`, `Iy`)
  - Thresholded Harris response
  - Harris corner response
  - Final image with detected corners

---

## ⚙️ Customization

- **Change Image:** Edit the filename in the `main()` function in `main.py`.
- **Tune Detection:** Adjust the `threshold` and `radius` parameters in the `harris_corner_detection` function call for more or fewer corners.

---

## 📝 License

This project is provided for educational and research purposes.

---

## 🤝 Contributing

Pull requests and suggestions are welcome!

---

**Enjoy exploring your images with Harris Corner Detection!**
```