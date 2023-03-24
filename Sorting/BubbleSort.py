def BubbleSort(tab):
    for step in range(len(tab)):
        for i in range(0, len(tab)-step-1):
            if (tab[i] > tab[i+1]):
                tab[i], tab[i+1] = tab[i+1], tab[i]

    print(tab)
BubbleSort([1,5,7,8,4,3])