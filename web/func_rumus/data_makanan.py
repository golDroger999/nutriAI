import spoonacular as sp
api = sp.API("2f48334627dc4111a06a4becc168aaf8")
response = api.search_recipes_complex('steak')
data = response
print(data.json())