# Financial Intelligence Chatbot

## Project Overview

The Financial Intelligence Chatbot is designed to process and analyze financial documents of various formats (CSV, Excel, Links, PDF, DOCX). It aims to extract key financial insights, summarize content, and answer user queries based on the uploaded data. The chatbot autonomously determines the appropriate processing action or tool to invoke, providing a seamless experience for users seeking financial information and analysis.

## Code Structure

```
Financial Intelligence Chatbot
|
├───app.py
├───requirements.txt
├───backend
│   │   .env
│   │   api_handler.py         # Handles routing user requests to appropriate backend logic.
│   │   file_processor.py      # Manages file uploads and initial data processing.
│   │   history_manager.py     # (To be implemented) Manages chat and document history.
│   │   language_handler.py    # Handles language detection and translation.
│   │   large_data_processor.py# (Potentially for future) Handles very large datasets.
│   │   logger.py              # Configures logging for the application.
│   │   rag_handler.py         # (Potentially for future) Handles Retrieval-Augmented Generation for more complex queries.
│   │   router.py              # (Potentially for future) More advanced routing based on user intent.
│   │   summarizer.py          # Contains logic for summarizing text content.
│   │   table_analyzer.py      # Contains logic for analyzing tabular data (e.g., calculations).
│   │   table_query.py         # Contains logic for querying specific information from tables.
│   │   visualizer.py          # Contains logic for generating charts and visualizations.
│   │   web_scraper.py         # Handles fetching and extracting content from URLs.
│
├───logs                     # Directory to store application logs.
├───temp_files               # Directory for temporary file storage during processing.
├───utils
│   │   config_loader.py     # (Potentially for future) Loads configuration settings.
│   │   helpers.py           # Contains utility functions.
│
└───vector_store             # (Potentially for future) Directory for storing vector embeddings for RAG.
```

## Simple Explanation

This project provides a chatbot that can understand your questions about financial documents. You can upload files like CSVs, Excel sheets, PDFs, and Word documents, or provide links to online reports. The chatbot will then try to understand what you're asking – whether you want to see trends, compare numbers, get a summary, or find specific data in a table. Behind the scenes, it uses different tools (like web scraping for links, Pandas for tables, and language models for understanding and summarizing) to get you the information you need.

## Setup to Run the File

This guide assumes you have Python 3.11 installed on your system.

### Steps to Create and Activate the Environment

1.  **Create a Virtual Environment:** Open your terminal or command prompt and navigate to the root directory of your project (`Financial-Intelligence-Chatbot`). Then, create a virtual environment using `venv`:

    ```bash
    python -m venv venv
    ```

2.  **Activate the Virtual Environment:**

    * **On Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    * **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

    Your terminal prompt should now be prefixed with `(venv)`, indicating that the virtual environment is active.

### Install Dependencies

1.  Navigate to the root directory of your project if you're not already there.
2.  Install the required Python libraries using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Configure Environment Variables

1.  Navigate to the `backend` directory.
2.  Create a file named `.env` if it doesn't exist.
3.  **Set your OpenAI API Key:** Add the following line to your `.env` file, replacing `YOUR_OPENAI_API_KEY` with your actual OpenAI API key:

    ```
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

    **(How to create an OpenAI API Key):**
    * Go to the [OpenAI Platform website](https://platform.openai.com/).
    * If you don't have an account, sign up.
    * Once logged in, navigate to the "API keys" section (usually under your profile or settings).
    * Click on "Create new secret key".
    * Copy the generated API key and paste it into your `.env` file. **Keep this key secure and do not share it.**

### Run the Application

The main entry point for your application is likely `app.py` (if you are using Streamlit for the frontend).

1.  Navigate to the root directory of your project in your terminal (where `app.py` is located).
2.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

    This command should open a new tab in your web browser with the chatbot interface.

## Simple Query Samples

Here are a few example queries you can try once the chatbot is running:

* **Financial Trend Analysis (assuming an uploaded Excel or CSV with "Date" and "Revenue" columns):**
    ```
    Show me the revenue trends over time.
    ```
* **Comparative Analysis (assuming uploaded PDF reports with expense data):**
    ```
    Compare the total expenses in the last two reports.
    ```
* **Statistical Summaries (assuming uploaded CSV data with a "Profit" column):**
    ```
    What is the average profit?
    ```
* **Detailed Document Summaries (assuming uploaded DOCX or PDF):**
    ```
    Summarize the key points of this document.
    ```
* **Data Extraction from Tables (assuming a table in an uploaded Excel or web page):**
    ```
    Extract the top 3 products by sales.
    ```
* **Web Content Analysis (using a link):**
    ```
    Summarize the key findings from this URL: [paste a financial news URL here]
    ```

## How to Create an NVIDIA NIM Key

Based on the initial code, you were using the NVIDIA API. If you want to use NVIDIA NIM (NVIDIA Inference Microservices), the process to obtain an API key would be different from OpenAI.

1.  **Access NVIDIA Cloud:** You would typically need to have access to the NVIDIA Cloud platform or a service that integrates with NIM. This might require an organizational account or specific subscriptions.
2.  **NIM Service/Endpoint:** Identify the specific NIM service or endpoint you intend to use (e.g., a summarization model, a data analysis service).
3.  **API Key Generation:** The method for generating an API key for NVIDIA NIM would depend on the platform or service you are using. It might involve:
    * Logging into the NVIDIA Cloud portal.
    * Navigating to a section related to API keys or credentials.
    * Creating a new API key associated with your account or the specific NIM service you want to access.
4.  **Documentation:** Refer to the official documentation of the NVIDIA NIM service you are using for detailed instructions on API key management and authentication.

