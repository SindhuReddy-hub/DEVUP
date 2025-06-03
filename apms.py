# Automated Problem Management System (APMS) - Prototype Code
# Goal: Parse RCA and chat logs, extract insights using LLM, create structured payload for ServiceNow

import re
import json
import requests
from transformers import pipeline
from typing import List, Dict

# Step 1: Sample inputs (RCA text + Chat log)
rca_text = """
Incident ID: INC123456
System Impacted: Payments Gateway
Root Cause: Misconfigured firewall blocked outbound API requests.
Resolution: Updated firewall rules to allow specific traffic.
"""

chat_log = """
[10:01 AM] Alice: We’re seeing dropped connections from the Payments system.
[10:05 AM] Bob: Confirmed. Looks like the firewall's blocking traffic to the payment API endpoint.
[10:15 AM] Alice: Adding exception in the firewall. Retesting now.
[10:20 AM] Bob: All good now. Root cause seems to be misconfigured firewall.
"""

# Step 2: Basic NLP preprocessing (optional if using LLM)
def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())

# Step 3: Use an LLM pipeline to extract entities (mocked with summarizer for now)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_summary(text: str) -> str:
    summary = summarizer(clean_text(text), max_length=60, min_length=20, do_sample=False)
    return summary[0]['summary_text']

# Step 4: Mocked entity extraction (replace with NER or LLM extraction)
def extract_entities(rca: str, chat: str) -> Dict:
    return {
        "problem_description": extract_summary(rca + " " + chat),
        "affected_component": "Payments Gateway",
        "category": "Firewall / Network",
        "root_cause": "Misconfigured firewall",
        "detected_by": "Alice",
        "timestamp": "2025-06-03T10:01:00Z"
    }

# Step 5: Generate ServiceNow-compatible payload
def generate_payload(entities: Dict) -> Dict:
    return {
        "short_description": entities['problem_description'],
        "category": entities['category'],
        "cmdb_ci": entities['affected_component'],
        "cause": entities['root_cause'],
        "caller_id": entities['detected_by'],
        "opened_at": entities['timestamp'],
        "assignment_group": "Network Operations",
        "state": "New"
    }

# Step 6: Send to ServiceNow (mocked REST API request)
def send_to_servicenow(payload: Dict):
    url = "https://your-instance.service-now.com/api/now/table/problem"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    auth = ("your-username", "your-password")
    # response = requests.post(url, headers=headers, auth=auth, json=payload)
    # return response.status_code, response.json()
    print("[MOCK] Would POST to ServiceNow:", json.dumps(payload, indent=2))

# Run the pipeline
entities = extract_entities(rca_text, chat_log)
payload = generate_payload(entities)
send_to_servicenow(payload)
