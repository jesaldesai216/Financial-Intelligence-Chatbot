import streamlit as st
import os
import uuid
import pandas as pd
import io
from backend.api_handler import handle_user_query
from backend.history_manager import get_history, get_all_history, clear_history

st.set_page_config(page_title="🧠 Financial Chatbot", layout="wide")
st.title("🧠 Financial Intelligence Chatbot")

# Sidebar
st.sidebar.header("🔧 Configuration")

if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())
session_id = st.session_state["session_id"]

uploaded_file = st.sidebar.file_uploader("📁 Upload Financial Document", type=["csv", "xlsx", "pdf", "docx"],
                                         help="Upload your financial reports for analysis.")
query_url = st.sidebar.text_input("🌐 Or paste a link to a financial webpage for analysis",
                                  help="Enter a URL to scrape content from.")
user_lang = st.sidebar.selectbox("🌍 Response Language", ["en", "es", "fr", "de", "hi", "zh", "ar", "ru", "ja"],
                                 help="Choose the language for the chatbot's responses.")

st.sidebar.subheader("Chat History")
if st.sidebar.button("🗑️ Clear History", help="Clears the chat history for the current session."):
    clear_history()
    st.sidebar.success("Chat history cleared.")

if st.sidebar.button("📤 Export History", help="Exports the entire chat history to an Excel file."):
    data = get_all_history()
    if data:
        df = pd.DataFrame([{
            "timestamp": item.timestamp,
            "session_id": item.session_id,
            "query": item.query,
            "response": item.response,
            "file_name": item.file_name
        } for item in data])

        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        output.seek(0)

        st.sidebar.download_button(
            label="⬇️ Download Excel File",
            data=output,
            file_name="chat_history.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            help="Download the entire chat history as an Excel file."
        )
    else:
        st.sidebar.info("No chat history to export.")



# Main chat interface
st.subheader("💬 Ask a Financial Question")
chat_input = st.chat_input("Type your financial question here...")

                        #    placeholder="e.g., Summarize the key findings, What is the total revenue for 2023?")

if chat_input and (uploaded_file or query_url):
    filepath = None
    if uploaded_file:
        filepath = os.path.join("temp_files", uploaded_file.name)
        os.makedirs("temp_files", exist_ok=True)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.getbuffer())
    elif query_url:
        # Backend needs to handle the scraping of this URL
        filepath = query_url  # Pass the URL as the filepath for the backend to handle

    with st.chat_message("user"):
        st.markdown(chat_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = handle_user_query(chat_input, uploaded_file if uploaded_file else query_url, session_id, user_lang)
            st.markdown(response, unsafe_allow_html=True)


