# SecurePass Generator

A simple yet robust cross-platform **Random Password Generator** built using **Python** and the **Tkinter** GUI library. This application allows users to generate strong, customizable passwords based on desired length and character sets, and provides a strength assessment based on **entropy**.

## ✨ Features

* **Custom Length:** Generate passwords from 4 to 64 characters long.
* **Character Set Selection:** Choose to include uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and symbols (!@#).
* **Character Exclusion:** Easily specify characters to exclude (e.g., 'l', '1', 'O', '0') to avoid ambiguous characters.
* **Mandatory Character Inclusion:** Ensures at least one character from each selected set is included for maximum strength.
* **Password Strength Assessment:** Calculates the password's **entropy** (measured in bits) to provide a strength rating (Weak, Moderate, Strong).
* **Copy to Clipboard:** One-click button to securely copy the generated password.
* **Secure Randomness:** Uses Python's `secrets` module for cryptographically strong random number generation.

## 💻 Requirements

To run this application, you need **Python 3.x** installed. The only external dependency is the `math` module (which is built-in) and the standard library modules `tkinter`, `string`, and `secrets`.

See the `requirements.txt` file for details.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.x installed.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/anmolingle/OIBSIP_Python_Task5.git
    cd OIBSIP_Python_Task5
    ```
2.  **Install dependencies** (Tkinter is usually included with standard Python installations, but this step is good practice):
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

Execute the Python script directly:

```bash
python Random_Password_Generator.py
````

## ⚙️ How It Works

The password strength is assessed using the concept of **information entropy** in bits, which measures the unpredictability of the password.

The formula used is:
$$ \text{Entropy} = \text{Length} \times \log_2(\text{Pool Size}) $$

Where:

  * **Length** is the number of characters in the password.
  * **Pool Size** is the total number of unique characters available for generating the password (based on selected and excluded character sets).

| Entropy (Bits) | Strength Rating |
| :---: | :---: |
| $< 50$ | **Weak** (Red) |
| $50 - 79$ | **Moderate** (Orange) |
| $\ge 80$ | **Strong** (Green) |

## 🤝 Contributing

Contributions are welcome\! Feel free to open issues or submit pull requests with improvements, bug fixes, or new features.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

```
