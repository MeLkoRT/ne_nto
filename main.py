import requests
import datetime as dt
import tables

def temperature_and_humidity_sensors():
    sensors = []
    for i in range(1, 5):
        link = f'https://dt.miet.ru/ppo_it/api/temp_hum/{i}'
        response = requests.get(link)
        sensors.append(response.json())
    return sensors


def air_temperature():
    sensors = []
    cur_time = dt.datetime.now()
    for i in range(1, 7):
        link = f'https://dt.miet.ru/ppo_it/api/hum/{i}'
        response = requests.get(link)
        resp = response.json()
        sens = Air_sens()
        sens.device_id = resp['id']
        sens.hum = resp['humidity']
        sens.time = cur_time
        sensors.append(sens)
    return sensors


def window_pane_control(state):
    link = f'https://dt.miet.ru/ppo_it/api/fork_drive?state={state}'
    response = requests.patch(link)
    return response.json()


def management_of_watering_beds(state, id):
    link = f'https://dt.miet.ru/ppo_it/api/watering?state={state}&id={id}'
    response = requests.patch(link)
    return response.json()


def control_of_the_humidification_system(state_value):
    link = f'https://dt.miet.ru/ppo_it/api/total_hum?state={state_value}'
    response = requests.patch(link)
    return response.json()


print(air_temperature())
