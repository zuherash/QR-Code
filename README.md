# QR-Code

This repository provides a simple Python script to generate a QR code that links to the Castera Plus project on Vercel. The generated QR code can be printed on souvenirs or other materials so visitors can easily access the project.

## Usage

1. Install dependencies (requires Python 3 and `pip`):
   ```bash
   pip install qrcode[pil]
   ```
2. Run the script:
   ```bash
   python3 generate_qr.py
   ```
   The script creates `castera_plus_qr.png` in the repository directory. This
   file is ignored by git so you can regenerate it whenever needed.

Scanning the generated image will open the site:
<https://castera-plus.vercel.app/>
