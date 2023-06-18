#reading the first file which is going to represent the information
def ReadAttendence(file_directory):
  try:
    with open(file_directory, 'r') as file_input:
      #read all lines
      reader = file_input.readlines()
  except OSError as problem:
    print("Error Happened with Attendence part", problem)
    exit
  # creating a dictionary to separate the information.
  dict_of_person = dict()
  for each in reader:
    each = each.strip()
    templist = each.split(',')
    #print(templist)
    #sepating the information so we can call each
    dict_of_person[templist[0]] = {"Contact" : templist[1], "Entry" : int(templist[2]), "Exit" : int(templist[3])}
  return dict_of_person


#reading the second file 
def ReadSuspicious(file_path):
  try:
    with open(file_path, 'r') as files:
      reader = files.readlines()
  except OSError as problem:
    print("Error Happened with suspicious part", problem)
    exit
  #we put the names in a list
  list_of_person = []
  for person in reader :
    #by the time we deleted the empty lines we will add each to our list
    person = person.strip()
    list_of_person.append(person)
  #print(list_of_person)
  return list_of_person

#doing the operation 
def find(list_person, dict_person): #(list of names , their details)
  for person in list_person : # 3 names in the list that has appended
    list_of_sus = [] #empty list of suspects ...
    flag = 0 # we have created a variable that nothing matches we will equal that to 1 later ...
    for each in dict_person :
      if (dict_person[each]['Entry'] <= dict_person[person]['Entry'] <= dict_person[each]['Exit']) or (dict_person[each]['Entry'] <= dict_person[person]['Exit'] <= dict_person[each]['Exit']) and person != each:
        list_of_sus.append(each)
        flag = 1
    print(f"\n** Customer contacts : {person} : **\n")
    sorted_list = sorted(list_of_sus)
    #sorted("chio sort kone , key=ba ki sort kone , reverse=True/False")
    for every in sorted_list : 
      print(f"Contact with {every}, phone {dict_person[every]['Contact']}")
    if flag == 0 :
      print(f"** THe customer {person} had no contacts**")
    
        

def main():
  file_path1 = 'attendence.txt'
  file_path2 = 'suspicious.txt'
  ReadAttendence(file_path1)
  ReadSuspicious(file_path2)
  find(ReadSuspicious(file_path2), ReadAttendence(file_path1))


if __name__ == '__main__' : 
  main()