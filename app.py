import streamlit as st
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Spam & Phishing Email Detector",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

/* Main App */
.stApp{
    background: linear-gradient(135deg,#F5FAFF,#EAF4FF);
}

/* Reduce top padding */
.main{
    padding-top:0.5rem;
}

/* Main title */
h1{
    color:#0D47A1;
    text-align:center;
    font-weight:700;
}

/* Headers */
h2,h3{
    color:#1565C0;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#FFFFFF;
    border-right:1px solid #E3EAF3;
}

/* Metric cards */
[data-testid="metric-container"]{
    background:white;
    border:1px solid #E6EEF7;
    padding:18px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.05);
}

/* Text Input */
div[data-testid="stTextInput"] input{
    border-radius:10px;
    border:1px solid #C7D9F2;
}

/* Text Area */
textarea{
    border-radius:10px !important;
    border:1px solid #C7D9F2 !important;
}

/* Button */
.stButton>button{
    width:100%;
    height:52px;
    border-radius:12px;
    background:#1565C0;
    color:white;
    font-size:18px;
    font-weight:600;
    border:none;
}

.stButton>button:hover{
    background:#0D47A1;
    color:white;
}

/* Progress Bar */
.stProgress > div > div > div > div{
    background:#1565C0;
}

/* Footer */
footer{
    visibility:hidden;
}

/* Streamlit menu */
#MainMenu{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("models/spam_classifier.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.markdown(
    """
    <div style="text-align:center; font-size:70px;">
        🛡️
    </div>
    """,
    unsafe_allow_html=True

    )

    st.title("Spam Email Classifier")

    st.markdown("---")

    st.subheader("📊 Dataset")

    st.write("• Total Emails : **5,851**")
    st.write("• Spam : **1,426**")
    st.write("• Not Spam : **4,425**")

    st.markdown("---")

    st.subheader("🧠 Model")

    st.write("Algorithm")
    st.success("Multinomial Naive Bayes")

    st.write("Vectorizer")
    st.success("TF-IDF")

    st.write("Overall Accuracy")
    st.success("96%")

    st.markdown("---")

    st.subheader("⚙️ Technologies")

    st.write("""
- Python
- Streamlit
- Scikit-learn
- TF-IDF
- Joblib
""")

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.write("Kasi Rajan")

    st.caption("AI/ML Internship Project")

# -----------------------------
# Title
# -----------------------------
st.markdown("""
# 🛡️ AI-Powered Spam & Phishing Email Classifier

<div style='text-align:center;
font-size:18px;
color:#555;
margin-bottom:20px;'>

Secure Email Analysis using Machine Learning

</div>

""", unsafe_allow_html=True)

with st.container():

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Accuracy", "96%")

    with col2:
        st.metric("Model", "Naive Bayes")

    with col3:
        st.metric("Vectorizer", "TF-IDF")

# -----------------------------
# Email Input
# -----------------------------

st.markdown("### Analyze an Email")

st.caption(
    "Enter the email subject and body below to classify it as Spam or Legitimate."
)

st.header("📧 Email Analysis")

subject = st.text_input(
    "📨 Email Subject",
    placeholder="Enter the email subject..."
)

body = st.text_area(
    "📝 Email Body",
    height=250,
    placeholder="Paste the email content here..."
)

predict = st.button("🔍 Analyze Email")


if predict:

    if subject.strip() == "" and body.strip() == "":
        st.warning("Please enter an email subject or body.")

    else:

        combined_text = subject + " " + body

        vector = vectorizer.transform([combined_text])

        prediction = model.predict(vector)[0]

        probability = model.predict_proba(vector)[0]

        confidence = max(probability) * 100

        st.write("")
        st.write("")

        st.divider()

        if prediction == 1:

            st.error("🚨 Spam Email Detected")

            st.progress(confidence/100)

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Prediction",
                    "Spam" if prediction == 1 else "Not Spam"
                )

            with col2:
                st.metric(
                    "Confidence",
                    f"{confidence:.2f}%"
                )

            st.warning("""
        ### Recommendation

        - Do NOT click unknown links.
        - Do NOT download attachments.
        - Verify the sender before responding.
        """)

        else:

            st.success("✅ Legitimate Email")

            st.progress(confidence/100)

            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )

            st.info("""
        ### Recommendation

        This email appears safe.

        Still verify unexpected links and attachments before opening.
        """)
            
st.markdown("---")

st.caption(
    "Developed using Streamlit • Scikit-learn • TF-IDF • Multinomial Naive Bayes"
)