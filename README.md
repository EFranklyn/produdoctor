
# produdoctor
Price products and suppliers

# Projeto de Gerenciamento de Fornecedores e Produtos

## Introdução

Este é um projeto de exemplo de um sistema de gerenciamento de fornecedores e produtos desenvolvido em Django. O sistema permite o registro de fornecedores e produtos, 
bem como a associação de produtos a fornecedores. É uma base sólida para desenvolver um sistema mais completo, expandindo funcionalidades e personalizando-o de acordo com suas necessidades específicas.
Detalhe: a arquitetura deste projeto foi projetada para um facil versionamento e desacoplamento caso seja necessário, tendo uma divisão de rotas por versão e por app, podendo assim gerar uma nova versão de api com
facilidade e tranquilidade.
Para isso foi criada a estrutura de API Collection, nela fica localizada a business do projeto(serializers, views e tests tambem podem ficar), por ser subdividida em versões isso pode facilitar o desacoplamennto e faciltar 
a geração de novas versões.

## Pré-requisitos

Antes de iniciar o projeto, certifique-se de ter as seguintes dependências instaladas:

- Python (versão recomendada: 3.x)
- Django (versão recomendada: 3.x)
- Virtualenv (opcional, mas recomendado para ambientes virtuais)

## Inicialização do Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local:

1. Clone este repositório:
   git clone [https://github.com/seurepositorio/nome-do-projeto.git](https://github.com/EFranklyn/produdoctor.git)https://github.com/EFranklyn/produdoctor.git

2. python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

3. pip install -r requirements.txt

4. python manage.py runserver


endpoints
  - api/v1/suppliers/
  - api/v1/categories/
  - api/v1/products/
  - api/v1/products-catalog/
