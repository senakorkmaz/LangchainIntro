#  LangChain Intro
This project contains examples demonstrating how to build basic language model (LLM) applications using the [LangChain](https://www.langchain.com/) library. The goal is to introduce the core components of LangChain and teach how to develop LLM-based applications.
## 📂 Project Structure

```
LangchainIntro/
├── simple_message.py
├── simple_message_with_templates.py
├── simple_message_with_output_parser.py
├── serve.py
├── requirements.txt
└── .gitignore
```

### File Descriptions

- `simple_message.py`: A basic example of an LLM call.
- `simple_message_with_templates.py`: Example of creating dynamic prompts using PromptTemplate.
- `simple_message_with_output_parser.py`: Example of structuring model output using OutputParser.
- `serve.py`: An interactive chatbot application with a Streamlit interface.

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/senakorkmaz/LangchainIntro.git
cd LangchainIntro
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
(Optional for tracing)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=SIMPLECHATBOT
```

### 5. Run the examples

You can run each Python file separately to try out different LangChain features:
```bash
python simple_message.py
python simple_message_with_templates.py
python simple_message_with_output_parser.py
```

## 📌 Notes

- The `serve.py` file provides an interface for chatting interactively with the model.
- The `simple_message_with_output_parser.py` file demonstrates how to use an OutputParser to structure the model's output.


