import json
import xml.etree.ElementTree as ET
import yaml
import configparser
import csv
import os
import re

class check_json:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                json.load(f)
            return ["✅ Valid JSON file."]
        except Exception as e:
            return [f"❌ Invalid JSON: {e}"]

class check_xml:
    @staticmethod
    def validate(file_path):
        try:
            ET.parse(file_path)
            return ["✅ Valid XML file."]
        except Exception as e:
            return [f"❌ Invalid XML: {e}"]

class check_yaml:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                yaml.safe_load(f)
            return ["✅ Valid YAML file."]
        except Exception as e:
            return [f"❌ Invalid YAML: {e}"]

class check_ini:
    @staticmethod
    def validate(file_path):
        config = configparser.ConfigParser()
        try:
            config.read(file_path, encoding='utf-8')
            return ["✅ Valid INI file."]
        except Exception as e:
            return [f"❌ Invalid INI: {e}"]

class check_html:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if "<html" in content.lower() and "</html>" in content.lower():
                return ["✅ Likely valid HTML."]
            return ["⚠️ No <html> tags found."]
        except Exception as e:
            return [f"❌ Error reading HTML: {e}"]

class check_md:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            headings = len(re.findall(r'^#+ ', content, re.MULTILINE))
            return [f"✅ Markdown file with {headings} headings."]
        except Exception as e:
            return [f"❌ Invalid Markdown: {e}"]

class check_csv:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                rows = list(reader)
                if not rows:
                    return ["⚠️ Empty CSV file."]
                return [f"✅ Valid CSV with {len(rows)} rows."]
        except Exception as e:
            return [f"❌ Invalid CSV: {e}"]

class check_log:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            return [f"✅ Log file with {len(lines)} lines."]
        except Exception as e:
            return [f"❌ Cannot read log file: {e}"]

class check_python:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                compile(f.read(), file_path, 'exec')
            return ["✅ Python script is syntactically valid."]
        except Exception as e:
            return [f"❌ Python error: {e}"]

class check_css:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if "{" in content and "}" in content:
                return ["✅ CSS syntax appears valid."]
            return ["⚠️ Could not find CSS blocks."]
        except Exception as e:
            return [f"❌ CSS error: {e}"]

class check_js:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if "function" in content or "=>" in content:
                return ["✅ JavaScript detected."]
            return ["⚠️ No JS functions found."]
        except Exception as e:
            return [f"❌ JavaScript read error: {e}"]

class check_shell:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if "#!" in content or "echo" in content:
                return ["✅ Shell script detected."]
            return ["⚠️ Might not be a real shell script."]
        except Exception as e:
            return [f"❌ Shell script error: {e}"]

class check_sql:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if re.search(r"\bSELECT\b|\bINSERT\b|\bUPDATE\b|\bDELETE\b", content, re.IGNORECASE):
                return ["✅ SQL commands found."]
            return ["⚠️ No standard SQL keywords found."]
        except Exception as e:
            return [f"❌ SQL file error: {e}"]

class check_tmx:
    @staticmethod
    def validate(file_path):
        return check_xml.validate(file_path)

class check_binary:
    @staticmethod
    def validate(file_path):
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(1024)
            if b'\0' in chunk:
                return ["✅ Likely binary file."]
            return ["⚠️ No binary signature found."]
        except Exception as e:
            return [f"❌ Binary check error: {e}"]
