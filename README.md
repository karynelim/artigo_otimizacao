### Otimização Contínua e Combinatória - 2025.1
### Artigo final da disciplína
#### Aluna: Karyne Lima Pessoa

#### Descrição do Problema

Deseja-se otimizar a alocação de tarefas em uma sprint backlog, maximizando o benefício gerado por essa alocação. Cada tarefa possui uma prioridade (1, 2 ou 3) atribuída pelo Product Owner. Cada membro da equipe tem uma escala de proficiência (0 a 3) para aquela atividade, baseada em sua experiência na atividade desempenhada:

- 0: até 1 ano de experiência;
- 1: de 1 a 2 anos de experiência;
- 3: acima de 2 anos de experiência.

O problema está sujeito às seguintes restrições:
1. Cada tarefa deve ser alocada a apenas um membro da equipe.
2. O tempo total de tarefas atribuídas a um membro não pode exceder sua carga horária disponível na sprint.
3. As variáveis de decisão são binárias (0 ou 1)

#### Dados utilizados:

**Cenário 1 — Sprint Prioridade Alta com Diversidade de Tarefas**

3 membros com 40h disponíveis cada.

15 tarefas com diferentes prioridades e tempos.

**Cenário 2 — Equipe Heterogênea em Conhecimento e Experiência**

5 membros com cargas horárias de 30h a 40h.

20 tarefas com tempos de execução de 2h a 8h.

**Cenário 3 — Sprint com Capacidade Limitada de Recursos**

4 membros, mas 2 deles com apenas 20h disponíveis.

12 tarefas com alta prioridade e tempos entre 3h e 7h.

**Cenário 4 — Grande Escala com Alta Complexidade**

10 membros com cargas horárias de 30h a 40h.

50 tarefas com diferentes prioridades (1 a 3) e durações de 2h a 8h.


