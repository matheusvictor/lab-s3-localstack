from utils import *

s3 = criar_client_s3()  # Obtém a "instância" do S3
listar_buckets(s3)  # Lista os buckets existentes

fazer_upload_objeto(s3)
fazer_upload_objeto(s3, './assets/musica.mp3', 'musica.mp3')

listar_objetos_bucket(s3)

opc = input('Executar áudio?: ').lower()
if 's' in opc:
    executar_obj_audio(s3)

fazer_upload_objeto(s3, './assets/ciandt.png', 'ciandt.png')
listar_objetos_bucket(s3)

opc = input('Exibir imagem?: ').lower()
if 's' in opc:
    abrir_obj_imagem(s3, './assets/ciandt.png')
