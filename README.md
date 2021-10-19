# Phase 1: Automating QC with DeepSpeech

In the Quality Control(QC) Department at RT Knits Ltd, we have people taking measurements of garments to ensure there are no discrepancies between the actual size of the garment and the desired one. If any aberration, the value is typed in an excel sheet.

After all the pieces(front panel, back panel, side panels,...) of the garments have been cut in the Cutting Department, they are assembled in the Make-Up Department. After being assembled, a group of people need to check if the final product matches the desired measurements given by the client. These QC people uses a tape measure to take the measurements and after each measurement between two points, they enter the value in a specific excel sheet, they then move on to the next measurements and continue as such. 

### Data on Current Procedure

Different clients require different types of measurement to be taken. For the purpose of this project, I collected data on measuring T-Shirts for ASOS. I timed the process and counted the number of T-shirts they need to measure and the number of people required to do so.

| Attempt | #1 | #2 | #3 | #4 | #5 | #6 | #7 | #8 | #9 | #10 | #11 | #12 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Seconds | 301 | 283 | 290 | 286 | 289 | 285 | 287 | 287 | 272 | 276 | 269 | 254 |

## Abstract





## Methods

As a first step, I chose to automate the process of data entry on the excel. Using Natural Language Processing(NLP) - the **DeepSpeech** model, I imagine the QC people to have a headset in which they would talk into and the system would recognise specific keywords, and populate their excel sheet. 

Inside the main() function, a while loop has been used to continuously input measurements. While the user does not say **“stop”**, the program keeps asking for measurements. Each measurement is recorded inside a list called **“values”**. The list holds the measurements for 1 garment at a time. Each measurement should be input in English. The conditions to alter the state of the program (i.e “next”,”stop”) should be input in English. If the user does not say “next” or “stop” when asked for input, the input is treated as a measurement and recorded in the list. If the user says “next” or “stop”, the list is saved to a dictionary by adding it as a definition, with the current garment number being the index. An integer variable “count” has been used to keep track of the garment number (garment number 1, garment number 2, etc...). The variable “count” is incremented. The list “values” is re-initialised to empty. If the user did say “next”, the loop starts again, allowing input of measurements for next garment. If the user said “stop”, the while loop stops executing.

(To be revised...)

## Plan of Action

1. Import Dependencies
2. Setup API for Google Sheet
3. Configuring DeepSpeech

### 1. Import Dependencies

Libraries like ```word2number``` allow conversion of words into numbers that will be inserted into the Google Sheet. ```oauth2client.service_account import ServiceAccountCredentials``` allow setting up an instance on Google Cloud Console.

```
import time, logging
from datetime import datetime
import threading, collections, queue, os, os.path
import deepspeech
from word2number import w2n
import numpy as np
import pyaudio
import wave
import webrtcvad
from halo import Halo
from scipy import signal
from time import sleep
global global_data
global_data=[]
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
```

### 2. Setup API for Google Sheet

 We start by creating a template on Google Sheet as shown below. ```Sample``` are the different garments that will be measured and ```specs``` are the different parts(sleeve, collar, hem,...) that need to be measured.
 
 ![image](https://user-images.githubusercontent.com/59663734/137855649-52dbc6aa-4c1b-4657-9a89-fe5c9460fcf9.png)

We initialize our google sheet with our credentials:

```
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Template1").sheet1

logging.basicConfig(level=20)
```
### 3. Configuring DeepSpeech

DeepSpeech has been trained using machine learning techniques based on Baidu's Deep Speech Research Paper. It is an open-source speech to text engine which uses TensorFlow for easy implementation.




## Testing

## Conclusion

## Improvement
