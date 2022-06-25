if __name__ == "__main__":
    seed = 3697


    def random():
        global seed
        sqr = str(seed ** 2)
        while len(sqr) != 8:
            sqr = "0" + sqr
        seed = int(sqr[2:6])
        return seed


    for i in range(0, 25):
        print(random())