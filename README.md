This branch was created to keep track of my CS325, Operating Systems, Project 2. This is the second project in a series that we will build off of to create a web scrapper.

# Purpose:

   The purpose of this project is to create a program in python that reads urls from a file, pulls the reviews from the cite and then writes them to their own seperate files.

# Recreation:

   In order to recreate the environment that I used for this project; you will need to do the following steps. 
   **Disclaimer: ** These instructions are for a Windows machine, for Mac or Linux the steps may be different.

## Steps:
   1. Next you will need to install [conda](https://docs.anaconda.com/miniconda/miniconda-install/) on your local machine 
      - I have provided a link for anaconda, and you will follow the instructions on their to install it based on your machine specifications
   2. You will next need to open up Visual Studio Code, or another editor with a terminal, and then pull up the terminal.
   3. Then you will create a new folder in VS Code
   4. Next, you will paste: 
   ```
      git clone https://github.com/peachyem/Cs325Project1.git
   ```

   - This will clone the repository to your local machine
   5. Nagivate to the webScrapping Branch inside VSCode
   ```
      git checkout webScrapping 
   ```
   6. Now we will set up conda in order to run the program. First, type in conda in the terminal
   7. Them import the conda environment into your space.
   ```
      --name my_yaml_env --file requirement.yaml
   ```
   - my_yaml_env can be named anythin you prefer for your environment
   - this installs all specific packages tha I used for this project
   8. Finally, enter your newly created environment!
   ```
      conda activate my_yaml_env
   ```
   - This may pop up an error that says you must first run conda init, so type conda init and then retry
   - If it still does not work, try switching what terminal you are using, command prompt seemed to reliably work for me
   9. Finally, you will click into webScrapping2.py and hit run. You should then see all reviews in each text response file