# User Events Pipeline

## Описание пайплайна
Пайплайн для переноса данных о событиях пользователей из PostgreSQL в ClickHouse через Kafka с защитой от дублирования.

## Компоненты
1. **init_producer.py** - Генератор создает тестовые сообщения пользователей. Данные попадают в Kafka топик 'user_events_data'
2. **consumer_to_pg.py** - Cохраняет сообщения из топика 'user_events_data' в таблицу PostgreSQL
3. **producer_pg_to_kafka.py** - Создает новые сообщения из PostgreSQL и отправляет в топик 'user_events' Kafka
4. **consumer_to_clickhouse.py** - Получает события из топика 'user_events' Kafka и сохраняет в ClickHouse

  
## Запуск
1. python init_producer.py
2. python consumer_to_pg.py
3. python producer_pg_to_kafka.py
4. python consumer_to_clickhouse.py
