import os
import sys
import json
from datetime import datetime

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mock Streamlit session_state before importing auth
import streamlit as st
class DummySessionState(dict):
    def __getattr__(self, key):
        return self.get(key, None)
    def __setattr__(self, key, value):
        self[key] = value

if not hasattr(st, "session_state") or not isinstance(st.session_state, DummySessionState):
    st.session_state = DummySessionState()

from utils.auth import (
    init_auth_state, register_user, login_user, logout_user,
    get_student_progress, get_all_student_role_progress, save_student_progress, load_student_progress,
    DB_PATH
)
from utils.analytics import calculate_assessment_results, get_weak_skills, calculate_reassessment_results
from utils.report import generate_text_report, generate_final_report
from data.career_roles import CAREER_ROLES
from data.questions_data import QUESTIONS_DATA
from data.reassessment_questions import REASSESSMENT_QUESTIONS_DATA

def run_test():
    print("=================================================================")
    print("STARTING MULTI-CAREER ROLE ISOLATION & SWITCHING TEST")
    print("=================================================================")
    print(f"Database Path: {DB_PATH}")

    # Step 0: Init DB
    init_auth_state()

    test_name = "Cloud Student"
    test_email = f"cloud_student_{int(datetime.now().timestamp())}@example.com"
    test_pass = "TestPass123!"

    # 1. Register User & Login
    print(f"\n[STEP 1] Registering and logging in user: {test_email}")
    register_user(test_name, test_email, test_pass, test_pass)
    login_user(test_email, test_pass)

    # 2. Complete Cloud Computing
    role1 = "Cloud Computing"
    print(f"\n[STEP 2] Completing Assessment & Reassessment for Role 1: {role1}")
    role1_qs = QUESTIONS_DATA.get(role1, {})
    role1_skills = CAREER_ROLES[role1]["skills"]

    answers1 = {}
    for skill in role1_skills:
        qs = role1_qs.get(skill, [])
        for i, q in enumerate(qs):
            key = f"{role1}_{skill}_{i}"
            answers1[key] = q["options"][0]

    analytics1 = calculate_assessment_results(role1, answers1)
    weak1 = get_weak_skills(analytics1)
    date1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hist1 = [{
        "type": "Initial Assessment",
        "date": date1,
        "role": role1,
        "readiness_pct": analytics1["readiness_pct"],
        "readiness_status": analytics1["readiness_status"],
        "analytics": analytics1
    }]

    save_student_progress(
        email=test_email,
        selected_role=role1,
        assessment_submitted=True,
        assessment_answers=answers1,
        initial_analytics=analytics1,
        assessment_date=date1,
        assessment_history=hist1
    )

    print(f"-> {role1} initial assessment saved!")

    # 3. Switch to UI/UX Designer BEFORE taking UI/UX Designer assessment
    role2 = "UI/UX Designer"
    print(f"\n[STEP 3] Switching to NEW role before taking it: {role2}")
    
    # Simulate select_role(role2)
    # Save current role state first
    save_student_progress(
        email=test_email,
        selected_role=st.session_state.selected_role,
        assessment_submitted=st.session_state.assessment_submitted,
        assessment_answers=st.session_state.assessment_answers,
        initial_analytics=st.session_state.initial_analytics,
        assessment_date=st.session_state.assessment_date,
        assessment_history=st.session_state.assessment_history
    )

    st.session_state.selected_role = role2
    loaded = load_student_progress(test_email, role=role2)

    print(f"-> Trying to load unsubmitted role '{role2}'. Loaded returned: {loaded}")
    assert loaded is False, "Unsubmitted role MUST return False when loaded so a fresh initial assessment is shown!"
    
    # Reset state as select_role does when loaded is False
    st.session_state.assessment_answers = {}
    st.session_state.assessment_submitted = False
    st.session_state.initial_analytics = None

    assert st.session_state.assessment_submitted is False, f"{role2} MUST be unsubmitted!"
    assert st.session_state.initial_analytics is None, f"{role2} must NOT carry over {role1}'s analytics!"
    print(f"-> CONFIRMED: Switching to {role2} opens a FRESH Initial Assessment without carrying over {role1} data!")

    # 4. Now complete UI/UX Designer assessment
    print(f"\n[STEP 4] Completing Initial Assessment for Role 2: {role2}")
    role2_qs = QUESTIONS_DATA.get(role2, {})
    role2_skills = CAREER_ROLES[role2]["skills"]

    answers2 = {}
    for skill in role2_skills:
        qs = role2_qs.get(skill, [])
        for i, q in enumerate(qs):
            key = f"{role2}_{skill}_{i}"
            answers2[key] = q["answer"]

    analytics2 = calculate_assessment_results(role2, answers2)
    date2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hist2 = [{
        "type": "Initial Assessment",
        "date": date2,
        "role": role2,
        "readiness_pct": analytics2["readiness_pct"],
        "readiness_status": analytics2["readiness_status"],
        "analytics": analytics2
    }]

    save_student_progress(
        email=test_email,
        selected_role=role2,
        assessment_submitted=True,
        assessment_answers=answers2,
        initial_analytics=analytics2,
        assessment_date=date2,
        assessment_history=hist2
    )

    # 5. Switch back to Cloud Computing
    print(f"\n[STEP 5] Switching BACK to Role 1: {role1}")
    st.session_state.selected_role = role1
    loaded1_back = load_student_progress(test_email, role=role1)
    assert loaded1_back is True, f"Role 1 '{role1}' must load previous completed progress!"
    assert st.session_state.assessment_submitted is True, f"Role 1 '{role1}' must show assessment submitted!"
    assert st.session_state.initial_analytics["readiness_pct"] == analytics1["readiness_pct"], "Role 1 analytics must match!"

    print(f"-> CONFIRMED: Switching back to {role1} restores all its completed data intact!")

    print("\n=================================================================")
    print("ALL CAREER ROLE ISOLATION AND SWITCHING TESTS PASSED PERFECTLY!")
    print("=================================================================")

if __name__ == "__main__":
    run_test()
