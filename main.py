from random import randint

eu = ''
peu = 0
pcpu = 0
rodada = 1

while eu != 'a':
    try:
        opt = ['a', 'pedra', 'papel', 'tesoura']

        print('Pedra, Papel, Tesoura')
        print('Escolha [1]Pedra - [2]Papel - [3]Tesoura - [0] para Sair')
        print('Placar Eu {} x CPU {}'.format(peu, pcpu))
        print('Rodada {}'.format(rodada))

        eu = opt[int(input('Digite a Opção: '))]
        cpu = opt[randint(1, 3)]
        rodada += 1
        print('=' * 50)
        if eu == opt[1] and cpu == opt[1] or eu == opt[2] and  \
                        cpu == opt[2] or eu == opt[3] and cpu == opt[3]:
            print('EU: {} - CPU: {} : Empate'.format(eu, cpu))

        elif eu == opt[1] and cpu == opt[2] or eu == opt[2] and  \
                        cpu == opt[3] or eu == opt[3] and cpu == opt[1]:
            print('EU {} - CPU: {} : Perdi'.format(eu, cpu))
            pcpu += 1

        elif eu == opt[2] and cpu == opt[1] or eu == opt[3] and  \
                          cpu == opt[2] or eu == opt[1] and cpu == opt[3]:
            print('EU {} - CPU: {} : Ganhei'.format(eu, cpu))
            peu += 1

    except IndexError:
        print('='*50)
        print('xxxxxx  VALOR INVALIDO  xxxxxxxx')
    except ValueError:
        print('='*50)
        print('xxxxxx  VALOR INVALIDO xxxxxxx')

    finally:
        print('=' * 50)
print('Saiu do Jogo !')
print('Rodadas: {}'.format(rodada))
print('Resultado Final: Eu {} X CPU {}'.format(peu, pcpu))
if peu > pcpu:
    print('Você Venceu, Parabéns')
elif peu == pcpu:
    print('Empatou !')
else:
    print('Você Perdeu , Mais sorte na proxima!')
