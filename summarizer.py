import os
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

key = os.getenv("AZURE_API_KEY")
endpoint = os.getenv("AZURE_ENDPOINT")

# Authenticate client
credential = AzureKeyCredential(key)
client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

def summarize_news(article_text):
    documents = [article_text]
    
    poller = client.begin_extract_summary(documents)
    response = poller.result()

    summary = ""
    for doc in response:
        if not doc.is_error:
            for sentence in doc.sentences:
                summary += sentence.text + " "
        else:
            summary = "Error in summarization."

    return summary
