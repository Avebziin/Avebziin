def ingredients(file_directory : str) -> dict:
  try: 
    with open(file_directory, 'r') as file_input:
      reader = file_input.readlines()
  except IOError as problem: 
    print('Error has happened with opening foods file.', problem)
    exit
  
  #print(reader) #reader[start : end : step]
  dict_of_ingredient = dict()
  for each in reader[1:-3]:
    each = each.strip()
    templist = each.split(';')
    dict_of_ingredient[templist[0]] = float(templist[1])/1000

  return dict_of_ingredient

def readfoods(file_path : str) : 
  try: 
    with open(file_path, 'r') as filepath : 
      reader = filepath.readlines()
  except IOError as problem : 
    print("Error happened with foods file", problem)
    exit
  dict_of_foods = {}
  for food in reader : 
    food = food.strip()
    templist = food.split(';')
    dict_of_foods[templist[0]] = [float(templist[1]), float(templist[2])]
  return dict_of_foods


def calculate(dict_recipe : dict ,dict_foods : dict):
  total_cost = 0
  total_calories = 0 
  for element in dict_recipe:
    for every in dict_foods:
      if element == every : 
        total_cost = total_cost + dict_recipe[element]*dict_foods[every][0]
        total_calories = (total_calories + dict_recipe[element]*dict_foods[every][1])
  print("Ingredients:")
  for each in dict_recipe:
    print(f"{each} - {dict_recipe[each] * 1000}")
  print(f"\nNumber of ingredients : {len(dict_recipe)} \nTotal_cost : {total_cost} \nTotal Calories : {total_calories}")
        


def main():
  file_path1 = 'foods.txt'
  file_path2 = 'fusilli_alle_olive.txt'
  file_path3 = 'polenta_concia.txt'
  #ingredients(file_path3)
  readfoods(file_path1)
  calculate(ingredients(file_path3),readfoods(file_path1))



if __name__ == '__main__':
  main()