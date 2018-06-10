import json
from django.http import JsonResponse
from django.views import View
import numpy as np
import pandas as pd
from time import time
import scipy
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import auc, roc_curve, f1_score
from sklearn.model_selection import KFold,cross_val_score, GridSearchCV

def get(request):
  # data = {
  #   'genero': request.GET.get('gender', 0),
  #   # 'course': 'que todos respeitam',
  #   'media': request.GET.get('average', 6),
  #   'satisf_curso': request.GET.get('courseSatisfaction', 2),
  #   'satisf_vida': request.GET.get('lifeSatisfaction', 2),
  #   'expect': request.GET.get('courseExpectation', 2),
  #   'pression': request.GET.get('pressionedByFriends', 0.5),
  #   'curso_certo': request.GET.get('chooseRightCourse', 0.5),
  #   'dif_financ': request.GET.get('financialDifficult', 0.5),
  #   'ativ_extra': request.GET.get('extracurricularActivity', 0.5),
  # }

  userInput = [
    request.GET.get('gender', 0),
    request.GET.get('average', 6),
    request.GET.get('courseSatisfaction', 2),
    request.GET.get('lifeSatisfaction', 2),
    request.GET.get('courseExpectation', 2),
    request.GET.get('pressionedByFriends', 0.5),
    request.GET.get('chooseRightCourse', 0.5),
    request.GET.get('financialDifficult', 0.5),
    request.GET.get('extracurricularActivity', 0.5),
  ]

  print(userInput)

  # CRÉDITOS (modificicado, portanto foi mais uma inspiração, parte de preprocessamento): https://github.com/udacity/machine-learning/blob/master/projects/student_intervention/student_intervention.ipynb
  # importando bibliotecas
  
  # pegando o dataset
  data = pd.read_csv("/Users/taqtile/Documents/Project/lovelace/hackathonserver/hackathonserver/final.csv")

  data['media0'] = 0
  data['media1'] = 0
  data['media2'] = 0
  data['media3'] = 0
  data.loc[data.media < 5,'media0'] = 1
  data.loc[data.media == 6,'media1'] = 1
  data.loc[data.media == 7,'media1'] = 1
  data.loc[data.media == 8,'media1'] = 1
  data.loc[data.media == 9,'media1'] = 1
  data.loc[data.media == 10,'media2'] = 1
  data.loc[data.media == 11,'media2'] = 1
  data.loc[data.media == 12,'media2'] = 1
  data.loc[data.media == 13,'media2'] = 1
  data.loc[data.media == 14,'media2'] = 1
  data.loc[data.media == 15,'media3'] = 1
  data.loc[data.media == 16,'media3'] = 1
  data.loc[data.media == 17,'media3'] = 1
  data.loc[data.media == 18,'media3'] = 1
  data.loc[data.media == 19,'media3'] = 1

  data['satisf_curso0'] = 0
  data['satisf_curso1'] = 0
  data.loc[data.satisf_curso < 3,'satisf_curso0'] = 1
  data.loc[data.satisf_curso == 3,'satisf_curso1'] = 1
  data.loc[data.satisf_curso == 4,'satisf_curso1'] = 1

  data['satisf_vida0'] = 0
  data['satisf_vida1'] = 0
  data.loc[data.satisf_vida < 3,'satisf_vida0'] = 1
  data.loc[data.satisf_vida == 3,'satisf_vida1'] = 1
  data.loc[data.satisf_vida == 4,'satisf_vida1'] = 1

  # mergeando infos separadas do forms
  features = data.loc[:,['genero', 'media0', 'media1', 'media2', 'media3', 'satisf_curso0', 'satisf_curso1',
                       'satisf_vida0', 'satisf_vida1',
                        'expect', 'pression', 'curso_certo', 'dif_financ',
                       'ativ_extra']].sample(frac=1).reset_index(drop=True)
  target = data.loc[:,['evasao']].sample(frac=1).reset_index(drop=True)

  X = features
  y = target
  model = RandomForestClassifier()
  model.fit(X, y.values.ravel())

  resultado_df = pd.DataFrame(userInput)
  resultado_df = resultado_df.T

  resultado_df['media0'] = 0
  resultado_df['media1'] = 0
  resultado_df['media2'] = 0
  resultado_df['media3'] = 0
  if int(resultado_df.iloc[0][1]) < 5:
      resultado_df['media0'] = 1
  elif int(resultado_df.iloc[0][1]) < 10:
      resultado_df['media1'] = 1
  elif int(resultado_df.iloc[0][1]) < 15:
      resultado_df['media2'] = 1
  else:
      resultado_df['media3'] = 1

  resultado_df['satisf_curso0'] = 0
  resultado_df['satisf_curso1'] = 0
  if int(resultado_df.iloc[0][2]) < 3:
      resultado_df['satisf_curso0'] = 1
  else:
      resultado_df['satisf_curso1'] = 1

  resultado_df['satisf_vida0'] = 0
  resultado_df['satisf_vida1'] = 0
  if int(resultado_df.iloc[0][3]) < 3:
      resultado_df['satisf_vida0'] = 1
  else:
      resultado_df['satisf_vida1'] = 1



  resultado_df = resultado_df.loc[:,[0, 'media0', 'media1', 'media2', 'media3', 'satisf_curso0', 'satisf_curso1',
                        'satisf_vida0', 'satisf_vida1',
                          4, 5, 6, 7, 8]]

  resultado = model.predict_proba(resultado_df)[:, 1]


  print(data)
  print(resultado)

  return JsonResponse({'chanceOfEvasion': resultado[0]})