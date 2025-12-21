# Viva Questions & Answers
## Git Bash & GitHub Project

### Basic Git Questions

#### Q1. What is Git?
**Answer:**  
Git is a distributed version control system used to track changes in source code during software development. It allows multiple developers to collaborate on projects and maintain a complete history of all changes.

#### Q2. What is Git Bash?
**Answer:**  
Git Bash is a command-line application for Windows that provides Unix-like commands and allows developers to interact with Git repositories using bash commands.

#### Q3. Explain the difference between Git and GitHub.
**Answer:**  
- **Git**: A version control system installed locally on your computer
- **GitHub**: A cloud-based hosting platform for Git repositories that enables collaboration and remote storage

---

### Git Workflow Questions

#### Q4. Explain the Git workflow: Working Directory → Staging Area → Repository
**Answer:**  
1. **Working Directory**: Where you modify files
2. **Staging Area** (Index): Where you prepare changes using `git add`
3. **Repository**: Where committed changes are permanently stored using `git commit`

#### Q5. What is the difference between `git add` and `git commit`?
**Answer:**  
- `git add`: Stages files, moving them from working directory to staging area
- `git commit`: Permanently saves staged changes to the repository with a message

---

### Branching Questions

#### Q6. What is a branch in Git?
**Answer:**  
A branch is an independent line of development that allows you to work on features, fixes, or experiments without affecting the main code. It creates a separate working environment.

#### Q7. Why did you create multiple branches in your project?
**Answer:**  
I created 4 branches to demonstrate different development workflows:
- **feature**: For adding new statistics endpoint
- **test**: For adding unit tests
- **bugfix**: For fixing input validation issues
- **experiment**: For trying experimental changes and demonstrating merge conflicts

#### Q8. What is the command to create and switch to a new branch?
**Answer:**  
```bash
git checkout -b branch_name
# OR (newer syntax)
git switch -c branch_name
```

---

### Merging Questions

#### Q9. What is a merge in Git?
**Answer:**  
Merging is the process of integrating changes from one branch into another. It combines the commit history of both branches.

#### Q10. What is a merge conflict?
**Answer:**  
A merge conflict occurs when Git cannot automatically combine changes because two branches have modified the same part of a file differently. It requires manual resolution.

#### Q11. How did you create and resolve the merge conflict in your project?
**Answer:**  
**Creation:**
1. Modified the same section of README.md on master branch
2. Modified the same section differently on experiment branch
3. Attempted to merge experiment into master
4. Git detected the conflict

**Resolution:**
1. Opened README.md and located conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
2. Manually edited the file to combine both changes meaningfully
3. Removed all conflict markers
4. Staged the resolved file: `git add README.md`
5. Completed the merge: `git commit`

#### Q12. What are the conflict markers in Git?
**Answer:**  
```
<<<<<<< HEAD
Content from current branch
=======
Content from merging branch
>>>>>>> branch_name
```

---

### Remote Repository Questions

#### Q13. What is a remote repository?
**Answer:**  
A remote repository is a version of your project hosted on a server (like GitHub) that allows collaboration and backup of your code.

#### Q14. What is the difference between `git push` and `git pull`?
**Answer:**  
- `git push`: Uploads local commits to remote repository
- `git pull`: Downloads and merges remote changes into local repository

#### Q15. What is the difference between `git fetch` and `git pull`?
**Answer:**  
- `git fetch`: Downloads remote changes but doesn't merge them
- `git pull`: Downloads and automatically merges remote changes (fetch + merge)

#### Q16. What is the difference between `git clone` and `git pull`?
**Answer:**  
- `git clone`: Creates a complete copy of a remote repository (first-time setup)
- `git pull`: Updates an existing local repository with remote changes

---

### Commit Questions

#### Q17. How many commits did you make in this project?
**Answer:**  
I made **12 meaningful commits** with clear messages describing each change.

#### Q18. Why are good commit messages important?
**Answer:**  
Good commit messages:
- Help understand project history
- Make debugging easier
- Facilitate code reviews
- Improve team collaboration
- Serve as documentation

#### Q19. Show some examples of your commit messages.
**Answer:**  
- "Initial project setup and Git initialization"
- "Add CSS styling for notes application"
- "Add statistics endpoint to track note counts"
- "Fix input validation bug in add_note function"
- "Resolve merge conflict between master and experiment branches"

---

### Project-Specific Questions

#### Q20. Describe your project.
**Answer:**  
This is a Student Notes Sharing Application built with Python Flask. It allows students to create, view, search, edit, pin, and delete notes. The project demonstrates Git and GitHub workflows including branching, merging, and conflict resolution.

#### Q21. What technologies did you use?
**Answer:**  
- **Backend**: Python 3.x with Flask framework
- **Frontend**: HTML and CSS
- **Containerization**: Docker
- **Version Control**: Git & GitHub
- **Testing**: Python unit tests

#### Q22. Why did you choose this project?
**Answer:**  
I chose this project because:
1. It's a practical, real-world application
2. It has enough complexity to demonstrate multiple Git operations
3. It shows both backend and frontend development
4. It's relevant to students and educational institutions

---

### Advanced Questions

#### Q23. What is .gitignore and why is it important?
**Answer:**  
`.gitignore` is a file that specifies which files Git should not track. It's important to exclude:
- Compiled code
- Dependencies (node_modules, __pycache__)
- Environment variables
- IDE configuration files
- Temporary files

#### Q24. What is the difference between `git reset` and `git revert`?
**Answer:**  
- `git reset`: Moves the branch pointer backward, removing commits from history (dangerous)
- `git revert`: Creates a new commit that undoes previous changes (safer for shared branches)

#### Q25. What is a merge vs rebase?
**Answer:**  
- **Merge**: Combines branches and preserves complete history with a merge commit
- **Rebase**: Replays commits on top of another branch, creating a linear history

#### Q26. Can you explain fast-forward merge?
**Answer:**  
A fast-forward merge occurs when the current branch has no new commits since the branch being merged was created. Git simply moves the pointer forward without creating a merge commit.

---

### Docker Questions (Bonus)

#### Q27. Why did you use Docker in this project?
**Answer:**  
Docker ensures:
- Consistent environment across different machines
- Easy deployment without dependency issues
- Isolation from system configuration
- Portability and scalability

#### Q28. What is in your Dockerfile?
**Answer:**  
My Dockerfile:
1. Uses Python base image
2. Sets working directory
3. Copies requirements.txt and installs dependencies
4. Copies application code
5. Exposes port 5000
6. Runs the Flask application

---

### Demonstration Questions

#### Q29. Can you show your commit history?
**Answer:**  
```bash
git log --oneline --all --graph
```

#### Q30. Can you show all your branches?
**Answer:**  
```bash
git branch
# Shows: feature, test, bugfix, experiment, master
```

---

## Tips for Viva

1. **Be Confident**: You did the work, own it
2. **Be Honest**: If you don't know something, say so
3. **Show Your Work**: Open Git Bash and demonstrate commands
4. **Explain Your Thinking**: Don't just say what you did, explain why
5. **Know Your Project**: Be ready to explain every file and commit
6. **Practice Commands**: Run git commands before viva to be comfortable

## Common Mistakes to Avoid

❌ Don't say "I used GitHub Desktop" - This is a Git Bash project  
❌ Don't confuse Git with GitHub  
❌ Don't claim you understand something if you don't  
✅ Show enthusiasm about what you learned  
✅ Demonstrate commands live  
✅ Explain real-world applications  
