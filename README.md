# DankBank-myResponderEnhanced_SCDFXIBM
Team Name: Dank Bank

Team Members: Ong Chuan Kai, Davis Zhang, Lim An Guan, Eu Zheng Xi, Sun Jiachen

## Short Description of Solution
### The Problem
The COVID-19 pandemic has turned our lives upside down. It has ushered us into a new era of remote learning and working from home. As Singaporeans spend more time in residential neighbourhoods, more incidents of medical emergencies will occur at homes as well. Our team thus believes that community responders will play an even more crucial role when it comes to saving lives. 

### The Solution
Our solution, myResponderEnhanced, improves the speed and consistency with which community first responders react to a life-threatening situation. MyResponderEnhanced builds on the current mobile application. Our new main feature is an artificial intelligent chatbot, which aids responders to take matters into their own hands and save precious seconds in a life-or-death situation.

### The Story
John, a community first responder, sees an elderly man shaking uncontrollably at the void deck. Like most community responders who are not medically trained,   John has no idea what the elderly man is suffering. All he can do is call 995 and hope that the paramedics will arrive in time and save the man’s life. 

myResponderEnhanced will do all the work for John. John only needs to open the app and inform the chatbot that there is an emergency. It will automatically inform SCDF to dispatch paramedics ASAP. By gathering information about the elderly man from John (e.g. age group, approximate height & weight and visible symptoms), the chatbot can accurately determine the medical emergency. If information is insufficient, and the machine learning model behind cannot narrow down, the chatbot can prompt John to check if other common symptoms are shown. 

Hence, John can focus on helping the elderly man to the best of his ability. The chatbot will have treatment options available and guide him step-by-step. To save time, John can converse with the chatbot and does not need to type using IBM’s Text-to-Speech. Furthermore, MyResponderEnhanced will notify nearby community responders to deliver crucial medical supplies, like AED, bandages or ice packs, to John. If said supplies are in John’s immediate vicinity, the app will direct John to the exact location. 

Behind the scenes, the chatbot will be relaying important information to the SCDF paramedics, allowing them to better prepare when they arrive at the scene.

## Pitch Video
<a href="http://www.youtube.com/watch?feature=player_embedded&v=vGj9X7jJNYE
" target="_blank"><img src="http://img.youtube.com/vi/vGj9X7jJNYE/0.jpg" 
alt="DankBankPitchVideo" width="720" height="540" border="10" /></a>

## Architecture
![Architecture Diagram](https://github.com/jiachenofsun/DankBank-myResponderEnhanced_SCDFXIBM/blob/main/architecture_diagram.jpg?raw=true)

## Detailed Solution
[Read More](https://docs.google.com/document/d/1A05Hdzwarb6KRHziTSzoAXsjwmgOxC-gNJo1I-aXs6c/edit?usp=sharing)

## Getting Started
### How to use our Python script
The following set of instructions covers how to execute the python file we have created, which is meant as a mockup of how Speech to Text will integrate with IBM Watson's AutoAI models.
#### How the program works
  1. The program accepts an .mp3 file, that is meant to simulate someone speaking into their mobile device's microphone and describing the symptoms they see (up to 4). The symptoms are separated by the word 'and' so the program can differentiate different symptoms.
  2. The script will open the .mp3 file and translate it to text using Watson Speech to Text, and store the symptoms in a list variable.
  3. The symptoms are then inserted into the AUTOAI and a prediction of the injury is displayed in .json format on the console.
#### Required software
  Python  
  Javascript  
  HTML  
  CSS
#### How to run a demo
  1. Open the terminal on your operating system
  2. Clone our repository by entering the following command: `git clone https://github.com/jiachenofsun/DankBank-myResponderEnhanced_SCDFXIBM.git`
  3. Navigate to the working directory by entering the following commands: `cd DankBank-myResponderEnhanced_SCDFXIBM` followed by `cd stt-and-ai-demo`
  4. Install the required modules by entering the following command: `pip install ibm_watson`
  5. Run the script by entering the following command: `python main.py`


### How to use our chatbot 
The following set of instructions covers the steps to effectively utilise the functions of the chatbot. The chatbot can be accessed within our web-app UI mockup (link found below). It is found at the bottom right corner of the interface.

1. Upon clicking onto the chatbot, users will be prompted to select one of the services offered by the chatbot. 
To select diagnosis, users will need to enter “diagnosis”
To select medical resources, users will need to enter “medical resources”
To select both diagnosis and medical resources, users will need to enter “both”
To make another selection, users will need to enter “restart”

2. Should users request for a diagnosis, they will be prompted to submit the symptoms they observed. A maximum of 4 symptoms can be submitted to the chatbot. If the user is unable to provide 4 symptoms, he / she can simply reply “no” to the request for more symptoms. Subsequently, a diagnosis will be made based on the symptoms submitted. To request for another diagnosis / medical resource, users need to input “restart”

3. Should users request for medical resources, they will be prompted to input the kind of resources they require, eg:bandage. Users will then be presented with a map showing the different locations they are able to get these resources. To request for another diagnosis / medical resource, users need to input “restart”

4. Should users request for both diagnosis and medical resources, they will be directed to make a diagnosis first. Thereafter, based on the diagnosis made, users will receive a map showing the different locations to get the resources to address the diagnosis that has been made. Similarly, to request for another diagnosis / medical resource, users need to input “restart”. 

  
## Our proposed solution's UI Mockup
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
