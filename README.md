<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">WIREGUARD-QR-GEN</h1></p>
<p align="center">
	<em><code>❯ Python script that generates QR image to console and save it to png file</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/languages/top/defendergr/wireguard-qr-gen?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/defendergr/wireguard-qr-gen?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ License](#-license)

---

##  Overview

1. Reads the contents of "wireguard.conf" into variable.
2. Creates a QR code object.
3. Adds the contents of "wireguard.conf" to the QR code.
4. Generates the QR code image.
5. Prints the QR code to the console in ASCII art format.
6. Saves the QR code as a PNG image named "wireguard.png" in the "images" directory.

<code>![WIREGUARD QR GEN](images/image.png?raw=true "Title")</code>

---


##  Project Structure

```sh
└── wireguard-qr-gen/
    ├── LICENSE
    ├── README.md
    ├── images
    │   ├── image.png
    │   └── wireguard.png
    ├── requirements.txt
    └── wireguard-qr-gen.py
```



##  Getting Started

###  Prerequisites

Before getting started with wireguard-qr-gen, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install wireguard-qr-gen using one of the following methods:

**Build from source:**

1. Clone the wireguard-qr-gen repository:
```sh
❯ git clone https://github.com/defendergr/wireguard-qr-gen
```

2. Navigate to the project directory:
```sh
❯ cd wireguard-qr-gen
```

3. Install the project dependencies:


```sh
❯ pip install -r requirements.txt
```




###  Usage
Run wireguard-qr-gen using the following command:

```sh
❯ python -m wireguard-qr-gen
```



##  License

This project is protected under the [AGPL-3.0 license](LICENCE) License.

---
