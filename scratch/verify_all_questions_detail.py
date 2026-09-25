import sys
import os

sys.path.append(os.path.abspath("."))

from data.career_roles import CAREER_ROLES
from data.questions_data import QUESTIONS_DATA

def verify_questions():
    print("=== RUNNING DETAILED QUESTION BANK AUDIT ===")

    expected_levels = ["Basic", "Beginner", "Intermediate", "Advanced", "Expert"]

    total_questions = 0
    total_skills = 0

    for role_name, role_info in CAREER_ROLES.items():
        assert role_name in QUESTIONS_DATA, f"Missing role '{role_name}' in QUESTIONS_DATA!"
        role_qs = QUESTIONS_DATA[role_name]
        skills_list = role_info["skills"]

        assert len(role_qs) == len(skills_list), f"Role '{role_name}' skill count mismatch: expected {len(skills_list)}, got {len(role_qs)}"

        for skill_name in skills_list:
            total_skills += 1
            assert skill_name in role_qs, f"Skill '{skill_name}' missing from role '{role_name}' in QUESTIONS_DATA!"
            qs = role_qs[skill_name]
            assert len(qs) == 5, f"Skill '{skill_name}' in role '{role_name}' has {len(qs)} questions instead of 5!"

            q_texts = set()
            for idx, q in enumerate(qs):
                total_questions += 1
                assert "q" in q and q["q"].strip(), f"Empty question text at {role_name}->{skill_name}->Q{idx+1}"
                assert "options" in q and len(q["options"]) >= 4, f"Invalid options at {role_name}->{skill_name}->Q{idx+1}"
                assert "answer" in q and q["answer"].strip(), f"Empty answer at {role_name}->{skill_name}->Q{idx+1}"
                assert q["answer"] in q["options"], f"Answer '{q['answer']}' not found in options {q['options']} at {role_name}->{skill_name}->Q{idx+1}"
                assert "difficulty" in q, f"Missing difficulty key at {role_name}->{skill_name}->Q{idx+1}"
                expected_diff = expected_levels[idx]
                assert q["difficulty"] == expected_diff, f"Expected difficulty '{expected_diff}' at {role_name}->{skill_name}->Q{idx+1}, got '{q['difficulty']}'"

                q_texts.add(q["q"])

            assert len(q_texts) == 5, f"Duplicate questions detected in {role_name}->{skill_name}!"

        print(f"[OK] {role_name}: Verified {len(skills_list)} skills, {len(skills_list) * 5} questions.")

    print(f"\nAUDIT SUCCESS: {total_skills} skills, {total_questions} total questions perfectly validated across all 7 Career Roles!")

if __name__ == "__main__":
    verify_questions()
