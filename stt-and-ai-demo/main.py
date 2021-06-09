
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import requests

# Speech-to-text API Key
apikey = 'qDWeKTmkraBi9GorMyQjOblOmUdEMoFtYj4GMIuxoHGB'
url = 'https://api.jp-tok.speech-to-text.watson.cloud.ibm.com/instances/740f059c-01eb-4d2c-b15a-051aaa7a53d5'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

with open('test.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()

# storing output in a string and stripping whitespaces
text = res['results'][0]['alternatives'][0]['transcript']
text.strip()

# storing each symptom separately in a list and stripping whitespaces
list = text.split('and')
for i in range(len(list)):
    list[i] = list[i].strip()
    list[i] = list[i].capitalize()

while len(list) <= 3:
    list.append('')

print(list)

# Inputting the list of symptoms into AUTOAI

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "jU2e_goVC4S_xu9hLuFjOk9nX92Umavo2zsF2cTmLlFF"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ['Symptom 1', 'Symptom 2', 'Symptom 3', 'Symptom 4'], "values": [[list[0], list[1], list[2], list[3]]]}]}

response_scoring = requests.post('https://jp-tok.ml.cloud.ibm.com/ml/v4/deployments/51538342-77fa-4abe-855b-949296bd2f60/predictions?version=2021-06-07', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response: ")
print(response_scoring.json())