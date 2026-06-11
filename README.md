# Nome do Jogo

Labirinto do tempo 

## Integrantes do grupo

- Enzo Carneiro Dias
- Gabriel Tavares Pandino
- Andre Luiz Pinheiro Lopes
- Daniel Carneiro

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo
O jogador está preso em labirintos de diferentes épocas e precisa coletar cristais do tempo para liberar o portal de saída. Cada fase apresenta desafios simples de exploração, incentivando o raciocínio lógico e a tomada de decisões. Conforme avança, o jogador visita cenários inspirados em diferentes períodos históricos, encontrando novos caminhos e obstáculos. Com mecânicas acessíveis e progressão gradual, o jogo foi desenvolvido para proporcionar uma experiência divertida e adequada para iniciantes em programação.

## Objetivo do jogador

O jogador está preso em labirintos de diferentes épocas e precisa coletar cristais do tempo para liberar o portal de saída.

## Regras do jogo

* O jogador se move pelo labirinto usando as setas.
* Deve coletar todos os cristais da fase.
* Depois de coletar os cristais, o portal é liberado.
* Se encostar em inimigos, perde vida.
* Se o tempo acabar, perde.
* Se chegar ao portal, passa de fase.

## Controles

## Controles
- **Seta para cima:** mover para cima
- **Seta para baixo:** mover para baixo
- **Seta para esquerda:** mover para esquerda
- **Seta para direita:** mover para direita
- **ESC:** sair do jogo

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
