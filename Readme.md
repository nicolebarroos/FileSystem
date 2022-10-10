# Sistema gerenciador de arquivos

Este documento tem como objetivo detalhar a construção do projeto gerenciador de arquivos.

## Avaliação do escopo
Baseado no cenário detalhado no escopo, julguei necessário arquitetar um projeto Python, utilizando seu framework Django, 
primeiramente contendo modelos representados pelas entidades: FileSystem e Files, onde os diretórios poderão conter sub-diretórios e arquivos

Optei por utilizar relação recursiva na tabela FileSystem, tendo em vista que um diretório pode conter outros diretórios e arquivos. E por armazenar dados no PostgreSQL.

Optei por persistir o conteúdo dos arquivos em um bucket no S3 da AWS,

## Diagramação

![Alt text](Diagrama_file_system.png?raw=true)
