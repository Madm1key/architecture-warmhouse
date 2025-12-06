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

[C4 Containers TO BE](https://editor.plantuml.com/uml/hLDDRzGm4BtdLmmHXwp49XTEI4XTMgG5RM7PjEULOq-pblo5FxfKYF_Es4dR5751ukHaPjwRvtdZYn2PZqchwfKqN2M1S8hHXNTTvzcv7MKyfI45zDoQY2QstEhEAMOoPXsYK7BeBj-kzpbqUxthD0iHFOMEbuHWqg1lNUQlzkY3DKqcUmFrBHqrdRsc_h2r6Y4y45H3BgXNLTMNt-C7cunW_g49BwkdTBs2dnN0Kwz6sq4gt3X7rTVb6vXpId8MfJNKyRN0mFtxUgEKFOVI3Q85pGmRIKDfSCeD1DvBZe6aBFc3Orc7DAF2jSkG_qb_DJHY8Fuh5jd00Yu8-sWzpeI2qi2Cc4c0pBcJO_95n9-AcPF4kDb_WirVbMw9I16pn-y9Gmnmvwq6hYJPdRb-LKzSnuy_8arO98KlpPXY2rA26EHq2VMOX0RRiGNop249JPwcWIPOlyfc7r3Dcx4qa9OaAtXEJjDVX1VLqprxD69nbsZpacrlRlPzzxd_-cM65Pv_01ntqnYBEGTaOfvIzk3iPSH7OFzjDoCE4-9vMgKFFHzQ1P7B2zWZHtbFy69fvYJu1PNc9_CR)

**Диаграмма компонентов (Components)**

[C4 Components TO BE]()

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
