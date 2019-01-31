moneybox = 500  # euro

cost_per_day = 15  # euro

count_trips = 3

days_by_trip1 = 10  # Турция
days_by_trip2 = 5  # Франция
days_by_trip3 = 14  # Германия

cost_ticket = 50
count_fly = 2

cost_trip = cost_per_day * (days_by_trip1 + days_by_trip2 + days_by_trip3)
cost_trip += cost_ticket * count_fly * count_trips

cost_in_ruble = int(cost_trip * 78.40)  # иначе неточность в виде 57624.0000000001

print(cost_trip, 'Евро')
print(cost_in_ruble, 'Рублей')

if cost_trip <= moneybox:
    print('Едем!')
else:
    print('Надо подкопить ещё {} евро'.format(cost_trip - moneybox))
