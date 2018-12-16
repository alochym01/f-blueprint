# Using `CLI`
1. git store user/pass
	- step 0:
	    - run command: `git config --global credential.helper store`
	- step 1:
	    - run command: `git add .`
	- step 2:
	    - run command: `git commit -m 'initial structure'`
	- step 3:
	    - run command: `git push` and then input username/password
2. git branch
	- Create new branch
		- git checkout -b add_templates
	- List all branch
		- git branch
	- Switch to new branch
		- git checkout add_templates
	- Check status of new branch
		- git status
	- Add all changed files
		- git add .
		- git commit -m "Added use of templates and Bootstrap"
	- Switch to master branch
		- git checkout master
	- Merge add_templates branch to mater branch
		- git merge add_templates
	- Delete git local branch
		- branch -d add_templates
	- Push all files
		- git push -u origin master
3. git release
	- Add a release
		- git tag -a v0.1 -m "finish guide for nginx and uwsgi"
		- git push --tags
	- Delete release/tag
		- delete local tag
			- git tag -d `tag-name`
		- delete remote tag
			- git push origin :refs/tags/`github-version`
		- alternative approach
			- git push --delete origin `tag-name`
			- git tag -d `tag-name`