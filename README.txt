To any developers looking to use this site after a Git clone, here are some instructions:

1. Create a directory called "build" in the ~/docs/ folder. Add this to the GitIgnore so that any build files don't get added into the repo.

2. Make sure you have sphinx installed. If not, you can install it with the following in a terminal: 

    sudo apt-get install python3-sphinx

Note that this command is for a Linux Mint installation. Check the sphinx ddocumentation for how to do it for your OS if you don't run Mint.

3. Open a terminal and navigate to the ~/docs/ folder.

4. Run the following command to install the correct theme for the site:

 pip install sphinx_rtd_theme

 This will install the Read The Docs theme for the website. If for some reason you can't get it to install correctly, go into the conf.py file and follow the instructions in the "options for HTML output" section.

5. Run the following command:

    make html

This will generate the files needed to run the website via HTML. Any time you make changes to the website, you must run this command again to update the files.
Additionally, you can use the command "make clean" to erase all build files from the build folder. This can help if something in the build gets corrupted or you forgot
to add the build folder to GitIgnore and don't want to individually delete the files.

5. In the build ~/docs/build/ folder, you should now see a folder called "html/". In this folder there should be a file called "index.html". Open this file in Firefox (or any other worse browser) to view the
webpage.

That's all! If you have any more questions, send me a Slack DM or email me at matzekec@clarkson.edu

Cheers,

Ethan

