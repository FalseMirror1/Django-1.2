from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def calculator(request, recipe):
    amount = int(request.GET.get('amount', 1))
    recipe = DATA.get(recipe).copy()
    for x, y in recipe.items():
        recipe[x] = y * amount

    context = {
        'recipe': recipe,
        'amount': amount
    }

    return render(request, 'calculator/index.html', context)
