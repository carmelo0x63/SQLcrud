### Git cheatsheet

#### Git global setup
###### Initial config
* `git config --global user.name "<Name> <Surname>"`
* `git config --global user.email "<userid>@example.com"`

###### Show configuration
* `git config -l`

#### Create Local Repository
```
mkdir <repo_name>
cd <repo_name>
git init
git add <file> or git add .
git commit -m '<put message here>'
  CLI: git remote add origin git@github.com:<userid>/<repo_name>.git
  HTTPS: git remote add origin https://github.com/<userid>/<repo_name>.git
git push -u origin <branch_name>
```

#### Existing Git Repo
```
cd <existing_git_repo>
git push [-u origin <branch_name>]
```

#### Cloning
```
git clone git@github.com:<userid>/<repo_name>.git
```

#### Branching
```
git checkout -b <new_branch_name>
git checkout <existing_branch_name>
```

#### Update local repository (e.g. after a merge)
```
git pull [origin <branch_name]
```

#### Delete Branch
```
git branch -D <local_branch_name>
git push origin --delete <remote_branch_name>
```
