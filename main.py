import csv

Vopros = []
Otvet = []
Otvet2 = []
Otvet3 = []
correct_answers = []

ss = 1

score = []

with open('sss.csv', newline="") as pythontext:
  reader = csv.reader(pythontext, delimiter = ';')
  for row in reader:
    Vopros.append(row[0])
    Otvet.append(row[1])
    Otvet2.append(row[2])
    Otvet3.append(row[3])
    correct_answers.append(row[4])

while ss < len(Vopros):
  print (Vopros[ss])
  print('--a--' + (Otvet[ss]))
  print('--b--' + (Otvet2[ss]))
  print('--c--' + (Otvet3[ss]))
  option = input('Ваш ответ господин: ')

  if option == 'a':
    if Otvet[ss] == correct_answers[ss]:
      print('Ммм ответ правильный')
      score.append(5)
    else:
      print('Извини ответ не верный')
  
  if option == 'b':
    if Otvet2[ss] == correct_answers[ss]:
      print('Господин вы ответили правильно')
      score.append(5)
    else:
      print('В моей системы написано что ответ не правильный')
  
  if option == 'c':
    if Otvet3[ss] == correct_answers[ss]:
      print('ммм правильно')
      score.append(5)
    else:
      print('Не правильный вопрос ') 

  ss += 1

totalscore = sum(score)
print("Вы набрали " + str(totalscore) + " баллов)")


if totalscore == 100:
  print("Вы готовились я знаю у тебя 'A'")
elif totalscore == 93:
  print("МММ довольно не плохо  '+B'")
elif totalscore == 87:
  print("ты серьёзно ты один из лучших 'B'")
elif totalscore == 80:
  print("круто у тебя '-B'")
elif totalscore == 76:
  print("ты ночью кажись готовился '+C'")
elif totalscore == 70:
  print("нормально 'C'")
elif totalscore == 66:
  print("ну ты хотябы выше среднего '-C'")
elif totalscore == 57:
  print("Среднячек нормально!!! 'D'")
elif totalscore == 45:
  print("но хотябы не отчислили '-D'")
else:
  print("Вы не готовились я знаю у тебя 'F'")