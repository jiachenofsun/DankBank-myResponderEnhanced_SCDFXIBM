REQUIREMENTS:
ibm_watson module
run the following command on the terminal: 
pip install ibm_watson

HOW IT WORKS: 
- The program accepts an .mp3 file, that is meant to simulate someone speaking into their mobile device's microphone and describing the symptoms they see (up to 4). The symptoms are separated by the word 'and' so the program can differentiate different symptoms.
- The script will open the .mp3 file and translate it to text using Watson Speech to Text, and save it in a variable named 'text'
- Then, a list of symptoms is saved in the variable 'list'
- The symptoms are then inserted into the AUTOAI and a prediction of the injury is displayed in .json format on the console
