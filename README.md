# QR Code Generator (Python)
A simple Python project that generates a QR code from a URL or text message and saves it as a PNG image.

## Features
* Generate QR codes from any URL or message
* Save QR code as a PNG image
* Simple command-line interaction
* Custom file name support

## Requirements
Make sure you have the following installed:

* Python 3.x
* Required Python libraries:

  * qrcode
  * Pillow

You can install the required libraries using:

```bash
pip install qrcode[pil]
```

##  Code

```python
import qrcode
from PIL import Image

url = input("Enter the URL or message You want to Display:\n")
filename = input("Enter the file name to save QR (without .png): ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(filename + ".png")

print("QR Code generated and saved as", filename + ".png")
```

##  How to Run

1. Save the code in a file named `qr_generator.py`
2. Open terminal in the project folder
3. Run the script:

```bash
python qr_generator.py
```

4. Enter the URL or message when prompted
5. Enter a filename for the QR code image

The QR code will be generated and saved in the same folder.

## Example

Input:

```
Enter the URL or message You want to Display:
https://example.com

Enter the file name to save QR (without .png):
my_qr
```

Output:

```
QR Code generated and saved as my_qr.png
```

## Output

The program generates a QR code image like:

```
my_qr.png
```

## License

This project is open source and free to use.
