import tkinter as tk
from tkinter import filedialog, messagebox

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi   

def kmp_string_matching(target_text, pattern):
    n = len(target_text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    occurrences = []
    for i in range(n):
        while q > 0 and pattern[q] != target_text[i]:
            q = pi[q - 1]
        if pattern[q] == target_text[i]:
            q += 1  
        if q == m:
            occurrences.append(i - m + 1)
            q = pi[q - 1]
    return occurrences

def tokenize_text(text):
    tokens = []
    current_token = ''
    for char in text:
        if char.isalnum():
            current_token += char
        elif current_token:
            tokens.append(current_token)
            current_token = ''
    if current_token:
        tokens.append(current_token)
    return tokens

def calculate_plagiarism_percentage(target_text, reference_text):
    target_tokens = tokenize_text(target_text.lower())
    reference_tokens = tokenize_text(reference_text.lower())
    
    # Calculate plagiarism percentage based on KMP string matching
    plagiarism_count = 0
    for token in target_tokens:
        occurrences = kmp_string_matching(" ".join(reference_tokens), token)
        plagiarism_count += len(occurrences)
    
    # Calculate plagiarism percentage as a percentage of total tokens
    total_tokens = len(target_tokens)
    plagiarism_percentage = (plagiarism_count / total_tokens) * 100
    return plagiarism_percentage

def calculate_button_click():
    target_text = target_text_entry.get("1.0", "end-1c")
    reference_text = reference_text_entry.get("1.0", "end-1c")
    
    plagiarism_percentage = calculate_plagiarism_percentage(target_text, reference_text)
    result_label.config(text=f"Plagiarism percentage: {plagiarism_percentage:.2f}%")

# Create the main window
root = tk.Tk()
root.title("Plagiarism Checker")

# Create input fields
target_text_label = tk.Label(root, text="Enter Target Text:")
target_text_entry = tk.Text(root, height=5, width=40)
reference_text_label = tk.Label(root, text="Enter Reference Text:")
reference_text_entry = tk.Text(root, height=5, width=40)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate Plagiarism Percentage", command=calculate_button_click)

# Create result label
result_label = tk.Label(root, text="")

# Arrange widgets using grid layout
target_text_label.grid(row=0, column=0, padx=10, pady=5)
target_text_entry.grid(row=0, column=1, padx=10, pady=5)
reference_text_label.grid(row=1, column=0, padx=10, pady=5)
reference_text_entry.grid(row=1, column=1, padx=10, pady=5)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
