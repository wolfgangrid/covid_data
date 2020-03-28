import numpy as np
import pandas as pd

def get_data():
    cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

    dta_cases = pd.read_csv(cases_url)
    dta_deaths = pd.read_csv(deaths_url)

    dates = dta_deaths.columns[4:]

    #"latest available date: " + dates[-1]

    dta_cases.insert(0,"region","")
    dta_deaths.insert(0,"region","")

    dta_cases["region"].loc[dta_cases["Province/State"].notna()] = dta_cases["Country/Region"].loc[dta_cases["Province/State"].notna()] +" "+ dta_cases["Province/State"].loc[dta_cases["Province/State"].notna()]
    dta_cases["region"].loc[dta_cases["Province/State"].isna()] = dta_cases["Country/Region"].loc[dta_cases["Province/State"].isna()]

    dta_deaths["region"].loc[dta_deaths["Province/State"].notna()] = dta_deaths["Country/Region"].loc[dta_deaths["Province/State"].notna()] +" "+ dta_deaths["Province/State"].loc[dta_deaths["Province/State"].notna()]
    dta_deaths["region"].loc[dta_deaths["Province/State"].isna()] = dta_deaths["Country/Region"].loc[dta_deaths["Province/State"].isna()]

    #countries = ["Austria","Belgium","Denmark","France","Germany","Italy","Netherlands","Spain","Sweden",
     #           "United Kingdom","US"]
    #regions = ["California","New York","Washington","Hubei","United Kingdom"]
    regions = ["Austria","United Kingdom","US","China Hubei","Italy","Germany","US","Spain"]

    dta = {}
    dta["cases"] = {}
    dta["deaths"] = {}
    #for c in countries:
    #    dta["cases"][c] = np.array(dta_cases.loc[dta_cases['Country/Region'] == c].iloc[:,4:-1])[0]
    #    dta["deaths"][c] = np.array(dta_deaths.loc[dta_deaths['Country/Region'] == c].iloc[:,4:-1])[0]

    for r in regions:
        dta["cases"][r] = np.array(dta_cases.loc[dta_cases["region"] == r].iloc[:,5:])[0]
        dta["deaths"][r] = np.array(dta_deaths.loc[dta_deaths["region"] == r].iloc[:,5:])[0]

    return dta,dates,regions