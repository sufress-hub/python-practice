def info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

info(game="Cricket", player="Virat", stadium="Wankhede")