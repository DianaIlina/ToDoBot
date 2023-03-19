import random
import telebot
from cfg import TOKEN
from Database import read_help_from_file, read_saves_from_file, read_tasks_from_file, write_saves_to_file, write_tasks_to_file


# мы создаем переменную bot, в которой будут содержаться те функции, которые нам нужны для обработки и ответа на
# сообщение
bot = telebot.TeleBot(TOKEN)

HELP = read_help_from_file()
saves = read_saves_from_file()
tasks = read_tasks_from_file()

# random_tasks = ["sport", "grocery", "playing piano", "study"]


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)


def save_me(key, note):
    if key in saves:
        saves[key].append(note)
    else:
        saves[key] = []
        saves[key].append(note)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    write_tasks_to_file(tasks)
    text = "Задача " + task + " на " + date + " добавлена!"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["save"])
def save(message):
    command = message.text.split(maxsplit=2)
    key = command[1].lower()
    note = command[2]
    save_me(key, note)
    text = "Запись " + note + " добавлена в хэштег " + key
    write_saves_to_file(saves)
    bot.send_message(message.chat.id, text)


# @bot.message_handler(commands=["random"])
# def random_add(message):
#     date = "cегодня"
#     task = random.choice(random_tasks)
#     add_todo(date, task)
#     text = "На сегодня появилась задача " + task + "!"
#     bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["show", "print"])
def show_tasks(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "-" + task + "\n"  # \n - перевод строки
    else:
        text = "День свободен"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["list"])
def show_list(message):
    key = message.text.split(maxsplit=1)[1]
    text = ""
    if key in saves:
        text = key.upper() + "\n"
        for note in saves[key]:
            text = text + "-" + note + "\n"
    else:
        text = "Такого тэга ещё нет"
    bot.send_message(message.chat.id, text)


@bot.message_handler(command=["keys"])
def show_keys(message):

    bot.send_message(message.chat.id, print(list(saves.keys())))


# @bot.message_handler(commands=["done"])
# def remove_note(message):
#     key = message.text.split(maxsplit=1)[1]
#     if key in saves:


# функция polling начинает отправку запросов в телеграм с заданным токеном и спрашивает, нет ли для него сообщений.
# Если сообщение есть, то вызывается обработка. Long polling - процесс постоянного обращения к серверам
bot.polling(none_stop=True)

# contrl^C - остановка бота
