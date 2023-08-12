import pandas as pd
from load_csv import load_csv
import calendar
#pip install openpyxl

# TODO Header mit Soll Uhrzeiten fürs Dataframe in CSV auslagern die man Einlesenkann oder in ander constants python ist glaube ich ebser

EXCEL_FILENAME = 'output.xlsx'
CSV_FILENAME = "SB56_t30.csv"
#Month to be filtered 01-12
MONTH = '07'
YEAR = '2023'

pd.set_option('display.max_columns', None)

def format_day(day_int: int):
    return f'{day_int:02}'

def get_all_dates(year, month):
    num_days = calendar.monthrange(year, month)[1]
    all_dates = [f"{year}-{month:02d}-{day:02d}" for day in range(1, num_days + 1)]
    return all_dates
def monatsauswertung():
    # CSV in DataFrame laden und auf angegebenen Monat filtern.
    data = load_csv(CSV_FILENAME)
    columns = ['Linie', 'Soll', 'Ist', 'Verspaetung', 'Datum', 'Wochentag']
    df_csv = pd.DataFrame(data, columns=columns)
    df_csv['Soll'] = pd.to_datetime(df_csv['Soll'], format='%H:%M')
    df_csv['Ist'] = pd.to_datetime(df_csv['Ist'], format='%H:%M')
    df_csv['Datum'] = pd.to_datetime(df_csv['Datum'], format='%d.%m.%Y', dayfirst=True)
    start_date = pd.to_datetime('2023-{}-01'.format(MONTH))
    end_date = pd.to_datetime('2023-{}-31'.format(MONTH))
    df_csv = df_csv[(df_csv['Datum'] >= start_date) & (df_csv['Datum'] <= end_date)]

    # Leeres Dataframe für das Ergebnis
    rows = 32  # Max Tage im Monat
    columns2 = ['07:16','07:46','08:16','08:46','09:16','09:46','10:16','10:46','11:16','11:46','12:16','12:46','13:16','13:46','14:16','14:46','15:16','15:46','16:16','16:46','17:16','17:46','18:16','18:46','19:16','19:46','20:16','20:46','21:16','21:46','22:16','22:46',]
    df_auswertung = pd.DataFrame(index=range(rows), columns=columns2)

#    day = 0
#    while day < 31:
#        date_of_the_day = pd.to_datetime('2023-{}-{}'.format(MONTH, fromat_day(day+1)))
#
#        df_tmp = df_csv[(df_csv['Datum'] == date_of_the_day)]
#        df_tmp = df_tmp.sort_values(by='Soll')
#        indeximexi = 0
#        df_auswertung.iloc[day, indeximexi] = date_of_the_day
#        for index, row in df_tmp.iterrows():
#            # Prüfen ob row[datum] = datum der Spalte ist und wenn nicht einfach indeximexi +1
#           if str(columns2[indeximexi+1]) == str(row['Soll']):
#                df_auswertung.iloc[day, indeximexi+1] = row['Verspaetung']
#            indeximexi += 1
#        day += 1
#        index2 = 1
#        for index in range(1, 32):
#            date_of_the_day = pd.to_datetime('2023-{}-{}'.format(MONTH, format_day(day + 1)))
#            df_tmp = df_csv[(df_csv['Datum'] == date_of_the_day)]
#            df_tmp = df_tmp.sort_values(by='Soll')
#            df_auswertung.iloc[day, 0] = date_of_the_day
#            # Prüfen ob row[datum] = datum der Spalte ist und wenn nicht einfach indeximexi +1
#            if not df_tmp.empty:
#                # NOTE: Der Index vom Array mit den Uhrzeiten muss hochgehen, der aus dem tmp DF aber nicht die Uhrzeit an Stelle 1 suchen wir ja mit einem Macthc
#                # an einer bestimmten Array Position, wenn man beide gleich hochzählt gibt ja nur nen treffer von 30 einträge da sind.
#                if not index2 > len(df_tmp['Soll']):
#                    if str(columns2[index + 1]) == df_tmp.loc[index2,'Soll']:
#                        df_auswertung.iloc[day, index + 1] = df_tmp.loc[day+1,'Verspaetung']
#                        index2 += 1
#            day += 1

    for index_day_in_month in range(1,32):
        date_day = pd.to_datetime('2023-{}-{}'.format(MONTH, format_day(index_day_in_month)))
        df_thisDay = df_csv[(df_csv['Datum'] == date_day)]
        df_thisDay['Ist'] = df_thisDay['Ist'].dt.strftime('%H:%M')
        df_thisDay['Soll'] = df_thisDay['Soll'].dt.strftime('%H:%M')
        df_thisDay = df_thisDay.sort_values(by='Soll')
        df_thisDay = df_thisDay.reset_index(drop=True)
        index_df_thisDay = 0
        if not df_thisDay.empty:
            for time_day in range(0,32):
                if not index_df_thisDay >= len(df_thisDay):
                    if df_auswertung.columns[time_day] == df_thisDay.loc[index_df_thisDay,'Soll']:
                        df_auswertung.iloc[index_day_in_month,time_day] = df_thisDay.loc[index_df_thisDay, 'Verspaetung']
                        index_df_thisDay += 1



 #   arra = get_all_dates(int(YEAR), int(MONTH))
  #  new_column = pd.Series(arra, name='Country')
   # df_auswertung.insert(0, 'Datum', new_column)



    df_auswertung.to_excel(EXCEL_FILENAME, index=False)

monatsauswertung()