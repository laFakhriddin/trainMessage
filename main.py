import support as s

senderStation = s.checkSenderStation('Код станции передачи информации: ')
senderStation = s.loopForTrain(senderStation)
trainNumber = s.checkTrainNumber('Номер поезда: ')
station = s.checkStation('Станция формирования: ')
station = s.loopStation(station)
compoundNum = input('Номер состава: ')
endStation = input('Станция назначения: ')
number = 1
date = input('Число: ')
month = input('Месяц: ')
hour = input('Часы: ')
minute = input('Минуты: ')
trainLength = input('Условная длина: ')
mass = input('Масса брутто: ')
coverCode = input('Код прикрытия: ')
oversizeIndex = input('Индекс негабаритности: ')
livestock = input('Живность: ')
route = input('Маршрут: ')

print('(: 02', senderStation, trainNumber, station, compoundNum, endStation, number, date, month, hour, minute,
      trainLength, mass, coverCode, oversizeIndex, livestock, route)
