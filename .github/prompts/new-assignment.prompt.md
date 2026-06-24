---
agent: agent
description: Criar uma nova tarefa de programação
argument-hint: Forneça os detalhes da tarefa
---

# Criar Nova Tarefa de Programação

Seu objetivo é gerar uma nova tarefa para os alunos da Mergington High School.

## Passo 1: Coletar Informações da Tarefa

Se ainda não fornecido pelo usuário, pergunte sobre o que será a tarefa.

## Passo 2: Criar a Estrutura da Tarefa

1. Crie um novo diretório na pasta `assignments` com um nome único baseado no tema da tarefa
1. Crie um novo arquivo no diretório chamado `README.md` com a estrutura do arquivo [assignment-template.md](../../templates/assignment-template.md)
1. Preencha os detalhes da tarefa no arquivo README
1. (Opcional) Adicione código inicial ou anexos se a tarefa precisar — adicione esses arquivos na mesma pasta da tarefa

## Passo 3: Atualizar a Configuração do Site

Atualize a lista de tarefas no arquivo de configuração do site [config.json](../../config.json) para incluir a nova tarefa. Para o campo dueDate, use a data atual mais 7 dias, a menos que especificado de outra forma.