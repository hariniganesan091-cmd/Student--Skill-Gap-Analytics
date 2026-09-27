import streamlit as st
import os
from dotenv import load_dotenv
from supabase import create_client
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
try:
    response = supabase.table("users").select("*").limit(1).execute()
    print("Supabase connection successful!")
    print(response.data)
except Exception as e:
    print("Supabase connection failed:", e)
import json
import base64
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

from styles import inject_custom_css
from utils.auth import (
    init_auth_state, register_user, login_user, logout_user,
    save_student_progress, load_student_progress, get_student_progress,
    get_all_student_role_progress
)
from data.career_roles import CAREER_ROLES, LEVEL_MAP
from data.questions_data import QUESTIONS_DATA
from data.reassessment_questions import REASSESSMENT_QUESTIONS_DATA
from data.recommendations import get_recommendation, get_youtube_link
from utils.analytics import calculate_assessment_results, get_weak_skills, calculate_reassessment_results
from utils.report import generate_text_report, generate_final_report

# Page Config
st.set_page_config(
    page_title="Student Skill Gap Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom CSS
inject_custom_css()

# Initialize Auth & Session State
init_auth_state()

if "selected_role" not in st.session_state:
    st.session_state.selected_role = "Data Analyst"

if "sidebar_nav" not in st.session_state:
    st.session_state.sidebar_nav = "Dashboard"

if "assessment_answers" not in st.session_state:
    st.session_state.assessment_answers = {}

if "assessment_submitted" not in st.session_state:
    st.session_state.assessment_submitted = False

if "initial_analytics" not in st.session_state:
    st.session_state.initial_analytics = None

if "assessment_date" not in st.session_state:
    st.session_state.assessment_date = ""

if "reassessment_answers" not in st.session_state:
    st.session_state.reassessment_answers = {}

if "reassessment_submitted" not in st.session_state:
    st.session_state.reassessment_submitted = False

if "reassessment_analytics" not in st.session_state:
    st.session_state.reassessment_analytics = None

if "reassessment_date" not in st.session_state:
    st.session_state.reassessment_date = ""

if "asked_question_ids" not in st.session_state:
    st.session_state.asked_question_ids = set()

if "reassessment_questions_map" not in st.session_state:
    st.session_state.reassessment_questions_map = {}

if "assessment_history" not in st.session_state:
    st.session_state.assessment_history = []


def select_role(new_role):
    if st.session_state.selected_role != new_role:
        old_role = st.session_state.selected_role
        user_email = st.session_state.get("user_email")
        if user_email and (st.session_state.get("assessment_submitted") or st.session_state.get("reassessment_submitted")):
            save_student_progress(
                email=user_email,
                selected_role=old_role,
                assessment_submitted=st.session_state.assessment_submitted,
                assessment_answers=st.session_state.assessment_answers,
                initial_analytics=st.session_state.initial_analytics,
                assessment_date=st.session_state.assessment_date,
                reassessment_submitted=st.session_state.reassessment_submitted,
                reassessment_answers=st.session_state.reassessment_answers,
                reassessment_analytics=st.session_state.reassessment_analytics,
                reassessment_date=st.session_state.reassessment_date,
                reassessment_questions_map=st.session_state.reassessment_questions_map,
                asked_question_ids=st.session_state.asked_question_ids,
                assessment_history=st.session_state.assessment_history
            )

        st.session_state.selected_role = new_role

        if user_email:
            loaded = load_student_progress(user_email, role=new_role)
            if not loaded:
                st.session_state.assessment_answers = {}
                st.session_state.assessment_submitted = False
                st.session_state.initial_analytics = None
                st.session_state.assessment_date = ""
                st.session_state.reassessment_answers = {}
                st.session_state.reassessment_submitted = False
                st.session_state.reassessment_analytics = None
                st.session_state.reassessment_date = ""
                st.session_state.reassessment_questions_map = {}
                st.session_state.assessment_history = []
        else:
            st.session_state.assessment_answers = {}
            st.session_state.assessment_submitted = False
            st.session_state.initial_analytics = None
            st.session_state.assessment_date = ""
            st.session_state.reassessment_answers = {}
            st.session_state.reassessment_submitted = False
            st.session_state.reassessment_analytics = None
            st.session_state.reassessment_date = ""
            st.session_state.reassessment_questions_map = {}
            st.session_state.assessment_history = []



# ==========================================
# PAGE ROUTING
# ==========================================

# Resolve exact logo path
logo_path = None
for p in ["logo_analytics-png.jpeg", "assets/logo_analytics-png.jpeg", "assets/logo.png", "assets/image.png"]:
    if os.path.exists(p):
        logo_path = p
        break

# 1. LOGIN PAGE (Clean Minimal Layout & Centered Logo)
if st.session_state.current_page == "login" and not st.session_state.authenticated:
    st.markdown("""
    <div class="login-bg-wrapper"></div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2.2, 1])
    with col2:
        # Centered Logo Card
        if logo_path:
            with open(logo_path, "rb") as _f:
                _b64 = base64.b64encode(_f.read()).decode()
            _ext = logo_path.split(".")[-1].lower()
            _mime = "image/jpeg" if _ext in ["jpg", "jpeg"] else "image/png"
            st.markdown(f'''
            <div class="login-logo-box">
                <img src="data:{_mime};base64,{_b64}" alt="Logo" />
            </div>
            <div class="green-logo-line"></div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown('''
            <div class="login-logo-box">
                <div style="font-size: 2.5rem; text-align: center;">🎓</div>
            </div>
            <div class="green-logo-line"></div>
            ''', unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align: center;">
            <div class="login-welcome-text">Welcome to</div>
            <div class="login-title-text">Student Skill Gap <span class="login-title-cyan">Analytics</span></div>
            <div class="login-subtitle-text">Login to continue your learning journey</div>
        </div>
        """, unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
            email = st.text_input("Email ID", placeholder="Enter your email ID")
            password = st.text_input("Password", type="password", placeholder="Enter your password")

            login_btn = st.form_submit_button("Login ➔", type="primary", use_container_width=True)

            if login_btn:
                success, msg = login_user(email, password)
                if success:
                    st.success("Login Successful")
                    st.rerun()
                else:
                    st.error(msg)

        st.markdown('<div class="login-divider">New User?</div>', unsafe_allow_html=True)
        
        if st.button("Create Account", key="btn_create_acc", use_container_width=True, type="secondary"):
            st.session_state.current_page = "register"
            st.rerun()


# 2. REGISTRATION PAGE
elif st.session_state.current_page == "register":
    st.markdown("""
    <div class="login-bg-wrapper"></div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2.2, 1])
    with col2:
        if logo_path:
            with open(logo_path, "rb") as _f:
                _b64 = base64.b64encode(_f.read()).decode()
            _ext = logo_path.split(".")[-1].lower()
            _mime = "image/jpeg" if _ext in ["jpg", "jpeg"] else "image/png"
            st.markdown(f'''
            <div class="login-logo-box">
                <img src="data:{_mime};base64,{_b64}" alt="Logo" />
            </div>
            ''', unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align: center;">
            <div class="login-welcome-text">Join Us Today</div>
            <div class="login-title-text">Create <span class="login-title-cyan">Account</span></div>
            <div class="login-title-line"></div>
        </div>
        """, unsafe_allow_html=True)

        if "reg_success" not in st.session_state:
            st.session_state.reg_success = False

        if not st.session_state.reg_success:
            with st.form("reg_form"):
                full_name = st.text_input("Full Name", placeholder="Enter your full name")
                reg_email = st.text_input("Email ID", placeholder="Enter your email ID")
                reg_pass = st.text_input("Password", type="password", placeholder="Create password")
                confirm_pass = st.text_input("Confirm Password", type="password", placeholder="Confirm password")

                reg_btn = st.form_submit_button("Register", type="primary", use_container_width=True)

                if reg_btn:
                    success, msg = register_user(full_name, reg_email, reg_pass, confirm_pass)
                    if success:
                        st.session_state.reg_success = True
                        st.success("Registration successful")
                        st.rerun()
                    else:
                        st.error(msg)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Back to Login Page", key="btn_back_login_form", use_container_width=True):
                st.session_state.current_page = "login"
                st.rerun()
        else:
            st.success("Registration successful")
            st.info("Your account has been saved. Click below to return to the login page.")
            if st.button("Back to Login Page", key="btn_back_login_success", type="primary", use_container_width=True):
                st.session_state.reg_success = False
                st.session_state.current_page = "login"
                st.rerun()

# 3. DASHBOARD PAGE (Screenshot 2 Match)
elif st.session_state.authenticated:

    # Top Header Navbar
    st.markdown(f"""
    <div class="main-header">
        <div class="header-logo-group">
            <div style="font-size: 1.5rem; font-weight: 800; color: #2563eb;">🎓</div>
            <div class="header-title">Student Skill Gap <span class="header-title-accent">Analytics</span></div>
        </div>
        <div class="header-user-group">
            <div>👤 Welcome, <strong>{st.session_state.user_name}</strong></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Logout button top right
    col_dash_title, col_logout = st.columns([8, 1.5])
    with col_logout:
        if st.button("🚪 Logout", use_container_width=True):
            logout_user()

    # Sidebar Navigation
    st.sidebar.markdown("### 📌 Navigation")
    
    sidebar_items = [
        "Dashboard",
        "Career Role Selection",
        "Industry Skill Requirements",
        "Student Skill Assessment",
        "Skill Gap Analysis",
        "Readiness Score Calculation",
        "Interactive Dashboard & Data Visualization",
        "Learning Recommendation",
        "My Progress",
        "Reassessment Available",
        "Report Generation",
        "Final Report"
    ]

    for item in sidebar_items:
        is_active = (st.session_state.sidebar_nav == item)
        btn_label = item
        if st.sidebar.button(btn_label, key=f"nav_{item}", use_container_width=True, type="primary" if is_active else "secondary"):
            st.session_state.sidebar_nav = item
            st.rerun()

    current_nav = st.session_state.sidebar_nav
    selected_role_name = st.session_state.selected_role
    role_data = CAREER_ROLES[selected_role_name]
    # Calculate initial analytics based on submitted answers (preserved in session state)
    if st.session_state.assessment_submitted and not st.session_state.initial_analytics:
        st.session_state.initial_analytics = calculate_assessment_results(selected_role_name, st.session_state.assessment_answers)

    analytics = st.session_state.initial_analytics if st.session_state.initial_analytics else calculate_assessment_results(selected_role_name, st.session_state.assessment_answers)

    # Defensive safety checks for analytics variable structure
    if not analytics or not isinstance(analytics, dict):
        analytics = calculate_assessment_results(selected_role_name, st.session_state.get("assessment_answers", {}))

    if "results" not in analytics or not isinstance(analytics.get("results"), list):
        analytics["results"] = []

    if "readiness_pct" not in analytics:
        analytics["readiness_pct"] = 0.0

    if "readiness_status" not in analytics:
        analytics["readiness_status"] = "Needs Improvement"

    if "status_color" not in analytics:
        analytics["status_color"] = "#d97706"

    if "student_total_score" not in analytics:
        analytics["student_total_score"] = sum(item.get("student_level_num", 1) for item in analytics.get("results", []))

    if "required_total_score" not in analytics:
        analytics["required_total_score"] = sum(item.get("industry_level_num", 3) for item in analytics.get("results", []))
    def render_career_roles_grid(key_prefix="main"):
        selected_role_name = st.session_state.selected_role
        top_roles = ["Data Analyst", "Python Developer", "Full Stack Developer", "AI/ML Engineer"]
        bottom_roles = ["Cyber Security Analyst", "UI/UX Designer", "Cloud Computing"]

        # Top Row — 4 roles
        r1_cols = st.columns(4)
        for idx, r_name in enumerate(top_roles):
            with r1_cols[idx]:
                r_info = CAREER_ROLES[r_name]
                is_sel = (r_name == selected_role_name)
                border_color = "#ff8c00" if is_sel else "#cbd5e1"
                bg_color = "#fff8f0" if is_sel else "#ffffff"
                badge_html = '<div style="margin-top: 6px;"><span style="background: #ff8c00; color: #ffffff; padding: 3px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;">ACTIVE</span></div>' if is_sel else ''

                st.markdown(f'''
                <div style="background: {bg_color}; border: 2px solid {border_color}; border-radius: 14px; padding: 20px 16px; min-height: 125px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin-bottom: 8px;">
                    <div style="font-size: 2.2rem; margin-bottom: 6px;">{r_info['icon']}</div>
                    <div style="font-size: 1.05rem; font-weight: 800; color: #000000;">{r_name}</div>
                    {badge_html}
                </div>
                ''', unsafe_allow_html=True)
                btn_wrapper = "role-btn-selected" if is_sel else "role-btn-unselected"
                st.markdown(f'<div class="{btn_wrapper}">', unsafe_allow_html=True)
                if st.button(f"Select {r_name}", key=f"role_grid_{key_prefix}_{r_name}", use_container_width=True):
                    select_role(r_name)
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        # Bottom Row — 3 roles
        r2_cols = st.columns(4)
        for idx, r_name in enumerate(bottom_roles):
            with r2_cols[idx]:
                r_info = CAREER_ROLES[r_name]
                is_sel = (r_name == selected_role_name)
                border_color = "#ff8c00" if is_sel else "#cbd5e1"
                bg_color = "#fff8f0" if is_sel else "#ffffff"
                badge_html = '<div style="margin-top: 6px;"><span style="background: #ff8c00; color: #ffffff; padding: 3px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;">ACTIVE</span></div>' if is_sel else ''

                st.markdown(f'''
                <div style="background: {bg_color}; border: 2px solid {border_color}; border-radius: 14px; padding: 20px 16px; min-height: 125px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.04); margin-bottom: 8px;">
                    <div style="font-size: 2.2rem; margin-bottom: 6px;">{r_info['icon']}</div>
                    <div style="font-size: 1.05rem; font-weight: 800; color: #000000;">{r_name}</div>
                    {badge_html}
                </div>
                ''', unsafe_allow_html=True)
                btn_wrapper = "role-btn-selected" if is_sel else "role-btn-unselected"
                st.markdown(f'<div class="{btn_wrapper}">', unsafe_allow_html=True)
                if st.button(f"Select {r_name}", key=f"role_grid_{key_prefix}_{r_name}", use_container_width=True):
                    select_role(r_name)
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

    recent_career_roles_grid = render_career_roles_grid


    # -------------------------------------------------------------
    # VIEW 1: DASHBOARD MAIN OVERVIEW (Matches Screenshot 2)
    # -------------------------------------------------------------
    if current_nav == "Dashboard":

        # Welcome Banner
        st.markdown("""
        <div class="welcome-banner">
            <div class="welcome-left">
                <div class="welcome-icon-circle">🎓</div>
                <div>
                    <div class="welcome-text-title">Welcome to Student Skill Gap Analytics!</div>
                    <div class="welcome-text-sub">Bridge the gap between your skills and industry needs</div>
                </div>
            </div>
            <div class="welcome-right-badge">
                🏃 Learn • Build • Grow
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 1. Career Role Selection Header
        st.markdown("""
        <div class="section-header">
            <span style="font-size: 1.3rem;">🎯</span>
            <span class="section-title">1. Career Role Selection</span>
        </div>
        <div class="section-subtitle">Choose your desired career role to view the required industry skills.</div>
        """, unsafe_allow_html=True)

        render_career_roles_grid(key_prefix="dash")

        # Selected Role Details Box (e.g. Data Analyst)
        st.markdown(f"""
        <div class="selected-role-header">
            <div class="selected-role-title">
                <span>{role_data['icon']}</span>
                <span>{selected_role_name}</span>
            </div>
            <div class="selected-role-desc">{role_data['description']}</div>
            <br>
            <div style="font-weight: 700; color: #1e293b; font-size: 0.95rem; margin-bottom: 8px;">
                📋 Required Industry Skills
            </div>
            <div class="skills-container">
        """, unsafe_allow_html=True)

        skill_pills_html = "".join([
            f'<div class="skill-pill"><span class="skill-check-icon">✓</span> {sk}</div>'
            for sk in role_data['skills']
        ])
        st.markdown(skill_pills_html + "</div></div>", unsafe_allow_html=True)

        # Next Steps Sequence
        st.markdown("""
        <div class="next-steps-title">
            ➔ Next Steps
        </div>
        <div class="next-steps-sub">Follow the steps below to analyze your skills and get personalized recommendations.</div>
        """, unsafe_allow_html=True)

        step_cols = st.columns(7)
        steps_info = [
            {"num": 1, "icon": "📋", "title": "Industry Skill Requirements", "color": "#dcfce7", "text_color": "#15803d", "nav": "Industry Skill Requirements"},
            {"num": 2, "icon": "👤", "title": "Student Skill Assessment", "color": "#dbeafe", "text_color": "#1d4ed8", "nav": "Student Skill Assessment"},
            {"num": 3, "icon": "🔍", "title": "Skill Gap Analysis", "color": "#f3e8ff", "text_color": "#6b21a8", "nav": "Skill Gap Analysis"},
            {"num": 4, "icon": "⏱️", "title": "Readiness Score Calculation", "color": "#ffedd5", "text_color": "#c2410c", "nav": "Readiness Score Calculation"},
            {"num": 5, "icon": "📊", "title": "Interactive Dashboard & Data Visualization", "color": "#ccfbf1", "text_color": "#0f766e", "nav": "Interactive Dashboard & Data Visualization"},
            {"num": 6, "icon": "💡", "title": "Learning Recommendation", "color": "#fce7f3", "text_color": "#be185d", "nav": "Learning Recommendation"},
            {"num": 7, "icon": "📄", "title": "Report Generation", "color": "#e0e7ff", "text_color": "#4338ca", "nav": "Report Generation"}
        ]

        for i, s in enumerate(steps_info):
            with step_cols[i]:
                st.markdown(f"""
                <div class="step-card" style="background: {s['color']}; border: 1px solid {s['color']};">
                    <div class="step-num-badge" style="background: {s['text_color']};">{s['num']}</div>
                    <div class="step-icon">{s['icon']}</div>
                    <div class="step-label" style="color: {s['text_color']};">{s['title']}</div>
                </div>
                """, unsafe_allow_html=True)
                st.markdown('<div class="go-btn-wrapper">', unsafe_allow_html=True)
                if st.button("Go ➔", key=f"step_go_{s['num']}", use_container_width=True):
                    st.session_state.sidebar_nav = s['nav']
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)


    # -------------------------------------------------------------
    # VIEW 2: CAREER ROLE SELECTION
    # -------------------------------------------------------------
    elif current_nav == "Career Role Selection":
        st.markdown("## 🎯 Career Role Selection")
        st.markdown("Choose your target career role to update industry skills and assessment questions.")

        render_career_roles_grid(key_prefix="page")


    # -------------------------------------------------------------
    # VIEW 3: INDUSTRY SKILL REQUIREMENTS
    # -------------------------------------------------------------
    elif current_nav == "Industry Skill Requirements":
        st.markdown(f"## 📋 Industry Skill Requirements: {selected_role_name}")
        st.markdown(f"*{role_data['description']}*")
        st.markdown("Below are the standard industry skill levels expected for entry to mid-level roles.")

        skills_list = role_data["skills"]
        ind_levels = role_data["industry_levels"]

        table_data = []
        for sk in skills_list:
            lvl_num = ind_levels.get(sk, 3)
            lvl_name = LEVEL_MAP[lvl_num]
            table_data.append({
                "Skill Name": sk,
                "Industry Required Level": lvl_name,
                "Level Rating (1-5)": f"{lvl_num} / 5"
            })

        df_ind = pd.DataFrame(table_data)
        st.table(df_ind)

        # Next Button Navigation
        st.markdown("<br>", unsafe_allow_html=True)
        col_n1, col_n2 = st.columns([8, 2])
        with col_n2:
            if st.button("Next ➔", key="next_from_ind_req", type="primary", use_container_width=True):
                st.session_state.sidebar_nav = "Student Skill Assessment"
                st.rerun()


    # -------------------------------------------------------------
    # VIEW 4: STUDENT SKILL ASSESSMENT (265 Total Questions Engine)
    # -------------------------------------------------------------
    elif current_nav == "Student Skill Assessment":
        st.markdown(f"## 📝 Student Skill Assessment: {selected_role_name}")
        st.markdown("Please answer all 5 questions for each required skill below.")

        role_questions = QUESTIONS_DATA.get(selected_role_name, {})
        skills_list = role_data["skills"]

        if st.session_state.assessment_submitted:
            ass_date_str = st.session_state.get("assessment_date") or "Completed"
            st.markdown(f"""
            <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 14px; padding: 22px 26px; margin-bottom: 24px;">
                <div style="font-size: 1.2rem; font-weight: 800; color: #166534; margin-bottom: 8px;">
                    ✅ Initial Assessment Completed
                </div>
                <div style="font-size: 0.95rem; color: #15803d; line-height: 1.6;">
                    You have already completed the initial skill assessment for <strong>{selected_role_name}</strong> on <strong>{ass_date_str}</strong>.
                    <br>Your results, readiness score, and skill gaps are permanently stored in your account. You do not need to retake this initial assessment.
                </div>
            </div>
            """, unsafe_allow_html=True)

            c_btn1, c_btn2, c_btn3 = st.columns([1, 1, 1])
            with c_btn1:
                if st.button("📈 View My Progress ➔", key="ass_go_to_progress", type="primary", use_container_width=True):
                    st.session_state.sidebar_nav = "My Progress"
                    st.rerun()
            with c_btn2:
                if st.button("🔄 Reassessment Available ➔", key="ass_go_to_reassessment", type="secondary", use_container_width=True):
                    st.session_state.sidebar_nav = "Reassessment Available"
                    st.rerun()
            with c_btn3:
                if st.button("🔍 View Skill Gap Analysis ➔", key="ass_go_to_gap", type="secondary", use_container_width=True):
                    st.session_state.sidebar_nav = "Skill Gap Analysis"
                    st.rerun()
        else:
            with st.form("assessment_form"):
                for skill in skills_list:
                    st.markdown(f"### 🔹 Skill: **{skill}**")
                    qs = role_questions.get(skill, [])
                    for i, q in enumerate(qs):
                        key = f"{selected_role_name}_{skill}_{i}"
                        current_val = st.session_state.assessment_answers.get(key, None)
                        
                        st.markdown(f"**Q{i+1}. {q['q']}**")
                        options = q["options"]
                        
                        selected_opt = st.radio(
                            label=f"q_{key}",
                            options=options,
                            index=options.index(current_val) if current_val in options else None,
                            key=f"radio_{key}",
                            label_visibility="collapsed"
                        )
                        if selected_opt:
                            st.session_state.assessment_answers[key] = selected_opt
                        st.markdown("---")

                submit_assessment = st.form_submit_button("Submit Assessment ➔", type="primary", use_container_width=True)

                if submit_assessment:
                    # Validate all questions answered
                    total_req_qs = len(skills_list) * 5
                    ans_count = len(st.session_state.assessment_answers)
                    
                    if ans_count < total_req_qs:
                        st.warning(f"Please answer all {total_req_qs} questions before submitting. ({ans_count}/{total_req_qs} answered)")
                    else:
                        st.session_state.assessment_submitted = True
                        st.session_state.initial_analytics = calculate_assessment_results(selected_role_name, st.session_state.assessment_answers)
                        
                        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        st.session_state.assessment_date = now_str
                        st.session_state.assessment_history = [{
                            "type": "Initial Assessment",
                            "date": now_str,
                            "role": selected_role_name,
                            "readiness_pct": st.session_state.initial_analytics.get("readiness_pct", 0.0),
                            "readiness_status": st.session_state.initial_analytics.get("readiness_status", "N/A"),
                            "analytics": st.session_state.initial_analytics
                        }]

                        # Record all asked question IDs/texts to guarantee NO REPEATED QUESTIONS
                        role_qs = QUESTIONS_DATA.get(selected_role_name, {})
                        for sk, q_list in role_qs.items():
                            for idx, q_obj in enumerate(q_list):
                                st.session_state.asked_question_ids.add(f"{selected_role_name}_{sk}_{idx}")
                                st.session_state.asked_question_ids.add(q_obj["q"].strip().lower())

                        if st.session_state.user_email:
                            save_student_progress(
                                email=st.session_state.user_email,
                                selected_role=selected_role_name,
                                assessment_submitted=True,
                                assessment_answers=st.session_state.assessment_answers,
                                initial_analytics=st.session_state.initial_analytics,
                                assessment_date=st.session_state.assessment_date,
                                asked_question_ids=st.session_state.asked_question_ids,
                                assessment_history=st.session_state.assessment_history
                            )

                        st.success("Assessment Submitted Successfully!")
                        st.session_state.sidebar_nav = "Skill Gap Analysis"
                        st.rerun()


    # -------------------------------------------------------------
    # VIEW 5: SKILL GAP ANALYSIS & STUDENT LEVEL CALCULATION
    # -------------------------------------------------------------
    elif current_nav in ["Skill Gap Analysis", "Readiness Score Calculation", "Interactive Dashboard & Data Visualization", "Learning Recommendation", "My Progress", "Reassessment Available", "Report Generation", "Final Report"]:

        if not st.session_state.assessment_submitted:
            st.warning("⚠️ You have not submitted the Student Skill Assessment yet!")
            st.info("Please complete the assessment first to calculate your skill levels, gaps, and readiness score.")
            if st.button("Take Assessment Now ➔", type="primary"):
                st.session_state.sidebar_nav = "Student Skill Assessment"
                st.rerun()
        else:
            # Display based on selected sidebar view

            # --- SKILL GAP ANALYSIS VIEW ---
            if current_nav == "Skill Gap Analysis":
                st.markdown(f"## 🔍 Skill Gap Analysis - {selected_role_name}")
                st.markdown("Comparing your calculated skill levels against industry required levels:")

                table_rows = []
                for item in analytics["results"]:
                    table_rows.append({
                        "Skill Name": item["skill"],
                        "Student Level": item["student_level_str"],
                        "Industry Required Level": item["industry_level_str"],
                        "Skill Gap": item["gap_str"],
                        "Status": item["status"]
                    })

                df_gap = pd.DataFrame(table_rows)
                st.dataframe(df_gap, use_container_width=True)

                st.markdown("### 📌 Level Summary per Skill:")
                cols = st.columns(len(analytics["results"]))
                for idx, item in enumerate(analytics["results"]):
                    with cols[idx % len(cols)]:
                        st.metric(
                            label=item["skill"],
                            value=item["student_level_str"],
                            delta=f"-{item['gap_str']}" if item["gap_num"] > 0 else "Met"
                        )

                # Next Button Navigation
                st.markdown("<br>", unsafe_allow_html=True)
                col_n1, col_n2 = st.columns([8, 2])
                with col_n2:
                    if st.button("Next ➔", key="next_from_gap_analysis", type="primary", use_container_width=True):
                        st.session_state.sidebar_nav = "Readiness Score Calculation"
                        st.rerun()


            # --- READINESS SCORE CALCULATION VIEW ---
            elif current_nav == "Readiness Score Calculation":
                st.markdown("## ⏱️ Readiness Score Calculation")
                st.markdown("Formula used:")
                st.code("Placement Readiness Percentage = (Student Total Level Score / Required Level Score) × 100", language="text")

                res_col1, res_col2, res_col3, res_col4 = st.columns(4)
                with res_col1:
                    st.metric("Student Score", analytics["student_total_score"])
                with res_col2:
                    st.metric("Required Level Score", analytics["required_total_score"])
                with res_col3:
                    st.metric("Placement Readiness", f"{analytics['readiness_pct']}%")
                with res_col4:
                    st.metric("Readiness Status", analytics["readiness_status"])

                st.markdown(f"""
                <div class="result-card" style="text-align: center; border-left: 6px solid {analytics['status_color']};">
                    <div style="font-size: 1.1rem; font-weight: 600; color: #64748b;">Placement Readiness Score</div>
                    <div class="result-score-highlight" style="color: {analytics['status_color']};">{analytics['readiness_pct']}%</div>
                    <div class="result-badge" style="background: {analytics['status_color']};">
                        Status: {analytics['readiness_status']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Categories rule breakdown
                st.markdown("### 📊 Readiness Categories Rule Reference:")
                st.markdown("""
                - **92% to 100%**: Excellent
                - **75% to 90%**: Good
                - **50% to 74%**: Average
                - **Below 50%**: Need Improvement
                """)

                # Next Button Navigation
                st.markdown("<br>", unsafe_allow_html=True)
                col_n1, col_n2 = st.columns([8, 2])
                with col_n2:
                    if st.button("Next ➔", key="next_from_readiness_score", type="primary", use_container_width=True):
                        st.session_state.sidebar_nav = "Interactive Dashboard & Data Visualization"
                        st.rerun()


            # --- INTERACTIVE DASHBOARD & DATA VISUALIZATION VIEW ---
            elif current_nav == "Interactive Dashboard & Data Visualization":
                st.markdown(f"## 📊 Interactive Dashboard & Data Visualization - {selected_role_name}")

                skills = [item["skill"] for item in analytics["results"]]
                student_lvls = [item["student_level_num"] for item in analytics["results"]]
                industry_lvls = [item["industry_level_num"] for item in analytics["results"]]
                gaps = [item["gap_num"] for item in analytics["results"]]

                # 1. Grouped Bar Chart: Student vs Industry Levels
                fig_bar = go.Figure()
                fig_bar.add_trace(go.Bar(
                    x=skills,
                    y=student_lvls,
                    name='Student Level',
                    marker_color='#2563eb'
                ))
                fig_bar.add_trace(go.Bar(
                    x=skills,
                    y=industry_lvls,
                    name='Industry Required Level',
                    marker_color='#0d9488'
                ))
                fig_bar.update_layout(
                    title="Student Skill Level vs Industry Required Level",
                    xaxis_title="Skills",
                    yaxis_title="Skill Level (1-5)",
                    barmode='group',
                    template="plotly_white",
                    height=420
                )
                st.plotly_chart(fig_bar, use_container_width=True)

                col_v1, col_v2 = st.columns(2)
                with col_v1:
                    # 2. Radar Chart
                    fig_radar = go.Figure()
                    fig_radar.add_trace(go.Scatterpolar(
                        r=student_lvls,
                        theta=skills,
                        fill='toself',
                        name='Student Level',
                        line_color='#2563eb'
                    ))
                    fig_radar.add_trace(go.Scatterpolar(
                        r=industry_lvls,
                        theta=skills,
                        fill='toself',
                        name='Industry Level',
                        line_color='#0d9488'
                    ))
                    fig_radar.update_layout(
                        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
                        showlegend=True,
                        title="Skill Profile Radar Chart",
                        height=380
                    )
                    st.plotly_chart(fig_radar, use_container_width=True)

                with col_v2:
                    # 3. Placement Readiness Gauge Chart
                    fig_gauge = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=analytics['readiness_pct'],
                        domain={'x': [0, 1], 'y': [0, 1]},
                        title={'text': f"Placement Readiness ({analytics['readiness_status']})"},
                        gauge={
                            'axis': {'range': [0, 100]},
                            'bar': {'color': analytics['status_color']},
                            'steps': [
                                {'range': [0, 50], 'color': "#fee2e2"},
                                {'range': [50, 75], 'color': "#fef3c7"},
                                {'range': [75, 91], 'color': "#dbeafe"},
                                {'range': [91, 100], 'color': "#dcfce7"}
                            ]
                        }
                    ))
                    fig_gauge.update_layout(height=380)
                    st.plotly_chart(fig_gauge, use_container_width=True)

                # Next Button Navigation
                st.markdown("<br>", unsafe_allow_html=True)
                col_n1, col_n2 = st.columns([8, 2])
                with col_n2:
                    if st.button("Next ➔", key="next_from_visualization", type="primary", use_container_width=True):
                        st.session_state.sidebar_nav = "Learning Recommendation"
                        st.rerun()


            # --- LEARNING RECOMMENDATION VIEW ---
            elif current_nav == "Learning Recommendation":
                st.markdown("## 💡 Learning Recommendation")
                st.markdown(f"Personalized action plan to bridge skill gaps for **{selected_role_name}**:")

                for item in analytics["results"]:
                    sk_name = item["skill"]
                    rec_text = get_recommendation(sk_name, item["student_level_num"], item["industry_level_num"])
                    yt_link = get_youtube_link(selected_role_name, sk_name)

                    gap_num = item["gap_num"]
                    student_lvl_str = item["student_level_str"]
                    industry_lvl_str = item["industry_level_str"]

                    current_lvl_html = (
                        f'<div style="background: #fef9c3; color: #854d0e; border: 1px solid #fde047; padding: 6px 12px; border-radius: 6px; font-weight: 700; font-size: 0.88rem; display: inline-block; margin-right: 8px; margin-bottom: 8px;">'
                        f'🟡 Current Level: {student_lvl_str}'
                        f'</div>'
                    )

                    industry_tgt_html = (
                        f'<div style="background: #dbeafe; color: #1e40af; border: 1px solid #93c5fd; padding: 6px 12px; border-radius: 6px; font-weight: 700; font-size: 0.88rem; display: inline-block; margin-right: 8px; margin-bottom: 8px;">'
                        f'🔵 Industry Target: {industry_lvl_str}'
                        f'</div>'
                    )

                    if gap_num > 0:
                        border_color = '#dc2626'
                        gap_html = (
                            f'<div style="background: #fee2e2; color: #991b1b; border: 1px solid #fca5a5; padding: 6px 12px; border-radius: 6px; font-weight: 700; font-size: 0.88rem; display: inline-block; margin-right: 8px; margin-bottom: 8px;">'
                            f'🔴 Skill Gap: {gap_num} Level{"s" if gap_num > 1 else ""}'
                            f'</div>'
                        )
                        improvement_html = (
                            f'<div style="font-size: 0.9rem; color: #991b1b; background: #fef2f2; border: 1px solid #fecaca; padding: 10px 14px; border-radius: 6px; margin-bottom: 8px; font-weight: 600;">'
                            f'<strong>Improvement Needed:</strong> Improve by {gap_num} level{"s" if gap_num > 1 else ""} to reach the industry target.'
                            f'</div>'
                        )
                    else:
                        border_color = '#16a34a'
                        gap_html = (
                            f'<div style="background: #dcfce7; color: #166534; border: 1px solid #86efac; padding: 6px 12px; border-radius: 6px; font-weight: 700; font-size: 0.88rem; display: inline-block; margin-right: 8px; margin-bottom: 8px;">'
                            f'🟢 Skill Gap: No Gap'
                            f'</div>'
                            f'<div style="background: #dcfce7; color: #166534; border: 1px solid #86efac; padding: 6px 12px; border-radius: 6px; font-weight: 700; font-size: 0.88rem; display: inline-block; margin-right: 8px; margin-bottom: 8px;">'
                            f'🟢 Status: Industry Target Met'
                            f'</div>'
                        )
                        improvement_html = (
                            f'<div style="font-size: 0.9rem; color: #166534; background: #f0fdf4; border: 1px solid #bbf7d0; padding: 10px 14px; border-radius: 6px; margin-bottom: 8px; font-weight: 600;">'
                            f'<strong>Status:</strong> Industry Target Met'
                            f'</div>'
                        )

                    card_html = (
                        f'<div style="background: #ffffff; border-left: 5px solid {border_color}; border-radius: 10px; padding: 18px 22px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">'
                        f'<div style="font-size: 1.1rem; font-weight: 800; color: #1e293b; margin-bottom: 10px;">Skill: {sk_name}</div>'
                        f'<div style="margin-bottom: 8px;">'
                        f'{current_lvl_html}'
                        f'{industry_tgt_html}'
                        f'{gap_html}'
                        f'</div>'
                        f'{improvement_html}'
                        f'<div style="font-size: 0.92rem; color: #1e3a8a; background: #eff6ff; border: 1px solid #bfdbfe; padding: 10px 14px; border-radius: 6px; margin-bottom: 4px;">'
                        f'<strong>Learning Recommendation:</strong> {rec_text}'
                        f'</div>'
                        f'</div>'
                    )
                    st.markdown(card_html, unsafe_allow_html=True)


                    if yt_link:
                        col_yt1, col_yt2 = st.columns([1.2, 3.8])
                        with col_yt1:
                            st.link_button(f"▶️ Watch {sk_name} Tutorial", yt_link, use_container_width=True, type="primary")
                        with col_yt2:
                            st.markdown(f"<div style='margin-top: 6px;'>🔗 <strong>Direct YouTube Link:</strong> <a href='{yt_link}' target='_blank' style='color: #2563eb; text-decoration: underline; word-break: break-all;'>{yt_link}</a></div>", unsafe_allow_html=True)

                    st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

                # Next Button Navigation to My Progress
                st.markdown("<br>", unsafe_allow_html=True)
                col_n1, col_n2 = st.columns([8, 2])
                with col_n2:
                    if st.button("Next ➔", key="next_from_learning_rec", type="primary", use_container_width=True):
                        st.session_state.sidebar_nav = "My Progress"
                        st.rerun()


            # --- MY PROGRESS VIEW ---
            elif current_nav == "My Progress":
                st.markdown(f"## 📈 My Progress - {selected_role_name}")
                st.markdown("Track your learning progress, initial assessment benchmarks, and reassessment status:")

                initial_analytics = st.session_state.initial_analytics or analytics
                weak_skills = get_weak_skills(initial_analytics)
                ass_date_str = st.session_state.get("assessment_date") or "N/A"
                re_date_str = st.session_state.get("reassessment_date") or "Not taken yet"

                st.markdown(f"""
                <div class="progress-banner">
                    <div style="font-size: 1.4rem; font-weight: 800; margin-bottom: 6px;">🎯 Student Learning Progress Overview</div>
                    <div style="font-size: 0.95rem; color: #cbd5e1; margin-bottom: 8px;">
                        User Account: <strong>{st.session_state.user_email}</strong> | Selected Role: <strong>{selected_role_name}</strong> | Initial Assessment Date: <strong>{ass_date_str}</strong>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                p_col1, p_col2, p_col3, p_col4 = st.columns(4)
                with p_col1:
                    st.metric("Initial Readiness", f"{initial_analytics['readiness_pct']}%")
                with p_col2:
                    st.metric("Initial Readiness Status", initial_analytics['readiness_status'])
                with p_col3:
                    st.metric("Weak Skills Identified", len(weak_skills))
                with p_col4:
                    re_status_label = f"Completed ({re_date_str})" if st.session_state.reassessment_submitted else "Reassessment Available"
                    st.metric("Reassessment Status", re_status_label)

                st.markdown(f"### 🔍 Previous Assessment Details ({ass_date_str})")
                p_table_rows = []
                for item in initial_analytics["results"]:
                    is_weak = item["student_level_num"] < item["industry_level_num"]
                    p_table_rows.append({
                        "Skill Name": item["skill"],
                        "Current Student Level": item["student_level_str"],
                        "Industry Target Level": item["industry_level_str"],
                        "Skill Gap": item["gap_str"],
                        "Target Status": "⚠️ Weak Skill (Target for Reassessment)" if is_weak else "✅ Strong Skill (Target Met)"
                    })

                df_p = pd.DataFrame(p_table_rows)
                st.dataframe(df_p, use_container_width=True)

                # Historical Progress Timeline over time
                st.markdown("### 📊 Assessment History & Progress Over Time")
                all_role_records = get_all_student_role_progress(st.session_state.get("user_email")) if st.session_state.get("user_email") else []
                combined_history = []
                if all_role_records:
                    for rec in all_role_records:
                        try:
                            h_list = json.loads(rec.get("assessment_history_json", "[]"))
                            combined_history.extend(h_list)
                        except Exception:
                            pass
                else:
                    combined_history = st.session_state.get("assessment_history", [])

                if combined_history:
                    h_rows = []
                    for h in combined_history:
                        h_rows.append({
                            "Attempt Type": h.get("type", "Assessment"),
                            "Date & Time": h.get("date", "N/A"),
                            "Career Role": h.get("role", selected_role_name),
                            "Readiness Score": f"{h.get('readiness_pct', 0.0)}%",
                            "Readiness Status": h.get("readiness_status", "N/A")
                        })
                    df_h = pd.DataFrame(h_rows)
                    st.dataframe(df_h, use_container_width=True)
                else:
                    st.info("No prior history recorded yet.")

                st.markdown("### 🚀 Progress Action Plan")
                if weak_skills:
                    st.warning(f"**Identified Weak Skills:** {', '.join(weak_skills)}")
                    st.markdown("Click below to attempt your personalized Reassessment with **NEW questions** for these weak skills.")
                else:
                    st.success("🎉 You met all industry required levels in your initial assessment! You can still take the Reassessment to attempt advanced challenges.")

                # Stage 2: Reassessment Available Section
                st.markdown("""
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 14px; padding: 20px 24px; margin-top: 24px; margin-bottom: 16px;">
                    <div style="font-size: 1.15rem; font-weight: 800; color: #166534; margin-bottom: 6px;">
                        🔄 Next Stage: Reassessment Available
                    </div>
                    <div style="font-size: 0.92rem; color: #15803d; line-height: 1.5;">
                        Reassessment focuses specifically on identified weak skills. Your initial assessment result remains saved permanently as historical progress, and your new reassessment result will be saved alongside it.
                    </div>
                </div>
                """, unsafe_allow_html=True)

                col_n1, col_n2 = st.columns([7, 3])
                with col_n2:
                    if st.button("Reassessment Available ➔", key="go_to_reassessment_from_progress", type="primary", use_container_width=True):
                        st.session_state.sidebar_nav = "Reassessment Available"
                        st.rerun()


            # --- REASSESSMENT AVAILABLE VIEW ---
            elif current_nav == "Reassessment Available":
                st.markdown(f"## 🔄 Reassessment Available - {selected_role_name}")

                initial_analytics = st.session_state.initial_analytics or analytics
                weak_skills = get_weak_skills(initial_analytics)

                st.markdown("""
                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 14px; padding: 20px 24px; margin-bottom: 20px;">
                    <div style="font-size: 1.15rem; font-weight: 800; color: #166534; margin-bottom: 6px;">
                        🎯 Weak Skills Reassessment Engine
                    </div>
                    <div style="font-size: 0.92rem; color: #15803d; line-height: 1.5;">
                        This reassessment presents <strong>NEW and DIFFERENT questions</strong> for your identified weak skills. Strong skills are excluded.
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if not weak_skills:
                    st.success("🎉 You have met or exceeded all industry required levels for this career role! No weak skills require reassessment.")
                else:
                    st.markdown(f"**Target Weak Skills for Reassessment ({len(weak_skills)}):** " + ", ".join([f"`{sk}`" for sk in weak_skills]))

                # Generate or load unique reassessment questions for weak skills
                if not st.session_state.reassessment_questions_map:
                    qs_map = {}
                    for sk in weak_skills:
                        avail_qs = REASSESSMENT_QUESTIONS_DATA.get(sk, [])
                        unasked = []
                        for q in avail_qs:
                            q_id = q.get("id", "")
                            q_norm = q.get("q", "").strip().lower()
                            if q_id not in st.session_state.asked_question_ids and q_norm not in st.session_state.asked_question_ids:
                                unasked.append(q)

                        if not unasked:
                            unasked = avail_qs

                        qs_map[sk] = unasked[:5] # 5 level questions per skill

                    st.session_state.reassessment_questions_map = qs_map

                qs_map = st.session_state.reassessment_questions_map

                with st.form("reassessment_quiz_form"):
                    for sk in weak_skills:
                        st.markdown(f"### 🔹 Weak Skill: **{sk}**")
                        sk_qs = qs_map.get(sk, [])

                        for i, q in enumerate(sk_qs):
                            q_id = q.get("id", f"{sk}_{i}")
                            st.markdown(f"**Q{i+1}. {q['q']}**")

                            ans_key = f"re_{selected_role_name}_{sk}_{q_id}"
                            current_val = st.session_state.reassessment_answers.get(ans_key, None)
                            options = q["options"]

                            selected_opt = st.radio(
                                label=f"q_{ans_key}",
                                options=options,
                                index=options.index(current_val) if current_val in options else None,
                                key=f"radio_{ans_key}",
                                label_visibility="collapsed"
                            )
                            if selected_opt:
                                st.session_state.reassessment_answers[ans_key] = selected_opt
                            st.markdown("---")

                    submit_reassessment = st.form_submit_button("Submit Answers ➔", type="primary", use_container_width=True)

                    if submit_reassessment:
                        total_qs_needed = sum(len(qs_map.get(sk, [])) for sk in weak_skills)
                        total_ans_given = sum(1 for sk in weak_skills for q in qs_map.get(sk, []) if f"re_{selected_role_name}_{sk}_{q.get('id','')}" in st.session_state.reassessment_answers)

                        if total_ans_given < total_qs_needed:
                            st.warning(f"Please answer all {total_qs_needed} questions before submitting. ({total_ans_given}/{total_qs_needed} answered)")
                        else:
                            st.session_state.reassessment_submitted = True
                            st.session_state.reassessment_analytics = calculate_reassessment_results(
                                selected_role_name,
                                initial_analytics,
                                st.session_state.reassessment_answers,
                                qs_map
                            )

                            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            st.session_state.reassessment_date = now_str

                            # Update history without deleting initial assessment
                            history = list(st.session_state.get("assessment_history", []))
                            if not history:
                                history.append({
                                    "type": "Initial Assessment",
                                    "date": st.session_state.get("assessment_date") or now_str,
                                    "role": selected_role_name,
                                    "readiness_pct": initial_analytics.get("readiness_pct", 0.0),
                                    "readiness_status": initial_analytics.get("readiness_status", "N/A"),
                                    "analytics": initial_analytics
                                })

                            history.append({
                                "type": "Reassessment",
                                "date": now_str,
                                "role": selected_role_name,
                                "readiness_pct": st.session_state.reassessment_analytics.get("updated_readiness_pct", 0.0),
                                "readiness_status": st.session_state.reassessment_analytics.get("updated_readiness_status", "N/A"),
                                "analytics": st.session_state.reassessment_analytics
                            })
                            st.session_state.assessment_history = history

                            # Record asked questions to prevent repetitions in future attempts
                            for sk in weak_skills:
                                for q in qs_map.get(sk, []):
                                    st.session_state.asked_question_ids.add(q.get("id", ""))
                                    st.session_state.asked_question_ids.add(q.get("q", "").strip().lower())

                            if st.session_state.user_email:
                                save_student_progress(
                                    email=st.session_state.user_email,
                                    selected_role=selected_role_name,
                                    assessment_submitted=True,
                                    assessment_answers=st.session_state.assessment_answers,
                                    initial_analytics=st.session_state.initial_analytics,
                                    assessment_date=st.session_state.get("assessment_date"),
                                    reassessment_submitted=True,
                                    reassessment_answers=st.session_state.reassessment_answers,
                                    reassessment_analytics=st.session_state.reassessment_analytics,
                                    reassessment_date=st.session_state.reassessment_date,
                                    reassessment_questions_map=qs_map,
                                    asked_question_ids=st.session_state.asked_question_ids,
                                    assessment_history=st.session_state.assessment_history
                                )

                            st.success("Reassessment Submitted Successfully!")
                            st.rerun()

                # BEFORE vs AFTER COMPARISON & UPDATED READINESS SCORE
                if st.session_state.reassessment_submitted and st.session_state.reassessment_analytics:
                    re_data = st.session_state.reassessment_analytics

                    st.markdown("<br><hr>", unsafe_allow_html=True)
                    st.markdown("## 📊 BEFORE vs AFTER COMPARISON")
                    st.markdown("Clear comparison showing your skill improvement from initial assessment to reassessment:")

                    # Top Metric Chips
                    mc1, mc2, mc3, mc4 = st.columns(4)
                    with mc1:
                        st.metric("Initial Score", f"{re_data['initial_readiness_pct']}%")
                    with mc2:
                        st.metric("Reassessment Score", f"{re_data['updated_readiness_pct']}%", delta=f"+{re_data['readiness_improvement']}%")
                    with mc3:
                        st.metric("Updated Status", re_data['updated_readiness_status'])
                    with mc4:
                        st.metric("Improvement", f"+{re_data['total_improvement_levels']} Levels")

                    # Detailed Comparison Table
                    comp_rows = []
                    for r in re_data["results"]:
                        comp_rows.append({
                            "Skill Name": r["skill"],
                            "Initial Score": r["initial_score"],
                            "Reassessment Score": r["reassessment_score"],
                            "Industry Expected": r["industry_expected_score"],
                            "Skill Gap Before": r["gap_before_str"],
                            "Skill Gap After": r["gap_after_str"],
                            "Improvement": f"+{r['pct_improvement']}%" if r["pct_improvement"] >= 0 else f"{r['pct_improvement']}%"
                        })

                    df_comp = pd.DataFrame(comp_rows)
                    st.dataframe(df_comp, use_container_width=True)

                    st.markdown("### ⏱️ UPDATED READINESS SCORE & STATUS")
                    st.markdown(f"""
                    <div class="result-card" style="text-align: center; border-left: 6px solid {re_data['updated_status_color']};">
                        <div style="font-size: 1.1rem; font-weight: 600; color: #64748b;">Updated Placement Readiness Score</div>
                        <div class="result-score-highlight" style="color: {re_data['updated_status_color']};">{re_data['updated_readiness_pct']}%</div>
                        <div class="result-badge" style="background: {re_data['updated_status_color']};">
                            Status: {re_data['updated_readiness_status']}
                        </div>
                        <br><br>
                        <div style="font-size: 0.95rem; color: #1e293b; text-align: left; background: #f8fafc; padding: 14px 18px; border-radius: 8px; border: 1px solid #e2e8f0;">
                            <strong>Updated Recommendation:</strong> Your readiness score increased by <strong>+{re_data['readiness_improvement']}%</strong> following the reassessment.
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    col_n1, col_n2 = st.columns([8, 2])
                    with col_n2:
                        if st.button("Next to Report ➔", key="next_from_reassessment_page", type="primary", use_container_width=True):
                            st.session_state.sidebar_nav = "Report Generation"
                            st.rerun()


            # --- REPORT GENERATION VIEW ---
            elif current_nav == "Report Generation":
                st.markdown("## 📄 Report Generation")
                st.markdown("Download your complete Student Skill Gap Analytics report (Includes Initial Assessment & Latest Reassessment Data):")

                user_email = st.session_state.get("user_email", "")
                all_role_records = get_all_student_role_progress(user_email) if user_email else []
                completed_records = [r for r in all_role_records if r.get("assessment_submitted")]

                if completed_records:
                    completed_roles = [r["selected_role"] for r in completed_records]
                    if selected_role_name in completed_roles:
                        default_idx = completed_roles.index(selected_role_name)
                    else:
                        default_idx = 0

                    rep_role = st.selectbox(
                        "📌 Select Career Role Report to View/Download:",
                        options=completed_roles,
                        index=default_idx,
                        key="rep_gen_role_select"
                    )

                    target_rec = next((r for r in completed_records if r["selected_role"] == rep_role), None)
                    if target_rec:
                        rep_init_analytics = json.loads(target_rec["initial_analytics_json"])
                        try:
                            rep_re_analytics = json.loads(target_rec["reassessment_analytics_json"])
                        except Exception:
                            rep_re_analytics = None
                    else:
                        rep_role = selected_role_name
                        rep_init_analytics = st.session_state.initial_analytics or analytics
                        rep_re_analytics = st.session_state.reassessment_analytics
                else:
                    rep_role = selected_role_name
                    rep_init_analytics = st.session_state.initial_analytics or analytics
                    rep_re_analytics = st.session_state.reassessment_analytics

                report_text = generate_text_report(
                    st.session_state.user_name,
                    st.session_state.user_email,
                    rep_role,
                    rep_init_analytics,
                    rep_re_analytics
                )

                st.text_area(f"Report Preview ({rep_role})", report_text, height=350)

                st.download_button(
                    label=f"📥 Download {rep_role} Analytics Report (.txt)",
                    data=report_text,
                    file_name=f"Skill_Gap_Report_{st.session_state.user_name.replace(' ', '_')}_{rep_role.replace(' ', '_')}.txt",
                    mime="text/plain",
                    type="primary",
                    use_container_width=True
                )

                # Next to Final Report
                st.markdown("<br>", unsafe_allow_html=True)
                col_n1, col_n2 = st.columns([8, 2])
                with col_n2:
                    if st.button("Final Report ➔", key="next_from_report_gen", type="primary", use_container_width=True):
                        st.session_state.sidebar_nav = "Final Report"
                        st.rerun()


            # --- FINAL REPORT VIEW ---
            elif current_nav == "Final Report":
                st.markdown("## 📋 Final Report")
                st.markdown("Comprehensive overall report detailing student performance, initial assessment, weak skills, learning recommendations, reassessment results, before vs after comparison, and updated readiness status:")

                user_email = st.session_state.get("user_email", "")
                all_role_records = get_all_student_role_progress(user_email) if user_email else []
                completed_records = [r for r in all_role_records if r.get("assessment_submitted")]

                if completed_records:
                    completed_roles = [r["selected_role"] for r in completed_records]
                    if selected_role_name in completed_roles:
                        default_idx = completed_roles.index(selected_role_name)
                    else:
                        default_idx = 0

                    rep_role = st.selectbox(
                        "📌 Select Career Role for Final Report:",
                        options=completed_roles,
                        index=default_idx,
                        key="final_rep_role_select"
                    )

                    target_rec = next((r for r in completed_records if r["selected_role"] == rep_role), None)
                    if target_rec:
                        rep_init_analytics = json.loads(target_rec["initial_analytics_json"])
                        try:
                            rep_re_analytics = json.loads(target_rec["reassessment_analytics_json"])
                        except Exception:
                            rep_re_analytics = None
                        rep_weak_skills = get_weak_skills(rep_init_analytics)
                    else:
                        rep_role = selected_role_name
                        rep_init_analytics = st.session_state.initial_analytics or analytics
                        rep_re_analytics = st.session_state.reassessment_analytics
                        rep_weak_skills = get_weak_skills(rep_init_analytics)
                else:
                    rep_role = selected_role_name
                    rep_init_analytics = st.session_state.initial_analytics or analytics
                    rep_re_analytics = st.session_state.reassessment_analytics
                    rep_weak_skills = get_weak_skills(rep_init_analytics)

                final_report_text = generate_final_report(
                    st.session_state.user_name,
                    st.session_state.user_email,
                    rep_role,
                    rep_init_analytics,
                    rep_re_analytics,
                    rep_weak_skills
                )

                st.text_area(f"Final Comprehensive Report Preview ({rep_role})", final_report_text, height=450)

                st.download_button(
                    label=f"📥 Download {rep_role} Final Report (.txt)",
                    data=final_report_text,
                    file_name=f"Final_Skill_Gap_Report_{st.session_state.user_name.replace(' ', '_')}_{rep_role.replace(' ', '_')}.txt",
                    mime="text/plain",
                    type="primary",
                    use_container_width=True
                )

                # Back to Dashboard
                st.markdown("<br>", unsafe_allow_html=True)
                col_n1, col_n2 = st.columns([8, 2])
                with col_n2:
                    if st.button("Back to Dashboard ➔", key="back_to_dash_from_final", type="primary", use_container_width=True):
                        st.session_state.sidebar_nav = "Dashboard"
                        st.rerun()


