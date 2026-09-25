import sys
sys.path.insert(0, '.')

from data.career_roles import CAREER_ROLES
from data.recommendations import YOUTUBE_LEARNING_LINKS, get_youtube_link

expected = {
    "Data Analyst": [
        ("Python", "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_"),
        ("SQL", "https://youtu.be/-6KHvE78Fv0?si=uqP0vgVVqJugMHt3"),
        ("Excel", "https://youtu.be/ZmBjibf8dyQ?si=HgrgMueuLgydW6CM"),
        ("Power BI", "https://youtu.be/GUzNVy4Elyo?si=NkNp9Qd8rIpe2ZRn"),
        ("Statistics", "https://youtu.be/_DrtU0LTOtU?si=t2zSkl-mjH828T5i"),
        ("Tableau", "https://youtu.be/K3pXnbniUcM?si=Y-Nj-jzOFimtp_ju")
    ],
    "Python Developer": [
        ("Python", "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_"),
        ("DSA using Python", "https://youtu.be/cKeKp17afZw?si=9pXdWW-40w13RfLb"),
        ("OOPs using Python", "https://youtu.be/Ej_02ICOIgs?si=Op3khY8gL5IBczqK"),
        ("SQL", "https://youtu.be/-6KHvE78Fv0?si=uqP0vgVVqJugMHt3"),
        ("Flask", "https://youtu.be/mvRPa9-5Zsc?si=GlsflChsLSGsVuvH"),
        ("Django", "https://youtu.be/gyAtd6Z2QmQ?si=5uwKpHdU_PFGzGp1"),
        ("REST API", "https://youtu.be/41bRmKMb464?si=m_dE8vQpl39w8jmc")
    ],
    "Full Stack Developer": [
        ("HTML", "https://youtu.be/8oONqsEKf6k?si=OuikFihHfpiN0Ry7"),
        ("CSS", "https://youtu.be/lgKbG9pKmx8?si=eq7HHCBcipEyBrUT"),
        ("JavaScript", "https://youtu.be/ynvnxx7rWQ4?si=wKhqNp_9d7vvBIBM"),
        ("React.js", "https://youtu.be/8pWdE6ozjf8?si=u79dK7Z_KPt0p536"),
        ("Python", "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_"),
        ("SQL", "https://youtu.be/-6KHvE78Fv0?si=uqP0vgVVqJugMHt3"),
        ("REST API", "https://youtu.be/41bRmKMb464?si=m_dE8vQpl39w8jmc"),
        ("Django", "https://youtu.be/gyAtd6Z2QmQ?si=5uwKpHdU_PFGzGp1")
    ],
    "AI/ML Engineer": [
        ("Python", "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_"),
        ("C++", "https://youtu.be/VnaKu8_H3jU?si=XMNukiFLuu8_z5gm"),
        ("C", "https://youtu.be/fmSnLiAv-zc?si=r7PtYpQdWItHWJce"),
        ("Java", "https://youtu.be/IT2durkDCXM?si=jNnysQdG2mOkmsT6"),
        ("Machine Learning", "https://youtu.be/aiCIWGSCCKo?si=GQJo6tU5HJH09Kxv"),
        ("Deep Learning", "https://youtu.be/8t_AJicjR-w?si=7-4H3Zm9-79PMC2a"),
        ("Statistics", "https://youtu.be/_DrtU0LTOtU?si=t2zSkl-mjH828T5i"),
        ("Linear Algebra", "https://youtu.be/LzLswBOf_vM?si=1FwWCYULZoYtg4h5"),
        ("Big Data", "https://youtu.be/TVNVQP7L9IE?si=nDcz8Jh_fWz4mu2p")
    ],
    "Cyber Security Analyst": [
        ("Computer Network", "https://youtu.be/yiIpBNBl4bc?si=EhiNcaIjs-FW6XE7"),
        ("OS", "https://youtu.be/S-qPQiD0vqU?si=KlsqEseXoJpHgcCp"),
        ("Ethical Hacking", "https://youtu.be/vh3WW3d0yxg?si=YbOJi55SHIfiE6YZ"),
        ("Vulnerability Assessment", "https://youtu.be/iLdsCnpMnTg?si=G12c5Tzhbiwu39_n"),
        ("Cryptography", "https://youtu.be/j_8PLI_wCVU?si=8y5H3gHeTvReuCNL"),
        ("Database Management", "https://youtu.be/mDFXzRBpJTI?si=TB57G0QHSg2U8Kc3"),
        ("C", "https://youtu.be/fmSnLiAv-zc?si=r7PtYpQdWItHWJce"),
        ("C++", "https://youtu.be/VnaKu8_H3jU?si=XMNukiFLuu8_z5gm"),
        ("Python", "https://youtu.be/m67-bOpOoPU?si=TrC5ps6H6prwTHa_"),
        ("Java", "https://youtu.be/IT2durkDCXM?si=jNnysQdG2mOkmsT6")
    ],
    "UI/UX Designer": [
        ("Figma", "https://youtu.be/NPhm4ObcWhE?si=OW1Bb-QdxI5lssRX"),
        ("Wireframing", "https://youtu.be/_vLXDrNUdJ0?si=K26gIm6lXmRfCljX"),
        ("Prototyping", "https://youtu.be/LlDOKy0DMWQ?si=tDSbdKO8-krO514G"),
        ("Color Theory", "https://youtu.be/xHI5z0XbeMY?si=L5ABHZ1QVIXXVb4j")
    ],
    "Cloud Computing": [
        ("Cloud Security", "https://www.youtube.com/live/Ijkvx1u0w6o?si=F6yMsyVTewMBtx7u"),
        ("AWS", "https://youtu.be/eZeNIakuqbc?si=4Tx0knd9oE3elYEH"),
        ("DevOps", "https://youtu.be/aXJ2tJT8xpY?si=jPqNeVrxanUFUC6W"),
        ("Networking", "https://youtu.be/kdYPGbEm4uA?si=RYfqhJia8DgFulsc"),
        ("Linux", "https://youtu.be/WmuE-MHRGbQ?si=FE_s3Xdvpt7vVPAC")
    ]
}

all_ok = True
for role, items in expected.items():
    print(f"\nChecking Role: {role}")
    for skill, expected_url in items:
        actual_url = get_youtube_link(role, skill)
        if actual_url != expected_url:
            print(f"[FAIL] MISMATCH for {skill}: Expected {expected_url}, Got {actual_url}")
            all_ok = False
        else:
            print(f"  [OK] {skill}: {actual_url}")

print("\nVerifying Database Management isolation:")
for role in CAREER_ROLES.keys():
    link = get_youtube_link(role, "Database Management")
    if role in ["Cyber Security Analyst", "Cybersecurity Analyst"]:
        assert link is not None, f"Expected link for {role}"
        print(f"  [OK] {role} has Database Management link: {link}")
    else:
        assert link is None, f"Database Management link found under {role}!"
        print(f"  [OK] {role} does NOT have Database Management link.")

if all_ok:
    print("\nALL TESTS PASSED SUCCESSFULLY!")
