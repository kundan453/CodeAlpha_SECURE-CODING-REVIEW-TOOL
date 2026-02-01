import tkinter as tk
from tkinter import scrolledtext, messagebox

# ================= ROOT =================
root = tk.Tk()
root.title("Secure Coding Review Tool - Python")
root.geometry("1000x650")
root.configure(bg="#020617")

# ================= COLORS (10+) =================
COLORS = {
    "bg": "#020617",
    "title": "#22c55e",
    "text": "#e5e7eb",
    "critical": "#ef4444",
    "warning": "#f97316",
    "info": "#38bdf8",
    "success": "#10b981",
    "purple": "#a855f7",
    "yellow": "#facc15",
    "pink": "#ec4899",
    "gray": "#94a3b8"
}

# ================= TITLE =================
tk.Label(
    root,
    text="SECURE CODING REVIEW – PYTHON",
    font=("Consolas", 20, "bold"),
    fg=COLORS["title"],
    bg=COLORS["bg"]
).pack(pady=10)

# ================= INPUT LABEL =================
tk.Label(
    root,
    text="Paste Python Code Below:",
    fg=COLORS["info"],
    bg=COLORS["bg"],
    font=("Consolas", 11, "bold")
).pack()

# ================= CODE INPUT =================
code_input = scrolledtext.ScrolledText(
    root,
    width=120,
    height=16,
    bg="#020617",
    fg=COLORS["text"],
    insertbackground="white",
    font=("Consolas", 10)
)
code_input.pack(padx=10, pady=10)
code_input.focus_set()

# ENTER = newline fix
def insert_newline(event):
    code_input.insert(tk.INSERT, "\n")
    return "break"

code_input.bind("<Return>", insert_newline)

# ================= OUTPUT LABEL =================
tk.Label(
    root,
    text="Security Review Report:",
    fg=COLORS["purple"],
    bg=COLORS["bg"],
    font=("Consolas", 11, "bold")
).pack()

# ================= REPORT BOX =================
report = scrolledtext.ScrolledText(
    root,
    width=120,
    height=16,
    bg="#020617",
    fg=COLORS["gray"],
    insertbackground="white",
    font=("Consolas", 10)
)
report.pack(padx=10, pady=10)

# ================= TAGS =================
report.tag_config("CRITICAL", foreground=COLORS["critical"], font=("Consolas", 10, "bold"))
report.tag_config("WARNING", foreground=COLORS["warning"])
report.tag_config("INFO", foreground=COLORS["info"])
report.tag_config("SAFE", foreground=COLORS["success"])

# ================= ANALYSIS =================
def review_code():
    report.delete("1.0", tk.END)
    code = code_input.get("1.0", tk.END).strip()

    if not code:
        report.insert(
            tk.END,
            "[INFO] No code provided. Please paste Python code for review.\n",
            "INFO"
        )
        report.see(tk.END)
        return

    issues = 0

    def log(level, msg):
        report.insert(tk.END, f"[{level}] {msg}\n", level)

    log("INFO", "Starting secure code review...\n")

    if "eval(" in code or "exec(" in code:
        log("CRITICAL", "Use of eval/exec detected (Remote Code Execution risk).")
        log("INFO", "Fix: Remove eval/exec and use safe logic.")
        issues += 1

    if "password =" in code or "passwd =" in code or "secret =" in code:
        log("CRITICAL", "Hardcoded credentials detected.")
        log("INFO", "Fix: Use environment variables or secret manager.")
        issues += 1

    if "os.system" in code:
        log("CRITICAL", "Command Injection risk using os.system().")
        log("INFO", "Fix: Use subprocess with argument list.")
        issues += 1

    if "pickle.load" in code:
        log("WARNING", "Insecure deserialization using pickle.")
        log("INFO", "Fix: Avoid pickle with untrusted input.")
        issues += 1

    if "cursor.execute" in code and "%" in code:
        log("CRITICAL", "Possible SQL Injection vulnerability.")
        log("INFO", "Fix: Use parameterized queries.")
        issues += 1

    if "debug=True" in code:
        log("WARNING", "Debug mode enabled.")
        log("INFO", "Fix: Disable debug mode in production.")
        issues += 1

    if issues == 0:
        log("SAFE", "No common security vulnerabilities detected.")

    report.see(tk.END)

# ================= BUTTON =================
tk.Button(
    root,
    text="RUN SECURITY REVIEW",
    bg=COLORS["yellow"],
    fg="black",
    font=("Consolas", 12, "bold"),
    command=review_code
).pack(pady=10)

# ================= FOOTER =================
tk.Label(
    root,
    text="Follow On Instagram :- codewithiitian",
    fg=COLORS["pink"],
    bg=COLORS["bg"],
    font=("Consolas", 12, "bold")
).pack(pady=5)

root.mainloop()
