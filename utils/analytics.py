from data.career_roles import CAREER_ROLES, LEVEL_MAP
from data.questions_data import QUESTIONS_DATA

def calculate_assessment_results(role_name, answers):
    """
    Calculates detailed skill level, industry level comparison, gap analysis,
    and placement readiness percentage.
    """
    role_info = CAREER_ROLES.get(role_name, {})
    skills = role_info.get("skills", [])
    industry_levels = role_info.get("industry_levels", {})
    questions = QUESTIONS_DATA.get(role_name, {})

    results = []
    total_student_level_score = 0
    total_required_level_score = 0
    total_questions_answered = 0
    total_correct = 0
    total_questions_count = len(skills) * 5

    for skill in skills:
        skill_qs = questions.get(skill, [])
        correct_count = 0
        for i, q in enumerate(skill_qs):
            key = f"{role_name}_{skill}_{i}"
            user_ans = answers.get(key)
            if user_ans is not None:
                total_questions_answered += 1
            if user_ans == q["answer"]:
                correct_count += 1
                total_correct += 1

        # Level calculation (1 to 5)
        if correct_count <= 1:
            student_level_num = 1
        elif correct_count == 2:
            student_level_num = 2
        elif correct_count == 3:
            student_level_num = 3
        elif correct_count == 4:
            student_level_num = 4
        else:
            student_level_num = 5

        student_level_str = LEVEL_MAP[student_level_num]
        industry_level_num = industry_levels.get(skill, 3)
        industry_level_str = LEVEL_MAP[industry_level_num]

        gap_val = industry_level_num - student_level_num
        if gap_val > 0:
            gap_str = f"{gap_val} Level{'s' if gap_val > 1 else ''}"
            status = "Below Industry Requirement"
        elif gap_val == 0:
            gap_str = "No Gap"
            status = "Meets Industry Requirement"
        else:
            gap_str = "Exceeds"
            status = "Exceeds Industry Requirement"

        total_student_level_score += student_level_num
        total_required_level_score += industry_level_num

        results.append({
            "skill": skill,
            "correct_count": correct_count,
            "total_questions": len(skill_qs),
            "student_level_num": student_level_num,
            "student_level_str": student_level_str,
            "industry_level_num": industry_level_num,
            "industry_level_str": industry_level_str,
            "gap_num": gap_val if gap_val > 0 else 0,
            "gap_str": gap_str,
            "status": status
        })

    # Placement Readiness Percentage
    if total_required_level_score > 0:
        readiness_pct = round((total_student_level_score / total_required_level_score) * 100, 1)
    else:
        readiness_pct = 0.0

    # Cap at 100%
    readiness_pct = min(readiness_pct, 100.0)

    # Readiness Category rule:
    # 92 to 100 percentage = Excellent
    # 75 to 90 percentage = Good (75 <= pct < 92)
    # 50 to 74 percentage = Average
    # Below 50 percentage = Need Improvement
    if readiness_pct >= 91.0:
        readiness_status = "Excellent"
        status_color = "#16a34a" # Green
    elif readiness_pct >= 75.0:
        readiness_status = "Good"
        status_color = "#2563eb" # Blue
    elif readiness_pct >= 50.0:
        readiness_status = "Average"
        status_color = "#d97706" # Orange
    else:
        readiness_status = "Needs Improvement"
        status_color = "#dc2626" # Red

    return {
        "results": results,
        "student_total_score": total_student_level_score,
        "required_total_score": total_required_level_score,
        "total_correct": total_correct,
        "total_questions_count": total_questions_count,
        "total_questions_answered": total_questions_answered,
        "readiness_pct": readiness_pct,
        "readiness_status": readiness_status,
        "status_color": status_color
    }


def get_weak_skills(initial_analytics):
    """
    Identifies weak skills from initial assessment.
    Weak skills are skills where student level is below industry required level (gap_num > 0).
    """
    weak_skills = []
    if not initial_analytics or "results" not in initial_analytics:
        return weak_skills

    for item in initial_analytics["results"]:
        if item.get("gap_num", 0) > 0 or item.get("student_level_num", 0) < item.get("industry_level_num", 0):
            weak_skills.append(item["skill"])

    return weak_skills


def calculate_reassessment_results(role_name, initial_analytics, reassessment_answers, reassessment_qs_map):
    """
    Calculates reassessment results, Before vs After skill comparison,
    and updated placement readiness percentage.
    """
    role_info = CAREER_ROLES.get(role_name, {})
    skills = role_info.get("skills", [])
    industry_levels = role_info.get("industry_levels", {})

    initial_results_by_skill = {item["skill"]: item for item in initial_analytics.get("results", [])}

    comparison_results = []
    updated_student_total_score = 0
    total_required_level_score = 0
    total_reassessment_correct = 0
    total_reassessment_qs = 0
    total_improvement_levels = 0

    for skill in skills:
        init_item = initial_results_by_skill.get(skill, {})
        init_level_num = init_item.get("student_level_num", 1)
        init_correct = init_item.get("correct_count", 0)
        ind_level_num = industry_levels.get(skill, 3)

        # Check if skill was reassessed
        if skill in reassessment_qs_map and len(reassessment_qs_map[skill]) > 0:
            skill_qs = reassessment_qs_map[skill]
            correct_count = 0
            for i, q in enumerate(skill_qs):
                q_id = q.get("id", f"{skill}_{i}")
                ans_key = f"re_{role_name}_{skill}_{q_id}"
                user_ans = reassessment_answers.get(ans_key)
                if user_ans == q["answer"]:
                    correct_count += 1
                    total_reassessment_correct += 1

            total_reassessment_qs += len(skill_qs)

            # Reassessment Level calculation (1 to 5) based on correct count out of 5
            if correct_count <= 1:
                new_level_num = 1
            elif correct_count == 2:
                new_level_num = 2
            elif correct_count == 3:
                new_level_num = 3
            elif correct_count == 4:
                new_level_num = 4
            else:
                new_level_num = 5

            is_reassessed = True
        else:
            # Preserved from initial assessment
            correct_count = init_correct
            new_level_num = init_level_num
            is_reassessed = False

        init_score_pct = round((init_level_num / 5.0) * 100)
        new_score_pct = round((new_level_num / 5.0) * 100)
        ind_score_pct = round((ind_level_num / 5.0) * 100)

        gap_before_num = max(0, ind_level_num - init_level_num)
        gap_before_pct = max(0, ind_score_pct - init_score_pct)

        gap_after_num = max(0, ind_level_num - new_level_num)
        gap_after_pct = max(0, ind_score_pct - new_score_pct)

        level_improvement = new_level_num - init_level_num
        pct_improvement = new_score_pct - init_score_pct
        total_improvement_levels += level_improvement

        updated_student_total_score += new_level_num
        total_required_level_score += ind_level_num

        if gap_after_num > 0:
            gap_after_str = f"{gap_after_num} Level{'s' if gap_after_num > 1 else ''}"
            updated_status = "Below Industry Requirement"
        elif gap_after_num == 0:
            gap_after_str = "No Gap"
            updated_status = "Meets Industry Requirement"
        else:
            gap_after_str = "Exceeds"
            updated_status = "Exceeds Industry Requirement"

        comparison_results.append({
            "skill": skill,
            "is_reassessed": is_reassessed,

            # Levels
            "initial_level_num": init_level_num,
            "initial_level_str": LEVEL_MAP[init_level_num],
            "reassessment_level_num": new_level_num,
            "reassessment_level_str": LEVEL_MAP[new_level_num],
            "industry_level_num": ind_level_num,
            "industry_level_str": LEVEL_MAP[ind_level_num],

            # Scores (percentage equivalent out of 100)
            "initial_score": init_score_pct,
            "reassessment_score": new_score_pct,
            "industry_expected_score": ind_score_pct,

            # Gaps
            "gap_before_num": gap_before_num,
            "gap_before_str": f"{gap_before_num} Level{'s' if gap_before_num > 1 else ''}" if gap_before_num > 0 else "No Gap",
            "gap_before_pct": gap_before_pct,

            "gap_after_num": gap_after_num,
            "gap_after_str": gap_after_str,
            "gap_after_pct": gap_after_pct,

            # Improvement
            "level_improvement": level_improvement,
            "pct_improvement": pct_improvement,
            "improvement_str": f"+{pct_improvement}" if pct_improvement >= 0 else f"{pct_improvement}",
            "updated_status": updated_status
        })

    # Updated Placement Readiness Percentage
    if total_required_level_score > 0:
        updated_readiness_pct = round((updated_student_total_score / total_required_level_score) * 100, 1)
    else:
        updated_readiness_pct = 0.0

    updated_readiness_pct = min(updated_readiness_pct, 100.0)

    if updated_readiness_pct >= 91.0:
        updated_readiness_status = "Excellent"
        updated_status_color = "#16a34a" # Green
    elif updated_readiness_pct >= 75.0:
        updated_readiness_status = "Good"
        updated_status_color = "#2563eb" # Blue
    elif updated_readiness_pct >= 50.0:
        updated_readiness_status = "Average"
        updated_status_color = "#d97706" # Orange
    else:
        updated_readiness_status = "Needs Improvement"
        updated_status_color = "#dc2626" # Red

    initial_readiness_pct = initial_analytics.get("readiness_pct", 0.0)
    readiness_improvement = round(updated_readiness_pct - initial_readiness_pct, 1)

    return {
        "results": comparison_results,
        "initial_readiness_pct": initial_readiness_pct,
        "updated_readiness_pct": updated_readiness_pct,
        "readiness_improvement": readiness_improvement,
        "updated_readiness_status": updated_readiness_status,
        "updated_status_color": updated_status_color,
        "updated_student_total_score": updated_student_total_score,
        "required_total_score": total_required_level_score,
        "total_reassessment_correct": total_reassessment_correct,
        "total_reassessment_qs": total_reassessment_qs,
        "total_improvement_levels": total_improvement_levels
    }

