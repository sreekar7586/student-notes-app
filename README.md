# Student Notes Sharing Application  
**Git Bash & GitHub Hands-On Project**

## 📌 Introduction
This project is developed as part of the **Version Control Systems** course to demonstrate practical usage of **Git Bash and GitHub**.  

The project demonstrates advanced Git workflows including branching, merging, and conflict resolution techniques.

The application is a **Student Notes Sharing Web Application** where users can create, view, search, edit, pin, and delete notes using a Python Flask backend with a simple web interface.  

This is an educational project designed to master Git workflows and version control best practices with hands-on implementation.

The primary goal of this project is to showcase **professional Git practices** and version control in a real development scenario.

---

## 🛠 Technologies Used
- **Python 3.x**  
- **Flask Framework**  
- **HTML & CSS**  
- **Docker**  
- **Git & GitHub**  

---

## 📂 Project Structure
```
student-notes-app/
│
├── app.py                    # Main Flask application
├── notes.json                # Data storage for notes
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
├── static/                   # CSS and static assets
├── templates/                # HTML templates
│   ├── index.html
│   └── add_edit.html
├── tests/                    # Test files
└── README.md                 # Project documentation
```

## 🚀 Deployment

**Live Deployment:** https://student-notes-app-production.up.railway.app

The application is deployed on **Railway** with continuous deployment from GitHub.

### Accessing the Live Application

1. Visit the live URL: [Student Notes Sharing App](https://student-notes-app-production.up.railway.app)
2. Create, view, search, edit, pin, and delete notes in real-time
3. All changes are saved to the backend database

### Deployment Details

- **Platform:** Railway.app
- **Branch:** master
- **Auto-deploy:** Enabled (deploys on every git push)
- **Environment:** Production
- **Database:** JSON file storage

---

---

## 🚀 How to Run the Project

### Using Python
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Access in browser
http://localhost:5000

# View statistics endpoint
http://localhost:5000/stats
```

### Using Docker
```bash
# Build Docker image
docker build -t student-notes-app .

# Run Docker container
docker run -p 5000:5000 student-notes-app

# Access in browser
http://localhost:5000
```

---

## 🔧 Git and GitHub Operations Used

### Repository Initialization
```bash
git init
git add .
git commit -m "Initial project setup"
```

### Branching
```bash
git checkout -b feature       # Feature development branch
git checkout -b test          # Testing branch
git checkout -b bugfix        # Bug fixing branch
git checkout -b experiment    # Experimental changes branch
```

### Merging
```bash
git checkout main
git merge feature
git merge test
git merge bugfix
git merge experiment
```

### Remote Repository Operations
```bash
git remote add origin <GitHub-Repository-URL>
git push origin main
git push --all origin         # Push all branches
git pull origin main
git clone <GitHub-Repository-URL>
```

---

## ⚠️ Merge Conflict Demonstration

A merge conflict was intentionally created by modifying the same file (`README.md`) in two different branches (`main` and `experiment`).

**Steps:**
1. Modified README.md in main branch
2. Created experiment branch and modified the same section of README.md
3. Attempted to merge experiment into main
4. Git detected conflicting changes
5. Manually resolved the conflict by editing the file
6. Staged the resolved file with `git add README.md`
7. Completed the merge with `git commit`

**Conflict Markers:**
```
<<<<<<< HEAD
Content from main branch
=======
Content from experiment branch
>>>>>>> experiment
```

The conflict was resolved by choosing the appropriate content and removing conflict markers.

---

## 🖼 Screenshots

### Application Screenshots
- **Home Page**: Main interface showing all notes
- **Add Note**: Form to create new notes
- **Edit Note**: Modify existing notes
- **Search**: Search functionality for finding notes

### Git Workflow Screenshots
- **Commit History**: Shows all 10+ commits with meaningful messages
- **Branch List**: Displays all 4 branches (feature, test, bugfix, experiment)
- **Merge Conflict**: Demonstration of conflict and resolution
- **GitHub Repository**: Remote repository with all commits synced

---

## 🚧 Challenges Faced

1. **Merge Conflicts**: Understanding and resolving conflicts when merging branches with overlapping changes
2. **Branch Management**: Coordinating work across multiple branches simultaneously
3. **Commit Message Quality**: Writing clear, meaningful commit messages for each change
4. **Docker Configuration**: Setting up proper port mapping and environment variables
5. **Git Remote Setup**: Understanding the difference between local and remote operations

---

## ✅ Conclusion

This project provided hands-on experience with **Git Bash and GitHub**, covering essential version control concepts:

- **Repository Management**: Initializing and maintaining a Git repository
- **Staging & Committing**: Understanding the Git workflow (working directory → staging area → repository)
- **Branching Strategy**: Creating multiple branches for different purposes
- **Merging**: Combining work from different branches
- **Conflict Resolution**: Handling and resolving merge conflicts
- **Remote Collaboration**: Pushing, pulling, and synchronizing with GitHub

The project follows industry best practices and demonstrates real-world Git workflows that are essential for professional software development.

**Key Learnings:**
- Version control is crucial for tracking changes and collaboration
- Branches enable parallel development without affecting main code
- Meaningful commit messages make project history understandable
- Git and GitHub are essential tools for modern software development

---

## 👨‍💻 Author

**Student Name**: Mamidipaka Venkata Sai Sreekar  
**Course**: Version Control Systems  
**Project**: Git Bash & GitHub Hands-On Project  
**Date**: December 2025

---

## 📚 References

- [Git Official Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Branching Strategy](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows)

---

## 📸 Screenshots

Here are some screenshots of the Student Notes Sharing Application:

### Home Page
![Home Page](Screenshot%202026-01-02%20083912.png)

### Notes List View
![Notes List](Screenshot%202026-01-02%20084058.png)

### Add/Edit Note
![Add Note](Screenshot%202026-01-02%20084106.png)

### Search Functionality
![Search](Screenshot%202026-01-02%20084113.png)

### Pin Feature
![Pin Feature](Screenshot%202026-01-02%20084122.png)

### Delete Confirmation
![Delete](Screenshot%202026-01-02%20084131.png)

### Git Workflow Screenshots

#### Commit History
[View Commits](https://github.com/sreekar7586/student-notes-app/commits/master) - Shows all commits with meaningful messages demonstrating proper Git workflow

#### Git Branches
[View Branches](https://github.com/sreekar7586/student-notes-app/branches) - Displays all feature branches (master, feature, test, bugfix, experiment) and their status

#### Network Graph
[View Network](https://github.com/sreekar7586/student-notes-app/network) - Visual representation of the Git workflow showing branch merges and commit timeline
