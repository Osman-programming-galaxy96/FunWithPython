def selectionSort(tab):
    for i in range(len(tab)):
        min_idx = i
        for j in range(i +1, len(tab)):
            if tab[j] < tab[min_idx]:
                (tab[j], tab[min_idx]) = (tab[min_idx], tab[j])
                min_idx = j
    return tab

def min_elem(tab):
    min = tab[0]
    for i in range(len(tab)):
        if tab[i] < min:
            min = tab[i]
    return min

# min_elem([2,5,6,7,8])
print(selectionSort([2,5,4,6,7,1,8]))

