import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Make header background transparent so top-left sidebar hamburger menu is visible and functional */
    header[data-testid="stHeader"] {
        background: transparent !important;
        z-index: 100000 !important;
    }
    header[data-testid="stHeader"] button {
        color: #1e293b !important;
    }
    footer {
        display: none !important;
    }
    #MainMenu {
        visibility: hidden;
    }
    .stAppViewContainer {
        padding-top: 0rem;
    }

    /* ==========================================
       LOGIN PAGE STYLING (Exact Match to Reference Image)
       ========================================== */
    .login-bg-wrapper {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: radial-gradient(circle at 50% 35%, #0b1138 0%, #060924 65%, #020412 100%);
        z-index: 0;
        pointer-events: none;
        overflow: hidden;
    }

    /* Center Login Card Container */
    div[data-testid="stColumn"]:has(.login-logo-box),
    .login-card-container {
        background: rgba(8, 14, 44, 0.82) !important;
        backdrop-filter: blur(24px) !important;
        -webkit-backdrop-filter: blur(24px) !important;
        border: 1px solid rgba(0, 242, 254, 0.25) !important;
        border-radius: 28px !important;
        padding: 36px 32px !important;
        box-shadow: 0 30px 70px rgba(0, 0, 0, 0.7), 0 0 45px rgba(0, 114, 255, 0.25) !important;
        text-align: center !important;
        margin-top: 35px !important;
        position: relative !important;
        z-index: 10 !important;
    }

    /* Top Center Logo Box Card */
    .login-logo-box {
        background: #ffffff;
        width: 140px;
        height: 140px;
        border-radius: 24px;
        margin: 0 auto 12px auto;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5), 0 0 25px rgba(0, 242, 254, 0.4);
        padding: 12px;
    }

    .login-logo-box img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        margin: 0 auto !important;
        display: block !important;
    }

    /* Centered Streamlit Image Container Fallback */
    .login-card-container div[data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 0 auto 12px auto !important;
    }
    .login-card-container div[data-testid="stImage"] > img {
        margin: 0 auto !important;
        display: block !important;
    }

    /* Green Horizontal Line Below Logo */
    .green-logo-line {
        width: 110px;
        height: 3.5px;
        background: linear-gradient(90deg, #00e676 0%, #00b0ff 100%);
        border-radius: 2px;
        margin: 0 auto 20px auto;
        box-shadow: 0 0 12px rgba(0, 230, 118, 0.8);
    }

    .login-welcome-text {
        color: #ffffff;
        font-size: 1.25rem;
        font-weight: 500;
        margin-bottom: 2px;
        letter-spacing: 0.3px;
    }

    .login-title-text {
        color: #ffffff;
        font-size: 2.1rem;
        font-weight: 800;
        margin-bottom: 6px;
        letter-spacing: -0.5px;
    }

    .login-title-cyan {
        color: #00f2fe; /* Bright Cyan accent */
    }

    .login-subtitle-text {
        color: #b8c7ff;
        font-size: 0.98rem;
        font-weight: 400;
        margin-bottom: 24px;
    }

    /* Translucent Dark Input Fields */
    .stTextInput > div > div > input {
        background-color: rgba(10, 22, 58, 0.85) !important;
        border: 1px solid rgba(0, 198, 255, 0.4) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 0.95rem !important;
        box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.4) !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #00f2fe !important;
        box-shadow: 0 0 0 3px rgba(0, 242, 254, 0.35), inset 0 2px 4px rgba(0, 0, 0, 0.4) !important;
    }

    .stTextInput label {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        margin-bottom: 6px !important;
        text-align: left !important;
        display: block !important;
    }

    .stCheckbox label span {
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
    }

    /* Pill-Shaped Gradient Login Button */
    .stFormSubmitButton > button[kind="primary"], .stFormSubmitButton > button, div.stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #00c6ff 0%, #0072ff 35%, #722ed1 70%, #e040fb 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 14px 28px !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        width: 100% !important;
        cursor: pointer !important;
        box-shadow: 0 8px 25px rgba(0, 114, 255, 0.5) !important;
        transition: all 0.25s ease !important;
        letter-spacing: 0.5px !important;
    }

    .stFormSubmitButton > button[kind="primary"]:hover, .stFormSubmitButton > button:hover, div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(90deg, #00d2ff 0%, #0080ff 35%, #8000ff 70%, #f050ff 100%) !important;
        box-shadow: 0 10px 30px rgba(0, 114, 255, 0.7) !important;
        transform: translateY(-1px) !important;
    }

    /* Divider with New User text */
    .login-divider {
        display: flex;
        align-items: center;
        text-align: center;
        color: #a5b4fc;
        font-size: 0.88rem;
        margin: 22px 0 14px 0;
    }
    .login-divider::before, .login-divider::after {
        content: '';
        flex: 1;
        border-bottom: 1px solid rgba(165, 180, 252, 0.3);
    }
    .login-divider:not(:empty)::before { margin-right: .75em; }
    .login-divider:not(:empty)::after { margin-left: .75em; }

    /* Create Account Link / Button */
    .create-account-link {
        color: #00f2fe;
        font-weight: 700;
        font-size: 1rem;
        text-decoration: underline;
        cursor: pointer;
    }

    /* Streamlit Secondary Button Override for Create Account */
    div.stButton > button[kind="secondary"] {
        background: transparent !important;
        color: #00f2fe !important;
        border: none !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        text-decoration: underline !important;
        box-shadow: none !important;
    }
    div.stButton > button[kind="secondary"]:hover {
        color: #38bdf8 !important;
    }

    /* ==========================================
       DASHBOARD PAGE STYLING (Screenshot 2 Match)
       ========================================== */
    .main-header {
        background: #ffffff;
        border-bottom: 1px solid #e2e8f0;
        padding: 12px 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 24px;
        margin-top: -3.5rem;
        margin-left: -4rem;
        margin-right: -4rem;
    }
    .header-logo-group {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .header-logo-img {
        width: 36px;
        height: 36px;
        object-fit: contain;
    }
    .header-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #1e293b;
        margin: 0;
    }
    .header-title-accent {
        color: #4f46e5;
    }
    .header-user-group {
        display: flex;
        align-items: center;
        gap: 16px;
        font-size: 0.9rem;
        color: #334155;
    }

    /* Main Welcome Banner */
    .welcome-banner {
        background: linear-gradient(135deg, #eef5ff 0%, #e0edff 100%);
        border: 1px solid #c7dcfc;
        border-radius: 16px;
        padding: 24px 32px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 28px;
    }
    .welcome-left {
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .welcome-icon-circle {
        width: 68px;
        height: 68px;
        background: #ffffff;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15);
        border: 2px solid #2563eb;
    }
    .welcome-text-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 4px;
    }
    .welcome-text-sub {
        font-size: 0.95rem;
        color: #64748b;
    }
    .welcome-right-badge {
        display: flex;
        align-items: center;
        gap: 12px;
        background: #ffffff;
        padding: 10px 18px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        font-weight: 700;
        color: #1e293b;
        font-size: 0.85rem;
    }

    /* Section Title */
    .section-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 4px;
    }
    .section-title {
        font-size: 1.15rem;
        font-weight: 700;
        color: #1e293b;
    }
    .section-subtitle {
        font-size: 0.88rem;
        color: #64748b;
        margin-bottom: 16px;
    }

    /* Career Role Selection Cards */
    .role-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 16px 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        cursor: pointer;
        transition: all 0.2s ease;
        margin-bottom: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }
    .role-card:hover {
        border-color: #93c5fd;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.08);
        transform: translateY(-2px);
    }
    .role-card-active {
        background: #f0f7ff !important;
        border: 2px solid #2563eb !important;
        box-shadow: 0 4px 14px rgba(37, 99, 235, 0.15) !important;
    }
    .role-card-left {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    .role-icon-box {
        width: 44px;
        height: 44px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        background: #eff6ff;
    }
    .role-name {
        font-size: 1rem;
        font-weight: 700;
        color: #1e293b;
    }
    .role-arrow {
        color: #94a3b8;
        font-size: 1.1rem;
    }

    /* Selected Role Header Details */
    .selected-role-header {
        background: #edf5ff;
        border-radius: 14px;
        padding: 20px 24px;
        margin-top: 24px;
        margin-bottom: 20px;
        border: 1px solid #d0e2ff;
    }
    .selected-role-title {
        font-size: 1.25rem;
        font-weight: 800;
        color: #1e3a8a;
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 4px;
    }
    .selected-role-desc {
        color: #475569;
        font-size: 0.92rem;
    }

    /* Skills Pill Badges */
    .skills-container {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 14px;
    }
    .skill-pill {
        background: #eef4ff;
        color: #1d4ed8;
        border: 1px solid #bfdbfe;
        padding: 8px 18px;
        border-radius: 50px;
        font-size: 0.9rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .skill-check-icon {
        width: 18px;
        height: 18px;
        background: #2563eb;
        color: white;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 0.7rem;
        font-weight: 800;
    }

    /* Next Steps Flow */
    .next-steps-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1e293b;
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 24px;
        margin-bottom: 4px;
    }
    .next-steps-sub {
        font-size: 0.85rem;
        color: #64748b;
        margin-bottom: 16px;
    }

    .step-card {
        border-radius: 12px;
        padding: 16px 12px;
        text-align: center;
        transition: all 0.2s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .step-num-badge {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        color: white;
        font-weight: 700;
        font-size: 0.75rem;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 8px;
    }
    .step-icon {
        font-size: 1.5rem;
        margin-bottom: 8px;
    }
    .step-label {
        font-size: 0.82rem;
        font-weight: 700;
        line-height: 1.2;
    }

    /* Metric Result Card */
    .result-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        margin-bottom: 16px;
    }
    .result-score-highlight {
        font-size: 2.2rem;
        font-weight: 800;
        color: #2563eb;
    }
    .result-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 0.9rem;
        color: #ffffff;
    }

    /* Level Badges for Reassessment Questions */
    .level-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        margin-left: 8px;
    }
    .level-badge-basic { background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
    .level-badge-beginner { background: #dcfce7; color: #15803d; border: 1px solid #86efac; }
    .level-badge-intermediate { background: #fef3c7; color: #b45309; border: 1px solid #fde047; }
    .level-badge-advanced { background: #fce7f3; color: #be185d; border: 1px solid #fbcfe8; }
    .level-badge-expert { background: #f3e8ff; color: #6b21a8; border: 1px solid #d8b4fe; }

    /* Before vs After Comparison Cards & Tables */
    .comparison-card {
        background: #ffffff;
        border-radius: 14px;
        border: 1px solid #cbd5e1;
        padding: 20px 24px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
        margin-bottom: 20px;
    }
    .comparison-title {
        font-size: 1.2rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 14px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .metric-chip {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 0.88rem;
        font-weight: 700;
    }
    .chip-before { background: #fee2e2; color: #991b1b; }
    .chip-after { background: #dcfce7; color: #166534; }
    .chip-target { background: #dbeafe; color: #1e40af; }
    .chip-gain { background: #e0e7ff; color: #3730a3; }

    /* Progress Banner */
    .progress-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff;
        border-radius: 16px;
        padding: 24px 32px;
        margin-bottom: 24px;
        border: 1px solid #334155;
    }

    /* ==========================================
       NAVIGATION SIDEBAR ALIGNMENT & COLORS
       ========================================== */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 2px !important;
    }

    [data-testid="stSidebar"] [data-testid="stElementContainer"],
    [data-testid="stSidebar"] div.stButton {
        margin: 0 !important;
        padding: 0 !important;
    }

    [data-testid="stSidebar"] .stButton > button,
    section[data-testid="stSidebar"] .stButton > button {
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        text-align: left !important;
        outline: none !important;
        width: 100% !important;
        min-height: 38px !important;
        height: 38px !important;
        text-decoration: none !important;
        border: none !important;
        box-shadow: none !important;
        margin: 2px 0 !important;
        padding: 6px 12px !important;
        background: transparent !important;
        background-color: transparent !important;
        box-sizing: border-box !important;
    }

    [data-testid="stSidebar"] .stButton > button *,
    section[data-testid="stSidebar"] .stButton > button * {
        text-decoration: none !important;
        text-align: left !important;
        margin-left: 0 !important;
        padding-left: 0 !important;
        justify-content: flex-start !important;
    }

    /* 1. All inactive navigation text: BLACK, slightly bold */
    [data-testid="stSidebar"] .stButton > button[kind="secondary"],
    [data-testid="stSidebar"] .stButton > button[kind="secondary"] *,
    [data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-secondary"],
    [data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-secondary"] *,
    section[data-testid="stSidebar"] .stButton > button[kind="secondary"],
    section[data-testid="stSidebar"] .stButton > button[kind="secondary"] *,
    section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-secondary"],
    section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-secondary"] * {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        font-weight: 600 !important;
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        text-decoration: none !important;
    }

    /* 2. Active/selected navigation item: BLACK text with active style */
    [data-testid="stSidebar"] .stButton > button[kind="primary"],
    [data-testid="stSidebar"] .stButton > button[kind="primary"] *,
    [data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"],
    [data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"] *,
    section[data-testid="stSidebar"] .stButton > button[kind="primary"],
    section[data-testid="stSidebar"] .stButton > button[kind="primary"] *,
    section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"],
    section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"] * {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        font-weight: 700 !important;
        background: rgba(0, 0, 0, 0.04) !important;
        background-color: rgba(0, 0, 0, 0.04) !important;
        border: none !important;
        border-radius: 6px !important;
        box-shadow: none !important;
        text-decoration: none !important;
    }

    /* Hover state for sidebar buttons */
    [data-testid="stSidebar"] .stButton > button:hover,
    section[data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(0, 0, 0, 0.06) !important;
        border-radius: 6px !important;
    }

    /* ==========================================
       NEXT BUTTON STYLING (ORANGE)
       ========================================== */
    .next-btn-orange button,
    div.stButton > button[kind="primary"] {
        background: #ff8c00 !important;
        background-color: #ff8c00 !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: none !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 12px rgba(255, 140, 0, 0.3) !important;
    }
    .next-btn-orange button:hover,
    div.stButton > button[kind="primary"]:hover {
        background: #e07b00 !important;
        background-color: #e07b00 !important;
    }

    /* ==========================================
       CAREER ROLE SELECTION (SELECT ...) & GO BUTTONS STYLING (BLACK TEXT)
       ========================================== */
    .role-btn-unselected button,
    .role-btn-unselected button *,
    .role-btn-unselected button span,
    .role-btn-unselected button p,
    .role-btn-selected button,
    .role-btn-selected button *,
    .role-btn-selected button span,
    .role-btn-selected button p,
    div.role-btn-unselected button,
    div.role-btn-selected button,
    .go-btn-wrapper button,
    .go-btn-wrapper button *,
    .go-btn-wrapper button span,
    .go-btn-wrapper button p,
    div.go-btn-wrapper button {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
    }

    /* ==========================================
       LOGOUT BUTTON STYLING (BLACK TEXT)
       ========================================== */
    .logout-btn-wrapper button,
    .logout-btn-wrapper button *,
    .logout-btn-wrapper button span,
    .logout-btn-wrapper button p {
        color: #000000 !important;
        -webkit-text-fill-color: #000000 !important;
        font-weight: 600 !important;
    }

    </style>
    """, unsafe_allow_html=True)


