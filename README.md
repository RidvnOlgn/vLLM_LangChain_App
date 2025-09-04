# vLLM and LangChain Application

This project is a language model application built using the `vllm` and `langchain` libraries.

## Requirements

*   Python 3.8+
*   NVIDIA GPU (required for vLLM)
*   CUDA Toolkit (must be compatible with your GPU and PyTorch version)

## Installation

It is strongly recommended to create and activate a virtual environment before starting the installation.

```bash
# Create a virtual environment in the project directory
python -m venv venv

# Activate the virtual environment
# For Windows:
.\venv\Scripts\activate
# For macOS/Linux:
# source venv/bin/activate
```

### 1. vLLM Installation

> **Important Note:** The `vLLM` library does not officially support Windows. It is required to run this project on WSL 2 (Windows Subsystem for Linux) or directly on a Linux distribution.

vLLM requires a specific installation depending on the NVIDIA GPU, CUDA version, and PyTorch version on your system. Therefore, a simple `pip install vllm` command usually does not work.

For the most accurate and up-to-date installation instructions, please visit the **[Official vLLM Installation Documentation](https://docs.vllm.ai/en/latest/getting_started/installation.html)**.

In the official documentation, you will find the appropriate `pip install` command for your system (CUDA version, PyTorch version). The installation usually consists of two steps:

1.  **Installing the appropriate PyTorch for your system.**
2.  **Installing vLLM.**

An example command might look like the following (Do not use this directly; find the one suitable for your system from the official documentation):

```bash
# Example: Installation for CUDA 12.1 with PyTorch 2.1.2
pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121
pip install vllm
```

### 2. Installing Other Dependencies

Install the project's other dependencies (like `langchain`). The best practice is to add these dependencies to a `requirements.txt` file.

```bash
pip install langchain
```

If you have created a `requirements.txt` file containing all dependencies, you can install them all at once:

```bash
pip install -r requirements.txt
```

## Running the Application

To run this project, you need to start the vLLM server first and then run the client application (`app.py`) in a separate terminal.

### Step 1: Start the vLLM Server

Open a terminal (ensure your virtual environment is activated) and run the following command to start the OpenAI-compatible server. This command will host the model that `app.py` connects to.

```bash
python -m vllm.entrypoints.openai.api_server --model "meta-llama/Meta-Llama-3-8B-Instruct"
```

- **Note:** The first time you run this, it will download the model from the Hugging Face Hub, which may take a significant amount of time and disk space.
- Keep this terminal open. The server is ready when you see log messages indicating it is running and waiting for requests.

### Step 2: Run the Client Application

Open a **new** terminal, activate the virtual environment again, and run the client script:

```bash
python app.py
```

You can now interact with the model through the terminal.