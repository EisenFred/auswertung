import pandas as pd
from load_csv import load_csv
import datetime
#pip install openpyxl

# TODO Header mit Soll Uhrzeiten fürs Dataframe in CSV auslagern die man Einlesenkann oder in ander constants python ist glaube ich ebser

EXCEL_FILENAME = 'output.xlsx'
CSV_FILENAME = "SB56_t30.csv"
#Month to be filtered 01-12
MONTH = 7
YEAR = 2023

pd.set_option('display.max_columns', None)

def generate_dates(year, month):
    num_days = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
    dates = [datetime.date(year, month, day).strftime('%d-%m-%Y') for day in range(1, num_days + 1)]
    return dates

def monatsauswertung():
    # CSV in DataFrame laden und auf angegebenen Monat filtern.
    data = load_csv(CSV_FILENAME)
    columns = ['Linie', 'Soll', 'Ist', 'Verspaetung', 'Datum', 'Wochentag']
    df_csv = pd.DataFrame(data, columns=columns)
    df_csv['Soll'] = pd.to_datetime(df_csv['Soll'], format='%H:%M')
    df_csv['Ist'] = pd.to_datetime(df_csv['Ist'], format='%H:%M')
    df_csv['Datum'] = pd.to_datetime(df_csv['Datum'], format='%d.%m.%Y', dayfirst=True)
    start_date = pd.to_datetime(f'2023-{MONTH:02d}-01')
    end_date = pd.to_datetime(f'2023-{MONTH:02d}-31')
    df_csv = df_csv[(df_csv['Datum'] >= start_date) & (df_csv['Datum'] <= end_date)]

    # Leeres Dataframe für das Ergebnis
    rows = 32  # Max Tage im Monat
    columns2 = ['07:16','07:46','08:16','08:46','09:16','09:46','10:16','10:46','11:16','11:46','12:16','12:46','13:16','13:46','14:16','14:46','15:16','15:46','16:16','16:46','17:16','17:46','18:16','18:46','19:16','19:46','20:16','20:46','21:16','21:46','22:16','22:46',]
    df_auswertung = pd.DataFrame(index=range(rows), columns=columns2)

    for index_day_in_month in range(1,32):
        date_day = pd.to_datetime(f'2023-{MONTH:02d}-{index_day_in_month:02d}')
        df_thisDay = df_csv[(df_csv['Datum'] == date_day)]
        df_thisDay = df_thisDay.copy() # Verhindert eine Warnung die durch die beiden folgenden Zeilen sonst entstehen würden.
        df_thisDay['Ist'] = df_thisDay['Ist'].dt.strftime('%H:%M')
        df_thisDay['Soll'] = df_thisDay['Soll'].dt.strftime('%H:%M')
        print(df_thisDay.head())
        df_thisDay = df_thisDay.sort_values(by='Soll')
        df_thisDay = df_thisDay.reset_index(drop=True)
        index_df_thisDay = 0
        if not df_thisDay.empty:
            for time_day in range(0,32):
                if not index_df_thisDay >= len(df_thisDay):
                    if df_auswertung.columns[time_day] == df_thisDay.loc[index_df_thisDay,'Soll']:
                        df_auswertung.iloc[index_day_in_month-1,time_day] = df_thisDay.loc[index_df_thisDay, 'Verspaetung']
                        index_df_thisDay += 1
    array = generate_dates(YEAR, MONTH)
    new_column = pd.Series(array, name='Datum')
    df_auswertung.insert(0, 'Datum', new_column)

    df_auswertung.to_excel(EXCEL_FILENAME, index=False)

monatsauswertung()