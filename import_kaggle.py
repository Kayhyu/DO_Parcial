import json
import zipfile
import os 
api_token={"username":"kayhyu1","key":"8660ba8d5ae769005919c7d90d5a3e11"} #contenido de archivo kaggle.json

#conectar a kaggle
with open('C:/Users/Jefferson/.kaggle/kaggle.json',"w") as file:
    json.dump(api_token,file)
    
location="D:/Ejercicios_de_python/PROYECTO_PARCIAL/dataset"  

#validar que la carpeta exista
if not os.path.exists(location):
    #si no existe la carpeta dataset entonces la creo
    os.mkdir(location)
else:
    #si la carpeta si existe, entonces voy a borrar su contenido
    for root,dirs, files in os.walk(location, topdown=False):
        for name in file:
            os.remove(os.path.join(root,name))# elimino todos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name))#elimino todas las carpetas             
#descargar dataset de kaggle
#os.system("kaggle datassets download -d henryshan/starbucks -p D:/Ejercicios_de_python/PROYECTO_PARCIAL/dataset")
os.system("kaggle datassets download -d JAKKI SESHAPANPU/Students Performance in Exams -p D:/Ejercicios_de_python/PROYECTO_PARCIAL/dataset")

#descomprimir el archivo de kaggle
os.chdir(location)
for file in os.listdir():
    zip_ref=zipfile.ZipFile(file,"r") #lee el archi .zip
    zip_ref.extractall() #extrae contenido de archivo.zip
    zip_ref	.close() #cierra archivo
