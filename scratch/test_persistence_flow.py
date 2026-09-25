import os
import sys
import json
from datetime import datetime

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.auth import (
    init_auth_state, register_user, login_user, logout_user,
    get_student_progress, save_student_progress, load_student_progress,
    get_user_by_email, DB_PATH
)
from utils.analytics import calculate_assessment_results, get_weak_skills, calculate_reassessment_results
from data.career_roles import CAREER_ROLES
from data.questions_data import QUESTIONS_DATA
from data.reassessment_questions import REASSESSMENT_QUESTIONS_DATA

def run_test():
    print("=================================================================")
    print("STARTING PERSISTENCE FLOW VERIFICATION TEST")
    print("=================================================================")
    print(f"Database Path: {DB_PATH}")

    # Step 0: Init DB
    init_auth_state()

    test_name = "Persistence Test Student"
    test_email = f"persistence_student_{int(datetime.now().timestamp())}@example.com"
    test_pass = "TestPass123!"

    # 1. Register User
    print(f"\n[STEP 1] Registering user: {test_email}")
    success, msg = register_user(test_name, test_email, test_pass, test_pass)
    assert success is True, f"Registration failed: {msg}"
    print("-> Registration successful!")

    # 2. Login User
    print(f"\n[STEP 2] Logging in user: {test_email}")
    success_login, msg_login = login_user(test_email, test_pass)
    assert success_login is True, f"Login failed: {msg_login}"
    print("-> Login successful!")

    # 3. Select Career Role and Complete First Assessment
    role_name = "Data Analyst"
    print(f"\n[STEP 3] Completing First Assessment for role: {role_name}")
    role_qs = QUESTIONS_DATA.get(role_name, {})
    skills = CAREER_ROLES[role_name]["skills"]

    # Generate test answers (intentionally answer some wrong to create weak skills)
    assessment_answers = {}
    for skill in skills:
        qs = role_qs.get(skill, [])
        for i, q in enumerate(qs):
            key = f"{role_name}_{skill}_{i}"
            # Choose correct answer for 1st skill, wrong for others to ensure weak skills
            if skill == skills[0]:
                assessment_answers[key] = q["answer"]
            else:
                # choose first option which might or might not be correct
                assessment_answers[key] = q["options"][0]

    analytics = calculate_assessment_results(role_name, assessment_answers)
    weak_skills = get_weak_skills(analytics)
    ass_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    history = [{
        "type": "Initial Assessment",
        "date": ass_date,
        "role": role_name,
        "readiness_pct": analytics["readiness_pct"],
        "readiness_status": analytics["readiness_status"],
        "analytics": analytics
    }]

    # Permanently save to users.db
    save_student_progress(
        email=test_email,
        selected_role=role_name,
        assessment_submitted=True,
        assessment_answers=assessment_answers,
        initial_analytics=analytics,
        assessment_date=ass_date,
        assessment_history=history
    )
    print("-> First Assessment completed and saved to users.db!")
    print(f"   Readiness Pct: {analytics['readiness_pct']}%, Status: {analytics['readiness_status']}")
    print(f"   Weak Skills Identified: {weak_skills}")
    print(f"   Assessment Date: {ass_date}")

    # 4. Simulate Logout and passage of time (10 days later / browser restart)
    print("\n[STEP 4] Simulating logout and passage of 10 days...")
    logout_user()
    print("-> Session cleared completely.")

    # 5. Login again with SAME account
    print(f"\n[STEP 5] Logging in again after time passage with SAME account: {test_email}")
    success_relogin, msg_relogin = login_user(test_email, test_pass)
    assert success_relogin is True, f"Re-login failed: {msg_relogin}"

    # 6. Verify retrieved progress directly from DB & session state
    print("\n[STEP 6] Verifying loaded progress from users.db:")
    db_progress = get_student_progress(test_email)
    assert db_progress is not None, "Progress record should exist in DB!"
    assert db_progress["assessment_submitted"] is True, "First assessment MUST show completed!"
    assert db_progress["selected_role"] == role_name, f"Role should be {role_name}"
    assert db_progress["assessment_date"] == ass_date, f"Assessment date should match {ass_date}"

    loaded_analytics = json.loads(db_progress["initial_analytics_json"])
    assert loaded_analytics["readiness_pct"] == analytics["readiness_pct"], "Readiness score must match!"
    assert loaded_analytics["readiness_status"] == analytics["readiness_status"], "Readiness status must match!"

    loaded_history = json.loads(db_progress["assessment_history_json"])
    assert len(loaded_history) >= 1, "History must contain initial assessment record!"
    assert loaded_history[0]["type"] == "Initial Assessment"

    print("-> First assessment data verified inside DB!")
    print(f"   Retrieved Email: {test_email}")
    print(f"   Retrieved Role: {db_progress['selected_role']}")
    print(f"   Retrieved Readiness Score: {loaded_analytics['readiness_pct']}%")
    print(f"   Retrieved Readiness Status: {loaded_analytics['readiness_status']}")
    print(f"   Retrieved Assessment Date: {db_progress['assessment_date']}")

    # 7. Complete Reassessment for weak skills
    print("\n[STEP 7] Completing Reassessment for weak skills...")
    re_qs_map = {}
    re_answers = {}
    for sk in weak_skills:
        avail_qs = REASSESSMENT_QUESTIONS_DATA.get(sk, [])
        re_qs_map[sk] = avail_qs[:5]
        for i, q in enumerate(avail_qs[:5]):
            q_id = q.get("id", f"{sk}_{i}")
            ans_key = f"re_{role_name}_{sk}_{q_id}"
            re_answers[ans_key] = q["answer"] # give correct answers to demonstrate improvement

    re_analytics = calculate_reassessment_results(
        role_name,
        loaded_analytics,
        re_answers,
        re_qs_map
    )
    re_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append reassessment attempt to history without deleting initial assessment
    updated_history = loaded_history + [{
        "type": "Reassessment",
        "date": re_date,
        "role": role_name,
        "readiness_pct": re_analytics["updated_readiness_pct"],
        "readiness_status": re_analytics["updated_readiness_status"],
        "analytics": re_analytics
    }]

    save_student_progress(
        email=test_email,
        selected_role=role_name,
        assessment_submitted=True,
        assessment_answers=json.loads(db_progress["assessment_answers_json"]),
        initial_analytics=loaded_analytics,
        assessment_date=ass_date,
        reassessment_submitted=True,
        reassessment_answers=re_answers,
        reassessment_analytics=re_analytics,
        reassessment_date=re_date,
        reassessment_questions_map=re_qs_map,
        assessment_history=updated_history
    )
    print("-> Reassessment completed and saved!")

    # 8. Final Verification of Both Initial Assessment & Reassessment Data
    final_progress = get_student_progress(test_email)
    final_history = json.loads(final_progress["assessment_history_json"])

    print("\n[STEP 8] Final Verification of Historical Progress in users.db:")
    assert len(final_history) == 2, f"History should contain exactly 2 entries (Initial + Reassessment), got {len(final_history)}"
    assert final_history[0]["type"] == "Initial Assessment"
    assert final_history[1]["type"] == "Reassessment"

    print("-> Initial Assessment entry 0:")
    print(f"   Type: {final_history[0]['type']}, Date: {final_history[0]['date']}, Score: {final_history[0]['readiness_pct']}%")

    print("-> Reassessment entry 1:")
    print(f"   Type: {final_history[1]['type']}, Date: {final_history[1]['date']}, Score: {final_history[1]['readiness_pct']}%")

    print("\n=================================================================")
    print("ALL PERSISTENCE AND REASSESSMENT TESTS PASSED SUCCESSFULLY!")
    print("=================================================================")

if __name__ == "__main__":
    run_test()
