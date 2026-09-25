def generate_text_report(student_name, email, role_name, analytics_data, reassessment_data=None):
    """
    Generates a structured text report containing initial assessment information,
    and optionally includes latest reassessment results.
    """
    results = analytics_data["results"]
    readiness_pct = analytics_data["readiness_pct"]
    readiness_status = analytics_data["readiness_status"]
    student_score = analytics_data["student_total_score"]
    required_score = analytics_data["required_total_score"]

    from data.recommendations import get_recommendation

    lines = []
    lines.append("=========================================================================")
    lines.append("                STUDENT SKILL GAP ANALYTICS REPORT                      ")
    lines.append("=========================================================================")
    lines.append("")
    lines.append(f"Student Name            : {student_name}")
    lines.append(f"Email ID                : {email}")
    lines.append(f"Selected Career Role    : {role_name}")
    lines.append(f"Initial Student Score   : {student_score}")
    lines.append(f"Recruiter Level Score   : {required_score}")
    lines.append(f"Initial Readiness       : {readiness_pct}%")
    lines.append(f"Initial Status          : {readiness_status}")
    lines.append("")
    lines.append("-------------------------------------------------------------------------")
    lines.append(" INITIAL SKILL GAP BREAKDOWN & LEVEL ANALYSIS")
    lines.append("-------------------------------------------------------------------------")
    lines.append(f"{'Skill Name':<28} | {'Student Level':<16} | {'Industry Level':<16} | {'Skill Gap'}")
    lines.append("-" * 75)

    for item in results:
        lines.append(f"{item['skill']:<28} | {item['student_level_str']:<16} | {item['industry_level_str']:<16} | {item['gap_str']}")

    lines.append("")
    lines.append("-------------------------------------------------------------------------")
    lines.append(" LEARNING RECOMMENDATIONS")
    lines.append("-------------------------------------------------------------------------")

    for item in results:
        rec = get_recommendation(item['skill'], item['student_level_num'], item['industry_level_num'])
        lines.append(f"• {item['skill']} (Student: {item['student_level_str']} | Required: {item['industry_level_str']}):")
        lines.append(f"  {rec}")
        lines.append("")

    if reassessment_data:
        re_results = reassessment_data.get("results", [])
        lines.append("-------------------------------------------------------------------------")
        lines.append(" LATEST REASSESSMENT & BEFORE VS AFTER COMPARISON")
        lines.append("-------------------------------------------------------------------------")
        lines.append(f"Updated Student Score   : {reassessment_data.get('updated_student_total_score')}")
        lines.append(f"Updated Readiness       : {reassessment_data.get('updated_readiness_pct')}%")
        lines.append(f"Updated Status          : {reassessment_data.get('updated_readiness_status')}")
        lines.append(f"Net Readiness Growth    : +{reassessment_data.get('readiness_improvement')}%")
        lines.append("")
        lines.append(f"{'Skill Name':<22} | {'Before':<10} | {'After':<10} | {'Industry':<10} | {'Gap Before':<12} | {'Gap After':<12} | {'Improvement'}")
        lines.append("-" * 95)
        for r_item in re_results:
            lines.append(
                f"{r_item['skill']:<22} | "
                f"{r_item['initial_score']:<10} | "
                f"{r_item['reassessment_score']:<10} | "
                f"{r_item['industry_expected_score']:<10} | "
                f"{r_item['gap_before_str']:<12} | "
                f"{r_item['gap_after_str']:<12} | "
                f"{r_item['improvement_str']}"
            )
        lines.append("")

    lines.append("=========================================================================")
    lines.append("             End of Student Skill Gap Analytics Report                   ")
    lines.append("=========================================================================")

    return "\n".join(lines)


def generate_final_report(student_name, email, role_name, initial_analytics, reassessment_analytics, weak_skills):
    """
    Generates the complete Final Analytics Report summarizing student details,
    initial assessment results, weak skills identified, learning recommendations,
    reassessment results, before vs after comparisons, and updated readiness score/status.
    """
    from data.recommendations import get_recommendation

    lines = []
    lines.append("=========================================================================================")
    lines.append("                         FINAL COMPREHENSIVE ANALYTICS REPORT                            ")
    lines.append("=========================================================================================")
    lines.append("")
    lines.append("1. STUDENT & CAREER ROLE DETAILS")
    lines.append("-----------------------------------------------------------------------------------------")
    lines.append(f"• Student Name          : {student_name}")
    lines.append(f"• Email ID              : {email}")
    lines.append(f"• Selected Career Role  : {role_name}")
    lines.append("")
    lines.append("2. INITIAL ASSESSMENT RESULTS")
    lines.append("-----------------------------------------------------------------------------------------")
    lines.append(f"• Initial Total Score   : {initial_analytics['student_total_score']} / {initial_analytics['required_total_score']}")
    lines.append(f"• Initial Readiness     : {initial_analytics['readiness_pct']}%")
    lines.append(f"• Initial Readiness Status: {initial_analytics['readiness_status']}")
    lines.append("")
    lines.append("Initial Skill Scores:")
    lines.append(f"  {'Skill Name':<28} | {'Student Level':<16} | {'Industry Level':<16} | {'Status'}")
    lines.append("  " + "-" * 75)
    for item in initial_analytics["results"]:
        lines.append(f"  {item['skill']:<28} | {item['student_level_str']:<16} | {item['industry_level_str']:<16} | {item['status']}")
    lines.append("")
    lines.append("3. WEAK SKILLS IDENTIFIED")
    lines.append("-----------------------------------------------------------------------------------------")
    if weak_skills:
        for ws in weak_skills:
            lines.append(f"  ⚠️  {ws}")
    else:
        lines.append("  None - All skills met or exceeded initial industry targets.")
    lines.append("")
    lines.append("4. LEARNING RECOMMENDATIONS")
    lines.append("-----------------------------------------------------------------------------------------")
    for item in initial_analytics["results"]:
        rec = get_recommendation(item['skill'], item['student_level_num'], item['industry_level_num'])
        lines.append(f"• {item['skill']}: {rec}")
    lines.append("")

    lines.append("5. REASSESSMENT & BEFORE VS AFTER COMPARISON")
    lines.append("-----------------------------------------------------------------------------------------")
    if reassessment_analytics:
        lines.append(f"• Reassessment Status   : COMPLETED")
        lines.append(f"• Questions Answered    : {reassessment_analytics.get('total_reassessment_qs', 0)} NEW non-repeating questions")
        lines.append(f"• Correct Reassessment  : {reassessment_analytics.get('total_reassessment_correct', 0)}")
        lines.append("")
        lines.append("BEFORE vs AFTER SKILL COMPARISON TABLE:")
        lines.append(f"{'Skill Name':<20} | {'Before':<8} | {'After':<8} | {'Expected':<8} | {'Gap Before':<12} | {'Gap After':<12} | {'Improvement'}")
        lines.append("-" * 90)
        for r in reassessment_analytics.get("results", []):
            lines.append(
                f"{r['skill']:<20} | "
                f"{r['initial_score']:<8} | "
                f"{r['reassessment_score']:<8} | "
                f"{r['industry_expected_score']:<8} | "
                f"{r['gap_before_str']:<12} | "
                f"{r['gap_after_str']:<12} | "
                f"{r['improvement_str']}"
            )
        lines.append("")
        lines.append("6. UPDATED READINESS SCORE & STATUS")
        lines.append("-----------------------------------------------------------------------------------------")
        lines.append(f"• Initial Readiness Score : {initial_analytics['readiness_pct']}% ({initial_analytics['readiness_status']})")
        lines.append(f"• Updated Readiness Score : {reassessment_analytics['updated_readiness_pct']}% ({reassessment_analytics['updated_readiness_status']})")
        lines.append(f"• Net Readiness Improvement: +{reassessment_analytics['readiness_improvement']}%")
        lines.append("")
        if reassessment_analytics['updated_readiness_pct'] >= 91.0:
            final_rec = "Excellent! The student has successfully closed critical skill gaps and meets industry standards for job readiness."
        elif reassessment_analytics['updated_readiness_pct'] >= 75.0:
            final_rec = "Good progress! The student has made significant gains. Continued practice on remaining weak skills will finalize readiness."
        else:
            final_rec = "Needs further improvement. Re-study recommended learning modules and attempt additional practice sessions."
        lines.append(f"• Final Recommendation   : {final_rec}")
    else:
        lines.append("• Reassessment Status   : PENDING (Student has not taken the reassessment yet)")
        lines.append("  Attempt the reassessment to generate before vs after performance comparisons.")

    lines.append("")
    lines.append("=========================================================================================")
    lines.append("                      END OF FINAL COMPREHENSIVE ANALYTICS REPORT                       ")
    lines.append("=========================================================================================")

    return "\n".join(lines)

