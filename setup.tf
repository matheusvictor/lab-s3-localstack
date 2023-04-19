# Definição do provedor que será utilizado, neste caso, o AWS.
provider "aws" {
  access_key        = "foo"
  secret_key        = "bar"
  region            = "us-east-1" # Definição da região em que o bucket S3 será criado.
  s3_use_path_style = true # Define que o caminho de acesso do S3 será usado ao invés do subdomíni
  #   skip_metadata_api_check     = true
  #   skip_requesting_account_id  = true

  # Define os endpoints da API do AWS. Neste caso, apenas o endpoint S3 está definido.
  endpoints {
    s3 = "http://localhost:4566" # Define o endpoint local do serviço S3 da AWS que está sendo executado no LocalStack
  }
}

# Define que o recurso a ser criado é um Bucket S3. O nome "example" identifica o recurso no Terraform
resource "aws_s3_bucket" "example" {
  bucket = "my-bucket" # "my-bucket" é o nome dado ao Bucket em si
  acl    = "private" # Define as permissões de acesso

  # Define as tags associadas ao bucket, que são pares de chave-valor. Isso ajuda a identificar e gerenciar recursos na AWS.
  tags = {
    Name        = "My bucket"
    Environment = "Dev" # Tag para sinalizar o ambiente em que o bucket está sendo criado.
  }
}
