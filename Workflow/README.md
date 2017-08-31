# Github workflow

Github is a great tool when used effectively. The learning curve is a bit steep as there is a lot of different terminology and weird things can happen pretty easily.

Here are instructions for a good workflow when using Github collaboratively. These instructions might seem complex but the process is actually very simple once you have done it a couple of times. It helps to keep things organized, make sure we are somewhat standardizing our coding practices, and help us to keep track of what each other is doing.

We can use forking and branching to work effectively on different sub-tasks without interrupting or over-writing each others work.

# Getting set up

1. Fork the main Github repo so that you have your own personal version. The master version will always be Charles' version (so no need for you to do this Charles). Clone your fork locally and `cd` into the directory. You can confirm you are in the directory with the command `git status`.

# The Workflow

2. Now set the `upstream` version to Charles' repo using the following command: `git remote add upstream https://github.com/cttong/info6742`. This will allow us to easily pull the latest version of the main repo into our forks. I'll come back to how to do this below.

3. For each task we work on we should be using a `branch` NOT the `master` repo. ***Never commit directly to master***

To make a new branch you can use the following command:
`git checkout -b branch_name` where `branch_name` is something informative, e.g. the branch I am using for this tutorial is called `github_workflow`.

You can confirm you are in the new branch using `git status` which will should you the branch name.

Make sure that when you are ready to `push` any work on the branch that you push to the branch and not master, e.g. `git push origin branch_name`.

You can do as many commits and pushes to your local branch as your need to. Generally you probably want to merge a branch once you have completed a moderately sized task, e.g. writing a script that defines a Class or fixing a bug with a script somebody else wrote.

4. When you are ready to merge your branch into master you can go to the Github website (Charles' branch) and open a `Pull request` (PR). You should see a prompt in the middle of the page asking if you want to do this.

5. Give the PR  an informative name and select one or more of the other team members as `Reviewers`.

6. ***Assuming there are no conflicts***
The reviewers can then check the files being added to see the commit and leave comments if they see any issues, for example if there is a bug, a typo, or some function could be written more efficiently. You can then amend these problems. As long as you are in the branch, new commits can be added and the PR will be updated.

This both helps to ensure that the code being committed is good, by having a second pair of eyes on it, and will help us to keep track of the project better by forcing us to look at code we didn't write.

When the reviewer is satisfied that the code is good to merge they can simply comment this on the thread. A standard phrase used is `LGTM` or Looks Good To Merge.

***Reviewers should not merge the pull request themselves, it should be down to the person making it***

You can then merge the pull request.

***If there are conflicts (you will see a message indicating this)*** then they will need to be resolved. For example if your PR conflicts with existing code you will need to do a merge. This makes things a bit more complicated. If the workflow above is adhered to closely then this should be a rare occurrence.

7. When you merge the PR you will be asked if you want to delete your branch. You should do this.

8. Now you are stuck in a deleted branch on your local fork. Even worse, your master branch is out of date as it doesn't have the new material you pushed. This is where the `upstream` thing you did earlier comes in. With a couple of simple commands you can easily get the latest version of the master branch into your fork.

First, use `git checkout master` to switch back to the `master` of your local fork. Second, use `git fetch upstream` to point your local git at the upstream branches. Finally, use `git pull upstream master` to pull the most up-to-date master from Charles' repo into your local fork.

### Now repeated steps 1-8 each time your start working on a new problem.

Let me know if you have any questions.
