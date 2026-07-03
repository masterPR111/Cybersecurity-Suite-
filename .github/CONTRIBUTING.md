---

## 📁 **Folder Structure එක**

```
Cybersecurity-Suite-/
├── .github/
│   ├── CONTRIBUTING.md          ← මෙය
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── cybersuite.py
├── README.md
├── LICENSE
└── requirements.txt
```

---

## 📝 **CONTRIBUTING.md - Complete Content**

**මෙය copy කරලා `.github/CONTRIBUTING.md` ලෙස save කරන්න:**

```markdown
# 🤝 Contributing to Cybersecurity Suite

First off, thank you for considering contributing to Cybersecurity Suite! 🎉 It's people like you that make this open-source project great.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
- [Getting Help](#getting-help)

---

## 📜 Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). We expect all contributors to be respectful and inclusive.

---

## 🎯 How Can I Contribute?

### 🐛 Reporting Bugs

If you find a bug, please create an issue with the following:

1. **Describe the bug** - What happened? What did you expect?
2. **Steps to reproduce** - How can we reproduce it?
3. **Environment** - OS, Python version, terminal type
4. **Screenshots** - If applicable, add screenshots
5. **Additional context** - Any other relevant information

**Bug Report Template:**
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Run `python3 cybersuite.py`
2. Select option '...'
3. See error

**Expected behavior**
What you expected to happen.

**Environment:**
- OS: [e.g. Kali Linux 2024.1]
- Python Version: [e.g. 3.13.0]
- Terminal: [e.g. bash]

**Additional context**
Add any other context here.
```

---

### 💡 Suggesting Features

Have an idea for a new tool or improvement? Open a feature request!

1. **Clear title** - What is the feature?
2. **Detailed description** - What does it do and why is it useful?
3. **Use case** - How would someone use this?
4. **Possible implementation** - Any ideas on how to implement it?

**Feature Request Template:**
```markdown
**Feature Name**
[Short name for the feature]

**Description**
[Detailed description of what the feature does]

**Use Case**
[Why is this useful? Who would use it?]

**Implementation Ideas**
[Any suggestions on how to implement it]

**Additional Context**
[Any other information]
```

---

## 🔧 Development Setup

### 1. Fork & Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/your-username/Cybersecurity-Suite-.git
cd Cybersecurity-Suite-
```

### 2. Set Up Environment

```bash
# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Make Your Changes

```bash
# Create a new branch
git checkout -b feature/your-feature-name

# Make your changes
# Test your changes
python3 cybersuite.py
```

### 4. Commit & Push

```bash
git add .
git commit -m "Add: Your feature description"
git push origin feature/your-feature-name
```

### 5. Create Pull Request

Go to the original repository and click "New Pull Request".

---

## 📝 Pull Request Guidelines

### Before Submitting

- [ ] Check that your code works
- [ ] Test all affected features
- [ ] Update documentation if needed
- [ ] Follow style guidelines
- [ ] Keep changes focused (one PR = one feature/fix)

### PR Description Template

```markdown
## Description
[What does this PR do?]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactor
- [ ] Performance improvement

## Testing
[How did you test this?]

## Checklist
- [ ] Code works
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No breaking changes

## Screenshots (if applicable)
[Add screenshots here]
```

---

## 🎨 Style Guidelines

### Python Code Style

- Follow **PEP 8** guidelines
- Use **4 spaces** for indentation
- Maximum line length: **79 characters** (or 99 for docstrings)
- Use **descriptive variable names**

### Function Documentation

```python
def function_name(param1, param2):
    """
    Brief description of what the function does.

    Args:
        param1 (str): Description of param1
        param2 (int): Description of param2

    Returns:
        bool: Description of return value

    Example:
        >>> function_name("test", 1)
        True
    """
    pass
```

### Code Examples

**Good ✅:**
```python
def check_breach(email):
    """Check if email has been breached."""
    try:
        response = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}")
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
```

**Bad ❌:**
```python
def c(e):
    try:
        r=requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{e}")
        if r.status_code==200:return r.json()
        return None
    except Exception as e:print(f"Error: {e}")
```

---

## 🧪 Testing

Before submitting, test your changes:

```bash
# Run the tool
python3 cybersuite.py

# Test all features
# 1. Linux Hardening
# 2. System Update
# 3. Breach Check
# ... test all 19 tools
```

---

## ❓ Getting Help

- Open an issue with your question
- Tag issues with `question` label
- Check existing documentation

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🌟 Contributors

Thank you to all contributors!

[![Contributors](https://img.shields.io/github/contributors/masterPR111/Cybersecurity-Suite-)](https://github.com/masterPR111/Cybersecurity-Suite-/graphs/contributors)

---

**Thank you for contributing! 🚀**
```

---
