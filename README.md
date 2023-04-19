### Executar definições do Terraform:

> `terraform init` 

> `terraform apply` 

### Executar LocalStack:

> sudo localstack run

### Listar Bucktes criados:

> aws --endpoint-url=http://localhost:4566 s3api list-buckets

### Listar objetos do Bucket

> aws --endpoint-url=http://localhost:4566 s3api list-objects --bucket my-bucket

### Remover um bucket 

>  aws --endpoint-url=http://localhost:4566 s3 rb s3://my-bucket

>  aws --endpoint-url=http://localhost:4566 s3 rb s3://my-bucket --force