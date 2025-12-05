# CALCULATOR PARSER – ANTLR & Python Project

## ⭐ Project Summary
This project implements a **mathematical expression parser and evaluator** using **ANTLR** and **Python**.  
It defines a full grammar for a basic calculator capable of handling arithmetic expressions, variables, parentheses, and operator precedence.  
The goal is to demonstrate how to design grammars, generate parsers automatically, and integrate them into a Python runtime environment.

The project is structured as a compact educational exercise in compiler construction and language processing.

---

## 🧩 Technologies & Skills Demonstrated

### **Language Processing / Compilers**
- Grammar design with ANTLR  
- Parsing arithmetic expressions  
- Tokenization rules & operator precedence  
- Abstract syntax tree generation  
- Evaluation of parsed expressions  

### **Python Development**
- Integration of ANTLR-generated parser into Python  
- Execution pipeline for evaluating expressions  
- Clean modular code  
- Command-line interaction with the calculator  

### **General Software Engineering**
- Workflow automation  
- Environment setup using virtual environments  
- Error handling and validation  

---

## 📁 Project Structure

```
LF-Calculator-Parser-ANTLR-Python/
│
├── Calculator.g4       → ANTLR grammar defining the calculator language
├── main.py             → Entry point: loads parser, evaluates expressions
└── readme.md           → Original documentation provided by the authors
```

### Design Philosophy
- **Grammar-first approach:** The grammar fully defines the calculator language.  
- **Generator-based workflow:** ANTLR generates the lexer/parser instead of writing them manually.  
- **Lightweight runtime:** Python executes the parsed expressions.  
- **Extensibility:** The grammar can be expanded (functions, assignments, unary ops…).  

---

## 🔍 Project Details

### **1. Grammar Definition (`Calculator.g4`)**
The grammar describes:
- Numbers  
- Variables  
- Parentheses  
- Addition, subtraction, multiplication, division  
- Operator precedence and evaluation order  

ANTLR uses this grammar to generate:
- A **lexer** (tokenizer)  
- A **parser** (syntax analyzer)  
- A syntax tree that `main.py` processes  

---

### **2. Python Runtime (`main.py`)**
The script:
1. Loads the generated ANTLR classes  
2. Reads an arithmetic expression  
3. Parses it into a syntax tree  
4. Evaluates the expression  
5. Prints the result

It serves as a simple interactive calculator.

---

### **3. Example Usage**
```
3 + 4 * (2 - 1)
```
Result:
```
7
```

The parser automatically handles operator precedence.

---

## ▶️ How to Run the Project

### **1. Create a virtual environment**
```
python3 -m venv venv
```

### **2. Activate it**
Linux/macOS:
```
source venv/bin/activate
```

Windows:
```
venv\Scripts\activate
```

### **3. Install ANTLR runtime**
```
pip install antlr4-python3-runtime
```

### **4. Generate the parser**
Inside the project folder:
```
antlr4 -Dlanguage=Python3 Calculator.g4
```

### **5. Run the calculator**
```
python3 main.py
```

The program will prompt you to input an arithmetic expression.

---

## ✔ Summary
This project showcases the construction of a fully functional **calculator parser** using ANTLR and Python.  
It demonstrates grammar design, parsing, and expression evaluation in a clean and educational structure.  
Ideal for learning compiler basics, language design, and parser-based program execution.

