import streamlit as st

# ── PAGE CONFIG ─────────────────────────
st.set_page_config(
    page_title="Agex Ventures",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CUSTOM CSS (PREMIUM UI) ─────────────
st.markdown("""
<style>

body {
    background-color: #0A1628;
}

/* Headings */
h1, h2, h3 {
    color: #F5F0E8;
}

/* Text */
p {
    color: #D4CAB8;
}

/* Section Card */
.section {
    background: rgba(255,255,255,0.03);
    padding: 25px;
    border-radius: 12px;
    margin-bottom: 25px;
}

/* Button */
.stButton>button {
    background: linear-gradient(135deg, #C8973A, #E8B84B);
    color: #0A1628;
    font-weight: bold;
    border-radius: 6px;
    padding: 10px 20px;
}

/* Input */
input, textarea, select {
    background-color: #111;
    color: white;
}

/* Metric Box */
.metric-box {
    background: #1B3A6B;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
}

.metric-box h2 {
    color: #C8973A;
}

</style>
""", unsafe_allow_html=True)

# ── HERO SECTION ────────────────────────
st.markdown("""
<h1 style='text-align:center; font-size:60px; letter-spacing:2px;'>
AGEX VENTURES
</h1>
<p style='text-align:center; color:#C8973A; font-size:20px;'>
Building India's Future
</p>
""", unsafe_allow_html=True)

st.image("logo.png", width=180)

st.markdown("---")

# ── OVERVIEW ───────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Company Overview")
st.write("""
Agex Ventures is a diversified infrastructure and industrial services enterprise based in Jaipur, Rajasthan.  
We specialize in Civil Construction and Oil & Gas Services across India.

We deliver high-performance solutions with engineering precision, safety, and reliability.
""")
st.markdown('</div>', unsafe_allow_html=True)

# ── SERVICES ───────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Our Services")

tab1, tab2 = st.tabs(["Civil Construction", "Oil & Gas"])

with tab1:
    st.write("""
    • Residential & Commercial Projects  
    • Road & Infrastructure Development  
    • Industrial Construction  
    • RCC & Structural Work  
    • Site Development  
    """)

with tab2:
    st.write("""
    • Pipeline Installation & Maintenance  
    • Oil Field Support  
    • Equipment Handling  
    • Industrial Maintenance  
    """)

st.markdown('</div>', unsafe_allow_html=True)

# ── EXPERIENCE ─────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Experience & Expertise")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="metric-box"><h2>2+</h2><p>Industry Sectors</p></div>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<div class="metric-box"><h2>10+</h2><p>Service Offerings</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-box"><h2>360°</h2><p>Project Delivery</p></div>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<div class="metric-box"><h2>0</h2><p>Safety Compromise</p></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── GOALS ──────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Future Goals")

st.write("""
• Scale to ₹100 Crore+ Revenue  
• Expand Pan-India  
• Secure PSU Contracts  
• Build 500+ Workforce  
• Technology Integration  
""")

st.markdown('</div>', unsafe_allow_html=True)

# ── CONTACT ────────────────────────────
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Contact Us")

name = st.text_input("Your Name")
contact = st.text_input("Phone / Email")

service = st.selectbox("Select Service", [
    "Civil Construction",
    "Road Projects",
    "Industrial Projects",
    "Pipeline Work",
    "Oil Field Services"
])

message = st.text_area("Your Requirement")

if st.button("Submit Enquiry"):
    st.success("✅ Enquiry Submitted! We will contact you soon.")

st.markdown('</div>', unsafe_allow_html=True)

# ── FOOTER ─────────────────────────────
st.markdown("---")
st.markdown("""
<p style='text-align:center; color:#8A8070;'>
© 2025 Agex Ventures | Jaipur, India
</p>
""", unsafe_allow_html=True)