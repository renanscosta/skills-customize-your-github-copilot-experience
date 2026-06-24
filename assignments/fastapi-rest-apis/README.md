# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Construir uma API REST usando FastAPI para praticar modelagem de dados, validação com Pydantic e criação de endpoints CRUD.

## 📝 Tasks

### 🛠️ Build Basic CRUD Endpoints

#### Description
Implemente uma API para gerenciar uma lista de produtos em memória. Sua API deve permitir criar, listar, buscar por ID, atualizar e remover produtos.

#### Requirements
Completed program should:

- Criar um app FastAPI executável com Uvicorn
- Definir um modelo `Product` com `id`, `name`, `price` e `in_stock`
- Implementar os endpoints: `POST /products`, `GET /products`, `GET /products/{product_id}`, `PUT /products/{product_id}` e `DELETE /products/{product_id}`
- Retornar códigos HTTP adequados (`201`, `200`, `404`)


### 🛠️ Add Validation and Improve API Experience

#### Description
Melhore a API adicionando validações de entrada e uma rota de saúde para facilitar testes e depuração.

#### Requirements
Completed program should:

- Validar que `price` seja maior que zero
- Validar que `name` tenha no mínimo 3 caracteres
- Retornar mensagens de erro claras para itens não encontrados
- Implementar `GET /health` retornando `{ "status": "ok" }`
- Testar os endpoints usando `/docs` (Swagger UI) gerado automaticamente pelo FastAPI
