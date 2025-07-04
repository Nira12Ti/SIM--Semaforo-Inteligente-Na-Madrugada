# Semáforo Inteligente na Madrugada 🚦

Este projeto simula um sistema de semáforo inteligente para funcionamento durante a madrugada, com foco em segurança e eficiência. O objetivo é adaptar o comportamento do semáforo conforme a presença de veículos, condições climáticas e possíveis situações de risco, tornando o trânsito mais seguro e fluido em horários de baixo movimento.

## Funcionalidades

- **Detecção de veículos:** O semáforo identifica a aproximação de carros.
- **Reconhecimento de motorista mulher:** Para reforço de segurança em situações específicas.
- **Detecção de movimento suspeito:** Aumenta a atenção do sistema em caso de risco.
- **Sensor de chuva:** Aciona refletores para melhor visibilidade em caso de chuva.
- **Modo inteligente:** Ativado automaticamente entre 00h e 06h.
- **Logs informativos:** Todas as decisões e leituras dos sensores são exibidas no console.

## Como funciona

Durante a madrugada, o sistema:
- Mantém o semáforo aberto (verde) caso detecte veículos ou situações suspeitas.
- Aciona refletores em caso de chuva.
- Exibe mensagens informativas sobre cada decisão tomada.

Fora do horário da madrugada, o semáforo opera no modo tradicional.

## Como executar

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/semaforo-inteligente-madrugada.git
   cd semaforo-inteligente-madrugada
   ```

2. **Execute o script principal:**
   ```bash
   python semaforo-inteligente.py
   ```

3. **Para interromper a simulação:**  
   Pressione `Ctrl+C` no terminal.

## Estrutura do código

- **Sensores:** Cada sensor é uma classe independente, facilitando manutenção e expansão.
- **Semáforo:** Classe responsável pelo estado e mudança de status do semáforo.
- **Controlador:** Função principal que integra sensores e lógica de decisão.

## Sugestões de melhorias

- Implementar interface gráfica para visualização em tempo real.
- Integrar sensores reais (hardware) via GPIO ou APIs.
- Adicionar testes unitários.
- Tornar parâmetros configuráveis via arquivo externo.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por [Nira Santos](https://github.com/Nira12Ti)
