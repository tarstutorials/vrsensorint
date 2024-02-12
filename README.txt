To anyone looking to update te Github Pages output:

1. When you have tested a build on your machine and verified that it works, go into the build folder on your machine.

2. Copy all the files in the build folder.

3. Navigate to the docs folder. 

4. Delete any files from the docs folder that have the same name as the ones you copied from build. DO NOT DELETE THE .nojekyll file!

5. Paste the new build files from the build folder into the docs folder.

6. Upload commit. Note that only commits done to main will be reflected on the site. 

7. If you are confused at all, message me! Please don't try it yourself if you are unsure, we don't want to brick the site. Thanks!

To any developers looking to use this site after a Git clone, here are some instructions:

1. Make sure you have sphinx installed. If not, you can install it with the following in a terminal: 

    sudo apt-get install python3-sphinx

Note that this command is for a Linux Mint installation. Check the sphinx documentation for how to do it for your OS if you don't run Mint.

2. Run the following command in the project folder to install the correct theme for the site:

 pip install sphinx_rtd_theme

 This will install the Read The Docs theme for the website. If for some reason you can't get it to install correctly, go into the conf.py file and follow the instructions in the "options for HTML output" section.

3. Run the following command in the same location to download the quizdown extension:

pip install git+git://github.com/bonartm/sphinxcontrib-quizdown

Note that you may also have to run "git config --global url.https://github.com/.insteadOf git://github.com/" if the install fails. This is because the install is using the old Github download, and must be configured to use the new one.

4. Run the following command:

    make html

This will generate the files needed to run the website via HTML. Any time you make changes to the website, you must run this command again to update the files.
Additionally, you can use the command "make clean" to erase all build files from the build folder.

5. In the build ~/build/ folder, you should now see a folder called "html/". In this folder there should be a file called "index.html". Open this file in Firefox (or any other worse browser) to view the
webpage.

That's all! If you have any more questions, send me a Slack DM or email me at matzekec@clarkson.edu

Cheers,

Ethan

