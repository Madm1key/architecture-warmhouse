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

[C4 Containers TO BE](https://editor.plantuml.com/uml/hLFBRjim4BphArYX1ncefKjF1Gh4YGkuXTqwLd8sA78Z4-MhVCGDYlvxbvJiA6aGzD0JfUNExEpEyi87wa9KidWZD9EH0pc4OFs7fd7qMFSY768NFJXcT00TQcPKOoNL2JFtWKlHDLVlvziKkjsi6qLz08UX_HKYgD3WQfluYoquRtILoDwHyXQF4izMONsoCWg8Vq2e8YcXd1L5ct_tboPgJjr3vPzc3zVbZFmg23dNgfJfX8I5jPYzoT-4MYi5eq4OZHNVSl3CVImNKfgZpzL8C4HHJNlKa0iSKW4EzuA1HobJVczfqY5qBs5k4-H_qY-xYdV8lwI1TjJ3XB0Dni58oF6QKCr74eBct8a-kYpY6ULrX0XLvyptFFSDU9-K3849_xC-gHMOlTX-9eiN-rjXUObw7Fo8u8CdTyuemgJ09KaAVXTdhlsddm5zuL72Kmk7s8GK8HeOjYvFbwI2kgy9Ecq1suiEPmZQ6pTBAx83EUxJr7PShQJWyNBmR0pd-2HzQBG5pIVD19DsStLpissRB-sthoDT9lfNG4BiryCWiwaxe7oSK_Bkw4I04xAzNfyWom5oTkmrsDy5TmFwSTnP9xvQt42UO9d40GDnZpHvan8tuYymDRtKFm00)

**Диаграмма компонентов (Components)**

[C4 Components TO BE](https://editor.plantuml.com/uml/hLLVRvim47_dKtXe3qHQafSzJPhKDDcKJKb3Iw9gJv616x5cR6IRPjtKxzwp8U1qLCkaFM7Ez_jpnvsuqeOgKvSyUCD4nkiSoC6OId-OJXKzJWfc3dLQQr2P50Q4cMIod5QS2eiPQvDpbaxdxyUn3UtMgsb9jG65eVrSbfKK5bDP_jNissQttMytyNwnkR-9Ha4GWz9IH9R-7Gbt-0ZncPJeY2nb2KG_8bb9R4A8-ObxtL_BMkHKFKRwFBkv3aVaTq387FrI9a15fKmPXrbLOVRQdGcjAiuoQfWKgFWs1vsfZ-6CStdKJeqOIKegQ84UdC312kJmm3BGQCNdrnMrFfWeE8mh2_cVz7srr5KmYx-GcSVVL6i1RRUZd1eQAvbXyWAFn9v1Q_H74b1MmZFLNe8c5aOKPC0U82VVbInzRwNCQzvwyyLeRGxM5JxmjJKreBEa8aTyKpqzpyOh5vAA_MgBUbcIwumjo1q6-DUkc_e2oxSrr12bIlvmKxV6wkrtk7O1Z_4ppHXdXXfanQ4lQt7ocu8v0WYY6nVQ5V2AsY9ruxr8sw-HKktRJenKfwxO3p00Rsh_2q6Jr5Cy1Kz1qC_GfvycQWoURqmJy-WG8Y135Nww915CYWd1nQf0KLCh75aGMggHtSWxuEtw-bk6csmRqLysAzA6NTnBRqVe3WgcZUf7Wik2sVq9bzjjd4o_9fkRbjJH_JlCq-m6gfcRRlLULRiKu13z1dPDlmEQQxTLVoPritYlc9qs8v5smCZ9GvVlaGxwQ5hKpL-VxXfrzDJ2v7RrGiMRkmk1NK63q3xv2aHk_mZF)

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
