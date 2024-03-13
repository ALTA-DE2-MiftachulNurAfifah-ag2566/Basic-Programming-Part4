def play_with_asterisk(n):
    pattern = ""
    for i in range(n):
    #     for sp in range(n-i-1):
    #         print(" ", end="")
    #     for j in range(i+1):
    #         print("* ", end="")
    #     print()
        # pattern += ' ' * (n-i-1) + '*' * (2 * i + 1) + '\n'
        pattern += ' ' * (n-i-1) + '* ' * (i+1) + '\n'
    return pattern

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
