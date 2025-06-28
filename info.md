---

## 🧪 Description

The **Automated QA Analyzer** is a desktop application designed to analyze and validate various file types using specialized validators for each format. It provides an intuitive way to detect issues and errors in different kinds of files, including text documents, code files, configuration files, and archives.

Its main goal is to help developers, system administrators, and QA engineers quickly identify and resolve issues that may affect functionality, security, or file integrity.

The program features a graphical user interface (GUI) built with Python’s `tkinter` library via `customtkinter`, making it user-friendly and accessible.

---

## 🎯 Key Features

* **Multi-format File Analysis**
  Supports a wide range of file formats such as JSON, XML, CSV, YAML, Python scripts, HTML, SQL, CSS, logs, and others. Each file type is processed by a corresponding validator that checks for structural issues or syntax errors.

* **Recent Files History**
  The app stores a list of the last five opened files or folders, making it easier to revisit previously analyzed items.

* **Color-Coded Results**
  Analysis results are displayed in a text area with color tags for different severity levels:

  * 🔴 Errors (red)
  * 🟠 Warnings (orange)
  * 🟢 Success messages (green)
  * 🔵 Informational notes (blue)

* **Export Options**
  Results can be exported in multiple formats: plain text, CSV, or HTML — for easy sharing or reporting.

* **Archive Support**
  The app can also validate archive files such as `.zip`, `.rar`, `.7z`, and others.

---

## 💼 Use Cases

### 👨‍💻 Software Developers

* Check configuration files, scripts, and datasets for missing values, syntax errors, and inconsistencies.
* Validate Python, CSS, or JavaScript files for code quality or structural issues.

### 🖥️ System Administrators

* Inspect configuration files and log files for incorrect settings or runtime errors.
* Scan log files for keywords like `error`, `exception`, etc., for faster system diagnostics.

### 🧪 QA Testers

* Automate the validation of input/output files in QA pipelines.
* Check XML or HTML files for structure and formatting issues.

### 🎓 Education & Learning

* Students and educators can use the app to explore how different file formats work.
* Useful in courses on programming, system administration, and web development.

### 📦 Archive Analysis

* Analyze contents of code packages, backup files, or software bundles in archive format.

---

## 🛠️ How It Works

1. **Select a File or Folder**
   Choose a target through the file selection dialog.

2. **Automatic File Scan**
   The application checks all supported files within the selected directory or the single selected file.

3. **Result Display**
   The analysis output is shown in a console-style text box with color-coded feedback.

4. **Export Results**
   Users can export the findings to `.txt`, `.csv`, or `.html` for documentation or sharing.

---

This program is ideal for anyone looking to streamline the file validation process and detect potential issues quickly and efficiently.

---