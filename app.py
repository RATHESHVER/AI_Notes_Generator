import streamlit as st
import PyPDF2
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Notes Generator (GenAI)",
    layout="wide"
)

# ---------------- FUNCTIONS ------------------

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text


def chunk_text(text, chunk_size=1200):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def generate_notes(chunk, difficulty, subject):
    prompt = f"""
You are an expert {subject} teacher.

Difficulty level: {difficulty}

From the content below, generate:
1. Short, clear study notes
2. Important key points
3. 3 questions for 2 marks
4. 3 questions for 5 marks
5. 2 questions for 10 marks

Use simple, exam-oriented language.

CONTENT:
{chunk}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    return response.json()["response"]

# ---------------- UI ------------------

st.title("📘 AI Notes Generator using GenAI")
st.markdown("Generate **exam-oriented notes and questions** from PDF files")

uploaded_file = st.file_uploader("📄 Upload a PDF file", type=["pdf"])

col1, col2 = st.columns(2)

with col1:
    difficulty = st.selectbox(
        "🎯 Select Difficulty Level",
        ["Beginner", "Intermediate", "Exam-Oriented"]
    )

with col2:
    subject = st.selectbox(
        "📚 Select Subject Type",
        ["General", "Engineering", "Medical"]
    )

if uploaded_file and st.button("🚀 Generate Notes"):
    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    if not text.strip():
        st.error("❌ No readable text found in the PDF.")
    else:
        chunks = chunk_text(text)
        final_notes = ""
        progress = st.progress(0)

        for i, chunk in enumerate(chunks):
            notes = generate_notes(chunk, difficulty, subject)
            final_notes += notes + "\n\n"
            progress.progress((i + 1) / len(chunks))

        st.success("✅ Notes generated successfully!")

        st.markdown("## 📝 Generated Notes")
        st.markdown(final_notes)

        st.download_button(
            label="📥 Download Notes",
            data=final_notes,
            file_name="AI_Generated_Notes.txt",
            mime="text/plain"
        )
