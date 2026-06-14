# Getting this repository onto your GitHub profile and testing it

This guide takes you from a folder on your computer to a live, tested
repository on your GitHub account. It offers two routes. The first uses the
command line and is the one to learn if you intend to keep the repository
updated as the book develops. The second uploads through the browser and needs
no tools beyond a web page. Both end in the same place.

Throughout, replace `drfahadhameedkhan` with your real GitHub username and
`computational-criminology` with whatever you decide to name the repository.

## Before you start

You need a GitHub account. If you do not have one, create it for free at
https://github.com/signup. Choose a username you are content to have appear in
citations, since it becomes part of the repository's web address.

You also need the repository folder on your computer, which is the folder this
guide sits inside.

## Route A: the command line

This route uses Git. If `git --version` prints a version number in your
terminal, you have it. If not, install it from https://git-scm.com/downloads.

### Step 1. Create the empty repository on GitHub

Sign in to GitHub, click the plus sign at the top right, and choose **New
repository**. Name it `computational-criminology`. Add a short description such
as "Companion code and figures for Computational Criminology". Leave it public
if you want others to use it. Do not tick any of the boxes that add a README, a
licence, or a gitignore, because this folder already has them and an empty
repository avoids a conflict on the first push. Click **Create repository**.

GitHub now shows a page with setup commands. Keep it open; you will use the web
address it shows, which looks like
`https://github.com/drfahadhameedkhan/computational-criminology.git`.

### Step 2. Set your username in the project files

Some links and the notebook setup cells contain the placeholder `drfahadhameedkhan`.
Replace it everywhere in one step. Open a terminal in this folder and run:

```bash
python set_username.py drfahadhameedkhan
```

This rewrites the Colab badges, the clone commands, and every notebook so they
point at your copy.

### Step 3. Turn the folder into a Git repository and make the first commit

Still in this folder, run these one at a time:

```bash
git init
git add .
git commit -m "Initial commit: companion repository for Computational Criminology"
git branch -M main
```

If Git asks who you are the first time you commit, set your name and email once:

```bash
git config --global user.name "Fahad Hameed Khan"
git config --global user.email "the-email-on-your-github-account@example.com"
```

Then commit again.

### Step 4. Connect the folder to GitHub and push

Use the web address from Step 1:

```bash
git remote add origin https://github.com/drfahadhameedkhan/computational-criminology.git
git push -u origin main
```

GitHub will ask you to sign in. Use a **personal access token** rather than your
password, because GitHub no longer accepts passwords here. Create one at
https://github.com/settings/tokens by choosing **Generate new token (classic)**,
ticking the **repo** scope, and copying the token. Paste it when the terminal
asks for a password. You can save it so you are not asked again.

Refresh the GitHub page. Your files are now online.

## Route B: upload through the browser

If you would rather not use the command line, you can upload the files
directly, though you will still want to set your username first.

### Step 1. Set your username in the project files

If you have Python, run `python set_username.py drfahadhameedkhan` in this folder as
in Route A, Step 2. If you do not, you can skip this and fix the links later by
editing the README and notebooks on GitHub, but running the script is far
easier.

### Step 2. Create the repository

Follow Route A, Step 1, but this time **do** tick the box to add a README. This
gives you a repository you can upload into.

### Step 3. Upload the files

On the repository page, click **Add file**, then **Upload files**. Drag the
whole contents of this folder into the page. GitHub accepts folders, so you can
drag `code`, `data`, `notebooks`, `figures`, and the rest together. Because
GitHub limits how many files you can upload at once through the browser, you may
need to do this in a few batches, for example one top-level folder at a time.
When the files finish uploading, write a commit message and click **Commit
changes**.

## Verifying it works

### Check the automated tests

This repository ships with a test workflow that runs on GitHub's own servers
every time you push. To watch it:

1. Open your repository on GitHub.
2. Click the **Actions** tab. If GitHub asks you to enable workflows, agree.
3. You will see a run named after your commit. Click it.
4. Open the **python** job. You will see it install the packages, build the
   synthetic data, run each chapter script, and regenerate the figures.

A green tick means every example ran. A red cross means one failed; click into
the step to read the error. The most common cause of an early failure is a
typo introduced while editing, so the message usually points straight at it.

The **spatial** job, which tests Chapter 9, is allowed to fail without turning
the whole run red, because its mapping libraries are heavy and occasionally
slow to install. A failure there is not a problem with your setup.

### Test a notebook on Colab

1. In your repository, open `notebooks/ch08_prediction.ipynb`.
2. At the top of the file view, GitHub shows the notebook. To run it, change the
   web address from `github.com` to `githubtocolab.com` and press enter, or use
   the Colab badge in the README.
3. In Colab, run the first cell. It will clone your repository, install what the
   chapter needs, and build the data. Then run the second cell, which trains the
   model and prints the AUC, precision, and recall.

If the numbers print, the notebook works end to end on a fresh machine, which
is the real test of reproducibility.

### Test locally, if you wish

From the repository folder:

```bash
pip install -r requirements.txt
python data/synthetic/make_synthetic_data.py
python code/python/ch08_prediction.py
python figures/generate_figures.py
```

The first command installs the libraries, the second builds the data, the third
runs a chapter, and the fourth regenerates the figures into `figures/output`.

## Keeping it updated

When you change a file later, the cycle is short:

```bash
git add .
git commit -m "a short note on what changed"
git push
```

Each push triggers the tests again, so you find out within a few minutes
whether the change broke anything.

## If something goes wrong

If the push is rejected with a message about the remote containing work you do
not have, it usually means you created the repository with a README in Route A
by mistake. Run `git pull --rebase origin main` and push again.

If Colab cannot find your repository, check that you replaced `drfahadhameedkhan`
and that the repository is public, since a private repository needs an extra
sign-in step that the simple clone command does not perform.

If a chapter script reports that a file is missing, you most likely have not yet
run `python data/synthetic/make_synthetic_data.py`, which builds the datasets
the scripts read.
