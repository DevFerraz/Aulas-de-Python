from datetime import datetime
date = str(input('Digite sua data de nascimento (modelo dd-mm-aaaa): '))
data = datetime.strptime(date)
today = datetime.today()
if date < today:
    print('Ainda nao esta na hora de se alistar! ')
elif date > today:
    print('Ja passou da hora de se alistar! ')
elif date == today:
    print('Eh hora de se alistar! ')