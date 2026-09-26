![alt text](images/banner.png)
# 🖼️ Image Processing App

A simple and interactive image processing web application built with **Python**, **Streamlit**, and **Pillow**.

This application provides a user-friendly interface built with Streamlit, allowing users to upload images and perform two main operations:

* 📐 Resize an image
* 🔄 Convert an image between PNG and JPEG formats

---

## ✨ Features

### 🖥️ User-Friendly Interface

Built with Streamlit, the application provides a simple and intuitive interface that allows users to convert images without requiring advanced technical knowledge.

### 📐 Image Resizing

The application supports resizing images with two different modes:

* **Keep aspect ratio**: Automatically calculates the height based on the selected width.
* **Custom dimensions**: Allows the user to manually specify both width and height.

When keeping the aspect ratio enabled, the application uses Pillow's `thumbnail()` method to prevent the image from being stretched or distorted.

### 🔄 Image Type Conversion

The application can convert images between:

* PNG
* JPEG

The converted image is stored in memory using `BytesIO`, so no temporary file is required.

### ⬇️ Download Results

After processing an image, users can download the result directly from the application.

### 👀 Image Preview

Users can preview the image before and after conversion to make sure the output meets their expectations.

---

## 🛠️ Technologies Used

* **Python** — Programming language
* **Streamlit** — Web application framework
* **Pillow (PIL)** — Image processing
* **BytesIO** — In-memory binary file handling

---

## 📁 Project Structure

```text
Image-Conversion/
│
├──src/
│    ├── app.py
│    └── utils.py
│         ├── resize_image()
│         └── convert_image_type()
│
├── requirements.txt
└── README.md
```

### `app.py`

Contains the Streamlit user interface and controls the application workflow.

Responsibilities include:

* Uploading images
* Displaying images
* Selecting the processing type
* Collecting width and height
* Selecting the output format
* Displaying processed images
* Providing download buttons

### `src/utils.py`

Contains the image-processing functions.

The file includes:

* `resize_image()`
* `convert_image_type()`

Keeping these functions separate from the UI makes the project easier to maintain and test.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/image-processing-app.git
```

Move into the project directory:

```bash
cd image-processing-app
```

---

### 2. Create a virtual environment

It is recommended to use a virtual environment.

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

Install the required packages:

```bash
pip install streamlit pillow
```

---

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run src/app.py
```

After running the command, Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open this address in your browser.

---

## 🖥️ How to Use

### Step 1 — Upload an Image

Click:

```text
Choose an image...
```

and upload a `.jpg`, `.jpeg`, or `.png` image.

---

### Step 2 — Select an Operation

The application provides two options:

```text
- Resize
- Type Conversion
```

---

## 📐 Resize

Select:

```text
Resize
```

The application displays the image dimensions.

### Keep Aspect Ratio 'Enabled'

When:

```text
Keep aspect ratio
```

is enabled, you only need to specify the width.

The application automatically calculates the appropriate height.

For example:

```text
Original:
1920 × 1080

aspect_ratio = image.width / image.height
aspect_ratio = 1920 / 1080 = 1.777...

New width:
960

Calculated height:
height = int(width / aspect_ratio)
960 / 1.777... ≈ 540
540
```

Result:

```text
960 × 540
```

This prevents the image from being distorted.

### Keep Aspect Ratio 'Disabled'

If the option is disabled, both width and height can be specified 'manually'.

For example:

```text
Width: 800
Height: 600
```

The image will be resized exactly to:

```text
800 × 600
```

Keep in mind that manually changing both dimensions can distort the original image proportions.

---

## 🔄 Type Conversion

Select:

```text
Type Conversion
```

Then select the desired output format:

```text
JPEG
PNG
```

For example:

```text
input.png
    ↓
JPEG
    ↓
converted_image.jpeg
```

or:

```text
input.jpg
    ↓
PNG
    ↓
converted_image.png
```

---

## 🧠 How the Application Works

The general workflow is:

```text
User
 │
 ▼
Upload Image
 │
 ▼
Pillow opens the image
 │
 ▼
Select operation
 │
 ├───────────────┐
 ▼               ▼
Resize       Type Conversion
 │               │
 ▼               ▼
Resize Image   Convert Format
 │               │
 └───────┬───────┘
         ▼
    Store result
      in memory
         │
         ▼
   Download Image
```

---

## 🔧 Utility Functions

### `1. resize_image()`

Located in:

```text
src/utils.py
```

Function:

```python
def resize_image(image, width, height, keep_aspect_ratio):
```

This function changes the dimensions of an image.

When `keep_aspect_ratio` is `True`, it uses:

```python
image.thumbnail((width, height))
```

When it is `False`, it uses:

```python
image.resize((width, height))
```

---

### `2. convert_image_type()`

Located in:

```text
src/utils.py
```

Function:

```python
def convert_image_type(image, output_format):
```

This function converts an image to the selected format and stores the result in a `BytesIO` object.

For example:

```text
Image
  ↓
Pillow
  ↓
JPEG / PNG encoding
  ↓
BytesIO
  ↓
Download
```

---

## 💾 In-Memory File Handling

The application uses Python's `BytesIO` class:

```python
from io import BytesIO
```

Instead of creating temporary files on disk, the processed image is stored directly in memory.

For example:

```python
buffer = BytesIO()
image.save(buffer, format="PNG")
```

The resulting binary data can then be passed directly to Streamlit:

```python
st.download_button(
    data=buffer.getvalue(),
    ...
)
```

This makes the application simple and avoids unnecessary temporary files.

---

## 📋 Supported Input Formats

The file uploader accepts:

| Format | Supported |
| ------ | --------- |
| JPG    | ✅         |
| JPEG   | ✅         |
| PNG    | ✅         |

---

## 📤 Supported Output Formats

### Resize

Resized images are currently exported as:

```text
PNG
```

### Type Conversion

Supported output formats:

```text
JPEG
PNG
```

---


## 🚀 Possible Improvements

This project can be extended with additional features, such as:

*  Support for WebP
*  Support for GIF
*  Support for BMP
*  Preset image sizes
*  Percentage-based resizing
*  Batch image processing
*  JPEG quality control
*  Image compression
*  Image rotation
*  Image flipping
*  Image cropping
*  Background handling for transparent images
*  Displaying original and processed file sizes
*  Unit tests
*  Docker support
*  Deployment to Streamlit Community Cloud

---

## 🔐 Privacy

Image processing is performed by the application during the current session.

The application code itself does not explicitly save uploaded images to disk or upload them to an external image-processing service.

For a deployed version, the actual privacy behavior can also depend on the hosting environment and its configuration.

---

## 👨‍💻 Author

Created as a simple Python image-processing project using:

```text
Python + Streamlit + Pillow
```

---

## ⭐ If You Like This Project

Feel free to fork the repository, experiment with the code, and add new image-processing features.
