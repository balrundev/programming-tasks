# Модуль tabulate

Модуль позволяет отображать информацию в табличном виде.

### Типы данных

Поддерживаются следующие типы данных:

- список из списков (и другие iterable of iterables)
- список из словарей (ключи словаря - столбцы таблицы)
- словарь из итерируемых объектов (ключи словаря - столбцы таблицы)
- двумерный массив NumPy
- массивы записей NumPy (названия записей - названия столбцов таблицы)
- pandas.DataFrame

### Заголовки

Названия столбцов определяет аргумент `headers`.

Если значение аргумента равно `firstrow`, в качестве заголовка используется первая строка данных.

```python
>>> from tabulate import tabulate
>>> data = [('John', 'john@example.com'), ('Maria', 'maria@mailserver.org'), ('Kate', 'kate@mailserver.org')]
>>> print(tabulate(data, headers=['Login', 'E-mail']))
Login    E-mail
-------  --------------------
John     john@example.com
Maria    maria@mailserver.org
Kate     kate@mailserver.org
```

### Порядковые номера

Для отображения порядковых номеров необходимо добавить аргумент `showindex="always"`.

```python
>>> print(tabulate(data, headers=['ID', 'Login', 'E-mail'], showindex='always'))
  ID  Login    E-mail
----  -------  --------------------
   0  John     john@example.com
   1  Maria    maria@mailserver.org
   2  Kate     kate@mailserver.org
```

### Вид таблицы

Вид таблицы определяется значением параметра `tablefmt`.

Поддерживаются следующие значения:

- "plain"
- "simple" (по умолчанию)
- "github"
- "grid"
- "fancy_grid"
- "pipe"
- "orgtbl"
- "jira"
- "presto"
- "pretty"
- "psql"
- "rst"
- "mediawiki"
- "moinmoin"
- "youtrack"
- "html"
- "unsafehtml"
- "latex"
- "latex_raw"
- "latex_booktabs"
- "latex_longtable"
- "textile"
- "tsv"

```python
>>> print(tabulate(data, headers=['Login', 'E-mail'], tablefmt='github'))
| Login   | E-mail               |
|---------|----------------------|
| John    | john@example.com     |
| Maria   | maria@mailserver.org |
| Kate    | kate@mailserver.org  |
```
