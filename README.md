# Project_template

Это шаблон для решения проектной работы. Структура этого файла повторяет структуру заданий.
Заполняйте его по мере работы над решением.

# Задание 1. Анализ и планирование

### 1. Описание функциональности монолитного приложения

**Управление отоплением:**

- Пользователь может управлять отоплением.

**Мониторинг температуры:**

- Пользователь может проверять температуру по локации;
- система поддерживает получение данных от датчиков.

### 2. Анализ архитектуры монолитного приложения

- **Язык программирования:** Go
- **БД:** PostgreSQL
- **Архитектура:** монолит
- **Взаимодействие**: синхронное
- **Масштабируемость:** недоступно масштабирование по частям
- **Развертываемость:** требует остановки всего приложения

### 3. Определение доменов и границы контекстов

- Управление отоплением;
- мониторинг температуры.

### **4. Проблемы монолитного решения**

- Не поддерживает самостоятельное подключение датчиков;
- не поддерживает датчики других типов;
- не поддерживает масштабирования отдельных частей;
- чтение данные с датчиков происходит синхронно.

### 5. Визуализация контекста системы — диаграмма С4

[C4 Context AS IS](https://editor.plantuml.com/uml/RL1BIyD04BxdLup1GuGskNWIX4eGF5WerfxBTZCsWNs4cTcs_djd4ob5F0txpVVQMR4OakHTSJS4wrA7q8kC_DGqPCxrSP0-7H8ZsHW4WzGs-cPq9cJDagLpmw5f7vUR3EtMxuqtB4WAxTkik4WzPlTYWyGnLDbg0ULEHwbpwpKTtg97u6yLUiY4yg7OJg_AZED_h2nzSIwUUUA3HCZzA3hGxOXa91622HqGMXnE29qH0ryKFJ06ZiJNaFthHQePLDlF6_qCQjXzXspfkLoZOLtmROhw51_eVdys5sxdCWmz6Xd2SP5h37XIfKr4UiS_3jbWabvxw8LonHM6Bj_l1m00)

# Задание 2. Проектирование микросервисной архитектуры

**Диаграмма контейнеров (Containers)**

[C4 Containers TO BE](https://editor.plantuml.com/uml/hPDDRzf048Rl_XLJr8EH2hxqLAbIIAYKLj0Id9ojzUvWLjslxgv9ewh_lREs0ODKAOUSCFFnpEkPrpSXCXzRhR9tqd3L2eHzZ2vyAWhFdkUDZFksRWDwRar44-VSwi8fPbBFB4IXP5tSVPnjKkXflIeq2n4zXQexwc3Ie9-xnCysw8CrUO9zWCaJ_KpejzGq7-wjHWWlrAeX5KocMLPsVwjRsnh1_4iUBglxz6GAVpA0qwnSsregN3X7rUlk6PXpId8MfJKqyRt0mFtdoSRRWwHdO9nZ210jn3s9w2Riptf8ofWV74iwf6aKpXnhtXZFd2JyOlCL5l_39Xnnqvh0uwyMGwJLQ6P8J02dscOc3MWhMeMKu5Ofv360D3lhTGU4dRVwM99sFPAmh7DHauObYwnc0KV3osZzSJ8p0WGU94SGL7dv6WyjjfZNtlxiRhqcnMbJVM04J3CWUcR2Zf2Tg2lznFsRPITmzULtpFlKfHlws0XDBOPUczNgc8GSvyqSzaWhC0qaGtkhXkGqRM6BQh3ds4Nar2JZdEmjC8Ix-AYyFs29HeJJTUZuoUhtZu-RilXM_lW-u3hGQnjIHxNg3T8TQ8jCXEBPoqX24k9XrNEhPLzrslzrvRMGQjitd1VRgQ5FdLmbo4CUESe3dNuuzGtbqpVz3m00)

**Диаграмма компонентов (Components)**

[C4 Components TO BE](https://editor.plantuml.com/uml/hLNVQzim47xtNt4pUqWWYL_sD1WqImVTQBOqRkbZaEsh8oPBGfBRbR7_VITPIPGVC2Y3WEFJtVVTz-akkRAE6TTt8dl7PItw1c7hdBOVYyAmbrdBtRQlUekcLjAXTBDQTOKMJFgQgNMDu5Mn-31T-T33yhRec7LeABHPg4uhwMkqnyzMQAoI8mysWVo17ZazouxuuKPr2FQLIZlm2VauoyhmklciUjamypgonzd3SJw6tnd0WhfZNA8PTQhY0kTQK_OoV0UcjU0rSrn9OdpVeAtDftnbr3Edxy3g6gq5fy1jgOd0i3tqGwsa-5OptmUNhS2fPkr_W4_n3t9Pa31VVOLvGZ38zGNHtE1dYUQPrnXjXVYQT1F21bjkdGb04z16FNbtEYP9HKTG4s0zzIZTdko4gc6EaQxwG7TD4V0XaaYMN62EXsI4hwOUQkJFsC2JKLtgHgUQNg0zvqGFc326zmj4wqHTH9k0HTa0ZIo9R6X-8ZlGqBlUGg-ffy1vJ7hNOu-ZogYVOLINrB-_w26GK0RrH2dj4zaR56dHjrCk4pd7qDTLkB3hAffNCPkAA9qoP9LF2NwTsa7bWo7_01YI3X1_iem-XodxyikDTXwbIpN44ZmgaLWJZTWTmWXdxGosI4xJZVlV1QD4F1nxmMiKSSlJPQGHz7OS3eTDYk4GJzAFf_heRkagGQYM-stBR-xlLsNnhVpnFM8d6AUZimoJ7iFsh3gKXwRUJ1wgtq2xkJtVhVtrh94rqRdD-Zplb2urz2nvFzEFXhlGp0KL9uZxcg6HYxOTEROVy51GlEoeylBkzZ95CjENQwveZ_sVo5y0)

**Диаграмма кода (Code)**

[C4 Code TO BE]()

# Задание 3. Разработка ER-диаграммы

Добавьте сюда ER-диаграмму. Она должна отражать ключевые сущности системы, их атрибуты и тип связей
между ними.

# Задание 4. Создание и документирование API

### 1. Тип API

Укажите, какой тип API вы будете использовать для взаимодействия микросервисов. Объясните своё
решение.

### 2. Документация API

Здесь приложите ссылки на документацию API для микросервисов, которые вы спроектировали в первой
части проектной работы. Для документирования используйте Swagger/OpenAPI или AsyncAPI.

# Задание 5. Работа с docker и docker-compose

Перейдите в apps.

Там находится приложение-монолит для работы с датчиками температуры. В README.md описано как
запустить решение.

Вам нужно:

1) сделать простое приложение temperature-api на любом удобном для вас языке программирования,
   которое при запросе /temperature?location= будет отдавать рандомное значение температуры.

Locations - название комнаты, sensorId - идентификатор названия комнаты

```
	// If no location is provided, use a default based on sensor ID
	if location == "" {
		switch sensorID {
		case "1":
			location = "Living Room"
		case "2":
			location = "Bedroom"
		case "3":
			location = "Kitchen"
		default:
			location = "Unknown"
		}
	}

	// If no sensor ID is provided, generate one based on location
	if sensorID == "" {
		switch location {
		case "Living Room":
			sensorID = "1"
		case "Bedroom":
			sensorID = "2"
		case "Kitchen":
			sensorID = "3"
		default:
			sensorID = "0"
		}
	}
```

2) Приложение следует упаковать в Docker и добавить в docker-compose. Порт по умолчанию должен быть
   8081

3) Кроме того для smart_home приложения требуется база данных - добавьте в docker-compose файл
   настройки для запуска postgres с указанием скрипта инициализации ./smart_home/init.sql

Для проверки можно использовать Postman коллекцию smarthome-api.postman_collection.json и вызвать:

- Create Sensor
- Get All Sensors

Должно при каждом вызове отображаться разное значение температуры

Ревьюер будет проверять точно так же.
