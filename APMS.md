📌 Project Title
Automated Problem Management System (APMS)
________________________________________
📄 Abstract
In large-scale enterprise environments like JPMC, managing recurring incidents and their underlying problems is crucial for maintaining service reliability. Manual problem record creation from RCA (Root Cause Analysis) documents and PARC (Problem and Root Cause) chat discussions is labor-intensive, error-prone, and inconsistent.
This project introduces the Automated Problem Management System (APMS)—a transformative AI-powered solution that automates the identification and creation of Problem records in ServiceNow. Leveraging advanced Natural Language Processing (NLP) and Generative AI techniques, APMS extracts insights from RCA documents and chat logs to generate structured, standardized problem records and tasks.
By integrating seamlessly with JPMC’s existing ServiceNow platform, APMS ensures compliance with internal problem management protocols while reducing manual effort and boosting consistency. Ultimately, this solution enables faster root cause documentation and resolution of recurring issues, driving operational efficiency.
________________________________________
🚩 Problem Statement
The current manual approach to parsing RCA documents and PARC chat transcripts for creating problem records in ServiceNow is time-consuming, inconsistent, and error-prone. This leads to delays in problem identification, inconsistent documentation, and slower resolution of recurring incidents.
________________________________________
🎯 Objective
• Automate the creation of Problem records and tasks in ServiceNow
• Extract insights from RCA documents and PARC chat logs using AI/NLP
• Improve consistency and accuracy in problem documentation
• Reduce manual effort and enable faster resolution of recurring issues
________________________________________
🏗️ System Design Overview
RCA Documents & PARC Chat Logs
       │
       ▼
  NLP/AI Text Parsing & Classification
       │
       ▼
  Structured Problem Record & Task Generation
       │
       ▼
  ServiceNow Integration (via API or platform connector)
________________________________________
⚙️ Tech Stack
• Python (for NLP pipeline and integration)
• Hugging Face Transformers / OpenAI API (for LLM/NLP parsing)
• spaCy or NLTK (for text preprocessing)
• ServiceNow API / IntegrationHub (for creating records/tasks)
• Docker (for deployment containerization)
________________________________________
🧪 Sample Input/Output (Illustrative Example)
Source Type	Input Excerpt	Output (Problem Record)
RCA Doc	"Service outage due to router misconfiguration on VLAN 203."	Problem: Network misconfiguration, Affected Component: VLAN 203
Chat Log	"We saw repeated failures post-patch deployment. Likely related to script error."	Problem: Automation script failure post-deployment
________________________________________
🧠 NLP Model Workflow
• Text Preprocessing: Cleaning, tokenization, stop-word removal
• Entity Recognition: Identify components, error types, timestamps
• Classification: Categorize problem type (e.g., network, automation, DB)
• Summarization: Extract concise problem statements from verbose input
• Integration Logic: Format output for ServiceNow record creation
________________________________________
💻 Planned UI or Monitoring Features (Optional)
• Web-based dashboard for problem record preview & approval
• Toggle for manual override/editing before submission
• Logs of processed documents/chats for audit trail
________________________________________
✅ Key Benefits
• Reduced manual intervention and analyst workload
• Higher accuracy and consistency in problem records
• Faster triaging and resolution of recurring incidents
• Improved compliance with organizational processes
________________________________________
📊 Expected Outcomes (Projected Metrics)
• 70–80% reduction in manual effort for problem documentation
• >90% accuracy in problem type and component extraction
• <5-minute turnaround time per problem record (vs. hours manually)
________________________________________
🧩 Next Steps / Future Scope
• Expand support to additional sources (e.g., Jira tickets, email threads)
• Train custom LLM on internal RCA/PARC language
• Add severity scoring for each problem detected
• Full integration with incident response workflows

