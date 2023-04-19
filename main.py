from io import BytesIO

import boto3
import pygame

BUCKET_NAME = 'my-bucket'


def selecionar_bucket(index):
    pass


# Cria um cliente do S3 usando o endpoint do LocalStack
s3 = boto3.client('s3', endpoint_url='http://localhost:4566/')

# Lista os buckets existentes
response = s3.list_buckets()
print('Buckets existentes:')
for bucket in response['Buckets']:
    print(f' - {bucket["Name"]}')

# Faça o upload de um arquivo chamado 'my-file.txt' para o bucket criado
with open(file='./assets/my-file.txt', mode='rb') as meu_objeto:
    s3.upload_fileobj(meu_objeto, BUCKET_NAME, 'my-file.txt')

with open(file='./assets/musica.mp3', mode='rb') as f:
    s3.upload_fileobj(f, BUCKET_NAME, 'musica.mp3')

# Liste os objetos armazenados no bucket
response = s3.list_objects_v2(Bucket=BUCKET_NAME)
print(f'Objetos armazenados no bucket {BUCKET_NAME}:')
for objeto in response['Contents']:
    print(f' - {objeto["Key"]}')

# Carregue o arquivo de áudio no Pygame mixer
obj = s3.get_object(Bucket=BUCKET_NAME, Key='musica.mp3')
audio_data = obj['Body'].read()

pygame.init()  # iniciando o módulo pygame
pygame.mixer.music.load(BytesIO(audio_data))  # abre o mixer de música e carrega o arquivo importado
pygame.mixer.music.play() # Reproduzir o arquivo de áudio

# Aguarde até que o arquivo termine de tocar
while pygame.mixer.music.get_busy():
    continue
# for bucket in response['Buckets']:
#     s3.delete_bucket(Bucket=bucket['Name'])
#
# print('Todos os buckets foram excluídos com sucesso.')
