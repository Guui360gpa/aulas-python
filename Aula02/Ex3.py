def linha_horizontal():
    print('+----+----+')


def linha_vertical():
    print('|    |    |')


def desenha_grid():
    linha_horizontal()
    for _ in range(4):
        linha_vertical()
    linha_horizontal()
    for _ in range(4):
        linha_vertical()
    linha_horizontal()


desenha_grid()