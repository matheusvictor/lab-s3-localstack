from io import BytesIO

import boto3
import pygame
from PIL import Image

BUCKET_NAME = 'my-bucket'


def criar_client_s3():
    s3 = boto3.client('s3',
                      endpoint_url='http://localhost:4566/')  # Cria um cliente do S3 usando o endpoint do LocalStack
    return s3


def listar_buckets(s3_client):
    response = s3_client.list_buckets()
    if response['Buckets']:
        print('Buckets existentes:')
        for numero, bucket in enumerate(response['Buckets']):
            print(f' {numero} - {bucket["Name"]}')
        return response
    else:
        print('Não há Buckets!')


def selecionar_bucket(index):
    pass


def excluir_todos_buckets(s3_client):
    response = s3_client.list_buckets()
    for bucket in response['Buckets']:
        s3_client.delete_bucket(Bucket=bucket['Name'])
    print('Todos os buckets foram excluídos com sucesso.')


def listar_objetos_bucket(s3_client):
    response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
    print(f'Objetos armazenados no bucket {BUCKET_NAME}:')
    for objeto in response['Contents']:
        print(f' - {objeto["Key"]}')


def fazer_upload_objeto(s3_client, diretorio='./assets/my-file.txt', nome='my-file.txt'):
    with open(file=diretorio, mode='rb') as obj:  # Upload de um arquivo para o bucket criado
        s3_client.upload_fileobj(obj, BUCKET_NAME, nome)


def executar_obj_audio(s3_client):
    obj = s3_client.get_object(Bucket=BUCKET_NAME, Key='audio.mp3')  # Carrega o arquivo de áudio no Pygame mixer
    audio_data = obj['Body'].read()

    pygame.init()  # Inicia o módulo pygame
    pygame.mixer.music.load(BytesIO(audio_data))  # Abre o mixer de música e carrega o arquivo importado
    pygame.mixer.music.play()  # Reproduz o arquivo de áudio

    while pygame.mixer.music.get_busy():  # Aguarda até que o arquivo de áudio termine de tocar
        continue
    print('Execução do arquivo de áudio finalizada! :)')


def abrir_obj_imagem(s3_client, diretorio):
    with open(file=diretorio, mode='rb') as f:  # Abre a imagem em modo de leitura
        imagem = Image.open(f)  # Cria um objeto Image

        # Exibe informações da imagem
        print(f"Formato: {imagem.format}")
        print(f"Modo: {imagem.mode}")
        print(f"Tamanho: {imagem.size}")

        imagem.show()  # Exibe a imagem
