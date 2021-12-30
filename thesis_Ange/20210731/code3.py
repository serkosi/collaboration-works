# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:44:15 2021

@author: serha
"""
import pandas as pd
df = pd.read_csv("data_model.csv")
df.head()
df.shape

df.insert(0, 'Participants', range(1, 1 + len(df)))
df['Participants'] = 'Participant-' + df['Participants'].astype(str)
df=df.rename(columns={'Modell 3 "Packstation“ mit "längere Wartezeiten“':'Modell 3'})

# -Participants who gave score 10 to the model 1 what kind of score they gave model 2&3
df.loc[df['Modell 1'] == 10][['Modell 2']].value_counts(normalize=True).plot(kind='bar',color='green',title='Scores for Model 2 \n from the Participants who gave score 10 to Model 1')
df.loc[df['Modell 1'] == 10][['Modell 3']].value_counts(normalize=True).plot(kind='bar',color='red',title='Scores for Model 3 \n from the Participants who gave score 10 to Model 1')

# -Participants who gave score,9,10 to the model 2 what kind of score they gave model 1&3
df.loc[(df['Modell 2'] == 9) | (df['Modell 2'] == 10)][['Modell 1']].value_counts(normalize=True).plot(kind='bar',color='blue',title='Scores for Model 1 \n from the Participants who gave scores 9&10 to Model 2')
df.loc[(df['Modell 2'] == 9) | (df['Modell 2'] == 10)][['Modell 3']].value_counts(normalize=True).plot(kind='bar',color='red',title='Scores for Model 3 \n from the Participants who gave scores 9&10 to Model 2')

# -Participants who gave score 9,10 to the model 1 what kind of score they gave model 2&3
df.loc[(df['Modell 1'] == 9) | (df['Modell 1'] == 10)][['Modell 2']].value_counts(normalize=True).plot(kind='bar',color='green',title='Scores for Model 2 \n from the Participants who gave scores 9&10 to Model 1')
df.loc[(df['Modell 1'] == 9) | (df['Modell 1'] == 10)][['Modell 3']].value_counts(normalize=True).plot(kind='bar',color='red',title='Scores for Model 3 \n from the Participants who gave scores 9&10 to Model 1')


# -Participants who gave score 1,2,3,4 to the model 1 what kind of score they gave model 2&3
df.loc[(df['Modell 1'] == 1) | (df['Modell 1'] == 2)| (df['Modell 1'] == 3)| (df['Modell 1'] == 4)][['Modell 2']].value_counts(normalize=True).plot(kind='bar',color='green',title='Scores for Model 2 \n from the Participants who gave scores 1, 2, 3, 4 to Model 1')
df.loc[(df['Modell 1'] == 1) | (df['Modell 1'] == 2)| (df['Modell 1'] == 3)| (df['Modell 1'] == 4)][['Modell 3']].value_counts(normalize=True).plot(kind='bar',color='red',title='Scores for Model 3 \n from the Participants who gave scores 1, 2, 3, 4 to Model 1')

# -Participants who gave score 1,2,3,4 to the model 3 what kind of score they gave model 1&2
df.loc[(df['Modell 3'] == 1) | (df['Modell 3'] == 2)| (df['Modell 3'] == 3)| (df['Modell 3'] == 4)][['Modell 1']].value_counts(normalize=True).plot(kind='bar',color='blue',title='Scores for Model 1 \n from the Participants who gave scores 1, 2, 3, 4 to Model 3')
df.loc[(df['Modell 3'] == 1) | (df['Modell 3'] == 2)| (df['Modell 3'] == 3)| (df['Modell 3'] == 4)][['Modell 2']].value_counts(normalize=True).plot(kind='bar',color='green',title='Scores for Model 2 \n from the Participants who gave scores 1, 2, 3, 4 to Model 3')

# -Participants who gave score 1,2,3,4 to the model 2 what kind of score they gave model 1&3
df.loc[(df['Modell 2'] == 1) | (df['Modell 2'] == 2)| (df['Modell 2'] == 3)| (df['Modell 2'] == 4)][['Modell 1']].value_counts(normalize=True).plot(kind='bar',color='blue',title='Scores for Model 1 \n from the Participants who gave scores 1, 2, 3, 4 to Model 2')
df.loc[(df['Modell 2'] == 1) | (df['Modell 2'] == 2)| (df['Modell 2'] == 3)| (df['Modell 2'] == 4)][['Modell 3']].value_counts(normalize=True).plot(kind='bar',color='red',title='Scores for Model 3 \n from the Participants who gave scores 1, 2, 3, 4 to Model 2')
