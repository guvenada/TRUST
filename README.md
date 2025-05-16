
<h1 align="center">
  🩸 TRUST - Firebase Vulnerability Analysis Tool
</h1>

![Banner](assets/banner.gif)

**Advanced security scanner to detect insecure Firebase databases in APK files**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-yellowgreen)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-red)](LICENSE)

## 📖 Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Sample Output](#-sample-output)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Features
- ✔️ Scans APK files for Firebase URLs
- 🔍 Automatically detects potential security vulnerabilities
- 📂 Analyzes compressed APK contents
- 🛡️ Interactive testing mode
- 📊 Generates JSON format reports
- 📱 Focused on mobile application security

## ⚙️ Installation
1. Requirements:
```
Python 3.8+ and pip installed
```
2. Install dependencies:
```
pip install requests
```

## 💻 Usage
Run the program with the path to the APK file as an argument:

```
python TRUST.py <apk_file>
```

Example:

```
python TRUST.py sample_app.apk
```

## 🖥️ Sample Output
```
[*] Scanning APK: sample_app.apk

[+] Firebase URL found: https://example.firebaseio.com
[?] Do you want to test this database? (y/n): y
[!] Open database found: https://example.firebaseio.com
🔍 Sample data: {...}
```

## 🤝 Contributing
Contributions are welcome! Please open issues or submit pull requests.

## 📄 License
This project is licensed under the MIT License.
