import sys
import os

sys.path.append(os.path.abspath("."))

from data.career_roles import CAREER_ROLES, LEVEL_MAP
from data.questions_data import QUESTIONS_DATA
from data.recommendations import SKILL_RECOMMENDATIONS, get_recommendation
from utils.auth import register_user, login_user
from utils.analytics import calculate_assessment_results
from utils.report import generate_text_report

def run_tests():
    print("=== STARTING APPLICATION VERIFICATION ===")

    expected_roles = [
        "Data Analyst",
        "Python Developer",
        "Full Stack Developer",
        "AI/ML Engineer",
        "Cyber Security Analyst",
        "UI/UX Designer",
        "Cloud Computing"
    ]
    assert list(CAREER_ROLES.keys()) == expected_roles, "Career Roles list mismatch!"
    print("[OK] Test 1 Passed: All 7 Career Roles defined correctly.")

    role_q_counts = {
        "Data Analyst": 30,
        "Python Developer": 35,
        "Full Stack Developer": 40,
        "AI/ML Engineer": 45,
        "Cyber Security Analyst": 55,
        "UI/UX Designer": 25,
        "Cloud Computing": 25
    }
    
    total_qs = 0
    for r_name, expected_count in role_q_counts.items():
        skills = CAREER_ROLES[r_name]["skills"]
        q_dict = QUESTIONS_DATA[r_name]
        role_total = 0
        for sk in skills:
            qs = q_dict.get(sk, [])
            assert len(qs) == 5, f"Skill '{sk}' in '{r_name}' does not have 5 questions! Found {len(qs)}"
            role_total += len(qs)
        assert role_total == expected_count, f"Role {r_name} expected {expected_count} Qs, got {role_total}"
        total_qs += role_total
    
    print(f"[OK] Test 2 Passed: Question count verified across all roles (Total Questions = {total_qs}).")

    answers = {}
    da_questions = QUESTIONS_DATA["Data Analyst"]
    
    for i in range(4):
        answers[f"Data Analyst_Python_{i}"] = da_questions["Python"][i]["answer"]
    answers["Data Analyst_Python_4"] = "WRONG_ANSWER"

    for i in range(5):
        answers[f"Data Analyst_SQL_{i}"] = da_questions["SQL"][i]["answer"]

    for i in range(3):
        answers[f"Data Analyst_Excel_{i}"] = da_questions["Excel"][i]["answer"]
    for i in range(3, 5):
        answers[f"Data Analyst_Excel_{i}"] = "WRONG_ANSWER"

    analytics = calculate_assessment_results("Data Analyst", answers)
    
    assert analytics["readiness_pct"] > 0, "Readiness percentage should be > 0"
    assert analytics["readiness_status"] in ["Excellent", "Good", "Average", "Needs Improvement", "Need Improvement"], "Invalid Readiness Category!"
    print(f"[OK] Test 3 Passed: Analytics readiness score calculated: {analytics['readiness_pct']}% ({analytics['readiness_status']})")

    report = generate_text_report("Hema Harini", "hema@gmail.com", "Data Analyst", analytics)
    assert "STUDENT SKILL GAP ANALYTICS REPORT" in report
    assert "Hema Harini" in report
    assert "Placement Readiness" in report
    print("[OK] Test 4 Passed: Report generation text rendered successfully.")

    print("\nALL TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
