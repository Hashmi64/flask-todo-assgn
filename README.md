# Flask To-Do Assignment – Full Git & Project Workflow

This project is a small Flask-based To-Do application using MongoDB.  
Below is the complete Git workflow followed during development, including branching, PR creation, rebase, stash, and merge.

---

## 1. Clone the repository
git clone https://github.com/Hashmi64/flask-todo-assgn.git
cd flask-todo-assgn

---

## 2. Create a new feature branch
git checkout -b master_1

---

## 3. Made code changes
- Updated `todo.html` (added itemID, itemUUID, itemHash fields)
- Updated backend route in `app.py`
- Updated templates (`form.html`, `success.html`, `todo.html`)
- Used `.env` and `data.json`

---

## 4. Stage and commit the changes
git add .
git commit -m "Added To-Do fields and updated backend"

---

## 5. Push the feature branch to GitHub
git push origin master_1

---

## 6. Create a Pull Request on GitHub
Branch: `master_1` → `main`  
Reviewed and merged the PR successfully.

---

## 7. Pull the latest changes into main branch
git checkout main
git pull

---

## 8. Rebase feature branch with main
git checkout master_1
git rebase main

If conflicts appear:
git add .
git rebase --continue

---

## 9. Used git stash when rebase failed due to unstaged changes
git stash
git rebase main
git stash list
git stash pop      # when needed

---

## 10. Force-pushed after rebase
git push origin master_1 --force

---

## 11. Final Pull Request merged
PR successfully merged into the `main` branch on GitHub.

---

## Project Structure
flask-todo-assgn/
│── app.py
│── data.json
│── .env
│── templates/
│     ├── form.html
│     ├── success.html
│     └── todo.html
│── README.md

---

## Final Summary
- Completed project using proper Git workflow
- Feature branch created and merged using PR
- Rebase, stash, and force-push used during conflict resolution
- Final code is available in the `main` branch

[Flask_TODO_Assignment_Git_Workflow.docx](https://github.com/user-attachments/files/23546496/Flask_TODO_Assignment_Git_Workflow.docx)
