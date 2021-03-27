#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importação de bibliotecas necessárias
from pytube import YouTube
import moviepy.editor as mp
import re
import os


# In[ ]:


#Insira o link do vídeo que você quer o mp3 e o diretório que o arquivo será salvo
link = input("Digite o link do vídeo que deseja baixar:  ")
path = input("Digite o diretório que deseja salvar o vídeo:  ")
yt = YouTube(link)

#Iniciar o Download do arquivo
print("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download concluído!")

#Converter mp4 para mp3
print("Convertendo arquivo...")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
print('==> Sucesso!')

