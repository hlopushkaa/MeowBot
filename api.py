# coding: utf-8
# Импортирует поддержку UTF-8.
from __future__ import unicode_literals

# Импортируем модули для работы с JSON и логами.
import json
import logging

# Импортируем подмодули Flask для запуска веб-сервиса.
import requests
from flask import Flask, request
app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG)

is_warmup = False

# Хранилище данных о сессиях.
sessionStorage = {}

# Задаем параметры приложения Flask.
@app.route("/", methods=['POST'])

def main():
# Функция получает тело запроса и возвращает ответ.
    logging.info('Request: %r', request.json)

    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)

    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )



@app.route('/is_warmup')
def warmup_api():
    global is_warmup
    if is_warmup:
        return 'ok'
    else:
        return 'no'

questions = [
    {'question': '', 'answer': 'лето', 'hint': 'Правильный ответ - это лето!'},
    {'question': 'Сколько всего цифр?', 'answer': '10', 'hint': 'К сожалению это неверный ответ, ничего страшного. На самом деле всего 10 цифр: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0.'},
]


# Функция для непосредственной обработки диалога.
def handle_dialog(req, res):
    global is_warmup
    user_id = req['session']['user_id']

    if req['session']['new'] or sessionStorage.get(user_id) is None:
        is_warmup = False
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        sessionStorage[user_id] = {
            'questionId': 0,
            'tries': 0
        }

        res['response']['text'] = '''<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
Привет, ребята!
Меня зовут Сема, я робот МяуБот.
Давайте играть и учиться вместе!
А сейчас начинается увлекательное занятие.
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
Внимательно слушайте задание и отвечайте на них.
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
Первый вопрос: Какое самое жаркое время года?'''
        return


    questionId = sessionStorage[user_id]['questionId']
    question = req['request']['original_utterance']



    try:
        if questionId >= 0:
            answer = questions[questionId]['answer'].lower()

            if question == answer:
                sessionStorage[user_id]['tries'] = 0
                res['response']['text'] = 'Всё верно!\n'
                sessionStorage[user_id]['questionId'] += 1
                if sessionStorage[user_id]['questionId'] == len(questions):
                    res['response']['text'] += '''Ребята, вы очень умные и сообразительные. На эти вопросы вы дали верные ответы.
    Подойдите ко мне поближе и попросите воспитателя выбрать подходящую и интересную для вас игру.
    <speaker audio="dialogs-upload/21248c49-2a8d-45dc-a4f3-baa6e93049fb/e32662ef-6adc-4ac5-ada2-45a27715abbc.opus">
    Я уверен, что это занятие вам точно понравится. Играйте по очереди и обучайтесь вместе. После обучения вас ждет физкульт разминка!
    <speaker audio="dialogs-upload/21248c49-2a8d-45dc-a4f3-baa6e93049fb/e32662ef-6adc-4ac5-ada2-45a27715abbc.opus">
    Ребята, вы большие молодцы!! А теперь физкульт минутка. Давайте вместе потанцуем под музыку. Но для этого вам нужно отойти на расстояние вытянутой руки друг от друга! Выберите песню. Синий трактор, Фиксики, Маша и медведь, Смешарики '''
                    sessionStorage[user_id]['questionId'] = -1
                else:
                    res['response']['text'] += questions[questionId + 1]['question']
            elif question == 'повтори' or question == 'повтори вопрос':
                res['response']['text'] = questions[questionId]['question']
            else:
                sessionStorage[user_id]['tries'] += 1
                if sessionStorage[user_id]['tries'] >= 3:
                    sessionStorage[user_id]['tries'] = 0
                    res['response']['text'] = questions[questionId]['hint'] + '\n'
                    sessionStorage[user_id]['questionId'] += 1
                    if sessionStorage[user_id]['questionId'] == len(questions):
                        res['response']['text'] += '''Ребята, вы очень умные и сообразительные. На эти вопросы вы дали верные ответы.
                    Подойдите ко мне поближе и попросите воспитателя выбрать подходящую и интересную для вас игру.
                    <speaker audio="dialogs-upload/21248c49-2a8d-45dc-a4f3-baa6e93049fb/e32662ef-6adc-4ac5-ada2-45a27715abbc.opus">
                    Я уверен, что это занятие вам точно понравится. Играйте по очереди и обучайтесь вместе. После обучения вас ждет физкульт разминка!
                    <speaker audio="dialogs-upload/21248c49-2a8d-45dc-a4f3-baa6e93049fb/e32662ef-6adc-4ac5-ada2-45a27715abbc.opus">
                    Ребята, вы большие молодцы!! А теперь физкульт минутка. Давайте вместе потанцуем под музыку. Но для этого вам нужно отойти на расстояние вытянутой руки друг от друга! Выберите песню. Синий трактор, Фиксики, Маша и медведь, Смешарики '''
                        sessionStorage[user_id]['questionId'] = -1
                    else:
                        res['response']['text'] += questions[questionId + 1]['question']
                else:
                    res['response']['text'] = 'Неправильно!'
        else:
            if question == 'смешарики':
                res['response']['text'] = '''Включаю песню "Смешарики - от винта!"", повторяйте движения за мной!
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/46884a60-a8bf-49bb-a85e-cec928207035.opus">
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/307260ab-1e4c-49d5-9565-6987bb95dbbe.opus">

Хорошая разминка!
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
Мы можем продолжить заниматься дальше. Хотите продолжить?'''
                is_warmup = True
            elif question == 'маша и медведь':
                res['response']['text'] = '''Включаю песню "Маша и медведь - Рок - н- рол", повторяйте движения за мной!
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/48bced0d-51ba-4bde-b0a3-7b1d9a0cacca.opus">

Хорошая разминка!
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
Мы можем продолжить заниматься дальше. Хотите продолжить?'''
                is_warmup = True
            elif question == 'фиксики':
                res['response']['text'] = '''Включаю песню "Фиксики - Помогатор", повторяйте движения за мной!
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/5c86f3a7-b9aa-434a-998d-37fc23881fe0.opus">

Хорошая разминка!
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
Мы можем продолжить заниматься дальше. Хотите продолжить?'''
                is_warmup = True
            elif question == 'синий трактор':
                res['response']['text'] = '''Включаю песню "синий трактор", повторяйте движения за мной!
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/6dd0216b-40c4-4478-bf2a-faaa9bd79b82.opus">

Хорошая разминка!
<speaker audio="dialogs-upload/6317b3d9-c9fb-41d0-829b-0a3702910e90/ffa2985c-4528-4c31-a4da-c3efc0826d2b.opus">
Мы можем продолжить заниматься дальше. Хотите продолжить? '''
                is_warmup = True
            else:
                res['response']['text'] = 'Такой песни я не знаю..'
    except Exception as e:
        res['response']['text'] = 'Ошибка: ' + str(e)
