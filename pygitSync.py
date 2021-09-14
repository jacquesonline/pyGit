import  git 
from git import Repo

repo_path = ""
repo = ""

# To initiate new Git repo in the mentioned directory
repository = Repo.init(repo_path)

# Clone an existing repository into a new directory,
git.Git(repo_path).clone("https://github.com/digitalvarys/test.git")

# Git Checkout
# To replace the current working files with files from a branch:
repo.git.checkout("branchename")
# Also, if you are checking out with a new branch:

repo.git.checkout("-b", "branchename")


# Git Fetch
repo = git.Repo("name_of_repo")
repo.remote().fetch()

# Git Add
# To put current working files into the current index:
repo.git.add("--all")  # to add all the working files.
repo.git.add("index.html", "style.css")
# to add specific working file(s).

# Git Commit
# To commit indexed changes to a local branch in the local repo.
repo.git.add("--all")  
repo.git.commit("-m", "commit message from python script", author="test_user@test.com")

# Git push
# To push all the committed changes in branch from the local repository to the remote repository.
repo.git.add("--all")
repo.git.commit("-m", "commit message from python script", author="test_user@test.com")
origin = repo.remote(name="origin")
origin.push()

# Git Pull
# To fetch all the changes from the remote repository to the local repository:



repo = git.Repo("name_of_repo")
origin = repo.remote(name="origin")
origin.pull()

# Git Merge
# To Merge the current branch to the master (or any specified) branch:

repo = git.Repo(".")
master = repo.branches["master"]
current = repo.branches["feature"]
root = repo.merge_base(current, master)
repo.index.merge_tree(master, base=root)
repo.index.commit("merging master into current branch", parent_commits=(current.commit, master.commit))

# Automatically provide credentials?
# git config --global credential.helper