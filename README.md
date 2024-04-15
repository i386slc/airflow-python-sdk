# airflow-python-sdk

## Overview

Этот пакет Python автоматически генерируется [OpenAPI Generator](https://openapi-generator.tech) проект, основанный на [specs](https://github.com/zachliu/airflow-openapi-specs):

- API версия: 1.0.0
- Версия пакета: 1.0.1
- Пакет сборки: org.openapitools.codegen.languages.PythonClientCodegen

Для получения дополнительной информации, пожалуйста, Google самостоятельно `¯\_(ツ)_/¯`

## Требования.

Python >= 3.6

## Установка и использование
### pip install

Пакет Python размещен на PyPI, его можно установить напрямую, используя:

```sh
pip install airflow-python-sdk
```

Затем импортируйте пакет:
```python
import airflow_python_sdk
```

### Setuptools

Установка через [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(или `sudo python setup.py install` установить пакет для всех пользователей)

Затем импортируйте пакет:
```python
import airflow_python_sdk
```

## Приступаем к работе

Пожалуйста, следуйте [порядку установки](#installation--usage) а затем запустите следующее:

```python

import time
import airflow_python_sdk
from pprint import pprint
from airflow_python_sdk.api import config_api
from airflow_python_sdk.model.config import Config
from airflow_python_sdk.model.error import Error
# Определение хоста не является обязательным и по умолчанию http://localhost/api/v1
# См. файл configuration.py для получения списка всех поддерживаемых параметров конфигурации.
configuration = airflow_python_sdk.Configuration(
    host = "http://localhost/api/v1"
)

# Клиент должен настроить параметры аутентификации и авторизации в соответствии
# с политикой безопасности API-сервера.
# Ниже приведены примеры для каждого метода аутентификации.
# Используйте пример, соответствующий вашему варианту использования аутентификации.

# Настройка базовой авторизации HTTP: Basic
configuration = airflow_python_sdk.Configuration(
    host = "https://<your-airflow-2.0.0>/api/v1",
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Введите контекст с экземпляром клиента API
with airflow_python_sdk.ApiClient(configuration) as api_client:
    # Создайте экземпляр класса API
    api_instance = config_api.ConfigApi(api_client)

    try:
        # Получить текущую конфигурацию
        api_response = api_instance.get_config()
        pprint(api_response)
    except airflow_python_sdk.ApiException as e:
        print("Exception when calling ConfigApi->get_config: %s\n" % e)
```

## Документация для конечных точек API

Все URI относятся к *http://localhost/api/v1*

Класс | Метод | HTTP запрос | Описание
------------ | ------------- | ------------- | -------------
*ConfigApi* | [**get_config**](docs/ConfigApi.md#get_config) | **GET** /config | Получить текущую конфигурацию
*ConnectionApi* | [**delete_connection**](docs/ConnectionApi.md#delete_connection) | **DELETE** /connections/{connection_id} | Удалить соединение
*ConnectionApi* | [**get_connection**](docs/ConnectionApi.md#get_connection) | **GET** /connections/{connection_id} | Получить соединение
*ConnectionApi* | [**get_connections**](docs/ConnectionApi.md#get_connections) | **GET** /connections | Получение списка соединений
*ConnectionApi* | [**patch_connection**](docs/ConnectionApi.md#patch_connection) | **PATCH** /connections/{connection_id} | Обновить соединение
*ConnectionApi* | [**post_connection**](docs/ConnectionApi.md#post_connection) | **POST** /connections | Создать соединение
*DAGApi* | [**get_dag**](docs/DAGApi.md#get_dag) | **GET** /dags/{dag_id} | Получите базовую информацию о DAG
*DAGApi* | [**get_dag_details**](docs/DAGApi.md#get_dag_details) | **GET** /dags/{dag_id}/details | Получите упрощенное представление DAG
*DAGApi* | [**get_dag_source**](docs/DAGApi.md#get_dag_source) | **GET** /dagSources/{file_token} | Получить исходный код
*DAGApi* | [**get_dags**](docs/DAGApi.md#get_dags) | **GET** /dags | Список DAG'ов
*DAGApi* | [**get_task**](docs/DAGApi.md#get_task) | **GET** /dags/{dag_id}/tasks/{task_id} | Получите упрощенное представление задачи
*DAGApi* | [**get_tasks**](docs/DAGApi.md#get_tasks) | **GET** /dags/{dag_id}/tasks | Получите задачи на DAG
*DAGApi* | [**patch_dag**](docs/DAGApi.md#patch_dag) | **PATCH** /dags/{dag_id} | Обновить DAG
*DAGApi* | [**post_clear_task_instances**](docs/DAGApi.md#post_clear_task_instances) | **POST** /dags/{dag_id}/clearTaskInstances | Очистить набор экземпляров задачи
*DAGApi* | [**post_set_task_instances_state**](docs/DAGApi.md#post_set_task_instances_state) | **POST** /dags/{dag_id}/updateTaskInstancesState | Установить состояние экземпляров задачи
*DAGRunApi* | [**delete_dag_run**](docs/DAGRunApi.md#delete_dag_run) | **DELETE** /dags/{dag_id}/dagRuns/{dag_run_id} | Удалить DAGrun
*DAGRunApi* | [**get_dag_run**](docs/DAGRunApi.md#get_dag_run) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id} | Получить DAGrun
*DAGRunApi* | [**get_dag_runs**](docs/DAGRunApi.md#get_dag_runs) | **GET** /dags/{dag_id}/dagRuns | Список DAGruns
*DAGRunApi* | [**get_dag_runs_batch**](docs/DAGRunApi.md#get_dag_runs_batch) | **POST** /dags/~/dagRuns/list | Список DAGruns (пакет)
*DAGRunApi* | [**post_dag_run**](docs/DAGRunApi.md#post_dag_run) | **POST** /dags/{dag_id}/dagRuns | Запустить новый DAGrun
*EventLogApi* | [**get_event_log**](docs/EventLogApi.md#get_event_log) | **GET** /eventLogs/{event_log_id} | Получить запись в журнале логов
*EventLogApi* | [**get_event_logs**](docs/EventLogApi.md#get_event_logs) | **GET** /eventLogs | Список записей журнала логов
*ImportErrorApi* | [**get_import_error**](docs/ImportErrorApi.md#get_import_error) | **GET** /importErrors/{import_error_id} | Получить ошибку импорта
*ImportErrorApi* | [**get_import_errors**](docs/ImportErrorApi.md#get_import_errors) | **GET** /importErrors | Список ошибок импорта
*MonitoringApi* | [**get_health**](docs/MonitoringApi.md#get_health) | **GET** /health | Получить статус экземпляра
*MonitoringApi* | [**get_version**](docs/MonitoringApi.md#get_version) | **GET** /version | Получить информацию о версии
*PoolApi* | [**delete_pool**](docs/PoolApi.md#delete_pool) | **DELETE** /pools/{pool_name} | Удалить пул
*PoolApi* | [**get_pool**](docs/PoolApi.md#get_pool) | **GET** /pools/{pool_name} | Получить пул
*PoolApi* | [**get_pools**](docs/PoolApi.md#get_pools) | **GET** /pools | Список пулов
*PoolApi* | [**patch_pool**](docs/PoolApi.md#patch_pool) | **PATCH** /pools/{pool_name} | Обновить пул
*PoolApi* | [**post_pool**](docs/PoolApi.md#post_pool) | **POST** /pools | Создать пул
*TaskInstanceApi* | [**get_extra_links**](docs/TaskInstanceApi.md#get_extra_links) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/links | Список дополнительных ссылок
*TaskInstanceApi* | [**get_log**](docs/TaskInstanceApi.md#get_log) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/logs/{task_try_number} | Получить логи
*TaskInstanceApi* | [**get_task_instance**](docs/TaskInstanceApi.md#get_task_instance) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id} | Получить экземпляр задачи
*TaskInstanceApi* | [**get_task_instances**](docs/TaskInstanceApi.md#get_task_instances) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances | Получение списка экземпляров задач
*TaskInstanceApi* | [**get_task_instances_batch**](docs/TaskInstanceApi.md#get_task_instances_batch) | **POST** /dags/~/dagRuns/~/taskInstances/list | Получение списка экземпляров задач (пакет)
*VariableApi* | [**delete_variable**](docs/VariableApi.md#delete_variable) | **DELETE** /variables/{variable_key} | Удалить переменную
*VariableApi* | [**get_variable**](docs/VariableApi.md#get_variable) | **GET** /variables/{variable_key} | Получить переменную
*VariableApi* | [**get_variables**](docs/VariableApi.md#get_variables) | **GET** /variables | Список переменных
*VariableApi* | [**patch_variable**](docs/VariableApi.md#patch_variable) | **PATCH** /variables/{variable_key} | Update a variable
*VariableApi* | [**post_variables**](docs/VariableApi.md#post_variables) | **POST** /variables | Создать переменную
*XComApi* | [**get_xcom_entries**](docs/XComApi.md#get_xcom_entries) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries | Список записей XCom
*XComApi* | [**get_xcom_entry**](docs/XComApi.md#get_xcom_entry) | **GET** /dags/{dag_id}/dagRuns/{dag_run_id}/taskInstances/{task_id}/xcomEntries/{xcom_key} | Получить запись XCom


## Документация для моделей

 - [ClassReference](docs/ClassReference.md)
 - [ClearTaskInstance](docs/ClearTaskInstance.md)
 - [CollectionInfo](docs/CollectionInfo.md)
 - [Color](docs/Color.md)
 - [Config](docs/Config.md)
 - [ConfigOption](docs/ConfigOption.md)
 - [ConfigSection](docs/ConfigSection.md)
 - [Connection](docs/Connection.md)
 - [ConnectionAllOf](docs/ConnectionAllOf.md)
 - [ConnectionCollection](docs/ConnectionCollection.md)
 - [ConnectionCollectionAllOf](docs/ConnectionCollectionAllOf.md)
 - [ConnectionCollectionItem](docs/ConnectionCollectionItem.md)
 - [CronExpression](docs/CronExpression.md)
 - [DAG](docs/DAG.md)
 - [DAGCollection](docs/DAGCollection.md)
 - [DAGCollectionAllOf](docs/DAGCollectionAllOf.md)
 - [DAGDetail](docs/DAGDetail.md)
 - [DAGDetailAllOf](docs/DAGDetailAllOf.md)
 - [DAGRun](docs/DAGRun.md)
 - [DAGRunCollection](docs/DAGRunCollection.md)
 - [DAGRunCollectionAllOf](docs/DAGRunCollectionAllOf.md)
 - [DagState](docs/DagState.md)
 - [Error](docs/Error.md)
 - [EventLog](docs/EventLog.md)
 - [EventLogCollection](docs/EventLogCollection.md)
 - [EventLogCollectionAllOf](docs/EventLogCollectionAllOf.md)
 - [ExtraLink](docs/ExtraLink.md)
 - [ExtraLinkCollection](docs/ExtraLinkCollection.md)
 - [HealthInfo](docs/HealthInfo.md)
 - [HealthStatus](docs/HealthStatus.md)
 - [ImportError](docs/ImportError.md)
 - [ImportErrorCollection](docs/ImportErrorCollection.md)
 - [ImportErrorCollectionAllOf](docs/ImportErrorCollectionAllOf.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [ListDagRunsForm](docs/ListDagRunsForm.md)
 - [ListTaskInstanceForm](docs/ListTaskInstanceForm.md)
 - [MetadatabaseStatus](docs/MetadatabaseStatus.md)
 - [Pool](docs/Pool.md)
 - [PoolCollection](docs/PoolCollection.md)
 - [PoolCollectionAllOf](docs/PoolCollectionAllOf.md)
 - [RelativeDelta](docs/RelativeDelta.md)
 - [SLAMiss](docs/SLAMiss.md)
 - [ScheduleInterval](docs/ScheduleInterval.md)
 - [SchedulerStatus](docs/SchedulerStatus.md)
 - [Tag](docs/Tag.md)
 - [Task](docs/Task.md)
 - [TaskCollection](docs/TaskCollection.md)
 - [TaskCollectionAllOf](docs/TaskCollectionAllOf.md)
 - [TaskExtraLinks](docs/TaskExtraLinks.md)
 - [TaskInstance](docs/TaskInstance.md)
 - [TaskInstanceCollection](docs/TaskInstanceCollection.md)
 - [TaskInstanceCollectionAllOf](docs/TaskInstanceCollectionAllOf.md)
 - [TaskInstanceReference](docs/TaskInstanceReference.md)
 - [TaskInstanceReferenceCollection](docs/TaskInstanceReferenceCollection.md)
 - [TaskState](docs/TaskState.md)
 - [TimeDelta](docs/TimeDelta.md)
 - [TriggerRule](docs/TriggerRule.md)
 - [UpdateTaskInstancesState](docs/UpdateTaskInstancesState.md)
 - [Variable](docs/Variable.md)
 - [VariableAllOf](docs/VariableAllOf.md)
 - [VariableCollection](docs/VariableCollection.md)
 - [VariableCollectionAllOf](docs/VariableCollectionAllOf.md)
 - [VariableCollectionItem](docs/VariableCollectionItem.md)
 - [VersionInfo](docs/VersionInfo.md)
 - [WeightRule](docs/WeightRule.md)
 - [XCom](docs/XCom.md)
 - [XComAllOf](docs/XComAllOf.md)
 - [XComCollection](docs/XComCollection.md)
 - [XComCollectionAllOf](docs/XComCollectionAllOf.md)
 - [XComCollectionItem](docs/XComCollectionItem.md)


## Документация для авторизации


## Базовая

- **Type**: Базовая HTTP-аутентификация


## Kerberos



## Автор

zach.z.liu@gmail.com


## Примечания для больших документов OpenAPI
Если документ OpenAPI большой, импорт в airflow_python_sdk.apis и airflow_python_sdk.models
может завершиться неудачно с ошибкой RecursionError, указывающей на превышение максимального предела рекурсии.
В таком случае есть несколько решений:

Решение 1:
Используйте специальный импорт для API и моделей, таких как:
- `from airflow_python_sdk.api.default_api import DefaultApi`
- `from airflow_python_sdk.model.pet import Pet`

Решение 1:
Перед импортом пакета настройте максимальный предел рекурсии, как показано ниже:
```python
import sys
sys.setrecursionlimit(1500)
import airflow_python_sdk
from airflow_python_sdk.apis import *
from airflow_python_sdk.models import *
```
