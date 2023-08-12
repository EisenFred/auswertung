Auswertung von gesammelten Verspätungsdaten in einem Diagramm (siehe Bild)

Verspätungsdaten werden in einer CSV angeliefert.
Die CSV-Datei ist nach folgendem Schema aufebaut ['Linie','Soll','Ist','Verspaetung','Datum','Wochentag']. 
Linie = String der Buslinie
Soll = planmäßige Ankunftszeit (HH:MM)
Ist = tatsächliche Ankunftszeit (HH:MM)
Verspaetung = Verspätung in Minuten
Datum = Datum der Fahrt (DD.MM.YYYY)
Wochentag = Wochentag als Zahl (1-7)

Für das Programm sind nur die Spalten 'Soll' und 'Verspaetung' relevant.
