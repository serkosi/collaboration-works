# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 10:44:15 2021

@author: serha
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("data.csv")
df.head()
df.shape

df.insert(0, 'Participants', range(1, 1 + len(df)))
df['Participants'] = 'Participant-' + df['Participants'].astype(str)
df=df.rename(columns={'Wie sind die ersten beiden Ziffern ihrer PLZ:':'PLZ'})
df=df.rename(columns={'Social Media:                                                                           Ich nutze folgende Dienste:':'Social Media'})
    
df=df.rename(columns={'ist Ihnen Umweltschutz wichtig?':'environmental protection importance'})

df=df.rename(columns={'Bitte ordnen Sie die Optionen entsprechend Ihrer Präferenz. von 1 als erste Wahl und 5 als letzte Wahl. [Der Einsatz nur eines Zustellers ]':'opt1-one delivery person'})
df=df.rename(columns={'Bitte ordnen Sie die Optionen entsprechend Ihrer Präferenz. von 1 als erste Wahl und 5 als letzte Wahl. [Der Einsatz von autonomen (fahrerlosen) Robotern]':'opt2-autonomous robots'})
df=df.rename(columns={'Bitte ordnen Sie die Optionen entsprechend Ihrer Präferenz. von 1 als erste Wahl und 5 als letzte Wahl. [Der Einsatz von Drohnen]':'opt3-drones'})
df=df.rename(columns={'Bitte ordnen Sie die Optionen entsprechend Ihrer Präferenz. von 1 als erste Wahl und 5 als letzte Wahl. [Der Einsatz von Packstationen]':'opt4-packstations'})
df=df.rename(columns={'Bitte ordnen Sie die Optionen entsprechend Ihrer Präferenz. von 1 als erste Wahl und 5 als letzte Wahl. [Längere Wartezeiten in Kauf nehmen ]':'opt5-longer waiting'})

df=df.rename(columns={'wenn Sie diese Möglichkeit gewählt haben:':'if you chose this option'})
df=df.rename(columns={'Haben Sie Ergänzungen oder andere Vorschläge?':'other comments'})
df=df.rename(columns={'wenn Sie diese Möglichkeit gewählt haben:.1':'if you chose opt1'})
df=df.rename(columns={'Haben Sie Ergänzungen oder andere Vorschläge?.1':'other comments-opt1'})
df=df.rename(columns={'Spielt das max. Paketgewicht von 2 KG für Sie eine Rolle?':'Is max weight of 2 KG important?'})
df=df.rename(columns={'wenn Sie diese Möglichkeit gewählt haben:.3':'if you chose opt3'})
df=df.rename(columns={'Haben Sie Ergänzungen oder andere Vorschläge?.3':'other comments-opt3'})
df=df.rename(columns={'wenn Sie diese Möglichkeit gewählt haben:.4':'if you chose opt4'})
df=df.rename(columns={'Haben Sie Ergänzungen oder andere Vorschläge?.4':'other comments-opt4'})
df=df.rename(columns={'Wenn Sie bereit sind zu warten, wie lange würden Sie warten?':'how long you would wait?'})
df=df.rename(columns={'wenn Sie diese Möglichkeit gewählt haben:.5':'if you chose opt5'})
df=df.rename(columns={'Haben Sie Ergänzungen oder andere Vorschläge?.5':'other comments-opt5'})

df=df.rename(columns={'Was halten Sie von der Möglichkeit, sich anzeigen zu lassen,wieviel CO2 Sie persönlich durch eine Aktion eingespart haben.':'how much CO2 you have saved personally through an action?'})
df=df.rename(columns={'Geschlecht':'Gender','Alter':'Age','Berufstätigkeit ':'Employment'})

option_columns=['opt1-one delivery person','opt2-autonomous robots','opt3-drones','opt4-packstations','opt5-longer waiting']

# Which option was the favorite? 

def hist(score,a,b):
    %matplotlib inline
    plt.style.use('ggplot')
    x = ['Option 1 \n One \n Delivery \n Person', 'Option 2 \n Autonomous \n Robots', 'Option 3 \n Drones', 'Option 4 \n Package \n Stations', 'Option 5 \n Longer \n Waiting']
    scores = score.sum()

    x_pos = [i for i, _ in enumerate(x)]

    plt.bar(x_pos, scores, color=b)
    #plt.xlabel("Options")
    plt.ylabel("Scores")
    plt.title(a)
    plt.xticks(x_pos, x)
    plt.show()


#-for all the range of age
ages=df['Age'].unique().tolist()[0:6]
over66=df[df['Age'] == ages[0]][option_columns]
i56_65=df[df['Age'] == ages[1]][option_columns]
i46_55=df[df['Age'] == ages[2]][option_columns]
i36_45=df[df['Age'] == ages[4]][option_columns]
i26_35=df[df['Age'] == ages[3]][option_columns]
i17_25=df[df['Age'] == ages[5]][option_columns]

hist(over66,"Ages over 66",'green')
hist(i56_65,"Ages between 56-65",'green')
hist(i46_55,"Ages between 46-55",'green')
hist(i36_45,"Ages between 36-45",'green')
hist(i26_35,"Ages between 26-35",'green')
hist(i17_25,"Ages between 17-25",'green')

#-for people who work fulltime or parttime
parttime=df[df['Employment'] == 'Teilzeit'][option_columns]
fulltime=df[df['Employment'] == 'Vollzeit'][option_columns]

hist(parttime,"Parttime Workers",'red')
hist(fulltime,"Fulltime Workers",'red')

#-for every kind of household 
haus=df['Haushaltsgröße'].unique().tolist()[0:3]
b1_2=df[df['Haushaltsgröße'] == haus[0]][option_columns]
b3_4=df[df['Haushaltsgröße'] == haus[1]][option_columns]
b4=df[df['Haushaltsgröße'] == haus[2]][option_columns]

hist(b1_2,"Households between 1-2",'blue')
hist(b3_4,"Households between 3-4",'blue')
hist(b4,"Households over 4",'blue')

#-for residential situation 
urban=df[df['Wohnsituation'] == 'städtisch'][option_columns]
rural=df[df['Wohnsituation'] == 'ländlich'][option_columns]

hist(urban,"Urban Residences",'orange')
hist(rural,"Rural Residences",'orange')

#-for people who are interested of how much co2 emission their action emitter
co2=df['how much CO2 you have saved personally through an action?'].unique().tolist()[0:4]
bra_nicht=df[df['how much CO2 you have saved personally through an action?'] == co2[1]][option_columns]
gut=df[df['how much CO2 you have saved personally through an action?'] == co2[3]][option_columns]
ganz_nett=df[df['how much CO2 you have saved personally through an action?'] == co2[0]][option_columns]
ex_gut=df[df['how much CO2 you have saved personally through an action?'] == co2[2]][option_columns]

hist(bra_nicht,"brauche ich nicht",'yellow')
hist(gut,"gut",'yellow')
hist(ganz_nett,"ganz nett",'yellow')
hist(ex_gut,"außerordentlich gut",'yellow')


# What kind of people (their age, work fulltime or parttime, household situation, residential (urban or rural)) 
# who gave score 1&2 to option 1, to option 2, option 3, option 4 and option 5.

# option-1
df.loc[(df['opt1-one delivery person'] == 1.0) | (df['opt1-one delivery person'] == 2.0)]['Age'].value_counts().plot(kind='bar',color='green',title='Scores 1&2 given to Option-1 \n according to Ages')
df.loc[(df['opt1-one delivery person'] == 1.0) | (df['opt1-one delivery person'] == 2.0)]['Employment'].value_counts().plot(kind='bar',color='red',title='Scores 1&2 given to Option-1 \n according to Employment')
df.loc[(df['opt1-one delivery person'] == 1.0) | (df['opt1-one delivery person'] == 2.0)]['Haushaltsgröße'].value_counts().plot(kind='bar',color='blue',title='Scores 1&2 given to Option-1 \n according to Households')
df.loc[(df['opt1-one delivery person'] == 1.0) | (df['opt1-one delivery person'] == 2.0)]['Wohnsituation'].value_counts().plot(kind='bar',color='orange',title='Scores 1&2 given to Option-1 \n according to Residencial')

# option-2
df.loc[(df[option_columns[1]] == 1.0) | (df[option_columns[1]] == 2.0)]['Age'].value_counts().plot(kind='bar',color='green',title='Scores 1&2 given to Option-2 \n according to Ages')
df.loc[(df[option_columns[1]] == 1.0) | (df[option_columns[1]] == 2.0)]['Employment'].value_counts().plot(kind='bar',color='red',title='Scores 1&2 given to Option-2 \n according to Employment')
df.loc[(df[option_columns[1]] == 1.0) | (df[option_columns[1]] == 2.0)]['Haushaltsgröße'].value_counts().plot(kind='bar',color='blue',title='Scores 1&2 given to Option-2 \n according to Households')
df.loc[(df[option_columns[1]] == 1.0) | (df[option_columns[1]] == 2.0)]['Wohnsituation'].value_counts().plot(kind='bar',color='orange',title='Scores 1&2 given to Option-2 \n according to Residencial')

# option-3
df.loc[(df[option_columns[2]] == 1.0) | (df[option_columns[2]] == 2.0)]['Age'].value_counts().plot(kind='bar',color='green',title='Scores 1&2 given to Option-3 \n according to Ages')
df.loc[(df[option_columns[2]] == 1.0) | (df[option_columns[2]] == 2.0)]['Employment'].value_counts().plot(kind='bar',color='red',title='Scores 1&2 given to Option-3 \n according to Employment')
df.loc[(df[option_columns[2]] == 1.0) | (df[option_columns[2]] == 2.0)]['Haushaltsgröße'].value_counts().plot(kind='bar',color='blue',title='Scores 1&2 given to Option-3 \n according to Households')
df.loc[(df[option_columns[2]] == 1.0) | (df[option_columns[2]] == 2.0)]['Wohnsituation'].value_counts().plot(kind='bar',color='orange',title='Scores 1&2 given to Option-3 \n according to Residencial')

# option-4
df.loc[(df[option_columns[3]] == 1.0) | (df[option_columns[3]] == 2.0)]['Age'].value_counts().plot(kind='bar',color='green',title='Scores 1&2 given to Option-4 \n according to Ages')
df.loc[(df[option_columns[3]] == 1.0) | (df[option_columns[3]] == 2.0)]['Employment'].value_counts().plot(kind='bar',color='red',title='Scores 1&2 given to Option-4 \n according to Employment')
df.loc[(df[option_columns[3]] == 1.0) | (df[option_columns[3]] == 2.0)]['Haushaltsgröße'].value_counts().plot(kind='bar',color='blue',title='Scores 1&2 given to Option-4 \n according to Households')
df.loc[(df[option_columns[3]] == 1.0) | (df[option_columns[3]] == 2.0)]['Wohnsituation'].value_counts().plot(kind='bar',color='orange',title='Scores 1&2 given to Option-4 \n according to Residencial')

# option-5
df.loc[(df[option_columns[4]] == 1.0) | (df[option_columns[4]] == 2.0)]['Age'].value_counts().plot(kind='bar',color='green',title='Scores 1&2 given to Option-5 \n according to Ages')
df.loc[(df[option_columns[4]] == 1.0) | (df[option_columns[4]] == 2.0)]['Employment'].value_counts().plot(kind='bar',color='red',title='Scores 1&2 given to Option-5 \n according to Employment')
df.loc[(df[option_columns[4]] == 1.0) | (df[option_columns[4]] == 2.0)]['Haushaltsgröße'].value_counts().plot(kind='bar',color='blue',title='Scores 1&2 given to Option-5 \n according to Households')
df.loc[(df[option_columns[4]] == 1.0) | (df[option_columns[4]] == 2.0)]['Wohnsituation'].value_counts().plot(kind='bar',color='orange',title='Scores 1&2 given to Option-5 \n according to Residencial')


#For the option 1:
#- What kind of people (their age, work fulltime or parttime, household situation, residential (urban or rural)) 
# who choose option 1
df.loc[df[option_columns[0]] == 1.0]['Age'].value_counts().plot(kind='bar',color='green',title='Scores 1 given to Option-1 \n according to Ages')
df.loc[df[option_columns[0]] == 1.0]['Employment'].value_counts().plot(kind='bar',color='red',title='Score 1 given to Option-1 \n according to Employment')
df.loc[df[option_columns[0]] == 1.0]['Haushaltsgröße'].value_counts().plot(kind='bar',color='blue',title='Score 1 given to Option-1 \n according to Households')
df.loc[df[option_columns[0]] == 1.0]['Wohnsituation'].value_counts().plot(kind='bar',color='orange',title='Score 1 given to Option-1 \n according to Residencial')


#For the option 1:
#-What kind of people (their age, work fulltime or parttime, household situation) 
# who are willing to pay 0,51-1€.
uniquefeevalues=df['if you chose this option'].unique().tolist()[0:13]

df.loc[df['if you chose this option'] == uniquefeevalues[2]]['Age'].value_counts().plot(kind='bar',color='green',title='People chose Option-1 who are willing to pay \n 0,51-1€ according to Ages')
df.loc[df['if you chose this option'] == uniquefeevalues[2]]['Employment'].value_counts().plot(kind='bar',color='red',title='People chose Option-1 who are willing to pay \n 0,51-1€ according to Employment')
df.loc[df['if you chose this option'] == uniquefeevalues[2]]['Haushaltsgröße'].value_counts().plot(kind='bar',color='blue',title='People chose Option-1 who are willing to pay \n 0,51-1€ according to Households')
df.loc[df['if you chose this option'] == uniquefeevalues[2]]['Wohnsituation'].value_counts().plot(kind='bar',color='orange',title='People chose Option-1 who are willing to pay \n 0,51-1€ according to Residencial')

#For the option 1:
#-What kind of people (their age, work fulltime or parttime, household situation) 
# who don’t want to pay an additional cost.
df.loc[df['if you chose this option'] == uniquefeevalues[4]]['Age'].value_counts().plot(kind='bar',color='green',title='People chose Option-1 who don’t want to pay \n an additional cost according to Ages')
df.loc[df['if you chose this option'] == uniquefeevalues[4]]['Employment'].value_counts().plot(kind='bar',color='red',title='People chose Option-1 who don’t want to pay \n an additional cost according to Employment')
df.loc[df['if you chose this option'] == uniquefeevalues[4]]['Haushaltsgröße'].value_counts().plot(kind='bar',color='blue',title='People chose Option-1 who don’t want to pay \n an additional cost according to Households')
df.loc[df['if you chose this option'] == uniquefeevalues[4]]['Wohnsituation'].value_counts().plot(kind='bar',color='orange',title='People chose Option-1 who don’t want to pay \n an additional cost according to Residencial')
