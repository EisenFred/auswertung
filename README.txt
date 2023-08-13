Was macht dieses Skript?
Es erstellt eine Auswertung eines bestimmten Monats von gesammelten Verspätungsdaten in einem Diagramm (siehe Bild)
--------------------------------------------------------------------------------------------
Was benötigt das Skript?
Die Verspätungsdaten werden in einer CSV angeliefert. Die CSV-Datei ist nach folgendem Schema aufebaut ['Linie','Soll','Ist','Verspaetung','Datum','Wochentag']. 
Für das Programm sind nur die Spalten 'Soll' und 'Verspaetung' relevant.

Linie = String der Buslinie
Soll = planmäßige Ankunftszeit (HH:MM)
Ist = tatsächliche Ankunftszeit (HH:MM)
Verspaetung = Verspätung in Minuten
Datum = Datum der Fahrt (DD.MM.YYYY)
Wochentag = Wochentag als Zahl (1-7)
--------------------------------------------------------------------------------------------
Was kann ich einstellen?
In der settings.py lassen sich folende Parameter einstellen.
1. Das Jahr und er Monat der ausgewertet werden soll.
2. Die Dateinamen der CSV und der Excel.
3. Die Colorcodes der einzelnen Werte als HEX-Code.
   eingestellt werden können die Verspätungen 0,1,2,3,4 >=5 und >=10
