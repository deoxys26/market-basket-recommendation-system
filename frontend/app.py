import streamlit as st
import requests

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="RetailIQ · Recommendations",
    page_icon="🛍️",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #0d0d0f;
    min-height: 100vh;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 4rem 2rem 2rem;
    max-width: 680px;
}

/* ── Hero header ── */
.hero {
    margin-bottom: 3rem;
    text-align: center;
}

.hero-badge {
    display: inline-block;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #c8a96e;
    border: 1px solid #c8a96e44;
    border-radius: 999px;
    padding: 0.35rem 1rem;
    margin-bottom: 1.4rem;
}

.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2.4rem, 6vw, 3.4rem);
    line-height: 1.1;
    color: #f0ece3;
    margin: 0 0 1rem;
    letter-spacing: -0.02em;
}

.hero-title em {
    font-style: italic;
    color: #c8a96e;
}

.hero-sub {
    font-size: 0.95rem;
    color: #7a7672;
    font-weight: 300;
    line-height: 1.6;
    max-width: 420px;
    margin: 0 auto;
}

/* ── Search card ── */
.search-card {
    background: #15141a;
    border: 1px solid #2a2830;
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 2rem;
}

.search-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #5c5864;
    margin-bottom: 0.6rem;
}

/* ── Streamlit input overrides ── */
.stTextInput > div > div > input {
    background: #0d0d0f !important;
    border: 1px solid #2a2830 !important;
    border-radius: 10px !important;
    color: #f0ece3 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.85rem 1.1rem !important;
    transition: border-color 0.2s;
}

.stTextInput > div > div > input:focus {
    border-color: #c8a96e !important;
    box-shadow: 0 0 0 3px #c8a96e18 !important;
}

.stTextInput > div > div > input::placeholder {
    color: #3d3b45 !important;
}

/* ── Button ── */
.stButton > button {
    width: 100%;
    background: #c8a96e !important;
    color: #0d0d0f !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.85rem 1.5rem !important;
    margin-top: 0.8rem;
    cursor: pointer;
    transition: background 0.2s, transform 0.1s !important;
}

.stButton > button:hover {
    background: #d9bc85 !important;
    transform: translateY(-1px);
}

.stButton > button:active {
    transform: translateY(0);
}

/* ── Results section ── */
.results-header {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #5c5864;
    margin: 2rem 0 1rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

.results-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #2a2830;
}

/* ── Recommendation chips ── */
.rec-list {
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
}

.rec-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    background: #15141a;
    border: 1px solid #2a2830;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    transition: border-color 0.2s, transform 0.15s;
    animation: slideIn 0.3s ease both;
}

.rec-item:hover {
    border-color: #c8a96e55;
    transform: translateX(4px);
}

@keyframes slideIn {
    from { opacity: 0; transform: translateY(8px); }
    to   { opacity: 1; transform: translateY(0); }
}

.rec-index {
    font-family: 'DM Serif Display', serif;
    font-size: 1.1rem;
    color: #c8a96e;
    min-width: 1.5rem;
    text-align: center;
}

.rec-name {
    font-size: 0.97rem;
    color: #d8d3c8;
    font-weight: 400;
}

/* ── Empty / warning / error states ── */
.state-box {
    border-radius: 12px;
    padding: 1.1rem 1.4rem;
    font-size: 0.9rem;
    font-weight: 400;
}

.state-warning {
    background: #1e1a0e;
    border: 1px solid #c8a96e44;
    color: #c8a96e;
}

.state-empty {
    background: #15141a;
    border: 1px solid #2a2830;
    color: #5c5864;
}

.state-error {
    background: #1a0e0e;
    border: 1px solid #c0444444;
    color: #e07070;
}

/* ── Divider ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #2a2830, transparent);
    margin: 2.5rem 0;
}

/* ── Footer ── */
.footer {
    text-align: center;
    font-size: 0.72rem;
    color: #3d3b45;
    letter-spacing: 0.08em;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">Apriori Association Mining</div>
    <h1 class="hero-title">Retail <em>Intelligence</em><br>Engine</h1>
    <p class="hero-sub">
        Discover what customers buy together.
        Enter any product to surface high-confidence pairings.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Search card ───────────────────────────────────────────────────────────────
st.markdown('<div class="search-card">', unsafe_allow_html=True)
st.markdown('<div class="search-label">Product lookup</div>', unsafe_allow_html=True)

product = st.text_input(
    label="",
    placeholder="e.g. Whole Milk, Bread, Diapers…",
    key="product_input",
    label_visibility="collapsed",
)

recommend_clicked = st.button("Find Recommendations →")
st.markdown('</div>', unsafe_allow_html=True)

# ── Logic ─────────────────────────────────────────────────────────────────────
if recommend_clicked:
    if product.strip() == "":
        st.markdown(
            '<div class="state-box state-warning">⚠ Please enter a product name to continue.</div>',
            unsafe_allow_html=True
        )
    else:
        try:
            response = requests.get(
                "http://127.0.0.1:8000/recommend",
                params={"product": product}
            )
            data = response.json()
            recommendations = data.get("recommendations", [])

            st.markdown(
                f'<div class="results-header">Recommended with "{product}"</div>',
                unsafe_allow_html=True
            )

            if recommendations:
                items_html = "".join([
                    f"""<div class="rec-item" style="animation-delay:{i*0.06}s">
                            <span class="rec-index">{i+1}</span>
                            <span class="rec-name">{item}</span>
                        </div>"""
                    for i, item in enumerate(recommendations)
                ])
                st.markdown(f'<div class="rec-list">{items_html}</div>', unsafe_allow_html=True)
            else:
                st.markdown(
                    '<div class="state-box state-empty">No associations found for this product. Try another one.</div>',
                    unsafe_allow_html=True
                )

        except Exception as e:
            st.markdown(
                f'<div class="state-box state-error">⚠ Cannot reach backend: {e}</div>',
                unsafe_allow_html=True
            )

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="footer">RetailIQ &nbsp;·&nbsp; Powered by Apriori Association Rules</div>',
    unsafe_allow_html=True
)
