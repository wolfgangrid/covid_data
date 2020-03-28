import numpy as np
import pandas as pd

def get_data():
    cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    deaths_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"

    dta_cases = pd.read_csv(cases_url)
    dta_deaths = pd.read_csv(deaths_url)

    dates = dta_deaths.columns[4:]

    #"latest available date: " + dates[-1]

    dta_cases.insert(0,"region",dta_cases.apply(lambda x: x['Country/Region'] if pd.isnull(x['Province/State']) else x['Country/Region'] + " " + x['Province/State'],axis=1))
    dta_deaths.insert(0,"region",dta_deaths.apply(lambda x: x['Country/Region'] if pd.isnull(x['Province/State']) else x['Country/Region'] + " " + x['Province/State'],axis=1))

    #countries = ["Austria","Belgium","Denmark","France","Germany","Italy","Netherlands","Spain","Sweden",
     #           "United Kingdom","US"]
    #regions = ["California","New York","Washington","Hubei","United Kingdom"]
    regions = ["Austria","United Kingdom","US","China Hubei","Italy","Germany","US","Spain","Korea, South"]

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
