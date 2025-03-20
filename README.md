# Documentação de Inicialização de Projetos

Este documento descreve como inicializar os projetos utilizando os scripts localizados no diretório `scripts_inicializacao`.

## Estrutura do Diretório

O diretório `scripts_inicializacao` contém os scripts necessários para configurar e inicializar os projetos. Certifique-se de que você tenha as permissões adequadas para executar os scripts.

```
/scripts_inicializacao
├── setup.sh
├── init_project.sh
└── config/
    ├── database_config.json
    └── app_config.json
```

## Pré-requisitos

Antes de executar os scripts, verifique se os seguintes requisitos estão atendidos:

1. **Sistema Operacional**: Linux ou macOS (para Windows, use WSL ou Git Bash).
2. **Dependências**:
   - Bash (v4.0 ou superior)
   - Python (v3.8 ou superior)
   - Node.js (v14 ou superior, se aplicável ao projeto)
3. **Permissões**: Certifique-se de que os scripts possuem permissão de execução:
   ```bash
   chmod +x scripts_inicializacao/*.sh
   ```

## Passo a Passo para Inicialização

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Execute o Script de Configuração**:
   O script `setup.sh` instala as dependências e configura o ambiente:
   ```bash
   ./scripts_inicializacao/setup.sh
   ```

3. **Inicialize o Projeto**:
   O script `init_project.sh` inicializa o projeto com base nas configurações fornecidas:
   ```bash
   ./scripts_inicializacao/init_project.sh
   ```

4. **Verifique o Status**:
   Após a execução, verifique se o projeto foi inicializado corretamente:
   ```bash
   ./scripts_inicializacao/init_project.sh --status
   ```

## Personalização

Os arquivos de configuração no diretório `config/` podem ser ajustados para atender às necessidades específicas do projeto. Por exemplo:

- `database_config.json`: Configurações do banco de dados.
- `app_config.json`: Configurações gerais da aplicação.

Edite os arquivos conforme necessário antes de executar os scripts.

## Solução de Problemas

- **Erro de Permissão**: Certifique-se de que os scripts possuem permissão de execução.
- **Dependências Ausentes**: Instale as dependências listadas nos pré-requisitos.
- **Logs**: Consulte os logs gerados pelos scripts para identificar problemas.

## Contato

Para dúvidas ou suporte, entre em contato com a equipe de desenvolvimento pelo e-mail: `suporte@seuprojeto.com`.
