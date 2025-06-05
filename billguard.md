Project Title
Bill Guard: Intelligent Cost Monitoring and Optimization for AWS
Abstract
Cloud spending can quickly spiral out of control due to dynamic workloads, unforeseen usage patterns, or configuration drift. Bill Guard is an intelligent AWS billing assistant that not only alerts users about abnormal cost spikes in real time but also predicts future billing trends and offers actionable cost optimization recommendations using machine learning models. The system leverages AWS Cost Explorer and CloudWatch for data ingestion and monitoring, and integrates predictive analytics to forecast expenses and optimize resource utilization.
Problem Statement
AWS users often receive billing alerts too late to take preventive actions. There’s a lack of proactive insight into what causes bill spikes and how to reduce them before they happen.
Objectives
•	Detect cost anomalies using AWS CloudWatch.
•	Forecast future AWS bills using ML models.
•	Recommend cost-saving actions based on usage patterns.
•	Provide a Streamlit dashboard for visual insights.

Tech Stack
•	AWS Services: Cost Explorer, CloudWatch, S3 (for logs)
•	Languages: Python
•	Libraries: Boto3, Scikit-learn/XGBoost, Pandas, Matplotlib, Streamlit

Sample dummy data

Future Scope
•	Add anomaly detection (e.g., Isolation Forest) for cost spikes.
•	Integrate with AWS Budgets API for automation.
•	NLP summarization of billing trends via chatbot.

