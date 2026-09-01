# GenAI RFP Analysis & GTM Solutioning Assistant

A dynamic Python-based document processing pipeline that leverages LangChain, Pydantic, and Gemini to ingest unstructured enterprise Requests for Proposals (RFPs), extract critical core requirements, and autonomously generate executive-ready Go-To-Market (GTM) overlay sales strategies.

## 🚀 Key Features
* **Structured Data Extraction:** Utilizes Pydantic schemas to enforce strict JSON outputs from LLMs, eliminating hallucination during document parsing.
* **Dynamic Pipeline Architecture:** Interactive terminal inputs allow users to target custom RFP text files, specific industry verticals, and tailored technical service focuses on the fly.
* **Automated GTM Generation:** Converts dense technical constraints and project scopes into actionable, 3-paragraph executive sales strategies.

## 🛠️ Tech Stack
* **Python**
* **LangChain**
* **Google GenAI SDK (Gemini 3.6 Flash)**
* **Pydantic**
* **Python-Dotenv**

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ArinDaniell/gtm-solutioning-assistant.git](https://github.com/ArinDaniell/gtm-solutioning-assistant.git)
   cd gtm-solutioning-assistant
