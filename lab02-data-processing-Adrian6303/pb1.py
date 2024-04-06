import pandas as pd
from matplotlib import pyplot as plt

#a

def getData():
    return pd.read_csv("data\employees.csv",delimiter=',',header='infer')

def getNrAngajati():
    return len(getData())

def getNrAndType():
    return getData().dtypes

def getNrAngajatiDateComplete():
    nan_counts_per_row = getData().isna().sum(axis=1)
    rows_with_zero_nan = nan_counts_per_row[nan_counts_per_row == 0]
    return len(rows_with_zero_nan)

def getMin():
    return getData().min(numeric_only=True)

def getMax():
    return getData().max(numeric_only=True)

def getMed():
    return getData().median(numeric_only=True)

def getPosibleValuesFirstName():
    data = getData()
    return data['First Name'].unique()

def getPosibleValuesGender():
    data = getData()
    return data['Gender'].unique()

def getPosibleValuesSeniorManagement():
    data = getData()
    return data['Senior Management'].unique()

def getPosibleValuesTeam():
    data = getData()
    return data['Team'].unique()

def ExistaDateLipsa():
    return getNrAngajati() - getNrAngajatiDateComplete() != 0


print("Nr angajati:",getNrAngajati())

print("Nr si tip proprietati:\n", getNrAndType())

print("Nr angajati date complete:",getNrAngajatiDateComplete())

print("Nr angajati date complete:",getNrAngajatiDateComplete())

print("Valoare minima:\n",getMin())

print("Valoare maxima:\n",getMax())

print("Valoare medie:\n",getMed())

print("Valori posibile First Name:", len(getPosibleValuesFirstName()))

print("Valori posibile Gender:", len(getPosibleValuesGender()))

print("Valori posibile Senior Management:", len(getPosibleValuesSeniorManagement()))

print("Valori posibile Team:", len(getPosibleValuesTeam()))

print('Exista date lipsa:', ExistaDateLipsa())

#b

def create_hist(): 
    df = getData()

    df.hist(column="Salary")
    plt.savefig("hist\salariu.png")
    plt.clf()

    df.hist(column="Salary", by="Team")
    plt.savefig("hist\salariu_echipe.png")
    return True

print('Diagrame realizate:', create_hist())
