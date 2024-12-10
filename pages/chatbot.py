import streamlit as st
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

st.set_page_config(
    page_title="Celerates's Group 9",
    layout="centered",
    initial_sidebar_state="expanded",
    page_icon="icons/smart_toy.svg")


def chat(contexts, history, question):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        api_key=API_KEY
        )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. You can use given data to answer question about product.",),
            ("human", "You have access to the following data: {contexts}. Refer to this data and the recent conversation history: {history} to provide a concise and accurate answer to the user's query: {question}. Your response should be relevant, clear, and contextual."),
        ]
    )
    
    chain = prompt | llm
    completion = chain.invoke(
        {
            "contexts": contexts,
            "history": history,
            "question": question,
        }
    )

    answer = completion.content

    result = {}
    result["answer"] = answer
    return result


df = pd.read_csv("datasets/coffeeshop_kmeans_clustered.csv")
contexts = df.to_string()  # Initialize contexts


# Sidebar for API Key Validation
with st.sidebar:
    st.sidebar.title("Configuration")
    api_valid = False
    # API Key Input
    API_KEY = st.text_input("Enter your Gemini API Key", type="password")
    if API_KEY:
        try:
            # Validate API key
            llm = ChatGoogleGenerativeAI(
                model="gemini-1.5-flash",
                temperature=0.7,
                api_key=API_KEY
            )
            llm.predict("Hello")
            st.success("API key is valid.")
            api_valid = True
        except Exception as e:
            st.error("Invalid API key. Please check and try again.")
    else:
        st.info("Enter your API key to proceed.")

st.title("AI Chatbot Assistant")

recommended_questions = [
    "Bagaimana Segmentasi Cluster pada Dataset ini?",
    "Bagaimana Hubungan antara Product Name dengan Unit Price berdasarkan Cluster?",
    "Berapa Rentang Harga untuk setiap Cluster?",
    "Berdasarkan Analisis Interpretasi Sebelumnya, Strategi Bisnis apa yang dapat diimplementasikan untuk meningkatkan penjualan?"
]
if "messages" not in st.session_state:
    st.session_state.messages = []


        # Ensure `history` is always defined
if st.session_state.messages:
    messages_history = st.session_state.messages[-10:]  # Get the last 10 messages
    history = "\n".join([f'{msg["role"]}: {msg["content"]}' for msg in messages_history])
else:
    history = ""  # Initialize empty history if no messages are available


if api_valid:
    with st.sidebar:
        st.markdown("Chatbot Assist")

        
        with st.expander("Rekomendasi Pertanyaan"):
            for i, question in enumerate(recommended_questions):
                if st.button(f"{i + 1}. {question}", key=f"question_{i}"):
                    # Jika tombol ditekan, tambahkan pertanyaan ke chat input secara otomatis
                    st.session_state.messages.append({"role": "user", "content": question})
                    
                    
                    # Proses jawaban untuk pertanyaan yang dipilih
                    response = chat(contexts, history, question)
                    answer = response["answer"]
                    
                    st.session_state.messages.append({"role": "assistant", "content": answer})

notif = st.chat_message("assistant")
if not api_valid:
    notif.write("Enter your API key to proceed.")
else:
    notif.write("Ask me anything! or You can see Recommended Questions in the sidebar")       
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    with st.spinner("Assistant is thinking..."):
        response = chat(contexts, history, prompt)
        answer = response["answer"]
    
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").markdown(answer)

