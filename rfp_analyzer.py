import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the API keys from your .env file
load_dotenv()

# --- 1. Define the Strict Data Schema (Pydantic) ---
class RFPRequirements(BaseModel):
    core_problem: str = Field(description="The primary business problem the client is facing.")
    technical_stack: list[str] = Field(description="List of specific technical services requested.")
    compliance_risks: list[str] = Field(description="Any regulatory or budget constraints mentioned.")

# --- 2. Initialize the LLM ---
print("🚀 Initializing Dynamic GenAI RFP Pipeline...")
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.1
)

structured_extractor = llm.with_structured_output(RFPRequirements)

# --- 3. Dynamic Terminal Inputs ---
print("\n--- RFP Solutioning Assistant Configuration ---")
rfp_filename = input("📄 Enter the RFP file name to analyze (default 'mock_rfp.txt'): ").strip()
if not rfp_filename:
    rfp_filename = "mock_rfp.txt"

target_industry = input("🏢 Enter the target client industry or vertical (e.g., Retail Logistics, Fintech, Healthcare): ").strip()
service_focus = input("💼 Enter the primary service focus to pitch (e.g., Cloud Modernization, GenAI Automation, Data Engineering): ").strip()

# --- 4. Ingest the Document ---
print(f"\nReading RFP document from {rfp_filename}...")
try:
    with open(rfp_filename, "r", encoding="utf-8") as file:
        rfp_text = file.read()
except FileNotFoundError:
    print(f"❌ Error: Could not find file '{rfp_filename}'. Make sure it's in the current folder.")
    exit()

# --- 5. Pass 1: Extraction ---
print("🧠 Extracting structured requirements via Pydantic schema...")
extracted_data = structured_extractor.invoke(
    f"Analyze this RFP document for a {target_industry} company and extract requirements: {rfp_text}"
)

print("\n--- STRUCTURED EXTRACTION OUTPUT ---")
print(f"Problem: {extracted_data.core_problem}")
print(f"Tech Stack: {extracted_data.technical_stack}")
print(f"Constraints: {extracted_data.compliance_risks}")
print("------------------------------------\n")

# --- 6. Pass 2: Dynamic GTM Solutioning ---
print(f"🎯 Generating tailored Go-To-Market Pitch focusing on {service_focus}...")

strategy_prompt = f"""
You are an Enterprise Sales Strategist for a global IT services firm like Hexaware.
Review the following extracted requirements from a {target_industry} RFP:

Client Problem: {extracted_data.core_problem}
Requested Tech: {extracted_data.technical_stack}
Constraints: {extracted_data.compliance_risks}

Draft a concise, 3-paragraph Go-To-Market overlay sales strategy. 
Specifically emphasize how our expertise in {service_focus} can solve their underlying issues while strictly honoring their listed compliance and budget constraints.
"""

final_pitch = llm.invoke(strategy_prompt)

# Save the final output safely handling list/dict formats
with open("gtm_sales_strategy.md", "w", encoding="utf-8") as out_file:
    content = final_pitch.content
    if isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, str):
                text_parts.append(item)
            elif isinstance(item, dict) and "text" in item:
                text_parts.append(item["text"])
            else:
                text_parts.append(str(item))
        content_to_write = "".join(text_parts)
    else:
        content_to_write = str(content)
        
    out_file.write(content_to_write)

print("✅ Pipeline Complete! Custom strategy saved to gtm_sales_strategy.md")