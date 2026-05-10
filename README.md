## Automação RPA de Cadastro ERP com Servidor Integrado

Este projeto é uma automação de Processos Robóticos (RPA) desenvolvida em Python para simular o fluxo de trabalho em um sistema ERP. O diferencial desta solução é a capacidade de gerenciar seu próprio ambiente de execução, iniciando e finalizando o servidor web automaticamente.

## Diferenciais do Projeto

- **Servidor Auto-Gerenciado:** O script utiliza a biblioteca `subprocess` para iniciar um servidor HTTP local na porta 8000, eliminando a necessidade de configuração manual do ambiente de teste.
- **Arquitetura Resiliente (Try/Finally):** Implementação de blocos de tratamento que garantem o encerramento seguro de processos e a liberação de portas de rede, mesmo em caso de erro crítico na automação.
- **Navegação Dinâmica:** O robô utiliza atalhos de sistema (`Ctrl + L`, `TAB`) em vez de coordenadas fixas, garantindo compatibilidade com diferentes resoluções de monitor.

## Tecnologias Utilizadas

- **Python 3.x**
- **PyAutoGUI:** Automação de interface (teclado e mouse).
- **Pandas:** Manipulação da base de dados (CSV).
- **Subprocess & OS:** Gerenciamento de infraestrutura e caminhos de sistema.
- **HTML/CSS:** Sistema ERP simulado para testes.

## Como Executar

### 1. Clonar o Repositório
```bash
git clone [https://github.com/seu-usuario/rpa_cadastro_no_sistema.git](https://github.com/seu-usuario/rpa_cadastro_no_sistema.git)
cd rpa_cadastro_no_sistema
