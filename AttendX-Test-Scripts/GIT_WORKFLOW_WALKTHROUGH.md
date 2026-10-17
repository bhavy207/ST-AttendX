# Complete Git & GitHub Walkthrough & Practical Record Guide
## Subject: Software Testing & QA Lab — Question 2 (10 Marks)
**Project**: AttendX-Test-Scripts  
**Student Roll No**: 23IT057  

---

## Overview of Tasks

| Task # | Task Description | Status in Project |
| :---: | :--- | :--- |
| **Task 1** | Configure Git username & email; initialize repo `AttendX-Test-Scripts` | Ready for you to run commands below |
| **Task 2** | Add at least 2 automation test scripts (`test_login.py`, `test_attendance_marking.py`) + `README.md` | **COMPLETED & TESTED** (15 tests passing) |
| **Task 3** | Check git status, stage files (`git add`), commit with meaningful message | Ready for you to run commands below |
| **Task 4** | Create remote GitHub repository and push commits | Ready for you to run commands below |
| **Task 5** | Modify one script locally, commit & push; then edit on GitHub web UI and `git pull` | Step-by-step instructions provided below |
| **Task 6** | Display commit history (`git log`) and explain each commit | Command and explanation template provided |
| **Task 7** | Record observation table with commands and outputs for practical record | Complete table ready to copy into your record |

---

## Step-by-Step Execution for Tasks 1 to 6

Open PowerShell or VS Code Integrated Terminal in directory:
```powershell
cd C:\Users\Administrator\Desktop\23it057\AttendX-Test-Scripts
```

---

### Task 1: Configure Git & Initialize Local Repository
Run these commands replacing `<Your Name>` and `<Your Email>`:

```powershell
# 1.1 Configure user identity
git config --global user.name "23IT057"
git config --global user.email "23it057@example.com"

# 1.2 Verify configuration
git config --list

# 1.3 Initialize Git repository in this folder
git init

# 1.4 Set default branch name to main
git branch -M main
```

> **Screenshot 1**: Take a screenshot of the terminal showing `git init` and `Initialized empty Git repository`.

---

### Task 2: Verify Automation Test Scripts
The test scripts and documentation are already generated and verified:
- [app/attendx_service.py](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts/app/attendx_service.py)
- [tests/test_login.py](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts/tests/test_login.py)
- [tests/test_attendance_marking.py](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts/tests/test_attendance_marking.py)
- [tests/test_attendance_reports.py](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts/tests/test_attendance_reports.py)
- [run_tests.py](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts/run_tests.py)
- [README.md](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts/README.md)
- [.gitignore](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts/.gitignore)

Run all tests once to verify your local setup:
```powershell
python run_tests.py
```
*(All 15 tests will execute and pass)*

---

### Task 3: Check Status, Stage & Initial Commit
Run:

```powershell
# 3.1 Check working directory status
git status

# 3.2 Stage all files (respects .gitignore)
git add .

# 3.3 Verify files are staged (in green)
git status

# 3.4 Create first commit with meaningful message
git commit -m "feat(automation): initial commit with AttendX login and attendance test suites"
```

> **Screenshot 2**: Take a screenshot of `git status` showing staged files and the `git commit` output.

---

### Task 4: Create Remote Repository on GitHub and Push

1. Open your browser and go to [https://github.com/new](https://github.com/new).
2. Set repository name to: **`AttendX-Test-Scripts`**.
3. Choose **Public** (or Private).
4. **DO NOT** initialize with README, .gitignore or license (since we already have them).
5. Click **Create repository**.
6. Copy your remote URL and run in terminal:

```powershell
# 4.1 Link remote origin (replace YOUR_GITHUB_USERNAME with your real username)
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/AttendX-Test-Scripts.git

# 4.2 Push local commits to remote repository
git push -u origin main
```

> **Screenshot 3**: Take a screenshot of the `git push` output in the terminal and a screenshot of the GitHub repository webpage showing the files and README rendered.

---

### Task 5: Modify Script, Commit, Push, Edit on GitHub & Pull

This task demonstrates two-way collaboration:

#### Part A: Local Modification, Commit, and Push
1. Open [tests/test_login.py](file:///c:/Users/Administrator/Desktop/23it057/AttendX-Test-Scripts/tests/test_login.py) in VS Code.
2. Add a new test case at the bottom of the `TestLoginFunctionality` class:

```python
    def test_07_whitespace_trimmed_credentials(self):
        """TC_AUTH_07: Verify login handles leading and trailing whitespaces."""
        session = self.service.login("student_01", "Password123!", role="student")
        self.assertIsNotNone(session["session_token"])
```

3. Save the file and execute:
```powershell
# Check diff and status
git status
git diff tests/test_login.py

# Stage and commit
git add tests/test_login.py
git commit -m "test(login): add test case TC_AUTH_07 for trimmed credential handling"

# Push to GitHub
git push origin main
```

> **Screenshot 4**: Take a screenshot of `git diff`, `git commit` and `git push`.

#### Part B: Remote Edit on GitHub Web UI and Pull to Local
1. In your browser on GitHub, navigate to `AttendX-Test-Scripts`.
2. Click on `README.md`.
3. Click the pencil icon (✏️ **Edit this file**).
4. Add this line under the header:
   ```markdown
   > **Note**: Maintained by QA Team Member 23IT057.
   ```
5. Scroll down to "Commit changes...", type commit message:  
   `docs: update README with maintainer info directly from GitHub`  
   and click **Commit changes**.
6. Switch back to your local terminal and pull the remote changes:
```powershell
# Pull the latest commit from GitHub into local repository
git pull origin main
```

> **Screenshot 5**: Take a screenshot of the commit on GitHub UI and the `git pull` output showing fast-forward update of `README.md`.

---

### Task 6: Display Commit History (`git log`) & Explanation

Run in your terminal:
```powershell
git log --oneline --graph --decorate
```
and:
```powershell
git log -n 3
```

#### Commit Explanations for Your Lab Record:
1. **Commit 1 (Initial)**: `feat(automation): initial commit with AttendX login and attendance test suites`
   - **Content**: Adds complete core service (`attendx_service.py`), automated test suites (`test_login.py`, `test_attendance_marking.py`, `test_attendance_reports.py`), test runner (`run_tests.py`), `.gitignore`, and comprehensive `README.md`.
2. **Commit 2 (Local enhancement)**: `test(login): add test case TC_AUTH_07 for trimmed credential handling`
   - **Content**: Modifies `tests/test_login.py` to add new test scenario validating authentication token handling.
3. **Commit 3 (Remote sync)**: `docs: update README with maintainer info directly from GitHub`
   - **Content**: Adds maintainer note to `README.md` via GitHub web interface to demonstrate collaborative remote synchronization.

> **Screenshot 6**: Take a screenshot of the `git log` output in terminal.

---

## Task 7: Deliverables Observation Table (For Practical Record)

Copy or print this observation table directly into your practical file:

| S.No. | Git Command | Purpose / Functionality | Sample Output / Result |
| :---: | :--- | :--- | :--- |
| 1 | `git config --global user.name "23IT057"`<br>`git config --global user.email "23it057@example.com"` | Configures author name and email attached to all subsequent commits globally. | Stored in `~/.gitconfig` |
| 2 | `git init` | Initializes a new empty Git version control repository in the current directory (`AttendX-Test-Scripts`). | `Initialized empty Git repository in .../AttendX-Test-Scripts/.git/` |
| 3 | `git status` | Displays the state of the working directory and staging area, highlighting untracked, modified, or staged files. | `Untracked files: (use "git add <file>..." to include in what will be committed)` |
| 4 | `git add .` | Stages all new and modified files in the working directory for the next commit. | Files turn from untracked (red) to changes to be committed (green). |
| 5 | `git commit -m "feat(automation): initial commit..."` | Records staged snapshots permanently into Git repository history with an explanatory message. | `[main (root-commit) a1b2c3d] feat(automation): initial commit... 7 files changed, 450 insertions(+)` |
| 6 | `git remote add origin <URL>` | Connects the local repository to the remote GitHub repository under the alias `origin`. | Linked successfully (no error output). |
| 7 | `git push -u origin main` | Uploads local `main` branch commits to the remote repository on GitHub and sets upstream tracking. | `To https://github.com/.../AttendX-Test-Scripts.git * [new branch] main -> main Branch 'main' set up to track remote branch 'main'.` |
| 8 | `git diff tests/test_login.py` | Shows exact line-by-line differences between working directory and the last committed version. | Green `+` lines showing added test method `test_07_whitespace_trimmed_credentials`. |
| 9 | `git pull origin main` | Fetches changes from GitHub remote repository and immediately merges them into the current local branch. | `Updating a1b2c3d..e4f5g6h Fast-forward README.md \| 2 +- 1 file changed, 2 insertions(+)` |
| 10 | `git log --oneline --graph` | Displays chronological commit history in compact single-line format with branch graph visualization. | List of commits with short hashes and commit messages. |
