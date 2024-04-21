my_favorites = {'lime', 'scarlet', 'turquoise'}

inas_favorites = {input("Enter Ina's favorite: ")}
dans_favorites = {input("Enter Dan's favorite: ")}
mels_favorites = {input("Enter Mel's favorite: ")}

all_favorites = [inas_favorites, dans_favorites, mels_favorites]

for i in range(len(all_favorites)):
    only_my_favorites = my_favorites.symmetric_difference(all_favorites[i])

print(only_my_favorites)
