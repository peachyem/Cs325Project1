This is the repo for my CS325 Project1.
The purpose is to use Phi3 and python to read from a file and get a response.

project notes:
use pip install to install ollama to the env

The follwing instructions are for Windows users
In order to do this project with my specifics you must:

1. Download Ollama from the official Ollama website:https://ollama.com/download
2. use ollama run phi3:mini to open phi3 in the ollama app
    -you can close Ollama after this if you would like
3. open Visual Studio Code
4. Create a GitHub for your project to save versions and save my files to yours
5. Now recreate my conda environment by first opening the terminal in VSCode in the Folder that GitHub is linked to
6. Then initailize conda by just typing conda in the terminal
7. Finally, type: conda create --name my_yaml_env --file requirement.yaml
    -my_yaml_env can be named anything you prefer for your environment
    -this installs all specific packages that I have.
8. Open sender.py and hit run!
    - you should not have responses in the response.txt file
