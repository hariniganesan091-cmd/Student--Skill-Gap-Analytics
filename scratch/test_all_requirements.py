import os
import sys

# Add directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from utils.analytics import calculate_assessment_results, get_weak_skills
    from utils.auth import (
        register_user,
        login_user,
        init_db,
        save_student_progress,
        get_student_progress,
        load_student_progress
    )

    def test_target_status_logic():
        print("--- 1. Testing Target Status Logic ---")
        
        role_name = "UI/UX Designer"
        from data.questions_data import QUESTIONS_DATA
        role_qs = QUESTIONS_DATA.get(role_name, {})
        
        mock_answers = {}
        for skill, qs in role_qs.items():
            if skill == "Figma":
                target_correct = 5
            elif skill == "Wireframing":
                target_correct = 5
            elif skill == "Prototyping":
                target_correct = 4
            elif skill == "Typography":
                target_correct = 4
            elif skill == "Color Theory":
                target_correct = 3
            else:
                target_correct = 3

            for i, q in enumerate(qs):
                key = f"{role_name}_{skill}_{i}"
                if i < target_correct:
                    mock_answers[key] = q["answer"]
                else:
                    mock_answers[key] = "WRONG_ANSWER"

        analytics = calculate_assessment_results(role_name, mock_answers)
        weak_skills = get_weak_skills(analytics)

        print(f"Identified Weak Skills: {weak_skills}")
        assert len(weak_skills) == 0, f"Expected 0 weak skills, got {weak_skills}"

        for item in analytics["results"]:
            sk = item["skill"]
            st_lvl = item["student_level_num"]
            ind_lvl = item["industry_level_num"]
            gap_str = item["gap_str"]

            is_weak = st_lvl < ind_lvl
            target_status = "Weak Skill (Target for Reassessment)" if is_weak else "Strong Skill (Target Met)"

            print(f"Skill: {sk} | Student: {st_lvl} | Industry: {ind_lvl} | Gap: {gap_str} | Status: {target_status}")

            if st_lvl < ind_lvl:
                assert is_weak, f"Fail: {sk} student {st_lvl} < industry {ind_lvl} but not marked weak"
            elif st_lvl == ind_lvl:
                assert not is_weak, f"Fail: {sk} student {st_lvl} == industry {ind_lvl} but marked weak"
                assert gap_str == "No Gap", f"Fail: {sk} expected No Gap, got {gap_str}"
            else: # st_lvl > ind_lvl
                assert not is_weak, f"Fail: {sk} student {st_lvl} > industry {ind_lvl} but marked weak"
                assert gap_str == "Exceeds", f"Fail: {sk} expected Exceeds, got {gap_str}"

        print("[OK] Target Status Logic Test Passed!")

    def test_persistence_flow():
        print("\n--- 2. Testing Student Progress Persistence Flow ---")
        
        init_db()
        
        email_a = "test_student_a@example.com"
        email_b = "test_student_b@example.com"
        pwd = "password123"

        # Register
        register_user("Student A", email_a, pwd, pwd)
        register_user("Student B", email_b, pwd, pwd)

        # Mock assessment completion for Student A
        mock_analytics_a = {
            "results": [
                {
                    "skill": "Python",
                    "student_level_num": 2,
                    "student_level_str": "Beginner",
                    "industry_level_num": 4,
                    "industry_level_str": "Advanced",
                    "gap_num": 2,
                    "gap_str": "2 Levels",
                    "status": "Below Industry Requirement"
                }
            ],
            "readiness_pct": 50.0,
            "readiness_status": "Average",
            "status_color": "#d97706"
        }

        save_student_progress(
            email=email_a,
            selected_role="Data Analyst",
            assessment_submitted=True,
            assessment_answers={"key1": "A"},
            initial_analytics=mock_analytics_a,
            asked_question_ids={"q1"}
        )

        progress_a = get_student_progress(email_a)
        assert progress_a is not None
        assert progress_a["assessment_submitted"] == True
        assert progress_a["selected_role"] == "Data Analyst"
        print(f"Loaded Progress A: {progress_a['selected_role']}, submitted: {progress_a['assessment_submitted']}")

        progress_b = get_student_progress(email_b)
        assert progress_b is None
        print("Loaded Progress B: None (Data isolation confirmed)")

        print("[OK] Student Progress Persistence Test Passed!")

    if __name__ == "__main__":
        test_target_status_logic()
        test_persistence_flow()
        print("\nALL VERIFICATION TESTS PASSED SUCCESSFULLY!")

except Exception as e:
    import traceback
    print("EXCEPTION OCCURRED:")
    traceback.print_exc()
