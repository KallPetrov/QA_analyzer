import os
import platform
import json
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Импортирай валидаторите от твоя модул
from modules import (
    check_json, check_xml, check_md, check_yaml, check_ini,
    check_html, check_tmx, check_binary,
    check_csv, check_log, check_python, check_css, check_js, check_sql, check_shell
)

# UI настройки
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

HISTORY_FILE = "history.json"
MAX_HISTORY = 5

SUPPORTED_EXTENSIONS = {
    'json': check_json, 'xml': check_xml, 'md': check_md,
    'yaml': check_yaml, 'yml': check_yaml, 'ini': check_ini,
    'html': check_html, 'tmx': check_tmx, 'csv': check_csv,
    'tsv': check_csv, 'log': check_log, 'py': check_python,
    'css': check_css, 'js': check_js, 'sql': check_sql, 'sh': check_shell,
    'zip': check_binary, 'rar': check_binary, '7z': check_binary,
    'tar': check_binary, 'iso': check_binary, 'nrg': check_binary,
    'img': check_binary, 'cdi': check_binary, 'cue': check_binary,
    'odt': check_binary, 'rtf': check_binary, 'psd': check_binary,
    'msi': check_binary, 'exe': check_binary, 'bat': check_binary,
    'bin': check_binary, 'app': check_binary
}

def get_os():
    return platform.system().lower()

def analyze_file(file_path):
    ext = file_path.split('.')[-1].lower()
    validator = SUPPORTED_EXTENSIONS.get(ext)
    if validator:
        try:
            return validator.validate(file_path)
        except Exception as e:
            return [f"❌ Error during processing: {e}"]
    return [f"⚠️ Unsupported file type: .{ext}"]

def load_history():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_history(path):
    history = load_history()
    if path in history:
        history.remove(path)
    history.insert(0, path)
    history = history[:MAX_HISTORY]
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f)

class QAApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🧪 Automated QA Analyzer by Hexagon Lab")
        self.geometry("1000x600")

        self.report_data = []

        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.history_menu = ctk.CTkOptionMenu(self, values=load_history())
        self.history_menu.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.select_btn = ctk.CTkButton(self, text="📂 Select File or Folder", command=self.select_path)
        self.select_btn.grid(row=0, column=1, padx=10)

        self.export_btn = ctk.CTkButton(self, text="📄 Export Results", command=self.export_results)
        self.export_btn.grid(row=0, column=2, padx=10)

        self.export_html_btn = ctk.CTkButton(self, text="🌐 Export to HTML", command=self.export_html)
        self.export_html_btn.grid(row=0, column=3, padx=10)

        self.result_box = ctk.CTkTextbox(self, wrap="word", font=("Consolas", 11))
        self.result_box.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

    def select_path(self):
        path = filedialog.askopenfilename(title="Select file") or filedialog.askdirectory(title="Select folder")
        if not path:
            return

        save_history(path)
        self.history_menu.configure(values=load_history())
        self.history_menu.set(path)

        files_to_check = []
        if os.path.isfile(path):
            files_to_check = [path]
        else:
            for root, _, files in os.walk(path):
                for file in files:
                    files_to_check.append(os.path.join(root, file))

        self.result_box.delete("1.0", "end")
        self.report_data.clear()

        matched = 0

        for file in files_to_check:
            ext = file.split('.')[-1].lower()
            if ext in SUPPORTED_EXTENSIONS:
                matched += 1
                self.result_box.insert("end", f"\n🔍 Analyzing: {file}\n")
                result = analyze_file(file)
                for line in result:
                    self.result_box.insert("end", f"  {line}\n")
                    self.report_data.append((file, line))
                self.result_box.insert("end", "-" * 80 + "\n")

        if matched == 0:
            self.result_box.insert("end", "⚠️ No supported files found.\n")

    def export_results(self):
        if not self.report_data:
            messagebox.showinfo("No Data", "No results to export.")
            return

        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")])
        if not path:
            return

        try:
            if path.endswith(".csv"):
                with open(path, 'w', encoding='utf-8-sig') as f:
                    f.write("File,Issue\n")
                    for file, issue in self.report_data:
                        f.write(f"\"{file}\",\"{issue}\"\n")
            else:
                with open(path, 'w', encoding='utf-8') as f:
                    for file, issue in self.report_data:
                        f.write(f"{file}: {issue}\n")
            messagebox.showinfo("Success", f"✅ Results saved to:\n{path}")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Failed to save: {e}")

    def export_html(self):
        if not self.report_data:
            messagebox.showinfo("No Data", "No results to export.")
            return

        path = filedialog.asksaveasfilename(defaultextension=".html",
                                            filetypes=[("HTML files", "*.html")])
        if not path:
            return

        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write("<html><head><meta charset='utf-8'><title>QA Report</title></head><body>\n")
                f.write("<h2>QA Analysis – Results</h2><hr>\n")
                for file, issue in self.report_data:
                    color = "black"
                    if "❌" in issue:
                        color = "red"
                    elif "⚠️" in issue:
                        color = "orange"
                    elif "✅" in issue:
                        color = "green"
                    f.write(f"<p><strong>{file}</strong>: <span style='color:{color}'>{issue}</span></p>\n")
                f.write("</body></html>")
            messagebox.showinfo("Success", f"📄 HTML report saved to:\n{path}")
        except Exception as e:
            messagebox.showerror("Error", f"❌ Failed to save HTML: {e}")

if __name__ == "__main__":
    app = QAApp()
    app.mainloop()
