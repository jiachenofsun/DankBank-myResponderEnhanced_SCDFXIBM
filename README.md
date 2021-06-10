# DankBank-myResponderEnhanced_SCDFXIBM
Team Name: Dank Bank

Team Members: Ong Chuan Kai, Davis Zhang, Lim An Guan, Eu Zheng Xi, Sun Jiachen

## Short Description of Solution

## Pitch Video
<a href="http://www.youtube.com/watch?feature=player_embedded&v=vGj9X7jJNYE
" target="_blank"><img src="http://img.youtube.com/vi/vGj9X7jJNYE/0.jpg" 
alt="DankBankPitchVideo" width="240" height="180" border="10" /></a>

## Architecture
![Architecture Diagram](https://github.com/jiachenofsun/DankBank-myResponderEnhanced_SCDFXIBM/blob/main/architecture_diagram.jpg?raw=true)

## Detailed Description of Solution
[Read More](https://docs.google.com/document/d/1A05Hdzwarb6KRHziTSzoAXsjwmgOxC-gNJo1I-aXs6c/edit?usp=sharing)

## Getting Started
This set of instructions will cover how to execute the python file we have created, which is meant as a mockup of how Speech-to-Text will integrate with IBM Watson's AutoAI models.
### How the program works
  1. The program accepts an .mp3 file, that is meant to simulate someone speaking into their mobile device's microphone and describing the symptoms they see (up to 4). The symptoms are separated by the word 'and' so the program can differentiate different symptoms.
  2. The script will open the .mp3 file and translate it to text using Watson Speech to Text, and store the symptoms in a list variable.
  3. The symptoms are then inserted into the AUTOAI and a prediction of the injury is displayed in .json format on the console.
### Required software
  Python
### How to run a demo
  1. Open the terminal on your operating system
  2. Clone our repository by entering the following command: `git clone https://github.com/jiachenofsun/DankBank-myResponderEnhanced_SCDFXIBM.git`
  3. Navigate to the working directory by entering the following commands: `cd DankBank-myResponderEnhanced_SCDFXIBM` followed by `cd stt-and-ai-demo`
  4. Install the required modules by entering the following command: `pip install ibm_watson`
  5. Run the script by entering the following command: `python main.py`


## How to use our chatbot 
The following set of instructions serves to cover the steps to effectively utilise the functions of the chatbot. 

1. Upon clicking onto the chatbot, users will be prompted to select one of the services offered by the chatbot. 
   To select diagnosis, users will need to enter “diagnosis”
   To select medical resources, users will need to enter “medical resources”
   To select both diagnosis and medical resources, users will need to enter “both”
   To make another selection, users will need to enter “restart”

2. Should users request for a diagnosis, they will be prompted to submit the symptoms they observed. A maximum of 4 symptoms can be submitted to the chatbot. If the user is unable to provide 4 symptoms, he / she can simply reply “no” to the request for more symptoms. Subsequently, a diagnosis will be made based on the symptoms submitted. To request for another diagnosis / medical resource, users need to input “restart”

3. Should users request for medical resources, they will be prompted to input the kind of resources they require, eg:bandage. Users will then be presented with a map showing the different locations they are able to get these resources. To request for another diagnosis / medical resource, users need to input “restart”

4. Should users request for both diagnosis and medical resources, they will be directed to make a diagnosis first. Thereafter, based on the diagnosis made, users will receive a map showing the different locations to get the resources to address the diagnosis that has been made. Similarly, to request for another diagnosis / medical resource, users need to input “restart”. 

  
## Link to mockup of UI of our proposed solution
[Webapp UI](https://myresponderenhanced.mybluemix.net/)
[Mobile application UI](https://snack.expo.io/@aderty/myresponder-enhanced)

## Tech Stack
1. IBM Cloud Pak for Data
2. WatsonMachineLearning
3. WatsonStudio
4. Speech to Text
5. Watson Assistant
6. Tone Analyzer
7. Cloud Object Storage
8. Cloud Foundry (Toolchain)
