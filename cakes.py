def cakes(recipe, available):
    if set(recipe) & set(available) == set(recipe):
        ratios = []
        for ingredient, ammount in recipe.items():
            ratio = int(str(available[ingredient] / ammount).split('.')[0])
            ratios.append(ratio)
        else:
            return min(ratios)
    else:
        return 0
