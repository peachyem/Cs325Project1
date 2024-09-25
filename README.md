This repository was created to keep track of my CS325, Operating Systems, Project 1. This is the first project in a series that we will build off of to create a web scrapper.

Purpose:

   - The purpose of this project is to create a program in python that prompts a small language model, phi-3, running on my local machine and prompt it with a query. In order to prompt phi-3, the program must be able to read from and file and then pass that data to the running model. Then, I am to store the responses from phi-3 in a separate file. 	

Recreation:

	- In order to recreate the environment that I used for this project; you will need to do the following steps. **Disclaimer: These instructions are for a Windows machine, for Mac or Linux the steps may be different.
1.	Go to https://ollama.com/ and download the latest version of Ollama.
2.	Once Ollama is downloaded, type ollama run phi3:mini and hit enter
-	This downloads an instance of phi3 mini, the smallest version of phi3 on your local machine to use
3.	Next you will need to install conda on your local machine https://docs.anaconda.com/miniconda/miniconda-install/
-	I have provided a link for anaconda, and you will follow the instructions on their to install it based on your machine specifications
4.	You will next need to open up Visual Studio Code, or another editor with a terminal, and then pull up the terminal. 
5.	Then you will create a new folder in VS Code.
6.	Next, you will paste: git clone https://github.com/peachyem/Cs325Project1.git
-	This will clone the repository to your local machine.
7.	Now we will set up conda in order to run the program. First, type in conda in the terminal
8.	Then type: conda create --name my_yaml_env --file requirement.yaml
-	my_yaml_env can be named anything you prefer for your environment
-	this installs all specific packages that I have.
9.	The next step is to then go into the environment you have just recreated by typing conda activate my_yaml_env 
-	This may pop up an error that says you must first run conda init, so type conda init and then retry
-	If it still does not work, try switching what terminal you are using, command prompt seemed to reliably work for me
10.	Finally, you will click into sender.py and hit run. You should then see phi3’s responses in the responses.txt file
	
