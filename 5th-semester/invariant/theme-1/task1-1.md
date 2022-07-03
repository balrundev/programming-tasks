# Модуль datetime

## Константы

- `datetime.MINYEAR` - минимальное значение года, допустимое в объектах `date` и `datetime`
- `datetime.MAXYEAR` - максимальное значение года, допустимое в объектах `date` и `datetime`

## Доступные типы

- `datetime.date` - дата. Атрибуты: `year`, `month`, `day`
- `datetime.time` - время, независимое от даты.
- `datetime.datetime` - комбинация времени и даты. Атрибуты: `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`
- `datetime.timedelta` - разница между двумя объектами `date`, `time` или `datetime`
- `datetime.tzinfo` - базовый класс для информации о часовом поясе (используется классами `datetime` и `time`)
- `datetime.timezone` - класс, который реализует `tzinfo` как фиксированное смещение от UTC

## timedelta

Объект `timedelta` представляет продолжительность, разницу между двумя датами или отметками времени.

Конструктор `timedelta` позволяет нормализовать аргументы (представляются как дни, секунды и микросекунды):

```python
>>> from datetime import timedelta
>>> delta = timedelta(days=15, seconds=25, minutes=25, hours=7, weeks=3)
>>> delta
datetime.timedelta(days=36, seconds=26725)
```

## date

Объект `date` представляет дату (год, месяц и день).

Конструктор `date`:

```python
>>> from datetime import date
>>> d = date(2021, 10, 5)
>>> d
datetime.date(2021, 10, 5)
```

Методы класса:

- `today()` - возвращает текущую дату
- `fromtimestamp(timestamp)` - возвращает дату по значению timestamp
- `fromordinal(ordinal)` - возвращает дату по пролептическому григорианскому календарю
- `fromisoformat(date_string)` - возвращает дату, соответствующую дате в виде строки в формате `YYYY-MM-DD`
- `fromisocalendar(year, week, day)` - возвращает дату по календарю ISO

Методы экземпляров класса:

- `replace(year=self.year, month=self.month, day=self.day)` - возвращает заданную дату с заменённым значением
- `timetuple()` - возвращает структуру `time.struct_time` (как `time.localtime()`)
- `toordinal()` - возвращает значение по пролептическому григорианскому календарю
- `weekday()` - возвращает день недели (понедельник - 0, воскресенье - 6)
- `isoweekday()` - возвращает день недели по ISO (понедельник - 1, воскресенье - 7)
- `isocalendar()` - возвращает named tuple с компонентами `year`, `week` и `weekday`
- `isoformat()` - возвращает строку , представляющую дату в формате ISO 8601, `YYYY-MM-DD`
- `__str__()` - эквивалентно `d.isoformat()`
- `ctime()` - возвращает строку, представляющую дату
- `strftime(format)` - возвращает строку, представляющую дату (с заданным форматированием)
- `__format__(format)`- то же самое, что `date.strftime()`

## datetime

Конструктор `datetime`:

```python
>>> from datetime import datetime
>>> d = datetime(2021, 10, 6, 12, 15)
>>> d
datetime.datetime(2021, 10, 6, 12, 15)
```

Методы класса:

- `today()` - возвращает текущую дату и время
- `now(tz=None)` - возвращает текущую дату и время
- `utcnow()` - возвращает текущую дату и время по UTC
- `fromtimestamp(timestamp, tz=None)` - возвращает дату и время по значению timestamp
- `utcfromtimestamp(timestamp)` - возвращает дату и время по UTC по значению timestamp
- `fromordinal(ordinal)` - возвращает дату и время по пролептическому григорианскому календарю
- `combine(date, time, tzinfo=self.tzinfo)` - возвращает объект `datetime`, составленный из объектов `date` и `time`
- `fromisoformat(date_string)` - возвращает объект `datetime` , соответствующий строке, созданной функциями `date.isoformat()` и `datetime.isoformat()`
- `fromisocalendar(year, week, day)` - возвращает объект `datetime` по ISO
- `strptime(date_string, format)` - возвращает объект `datetime` , соответствующий заданной строке

Методы экземпляров класса:

- `date()` - возвращает объект `date`
- `time()` - возвращает объект `time` (без указания часового пояса)
- `timetz()` - возвращает объект `time`
- `replace(year=self.year, month=self.month, day=self.day, hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)` - возвращает объект `datetime` с заменёнными значениями
- `astimezone(tz=None)` - возвращает объект `datetime` с новым значением `tz` (часовой пояс), время по UTC сохраняется
- `utcoffset()` - возвращает смещение от UTC в виде объекта `timedelta`
- `dst()` - возвращает корректировку летнего времени (Daylight saving time)
- `tzname()` - возвращает название часового пояса
- `timetuple()` - возвращает структуру `time.struct_time` (как `time.localtime()`)
- `utctimetuple()` - возвращает структуру `time.struct_time` в соответствии с часовым поясом
- `toordinal()` - возвращает значение по пролептическому григорианскому календарю
- `timestamp()` - возвращает timestamp
- `weekday()` - возвращает день недели (понедельник - 0, воскресенье - 6)
- `isoweekday()` - возвращает день недели по ISO (понедельник - 1, воскресенье - 7)
- `isocalendar()` - возвращает named tuple с компонентами `year`, `week` и `weekday`
- `isoformat(sep='T', timespec='auto')` - возвращает строковое представление даты и времени в формате ISO 8601
- `__str__()` - эквивалентно `d.isoformat(' ')`
- `ctime()` - возвращает строку, представляющую дату и время
- `strftime(format)` - возвращает строку, представляющую дату и время (с заданным форматированием)
- `__format__(format)` - то же самое, что `datetime.strftime()`

## time

Конструктор `time`:

```python
>>> from datetime import time
>>> t = time(12, 5, 24)
>>> t
datetime.time(12, 5, 24)
```

- `fromisoformat(time_string)` - возвращает объект `time`, соответствующий строуе, созданной функцией `time.isoformat()`
- `replace(hour=self.hour, minute=self.minute, second=self.second, microsecond=self.microsecond, tzinfo=self.tzinfo, *, fold=0)` - возвращает объект `time` с заменёнными значениями
- `isoformat(timespec='auto')` - возвращает строковое представление времени в формате ISO 8601
- `__str__()` - эквивалентно `t.isoformat()`
- `strftime(format)` - возвращает строку, представляющую  время (с заданным форматированием)
- `__format__(format)` - то же самое, что `time.strftime()`
- `utcoffset()` - возвращает смещение от UTC в виде объекта `timedelta`
- `dst()` - возвращает корректировку летнего времени (Daylight saving time)
- `tzname()` - возвращает название часового пояса
