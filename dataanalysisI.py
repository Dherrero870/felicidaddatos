import pandas
pokedex = pandas.readjson("https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json")
print (pokedex)