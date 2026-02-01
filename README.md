# Secure Coding Review Tool (Python)

A GUI-based **Secure Coding Review Tool** developed using **Python and Tkinter** to analyze source code and identify common security vulnerabilities using rule-based static analysis.

This project demonstrates secure coding review practices, manual inspection techniques, and basic static analysis concepts.

---

## 🎯 Objective

- Perform a secure code review on Python applications
- Identify common security vulnerabilities
- Provide clear remediation recommendations
- Promote secure coding best practices

---

## 🚀 Features

- GUI-based Python code review tool
- Detection of insecure coding patterns
- Rule-based static analysis
- Color-coded vulnerability severity
- Clear remediation suggestions
- Beginner-friendly and educational

---

## 🔍 Vulnerabilities Checked

- Use of `eval()` / `exec()` (Remote Code Execution risk)
- Hardcoded credentials
- Command Injection (`os.system`)
- Insecure deserialization (`pickle.load`)
- Possible SQL Injection patterns
- Debug mode enabled in production

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)

---

## ▶️ How to Run

```bash
python secure_code_review.py
