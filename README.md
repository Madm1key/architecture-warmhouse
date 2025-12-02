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

[C4 Context AS IS](https://editor.plantuml.com/uml/RL0xQyD03DxzArJJmON4NZeL0Wccj4C3eMdcSB7Ls70l93cFVr-TNK8edSJfUvwMB8PaS3Pxw7rZXnQX4udyKbLapkMnbsuu38pK12_efMo2gw8rFcdcBAtj3rNzFD-arMxzKJd3WgIhVPqK5obZSiysI1nyaQncaEzqv3gtJjFXFJW4lghGGIBaJzbsV1KcnlzOIRgoDfnvv8C4IFqeM50q8XaP2C7u5WWRx4y8hH43tnGSC7eEnEhnADU8Y_mjt0BthnSf9e96VDrvJSiaQf4RMkHhDAm0toUgJ_Q9zlUNK_bwAiRGeP7U7sUfKeydLJO3aTxqZqCo6AMt7dejLc29last_040)

# Задание 2. Проектирование микросервисной архитектуры

**Диаграмма контейнеров (Containers)**

[C4 Containers TO BE](https://editor.plantuml.com/uml/hLF1Rjim3BtxApIZ1mTOx4jF0mOqQmTaHRfvSNiEP8br1CYIAj7DWc7_FafnQmVRfK1ziKtnlKVoKLS1kSUXrza7POGU9B0zeWkVgihpGzaft0_j4C0BQn0CbiBsbTFSHCmoeDIghQulbtKCFTnjgfu714-XtJKXk3BWInVvinfyiAQ8P1zP_a2ldDvDJ_fiRNjWuKZGdiM4V95bJVhTVR63aTmVYt2UVJhE5-ntnkXvLIjwsoeDA-Se_ovzC-wSLeAZieOqBoG4uJ_dAwtj8IGzXfRrtF2EgaWI-oWXuLa925JCkK9mFDQYJATXwIBeVGLksaAsf733aRSyG9nJRGDs7fgVcvb0WzR3A20fcN4ZHr96XZsgRl2fg7zxw3Z2WH-9ULL_Owl_rhycEaty7fu621ZOexSz4rhH8aJ6Fzaht-xhBwJ9oq73kKsds8oK80O4DQPV3ba1PLSoSjC1bJjucX6OOFqYhi4MzBWpSsDfVM85q-79arbubZtrse2HitxGnj6kx-_hfhfjVdmVeOdhZQ3TPXffCcyBN8uJYwuSl49u0KSNJwZjX9gcb_Jeej72o0X911u4g6UYI4P7NgAuejHukVu2)

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
