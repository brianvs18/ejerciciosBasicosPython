from datetime import  date
actual = date.today()
nacimiento = date(1993,5,18)
diferencia = (actual.year - nacimiento.year) * 12 + actual.month - nacimiento.month
print(f"La diferencia de tiempo es de",diferencia,"meses hasta hoy")