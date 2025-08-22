📐 MathServer – MCP Project

MathServer is a simple Model Context Protocol (MCP) server built in Python that provides math operations (addition, subtraction, multiplication, division, etc.) through an API.
It is designed to be connected with MCP-compatible clients like chatbots or automation tools.

This project demonstrates how to create a custom MCP server for handling computations.

🌟 Features

✅ Supports basic math operations: addition, subtraction, multiplication, division

✅ Written in pure Python

✅ Easy to extend with new math functions (power, square root, modulo, etc.)

✅ Works as a local MCP server that clients can connect to

✅ Clean project structure with virtual environment setup

📂 Project Structure
mathserver/
├── server.py          # Main MCP math server (math logic lives here)
├── requirements.txt   # Dependencies (install with pip)
├── README.md          # Documentation
└── .gitignore         # Ignore .env, venv, cache files


server.py → contains the Python code for math operations

requirements.txt → contains libraries to install before running

.gitignore → ignores virtual environments and secret files

🛠️ Installation
1. Clone the repository
git clone https://github.com/your-username/mathserver.git
cd mathserver

2. Create a virtual environment
python -m venv .venv

3. Activate the virtual environment

Windows (Command Prompt):

.venv\Scripts\activate


Windows (PowerShell):

.venv\Scripts\Activate.ps1


Linux/Mac:

source .venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

▶️ Usage

Run the math server with:

python server.py


Once running, clients can send math requests.

Example Request
{
  "operation": "add",
  "numbers": [5, 10]
}

Example Response
{
  "result": 15
}

Other Supported Operations

sub → subtraction

mul → multiplication

div → division (handles divide-by-zero safely)

🧩 Extending the Server

You can easily add more operations inside server.py.
For example, to add power (^):

def power(a, b):
    return a ** b


Then update your request handler to support "operation": "power".

🤝 Contributing

Contributions are welcome! 🚀
If you’d like to add new math operations, improve the server, or fix bugs:

Fork the repo

Create a feature branch (git checkout -b feature-new-operation)

Commit your changes (git commit -m "Add power operation")

Push to the branch (git push origin feature-new-operation)

Open a Pull Request
