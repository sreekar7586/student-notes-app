# Git Workflow Documentation

## Repository Setup
```bash
git init
Initialized empty Git repository
```

## Commit History (11 Total Commits)

1. **ba3a70d** - Initial project setup and Git initialization
2. **30818f0** - Add CSS styling for notes application
3. **156ad77** - Add documentation to Flask routes
4. **e0b57a6** - Add testing documentation and test plan
5. **4fd0a1e** - Add statistics endpoint to track note counts (feature branch)
6. **6c6925a** - Update README with stats endpoint documentation (feature branch)
7. **a48cfc2** - Add unit tests for application functionality (test branch)
8. **9cbaca9** - Fix input validation bug in add_note function (bugfix branch)
9. **05b4eed** - Enhance README with educational context
10. **4a3e637** - Experiment: Simplify README introduction section (experiment branch)
11. **3c85deb** - Resolve merge conflict between master and experiment branches

## Branch Structure (4 Branches Created)

### 1. feature
- Purpose: Add new statistics endpoint
- Commits: 2
- Status: Merged into master

### 2. test
- Purpose: Add unit testing framework
- Commits: 1
- Status: Merged into master

### 3. bugfix
- Purpose: Fix input validation issues
- Commits: 1
- Status: Merged into master

### 4. experiment
- Purpose: Experimental README changes (created merge conflict)
- Commits: 1
- Status: Merged with conflict resolution

## Merge Operations

### Feature Branch Merge
```bash
git checkout master
git merge feature
Fast-forward merge successful
```

### Test Branch Merge
```bash
git checkout master
git merge test
Fast-forward merge successful
```

### Bugfix Branch Merge
```bash
git checkout master
git merge bugfix
Fast-forward merge successful
```

### Experiment Branch Merge (WITH CONFLICT)
```bash
git checkout master
git merge experiment
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

#### Conflict Resolution Steps:
1. Git detected conflicting changes in README.md
2. Opened README.md and found conflict markers:
   ```
   <<<<<<< HEAD
   Content from master branch
   =======
   Content from experiment branch
   >>>>>>> experiment
   ```
3. Manually edited the file to combine both changes meaningfully
4. Removed conflict markers
5. Staged the resolved file: `git add README.md`
6. Completed merge: `git commit`

## Branch Visualization
```
*   3c85deb (HEAD -> master) Resolve merge conflict
|\
| * 4a3e637 (experiment) Experiment: Simplify README
* | 05b4eed Enhance README with educational context
|/
* 9cbaca9 (bugfix) Fix input validation bug
* a48cfc2 (test) Add unit tests
* 6c6925a (feature) Update README with stats endpoint
* 4fd0a1e Add statistics endpoint
* e0b57a6 Add testing documentation
* 156ad77 Add documentation to Flask routes
* 30818f0 Add CSS styling
* ba3a70d Initial project setup
```

## Key Learnings

1. **Branching Strategy**: Created separate branches for different types of work
2. **Merge Conflicts**: Successfully demonstrated and resolved a merge conflict
3. **Commit Messages**: Used clear, descriptive commit messages
4. **Version Control**: Maintained clean project history with logical commits
5. **Collaboration**: Simulated real-world team development workflow
