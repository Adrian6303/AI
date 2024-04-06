from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from array import array
import os
from PIL import Image
import sys
import time
'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = 'd5acc9c7579e4d07ba7cfe36ca63873b'
endpoint = 'https://adrianai.cognitiveservices.azure.com/'
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

#img = open("test1.png", "rb")
img = open("test2.jpeg", "rb")
read_response = computervision_client.read_in_stream(
    image=img,
    mode="Printed",
    raw=True
)
# print(read_response.as_dict())

operation_id = read_response.headers['Operation-Location'].split('/')[-1]
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line
result = []
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            result.append(line.text)

print()

# get/define the ground truth

#groundTruth = ["Google Cloud", "Platform"]
groundTruth = ["Succes in rezolvarea", "tEMELOR la", "LABORAtoarele de", "Inteligenta Artificiala!"]

# compute the performance
noOfCorrectLines = sum(i == j for i, j in zip(result, groundTruth))
print("Linii corecte: ",noOfCorrectLines,"\n")



#Rezolvare

#1
#a
import Levenshtein


levenshtein_char_distance = Levenshtein.distance(result, groundTruth)
print("Levenshtein Character Distance:", levenshtein_char_distance)


words_recognized =' '.join(result).split() 
words_real = ' '.join(groundTruth).split()
levenshtein_word_distance = Levenshtein.distance(words_recognized, words_real)
print("Levenshtein Word Distance:", levenshtein_word_distance)


#b
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_recognition_quality(text_recognized, text_expected):
    levenshtein_dist = Levenshtein.distance(text_recognized, text_expected)
    cosine_sim = cosine_similarity([text_recognized], [text_expected])[0][0]
    return levenshtein_dist, cosine_sim

# Testare
text_recunoscut = result
text_asteptat = groundTruth
#distanta, similaritate_cosinus = evaluate_recognition_quality(text_recunoscut, text_asteptat)
#print("Distanța Levenshtein:", distanta)
#print("Similaritatea cosinusului:", similaritate_cosinus)

#2
import cv2
import easyocr


image = cv2.imread('test2.jpeg')
image2 = cv2.imread('test2.jpeg')

reader = easyocr.Reader(['en'])

result = reader.readtext(image)

detected_boxes=[]

#test1.png
#box_asteptata = [169, 38, 427, 153]   

#test2.png
box_asteptata = [63,285,1454,1341]

for detection in result:
    top_left = detection[0][0]
    bottom_right = detection[0][2]
    detected_boxes.append(top_left)
    detected_boxes.append(bottom_right)
    image = cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    image2 = cv2.rectangle(image2, [box_asteptata[0],box_asteptata[1]], [box_asteptata[2],box_asteptata[3]], (0, 255, 0), 2)


#Afișre imagini
img = cv2.resize(image, (500,500))
img2 = cv2.resize(image2, (500,500))
cv2.imshow('Text Detection', img)
cv2.imshow('Text Detection Real', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


def compute_IOU(boxA, boxB):
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou

# Testare
min_x = min(pair[0] for pair in detected_boxes)
max_x = max(pair[0] for pair in detected_boxes)
min_y = min(pair[1] for pair in detected_boxes)
max_y = max(pair[1] for pair in detected_boxes)
xy_top_left = [min_x, min_y]
xy_bottom_right =[max_x, max_y]
box_detectata = [xy_top_left[0],xy_top_left[1],xy_bottom_right[0],xy_bottom_right[1]]
print(box_detectata)
print(box_asteptata)
#test1.png
#box_asteptata = [169, 38, 427, 153]   

#test2.png
box_asteptata = [63,285,1454,1341]
iou = compute_IOU(box_detectata, box_asteptata)
print("Suprapunere IOU:", iou)


#3

# Pentru îmbunătățirea recunoașterii textului, se pot utiliza diverse tehnici de preprocesare a imaginilor, cum ar fi filtrarea Gaussiană, corectarea gamma, ajustarea contrastului, etc.
# Se pot ajusta parametrii algoritmului OCR sau să utilizezi alte modele de recunoaștere a textului disponibile.
# Antrenarea unui model propriu de recunoaștere a textului pe datele dvs. poate îmbunătăți performanța, în special dacă ai un set de date specific pentru aplicația dvs.