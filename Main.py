from datetime import datetime, timedelta

def get_sundays_in_2023():
    sundays = []
    year = 2023
    start_date = datetime(year, 1, 1)  # Premier jour de l'année 2023

    # Trouver le premier dimanche
    start_date += timedelta(days=(6 - start_date.weekday()))

    # Parcourir toutes les semaines de l'année
    while start_date.year == year:
        sundays.append(start_date)
        start_date += timedelta(weeks=1)

    return sundays

# Exemple d'utilisation :
sundays_2023 = get_sundays_in_2023()
for sunday in sundays_2023:
    print(sunday.strftime('%Y-%m-%d'))