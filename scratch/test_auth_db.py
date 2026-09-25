import os
import sys

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.auth import init_auth_state, register_user, login_user, get_user_by_email, DB_PATH

def test_flow():
    print(f"DB Path: {DB_PATH}")
    
    # Initialize DB
    init_auth_state()
    
    # 1. Verify default user hema@gmail.com exists
    hema = get_user_by_email("hema@gmail.com")
    print("Default user check:", hema)
    assert hema is not None, "Default user should exist!"
    assert hema["full_name"] == "Hema Harini"
    
    # 2. Register a new user
    test_email = "john.doe@example.com"
    success, msg = register_user("John Doe", test_email, "Secret123!", "Secret123!")
    print("Registration result:", success, msg)
    assert success is True, f"Registration failed: {msg}"
    
    # 3. Try to register duplicate user
    success_dup, msg_dup = register_user("John Doe", test_email, "Secret123!", "Secret123!")
    print("Duplicate registration result:", success_dup, msg_dup)
    assert success_dup is False
    assert "already exists" in msg_dup.lower()
    
    # 4. Login with wrong password
    success_wrong, msg_wrong = login_user(test_email, "WrongPassword")
    print("Wrong password login result:", success_wrong, msg_wrong)
    assert success_wrong is False
    assert "invalid" in msg_wrong.lower()
    
    # 5. Login with correct password
    success_login, msg_login = login_user(test_email, "Secret123!")
    print("Correct password login result:", success_login, msg_login)
    assert success_login is True
    
    # 6. Verify persistence by re-reading directly
    john_persisted = get_user_by_email(test_email)
    print("Persisted user record:", john_persisted)
    assert john_persisted is not None
    assert john_persisted["full_name"] == "John Doe"
    
    print("\nALL PERSISTENCE AND AUTH TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_flow()
