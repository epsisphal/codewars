# Pete the baker from CodeWars
import codewars_test as test

def cakes_alexis(recipe, available):
    cakes = 1e6
    for key, value in recipe.items():
        if key not in available:
            cakes = 0 
        else: 
            cakes = min(cakes, int(available.get(key)/value))
    return cakes

def cakes(recipe, available):
    # Answer (with my correction)
	return min(int(available.get(k, 0)/recipe[k]) for k in recipe)

@test.it('Testing Pete, the Baker')
def _():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    test.assert_equals(cakes(recipe, available), 2, 'example #1')

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    test.assert_equals(cakes(recipe, available), 0, 'example #2')

