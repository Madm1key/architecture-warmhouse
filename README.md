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

[C4 Containers TO BE](https://editor.plantuml.com/uml/hPDDRzGm48Rl-HL3n24hiSc54n9IbnQfe2s4JNkE77kQMF8NjhEbGlntnabsDprKui0fpdmyy-OTvof4vkEeLVP66gv6WJ34wCA7glBigUnb7CPk3EYvDH5DBBdLbLFCf9vjY4B9hhf-lwrJwE5kNsaM8deAjTVKmQH1Nxh4pshqmPeYmTv1_a2Fd9wDflbmQpL2UAPM3QaWtsHPCxssd-ne1FFFHNXPFQVp3VpE0Cwp2cqxgN3d75NVJMTWpYd9MPJMqCIt0WFt7_FQswEaCp3ECGI85k908gO9mqKFILdpWsD9XpIzmgrZ_N_6CoS9lwk_mEurRC8HDza47d-E629PevaXCG6S6lkjDA2j61LIWbkbaCS0qZnQhoSWF7ghJoN9wvM4cwuG7McuOP5rBE1gU1EjFqrcHe30e-G8WYe9yYVBpf3sywzOpFoNMvjZAoQr69B7EdLAGe5bNyA09DNqa2wUjsf9RfBQ0whb6gstJJSgVSibEQzg2K_nLVbiT8D6XBEBjAHq9M_lx-kc-jfy_xRW9j2_DgIETZylSZBoW4o4widBI48IuiT-vhQ7kUhYqmIdFuoMAMXr7ZdA8pc-E7n5-VGh_GK0)

**Диаграмма компонентов (Components)**

[C4 Components TO BE](https://editor.plantuml.com/uml/bLHRQzim57xthz3C7X98ufSz3GRjaa4taYwhs-SWssUEG1UZ8xShO_zzHv8JNvQs30AopkNxldDHhj1nwrebatT2bxAjW1sTQ_1Zbbd-jAg5ExP5Ys1BenrejogDoXh9jSzPegkaABBrX-NUcnvssqnnT639T5WRrHZjSngFd-p1ej4p3xPWwGCTAPsv8dvsOnGmVAPKnNn0Ea-IF5mFdqshAswVPpYEZkvqpdudZAr97HSQxAoKWYWfT1q-s7NJI55o9umcklSLO6a_fJjJ20cCzyu5Gw5h2Sk6roE7bp8WwFLG3D5Sxx-EEA8Udz1L7mhEmJwA4hgwMNST20fc2xL0PpizZJK_lKZ5DKbIeIhUkYDzzDB6LCfKhOIUR1Vk5-ZkW5TKBbF0iRK1dDgBe8FLpzeQIQSYyWh_uQd0u_Kyct2_oDDNnAAwI7F6Nb3L9OX76h_ZhaNMDXLtWB7j0z9D4JgvAJmVTxpWE6JAdR60ONaO0V2fPagFgjy0Y44lGSGIte0ODZLW_4aI-lKhzENNQLJZbOws0I2bQ2Y9HvwSR0QhUiMEG2qTJ2ewvxvfTo2xDtP-2hHSU7ATZEEj7Cs9niAagOL_CEdD_Vq-pxxbtsy9OGWmtO5TMDFEZA-cJjVqFxTn2ksn3zlfyfyRxD4nAZZSWgYFXR7Ju6anmuwDEdLUmO2QFLdXOh7vZsrNvGHhi7KlvrpK_ahE5VN6_wd-1G00)

**Диаграмма кода (Code)**

- [C4_Code_DeviceService](https://editor.plantuml.com/uml/NOzD2i8m48NtESNGfP0Um8KKx0dC2OPsq68cAPc9KCIxczQVYDllVJpUwqGnQMPlPXokU2OO8hV21LuYKplIRHe8xWQ0GcPe-WquHStI00hqpfJmXOynQ8hUKm9h3s_eA6qTUyX2ydK_k8edcgDC6jFox_uaLIyIOoYJgmSxQzT13zDH6DTNJm00)
- [C4_Code_ModuleService](https://editor.plantuml.com/uml/VP0z3i8m38NtdCBgtXo00LKgIuSkS88eDH2HFyK94aBS7RSKjO34PCllUy-M6yegvUAiY4fVr0b11oV9yV0S74eNXc8HxWB0-8pfg3H2rK_JDdYFEeTKWIBeMsQqLKG_UkUYdPbECCK5P8boonrimB2C3dscKPki1qnNmvlgUcOAuQ9oS4x1MamluCFonQwJTZYsFIegQLgunnZ8y8MtnVOFMeUyPNOwvVbp91wYGJ-Cptm2)
- [C4_Code_UserService](https://editor.plantuml.com/uml/SoWkIImgAStDuIf8JCvEJ4zLICxFrIlE1GfcvEUcwfKMfnOfL7CfA8G26SxvUIL5-JavG25TNJkmK71gKLbcSgg2bG9GPJ5K7KmGfYWejI2_EBCalwWIjph7qf8C3CEG1NLpKjDA21Y890wp6wWWDp4FwB5YhbekXzIy591V0G00)

# Задание 3. Разработка ER-диаграммы

[ER-диаграмма](https://editor.plantuml.com/uml/jLJ9Ri8m4BtxAzmRI8rAAt69eeXJBxtq3o8h7eebBy7si0Zwxns3I4be8v3WuiFCc_6yDyiiHE4Z6isU9CoL1VxvCTgCUO7bfdZ1iZM_7yqgcLN96DYeufPZ0CztZASm9SSyvuXAygBu0WjUH91bITuieoTXhJ10e9NmzKBuqTjqIaaBj6g9yCojYzoYreSOC4BfAx6D267jlAmM8YmkOphOsaEggnAHW54P80bCqqTX8_z0iU-MkOILgk5QxZVm9gNTcX9KdPnzoF7xAcuR60PgLuked1r04RM8uQoywUHHgfsgUOnkQS86UDwrymVf7qC3DZ5jYgwCawY7-djVHWP4G0-6hDSI-vt4_uiacl6C_ElaShfMGcCIQAuT5KbEr3UI93A7MxJVPvdRdROpvxHAeUDf9p3dT2pOUJFxiIfmmLfytrix6uMofnHTVqVBd7kewJe5DWChqx7z0G00)

# Задание 4. Создание и документирование API

### 1. Тип API

Для интеграции будет использоваться RESTful API. Причины решения:

- Простота использования: RESTful API использует стандартные HTTP методы (GET, POST, PUT, DELETE),
  что делает его простым для понимания и использования разработчиками.
- Широкая поддержка: RESTful API поддерживается большинством современных языков программирования и
  фреймворков
- Большинство операций в системе являются синхронными и не требуют сложной обработки сообщений

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
