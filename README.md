# DankBank-myResponderEnhanced_SCDFXIBM
Team Name: Dank Bank
Team Members: Ong Chuan Kai, Davis Zhang, Lim An Guan, Eu Zheng Xi, Sun Jiachen

## Short Description of Solution

## Pitch Video
<embed pitch video here>

## Architecture
<embed jpg of architecture here>

## Detailed Description of Solution
<insert link to google doc here>

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
  2. Clone our repository by entering the following command: git clone <inserturl>
  3. Navigate to the working directory by entering the following command: cd <...>
  4. Run the following command: pip install ibm-watson
  5. Run the following command: python main.py
  
## Link to mockup of UI of our proposed solution
<insert link to website here>

## Tech Stack
1. IBM Cloud Pak for Data
2. WatsonMachineLearning
3. WatsonStudio
4. Speech to Text
5. Watson Assistant
6. Tone Analyzer
7. Cloud Object Storage
8. Cloud Foundry (Toolchain)
