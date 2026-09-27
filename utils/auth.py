import sqlite3
import os
import json
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
from supabase import create_client
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "users.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                full_name TEXT NOT NULL,
                email TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        conn.commit()

        # Seed default registered demo account if hema@gmail.com does not exist
        cursor.execute("SELECT email FROM users WHERE LOWER(email) = ?", ("hema@gmail.com",))
        if not cursor.fetchone():
            cursor.execute("""
                INSERT INTO users (full_name, email, password)
                VALUES (?, ?, ?)
            """, ("Hema Harini", "hema@gmail.com", "password123"))
            conn.commit()
    finally:
        conn.close()

    init_progress_db()

def init_progress_db():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_progress (
                email TEXT PRIMARY KEY,
                selected_role TEXT,
                assessment_submitted INTEGER DEFAULT 0,
                assessment_answers TEXT,
                initial_analytics TEXT,
                assessment_date TEXT,
                reassessment_submitted INTEGER DEFAULT 0,
                reassessment_answers TEXT,
                reassessment_analytics TEXT,
                reassessment_date TEXT,
                reassessment_questions_map TEXT,
                asked_question_ids TEXT,
                assessment_history TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(email) REFERENCES users(email)
            )
        """)
        conn.commit()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS student_role_progress (
                email TEXT NOT NULL,
                selected_role TEXT NOT NULL,
                assessment_submitted INTEGER DEFAULT 0,
                assessment_answers TEXT,
                initial_analytics TEXT,
                assessment_date TEXT,
                reassessment_submitted INTEGER DEFAULT 0,
                reassessment_answers TEXT,
                reassessment_analytics TEXT,
                reassessment_date TEXT,
                reassessment_questions_map TEXT,
                asked_question_ids TEXT,
                assessment_history TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY(email, selected_role),
                FOREIGN KEY(email) REFERENCES users(email)
            )
        """)
        conn.commit()

        # Migrate existing single-role records into student_role_progress if missing
        cursor.execute("""
            INSERT OR IGNORE INTO student_role_progress (
                email, selected_role, assessment_submitted, assessment_answers,
                initial_analytics, assessment_date, reassessment_submitted, reassessment_answers,
                reassessment_analytics, reassessment_date, reassessment_questions_map,
                asked_question_ids, assessment_history
            )
            SELECT 
                email, COALESCE(selected_role, 'Data Analyst'), assessment_submitted, assessment_answers,
                initial_analytics, assessment_date, reassessment_submitted, reassessment_answers,
                reassessment_analytics, reassessment_date, reassessment_questions_map,
                asked_question_ids, assessment_history
            FROM student_progress
        """)
        conn.commit()

        # Safely migrate existing tables if new columns are missing
        cursor.execute("PRAGMA table_info(student_progress)")
        columns = [col[1] for col in cursor.fetchall()]

        if "assessment_date" not in columns:
            cursor.execute("ALTER TABLE student_progress ADD COLUMN assessment_date TEXT")
            conn.commit()

        if "reassessment_date" not in columns:
            cursor.execute("ALTER TABLE student_progress ADD COLUMN reassessment_date TEXT")
            conn.commit()

        if "assessment_history" not in columns:
            cursor.execute("ALTER TABLE student_progress ADD COLUMN assessment_history TEXT")
            conn.commit()

    finally:
        conn.close()

def save_student_progress(email, selected_role=None, assessment_submitted=None,
                          assessment_answers=None, initial_analytics=None,
                          assessment_date=None, reassessment_submitted=None,
                          reassessment_answers=None, reassessment_analytics=None,
                          reassessment_date=None, reassessment_questions_map=None,
                          asked_question_ids=None, assessment_history=None):
    if not email:
        return
    email = email.strip().lower()
    init_progress_db()

    role = selected_role if selected_role is not None else "Data Analyst"
    existing = get_student_progress(email, role=role) or {}

    ass_sub = int(assessment_submitted) if assessment_submitted is not None else (1 if existing.get("assessment_submitted") else 0)
    ass_ans = json.dumps(assessment_answers) if assessment_answers is not None else existing.get("assessment_answers_json", "{}")
    init_ana = json.dumps(initial_analytics) if initial_analytics is not None else existing.get("initial_analytics_json", "null")
    re_sub = int(reassessment_submitted) if reassessment_submitted is not None else (1 if existing.get("reassessment_submitted") else 0)
    re_ans = json.dumps(reassessment_answers) if reassessment_answers is not None else existing.get("reassessment_answers_json", "{}")
    re_ana = json.dumps(reassessment_analytics) if reassessment_analytics is not None else existing.get("reassessment_analytics_json", "null")
    re_qs = json.dumps(reassessment_questions_map) if reassessment_questions_map is not None else existing.get("reassessment_questions_map_json", "{}")

    # Handle completion dates
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if assessment_date is not None:
        ass_date = assessment_date
    elif ass_sub and existing.get("assessment_date"):
        ass_date = existing.get("assessment_date")
    elif ass_sub:
        ass_date = now_str
    else:
        ass_date = existing.get("assessment_date", "")

    if reassessment_date is not None:
        re_date = reassessment_date
    elif re_sub and existing.get("reassessment_date"):
        re_date = existing.get("reassessment_date")
    elif re_sub:
        re_date = now_str
    else:
        re_date = existing.get("reassessment_date", "")

    if asked_question_ids is not None:
        asked_ids = json.dumps(list(asked_question_ids))
    else:
        asked_ids = existing.get("asked_question_ids_json", "[]")

    # Build assessment_history JSON list
    if assessment_history is not None:
        ass_hist_json = json.dumps(assessment_history)
    else:
        # Load existing or reconstruct history
        existing_hist_raw = existing.get("assessment_history_json", "[]")
        try:
            hist_list = json.loads(existing_hist_raw)
        except Exception:
            hist_list = []

        if not hist_list:
            if initial_analytics:
                hist_list.append({
                    "type": "Initial Assessment",
                    "date": ass_date or now_str,
                    "role": role,
                    "readiness_pct": initial_analytics.get("readiness_pct", 0.0),
                    "readiness_status": initial_analytics.get("readiness_status", "N/A"),
                    "analytics": initial_analytics
                })
            if reassessment_analytics:
                hist_list.append({
                    "type": "Reassessment",
                    "date": re_date or now_str,
                    "role": role,
                    "readiness_pct": reassessment_analytics.get("updated_readiness_pct", 0.0),
                    "readiness_status": reassessment_analytics.get("updated_readiness_status", "N/A"),
                    "analytics": reassessment_analytics
                })

        ass_hist_json = json.dumps(hist_list)

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        # Save to per-role progress table
        cursor.execute("""
            INSERT INTO student_role_progress (
                email, selected_role, assessment_submitted, assessment_answers,
                initial_analytics, assessment_date, reassessment_submitted, reassessment_answers,
                reassessment_analytics, reassessment_date, reassessment_questions_map,
                asked_question_ids, assessment_history
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(email, selected_role) DO UPDATE SET
                assessment_submitted=excluded.assessment_submitted,
                assessment_answers=excluded.assessment_answers,
                initial_analytics=excluded.initial_analytics,
                assessment_date=excluded.assessment_date,
                reassessment_submitted=excluded.reassessment_submitted,
                reassessment_answers=excluded.reassessment_answers,
                reassessment_analytics=excluded.reassessment_analytics,
                reassessment_date=excluded.reassessment_date,
                reassessment_questions_map=excluded.reassessment_questions_map,
                asked_question_ids=excluded.asked_question_ids,
                assessment_history=excluded.assessment_history,
                updated_at=CURRENT_TIMESTAMP
        """, (email, role, ass_sub, ass_ans, init_ana, ass_date, re_sub, re_ans, re_ana, re_date, re_qs, asked_ids, ass_hist_json))

        # Also update fallback active role table student_progress
        cursor.execute("""
            INSERT INTO student_progress (
                email, selected_role, assessment_submitted, assessment_answers,
                initial_analytics, assessment_date, reassessment_submitted, reassessment_answers,
                reassessment_analytics, reassessment_date, reassessment_questions_map,
                asked_question_ids, assessment_history
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(email) DO UPDATE SET
                selected_role=excluded.selected_role,
                assessment_submitted=excluded.assessment_submitted,
                assessment_answers=excluded.assessment_answers,
                initial_analytics=excluded.initial_analytics,
                assessment_date=excluded.assessment_date,
                reassessment_submitted=excluded.reassessment_submitted,
                reassessment_answers=excluded.reassessment_answers,
                reassessment_analytics=excluded.reassessment_analytics,
                reassessment_date=excluded.reassessment_date,
                reassessment_questions_map=excluded.reassessment_questions_map,
                asked_question_ids=excluded.asked_question_ids,
                assessment_history=excluded.assessment_history,
                updated_at=CURRENT_TIMESTAMP
        """, (email, role, ass_sub, ass_ans, init_ana, ass_date, re_sub, re_ans, re_ana, re_date, re_qs, asked_ids, ass_hist_json))

        conn.commit()
    finally:
        conn.close()

def get_student_progress(email, role=None):
    if not email:
        return None
    email = email.strip().lower()
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='student_role_progress'")
        if not cursor.fetchone():
            return None

        row = None
        if role:
            cursor.execute("SELECT * FROM student_role_progress WHERE LOWER(email) = ? AND selected_role = ?", (email, role))
            row = cursor.fetchone()
            if not row:
                return None
        else:
            cursor.execute("SELECT * FROM student_progress WHERE LOWER(email) = ?", (email,))
            row = cursor.fetchone()

            if not row:
                cursor.execute("SELECT * FROM student_role_progress WHERE LOWER(email) = ? ORDER BY updated_at DESC LIMIT 1", (email,))
                row = cursor.fetchone()

        if not row:
            return None

        r = dict(row)
        return {
            "selected_role": r.get("selected_role") or "Data Analyst",
            "assessment_submitted": bool(r.get("assessment_submitted", 0)),
            "assessment_answers_json": r.get("assessment_answers") or "{}",
            "initial_analytics_json": r.get("initial_analytics") or "null",
            "assessment_date": r.get("assessment_date") or "",
            "reassessment_submitted": bool(r.get("reassessment_submitted", 0)),
            "reassessment_answers_json": r.get("reassessment_answers") or "{}",
            "reassessment_analytics_json": r.get("reassessment_analytics") or "null",
            "reassessment_date": r.get("reassessment_date") or "",
            "reassessment_questions_map_json": r.get("reassessment_questions_map") or "{}",
            "asked_question_ids_json": r.get("asked_question_ids") or "[]",
            "assessment_history_json": r.get("assessment_history") or "[]"
        }
    finally:
        conn.close()

def get_all_student_role_progress(email):
    if not email:
        return []
    email = email.strip().lower()
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='student_role_progress'")
        if not cursor.fetchone():
            return []

        cursor.execute("SELECT * FROM student_role_progress WHERE LOWER(email) = ? ORDER BY updated_at DESC", (email,))
        rows = cursor.fetchall()
        result = []
        for row in rows:
            r = dict(row)
            result.append({
                "selected_role": r.get("selected_role") or "Data Analyst",
                "assessment_submitted": bool(r.get("assessment_submitted", 0)),
                "assessment_answers_json": r.get("assessment_answers") or "{}",
                "initial_analytics_json": r.get("initial_analytics") or "null",
                "assessment_date": r.get("assessment_date") or "",
                "reassessment_submitted": bool(r.get("reassessment_submitted", 0)),
                "reassessment_answers_json": r.get("reassessment_answers") or "{}",
                "reassessment_analytics_json": r.get("reassessment_analytics") or "null",
                "reassessment_date": r.get("reassessment_date") or "",
                "reassessment_questions_map_json": r.get("reassessment_questions_map") or "{}",
                "asked_question_ids_json": r.get("asked_question_ids") or "[]",
                "assessment_history_json": r.get("assessment_history") or "[]"
            })
        return result
    finally:
        conn.close()

def load_student_progress(email, role=None):
    progress = get_student_progress(email, role=role)
    if not progress:
        return False

    st.session_state.selected_role = progress["selected_role"]
    st.session_state.assessment_submitted = progress["assessment_submitted"]
    st.session_state.assessment_date = progress.get("assessment_date", "")
    st.session_state.reassessment_date = progress.get("reassessment_date", "")

    try:
        st.session_state.assessment_answers = json.loads(progress["assessment_answers_json"])
    except Exception:
        st.session_state.assessment_answers = {}

    try:
        st.session_state.initial_analytics = json.loads(progress["initial_analytics_json"])
    except Exception:
        st.session_state.initial_analytics = None

    st.session_state.reassessment_submitted = progress["reassessment_submitted"]

    try:
        st.session_state.reassessment_answers = json.loads(progress["reassessment_answers_json"])
    except Exception:
        st.session_state.reassessment_answers = {}

    try:
        st.session_state.reassessment_analytics = json.loads(progress["reassessment_analytics_json"])
    except Exception:
        st.session_state.reassessment_analytics = None

    try:
        st.session_state.reassessment_questions_map = json.loads(progress["reassessment_questions_map_json"])
    except Exception:
        st.session_state.reassessment_questions_map = {}

    try:
        asked_list = json.loads(progress["asked_question_ids_json"])
        st.session_state.asked_question_ids = set(asked_list)
    except Exception:
        st.session_state.asked_question_ids = set()

    try:
        st.session_state.assessment_history = json.loads(progress.get("assessment_history_json", "[]"))
    except Exception:
        st.session_state.assessment_history = []

    return True

def get_user_by_email(email):
    email = email.strip().lower()
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        if not cursor.fetchone():
            return None
        
        cursor.execute("SELECT * FROM users WHERE LOWER(email) = ?", (email,))
        row = cursor.fetchone()
        if row:
            row_dict = dict(row)
            name = row_dict.get("full_name") or row_dict.get("name") or ""
            return {
                "full_name": name,
                "email": row_dict.get("email"),
                "password": row_dict.get("password")
            }
        return None
    finally:
        conn.close()

def init_auth_state():
    init_db()
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    if "user_email" not in st.session_state:
        st.session_state.user_email = ""
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login"  # 'login', 'register', 'dashboard'

    if st.session_state.authenticated and st.session_state.user_email:
        load_student_progress(st.session_state.user_email)

def register_user(full_name, email, password, confirm_password):
    full_name = full_name.strip()
    email = email.strip().lower()
    password = password.strip()
    confirm_password = confirm_password.strip()

    if not full_name:
        return False, "Full Name cannot be empty."

    if not email:
        return False, "Email ID cannot be empty."

    if not password:
        return False, "Password cannot be empty."

    if not confirm_password:
        return False, "Confirm Password cannot be empty."

    if password != confirm_password:
        return False, "Password and Confirm Password must match."

    # Save to local SQLite database for local/offline login fallback
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO users (full_name, email, password) VALUES (?, ?, ?)",
                       (full_name, email, password))
        conn.commit()
        conn.close()
    except Exception:
        pass

    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": password,
            "options": {
                "data": {
                    "full_name": full_name
                }
            }
        })

        if response.user:
            return True, "Registration Successful"

    except Exception:
        pass

    return True, "Registration Successful"

def login_user(email, password):
    email = email.strip().lower()
    password = password.strip()

    if not email:
        return False, "Please enter your Email ID."

    if not password:
        return False, "Please enter your Password."

    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        user = response.user

        if user:
            st.session_state.authenticated = True
            st.session_state.user_email = user.email
            st.session_state.user_name = (
                user.user_metadata.get("full_name", "")
                if user.user_metadata else ""
            )
            st.session_state.current_page = "dashboard"

            load_student_progress(email)

            return True, "Login Successful"

    except Exception:
        pass

    # Fallback to local SQLite database (for demo users & offline mode)
    local_user = get_user_by_email(email)
    if local_user and local_user.get("password") == password:
        st.session_state.authenticated = True
        st.session_state.user_email = local_user["email"]
        st.session_state.user_name = local_user["full_name"] or "Hema Harini"
        st.session_state.current_page = "dashboard"
        load_student_progress(local_user["email"])
        return True, "Login Successful"

    return False, "Invalid Email ID or Password."

def logout_user():
    st.session_state.authenticated = False
    st.session_state.user_email = ""
    st.session_state.user_name = ""
    st.session_state.current_page = "login"
    # Reset assessment state
    st.session_state.selected_role = "Data Analyst"
    st.session_state.assessment_answers = {}
    st.session_state.assessment_submitted = False
    st.session_state.initial_analytics = None
    st.session_state.assessment_date = ""
    st.session_state.reassessment_date = ""
    st.session_state.assessment_history = []
    st.session_state.reassessment_answers = {}
    st.session_state.reassessment_submitted = False
    st.session_state.reassessment_analytics = None
    st.session_state.reassessment_questions_map = {}
    st.session_state.asked_question_ids = set()
    st.experimental_rerun() if hasattr(st, "experimental_rerun") else st.rerun()