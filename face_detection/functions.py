#code to save pictures and save it.
import cv2
import os
import imutils
import shutil
import numpy as np
def make_db():
    #making the dir to save all data 
    DataBasePath = place = os.getcwd() + '/db'
    if not os.path.exists(DataBasePath):
        print('Carpeta para base de datos creada: ',DataBasePath)
        os.makedirs(DataBasePath)
    return DataBasePath

def make_pdb(DataBasePath,personName):
    personPath = DataBasePath + '/' + personName
    if not os.path.exists(personPath):
        print('base de datos personal creada: ',personPath)
        os.makedirs(personPath)
    return personPath

def make_sample(personPath):
    #making the personal database in the folder
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture('Video.mp4')
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0
    while True:   
        ret, frame = cap.read()
        if ret == False: break
        frame =  imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,'{}'.format(count),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
            count = count + 1
            cv2.imshow('frame',frame)
        k =  cv2.waitKey(1)
        if count >= 1000:
            break
        elif k == 99:
            shutil.rmtree(personPath)
            print("Operation Canceled")
            
    cap.release()
    cv2.destroyAllWindows()
    #os.exit()
    #print("500 pics where chapter as sample")
    
def make_name():
    name = input("Give me the name to register: ").lower().capitalize()
    last_name = input("Give me the last name to register: ").lower().capitalize()
    personName = name +"_" + last_name
    return personName

def train(DataBasePath,personPath):
    #Cambia a la ruta donde hayas almacenado Data
    peopleList = os.listdir(DataBasePath)#.remove(".ipynb_checkpoints")
    print('Lista de personas: ', peopleList)
    labels = []
    facesData = []
    label = 0
    for nameDir in peopleList:
        personPath = DataBasePath + '/' + nameDir
        print(f'Leyendo las imágenes of {nameDir}')
        for fileName in os.listdir(personPath):
            #print('Rostros: ', nameDir + '/' + fileName)
            labels.append(label)
            facesData.append(cv2.imread(personPath+'/'+fileName,0))
            #image = cv2.imread(personPath+'/'+fileName,0)
            #cv2.imshow('image',image)
            #cv2.waitKey(10)
        label = label + 1
        print(f'Amount labeled: {label}')
   
    return labels,facesData
    #print('labels= ',labels)
    #print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))
    #print('Número de etiquetas 1: ',np.count_nonzero(np.array(labels)==1))