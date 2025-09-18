# 🏦 Verna Bank - Console-Based Python Bank System

A simple terminal-based **banking system** developed in Python, featuring:

- Secure user registration
- BPIN-based authentication
- Account & IFSC number generation
- Deposit & withdrawal system
- Balance checking

---

## ✨ Features

### 🔐 User Registration
- Collects name, age, gender
- Validates:
  - Phone number (must be 10 digits, no leading zero)
  - Gmail address (must end with `@gmail.com`)
  - Pincode (6 digits)

### 🧾 Verification
- Generates a secure **verification code** (alphanumeric)
- Generates a 4-digit **BPIN** for future authentication

### 🏦 Bank Account Generation
- Automatically creates:
  - 11-character Account Number (e.g., `1234ABC567SS`)
  - 16-character IFSC Code (e.g., `1234ABCD5678MSS7`)

### 💸 Banking Operations
- **Deposit** money using BPIN
- **Withdraw** funds (with balance checks)
- **View balance**
- **View registered profile**

---

## 🛠️ Technologies Used

- Python 3
- Built-in modules:
  - `random`
  - `string`
  - `re` (regex)
  - `time`

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Save the file as `verna_bank.py`.
3. run the file and have fun. 
