# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:44:15 2021

@author: serha
"""
import pandas as pd
df = pd.read_csv("data.csv")
df.head()
df.shape

df.insert(0, 'Participants', range(1, 1 + len(df)))
df['Participants'] = 'Participant-' + df['Participants'].astype(str)
df=df.rename(columns={'Wie sind die ersten beiden Ziffern ihrer PLZ:':'PLZ'})
df=df.rename(columns={'Social Media:                                                                           Ich nutze folgende Dienste:':'Social Media'})
    
opt1 = 'Bitte ordnen Sie die Optionen entsprechend Ihrer Präferenz. von 1 als erste Wahl und 5 als letzte Wahl. [Der Einsatz nur eines Zustellers ]'
opt2 = 'Bitte ordnen Sie die Optionen entsprechend Ihrer Präferenz. von 1 als erste Wahl und 5 als letzte Wahl. [Der Einsatz von autonomen (fahrerlosen) Robotern]'
opt3 = 'Bitte ordnen Sie die Optionen entsprechend Ihrer Präferenz. von 1 als erste Wahl und 5 als letzte Wahl. [Der Einsatz von Drohnen]'
opt4 = 'Bitte ordnen Sie die Optionen entsprechend Ihrer Präferenz. von 1 als erste Wahl und 5 als letzte Wahl. [Der Einsatz von Packstationen]'
opt5 = 'Bitte ordnen Sie die Optionen entsprechend Ihrer Präferenz. von 1 als erste Wahl und 5 als letzte Wahl. [Längere Wartezeiten in Kauf nehmen ]'

df['ist Ihnen Umweltschutz wichtig?'].value_counts()
df['ist Ihnen Umweltschutz wichtig?'].value_counts(normalize=True)

%matplotlib inline
df['ist Ihnen Umweltschutz wichtig?'].value_counts().plot(kind="bar")
df['ist Ihnen Umweltschutz wichtig?'].value_counts().plot(kind="pie")

df['ist Ihnen Umweltschutz wichtig?'].value_counts().plot(kind="bar", figsize=(15,7), color="#61d199")

said_auß = df[df['ist Ihnen Umweltschutz wichtig?'] == "außerordentlich"]
said_auß.head(3)
df[opt4].value_counts(normalize=True)
df[opt5].value_counts()

df[opt1].value_counts().plot(kind="pie").get_figure().savefig('opt1_piechart.png')
df[opt2].value_counts().plot(kind="pie").get_figure().savefig('opt2_piechart.png')
df[opt3].value_counts().plot(kind="pie").get_figure().savefig('opt3_piechart.png')
df[opt4].value_counts().plot(kind="pie").get_figure().savefig('opt4_piechart.png')
df[opt5].value_counts().plot(kind="pie").get_figure().savefig('opt5_piechart.png')

'''
said_1_to_opt1['Und warum war es Ihr Favorit?'].value_counts().reset_index().to_csv('score1_to_option1_comments.csv')
said_1_to_opt1['Und warum war es Ihr Favorit?'].dropna().to_csv('score1_to_option1_comments_trial.csv',index=False)
'''
printed_columns = ['Participants','Und warum war es Ihr Favorit?','Geschlecht','Alter','Wohnsituation','Berufstätigkeit ','Haushaltsgröße','PLZ','Social Media']

said_1_to_opt1 = df[df[opt1] == 1.0]
said_2_to_opt1 = df[df[opt1] == 2.0]
said_3_to_opt1 = df[df[opt1] == 3.0]
said_4_to_opt1 = df[df[opt1] == 4.0]
said_5_to_opt1 = df[df[opt1] == 5.0]
said_1_to_opt1[printed_columns].to_csv('option1/score1_to_option1_comments.csv',index=False)
said_2_to_opt1[printed_columns].to_csv('option1/score2_to_option1_comments.csv',index=False)
said_3_to_opt1[printed_columns].to_csv('option1/score3_to_option1_comments.csv',index=False)
said_4_to_opt1[printed_columns].to_csv('option1/score4_to_option1_comments.csv',index=False)
said_5_to_opt1[printed_columns].to_csv('option1/score5_to_option1_comments.csv',index=False)

said_1_to_opt2 = df[df[opt2] == 1.0]
said_2_to_opt2 = df[df[opt2] == 2.0]
said_3_to_opt2 = df[df[opt2] == 3.0]
said_4_to_opt2 = df[df[opt2] == 4.0]
said_5_to_opt2 = df[df[opt2] == 5.0]
said_1_to_opt2[printed_columns].to_csv('option2/score1_to_option2_comments.csv',index=False)
said_2_to_opt2[printed_columns].to_csv('option2/score2_to_option2_comments.csv',index=False)
said_3_to_opt2[printed_columns].to_csv('option2/score3_to_option2_comments.csv',index=False)
said_4_to_opt2[printed_columns].to_csv('option2/score4_to_option2_comments.csv',index=False)
said_5_to_opt2[printed_columns].to_csv('option2/score5_to_option2_comments.csv',index=False)

said_1_to_opt3 = df[df[opt3] == 1.0]
said_2_to_opt3 = df[df[opt3] == 2.0]
said_3_to_opt3 = df[df[opt3] == 3.0]
said_4_to_opt3 = df[df[opt3] == 4.0]
said_5_to_opt3 = df[df[opt3] == 5.0]
said_1_to_opt3[printed_columns].to_csv('option3/score1_to_option3_comments.csv',index=False)
said_2_to_opt3[printed_columns].to_csv('option3/score2_to_option3_comments.csv',index=False)
said_3_to_opt3[printed_columns].to_csv('option3/score3_to_option3_comments.csv',index=False)
said_4_to_opt3[printed_columns].to_csv('option3/score4_to_option3_comments.csv',index=False)
said_5_to_opt3[printed_columns].to_csv('option3/score5_to_option3_comments.csv',index=False)

said_1_to_opt4 = df[df[opt4] == 1.0]
said_2_to_opt4 = df[df[opt4] == 2.0]
said_3_to_opt4 = df[df[opt4] == 3.0]
said_4_to_opt4 = df[df[opt4] == 4.0]
said_5_to_opt4 = df[df[opt4] == 5.0]
said_1_to_opt4[printed_columns].to_csv('option4/score1_to_option4_comments.csv',index=False)
said_2_to_opt4[printed_columns].to_csv('option4/score2_to_option4_comments.csv',index=False)
said_3_to_opt4[printed_columns].to_csv('option4/score3_to_option4_comments.csv',index=False)
said_4_to_opt4[printed_columns].to_csv('option4/score4_to_option4_comments.csv',index=False)
said_5_to_opt4[printed_columns].to_csv('option4/score5_to_option4_comments.csv',index=False)

said_1_to_opt5 = df[df[opt5] == 1.0]
said_2_to_opt5 = df[df[opt5] == 2.0]
said_3_to_opt5 = df[df[opt5] == 3.0]
said_4_to_opt5 = df[df[opt5] == 4.0]
said_5_to_opt5 = df[df[opt5] == 5.0]
said_1_to_opt5[printed_columns].to_csv('option5/score1_to_option5_comments.csv',index=False)
said_2_to_opt5[printed_columns].to_csv('option5/score2_to_option5_comments.csv',index=False)
said_3_to_opt5[printed_columns].to_csv('option5/score3_to_option5_comments.csv',index=False)
said_4_to_opt5[printed_columns].to_csv('option5/score4_to_option5_comments.csv',index=False)
said_5_to_opt5[printed_columns].to_csv('option5/score5_to_option5_comments.csv',index=False)

df.shape
said_1_to_opt1['Participants']
said_1_to_opt2.shape
said_1_to_opt3.shape
said_1_to_opt4.shape
said_1_to_opt5.shape

df[[opt1,opt2,opt3,opt4,opt5]].shape
list_of_optionsframe = df[[opt1,opt2,opt3,opt4,opt5]].values.tolist()

countlist=[]
for i in range(len(list_of_optionsframe)):
    countlist.append(list_of_optionsframe[i].count(1.0))

poslist=[]
for pos, j in enumerate(countlist):
    if j >= 2:
        poslist.append(pos)

df=df.rename(columns={opt1:'option-1'})
df=df.rename(columns={opt2:'option-2'})
df=df.rename(columns={opt3:'option-3'})
df=df.rename(columns={opt4:'option-4'})
df=df.rename(columns={opt5:'option-5'})
printed_columns_with_options=['Participants','Und warum war es Ihr Favorit?','Geschlecht','Alter','Wohnsituation','Berufstätigkeit ','Haushaltsgröße','PLZ','Social Media','option-1','option-2','option-3','option-4','option-5']
participants_voted_1_more_than_onetime=df.loc[poslist,printed_columns_with_options]
participants_voted_1_more_than_onetime.to_csv('participants_voted_1_more_than_one_time.csv',index=False)


opsframe=df[['option-1','option-2','option-3','option-4','option-5']]
opt1score1=opsframe.loc[opsframe['option-1'] == 1.0]
len(opt1score1.loc[opt1score1['option-4']==2.0])/len(opsframe)
len(opt1score1.loc[opt1score1['option-4']==3.0])/len(opsframe)
len(opt1score1.loc[opt1score1['option-5']==2.0])/len(opsframe)
len(opt1score1.loc[opt1score1['option-5']==3.0])/len(opsframe)

opt4score1=opsframe.loc[opsframe['option-4'] == 1.0]
len(opt4score1.loc[opt4score1['option-1']==2.0])/len(opsframe)
len(opt4score1.loc[opt4score1['option-1']==3.0])/len(opsframe)

opt5score1=opsframe.loc[opsframe['option-5'] == 1.0]
len(opt5score1.loc[opt5score1['option-1']==2.0])/len(opsframe)
len(opt5score1.loc[opt5score1['option-1']==3.0])/len(opsframe)











