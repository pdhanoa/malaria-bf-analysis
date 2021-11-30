import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def sex_tdr_corr(df):
    female_values = df[df['sex'] == 'female']
    male_values = df[df['sex'] == 'male']

    # chi-squared test
    chisqt = pd.crosstab(df['sex'], df['tdr_paludisme_string'])
    gender_significance_chi = stats.chi2_contingency(chisqt)
    print("Significance between positive test and gender:", gender_significance_chi)

    # print(df.corr())
    a = sns.catplot(x='tdr_paludisme_string', hue='sex', kind='count', data=df)
    plt.savefig('analysis.png')
    # Correlation between weight and positive test
    plt.clf()


def age_tdr_corr(df):
    positive_values = df[df['tdr_paludisme_string'] == 'tdr+']
    negative_values = df[df['tdr_paludisme_string'] == 'tdr-']

    # Using t-test to see if there is a significant difference between the age of those with and without HIV
    age_significance = stats.ttest_ind(positive_values['age_in_months'], negative_values['age_in_months'])
    print("age significance values:", age_significance)
    sns.kdeplot(data=df, x='age_in_months', hue='tdr_paludisme_string')
    plt.savefig('age_cluster.png')
    plt.clf()



def weight_tdr_corr(df):
    # Calculating BMI for BMI correlation with malaria positivity rate
    df['BMI'] = df['weight'] * np.power(df['height']/1000, 2)

    # Dividing positive values and negative values to observe any significant differences in weight, height, etc.
    positive_values = df[df['tdr_paludisme_string'] == 'tdr+']
    negative_values = df[df['tdr_paludisme_string'] == 'tdr-']
    weight_significance = stats.ttest_ind(positive_values['weight'], negative_values['weight'])
    print("weight significance values:", weight_significance)
    sns.kdeplot(data=df, x='weight', hue='tdr_paludisme_string')
    plt.savefig('weight_cluster.png')
    plt.clf()

    height_significance = stats.ttest_ind(positive_values['height'], negative_values['height'])
    sns.kdeplot(data=df, x='height', hue='tdr_paludisme_string')
    print("height significance values:", height_significance)
    plt.savefig('height_cluster.png')
    plt.clf()

    # Calculating BMI to see if people who are overweight given their weight and height tend to be infected with malaria
    bmi_significance = stats.ttest_ind(positive_values['BMI'], negative_values['BMI'])
    sns.kdeplot(data=df, x='BMI', hue='tdr_paludisme_string')
    print("BMI significance values:", bmi_significance)
    plt.savefig('bmi_cluster.png')
    plt.clf()

def hiv_tdr_corr(df):
    # The chi_2 test seems to state that there's a significant difference between the groups. Unlikely HIV test seems
    # more likely to provide positive TDR+ test results, but other resources indicate that this is not true.

    # Should look into why no HIV positive tests who up on the graph from what I have.
    chisqt = pd.crosstab(df['classification_vih'], df['tdr_paludisme_string'])
    vih_contingency = stats.chi2_contingency(chisqt)
    print("Significance between positive test and HIV positive test:", vih_contingency)

    b = sns.catplot(x='tdr_paludisme_string', hue='classification_vih', kind='count', data=df)
    plt.savefig('hiv_tdr_relationship.png')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv('/Users/pdhanoa/Box Sync/NU-malaria-team/data/burkina_TdH/Base_code/ieda_2_who.csv')
    d = {'tdr+': True, 'tdr-': False}
    df = df[df['tdr_paludisme_string'].notna()]
    hiv_tdr_corr(df)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
