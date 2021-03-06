from collections import Counter


def printer_results(results):
    '''
    ### Saída
    Uma execução do programa proposto deve rodar 300 simulações, imprimindo no
    console os dados referentes às execuções. Esperamos encontrar nos dados as
    seguintes informações:

    1 - Quantas partidas terminam portime out (1000 rodadas);

    2 -  Quantos turnos em média demora uma partida;

    3 - Qual a porcentagem de vitórias por comportamento dos jogadores;

    4 -  Qual o comportamento que mais vence.
    '''
    total_timeout = sum([1 for result in results if result["time_out"]])
    total_played = sum([result["played"] for result in results])
    count_winner = Counter()
    for result in results:
        strategy = str(result['strategy'])
        count_winner[strategy] += 1
    
    print(
        f'''Quantas partidas terminam por tempo esgotado(timeout): '''
        f'''{total_timeout}'''
    )
    print(
        f'''Quantos turnos em média demora uma partida: '''
        f'''{total_played / len(results):.1f}'''
    )
    print(
        f'''Qual o comportamento que mais venceu:
        {count_winner.most_common(1)[0][0]}
        venceu: {count_winner.most_common(1)[0][1]}'''
    )
    print("Qual a porcentagem de vitórias por comportamento dos jogadores")
    for strategy, winner in count_winner.most_common():
        print("  *  ", f"{strategy}: {(winner * 100)// len(results)}%")
