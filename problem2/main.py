def draw_xyz(N):
    pattern = ""
    for i in range(N):
        for j in range(N):
            digit = N*i + j + 1
            # print(digit, end=" ")
            if digit % 3 == 0:
                # print("X", end=" ")
                pattern += "X "
            elif digit % 2 == 0:
                # print("Z", end=" ")
                pattern += "Z "
            else:
                # print("Y", end=" ")
                pattern += "Y "
        pattern += "" * N + "\n"
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """