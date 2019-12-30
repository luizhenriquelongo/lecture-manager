import re
from datetime import datetime, timedelta

# local import
from error import NotEnoughLecturesError

def lectures_ordered_by_duration(data: list):
    """
        Ordena as palestras com base no seu tempo de duração.
    """
    new_data = []
    for lecture in data:
        lecture = re.split(r'(\d+)', lecture, maxsplit=1)
        
        if len(lecture) == 1:
            if 'lightning' not in lecture[0]:
                raise Exception
            lecture = ''.join(lecture[0].strip())
            lecture = (5, lecture)

        else:
            lecture = (int(lecture[1]), ''.join(lecture))
        new_data.append(lecture)
    
    return sorted(new_data)

def create_dict(data: list):
    """
        Cria um dicionário onde a chave é o tempo de duração da palestra 
        e o valor é uma lista que contém as palestras com essa duração.
    """
    data = lectures_ordered_by_duration(data)
    new_set = {}
    for item in data:
        if item[0] not in new_set:
            new_set[item[0]] = [item[1]]

        else:
            new_set[item[0]].append(item[1])

    return new_set

def total_minutes(data):
    """
        Calcula a quantidade total de minutos com base nas palestras 
        submetidas.
    """
    soma = 0

    for item in data.keys():
        soma += (item*len(data[item]))

    return soma

def start_time(time, value):
    """
        Converte o horario pra um objeto datetime, efetua o cálculo
        da hora de inicio da próxima palestra e retorna um string
        com esse novo horário.
    """
    dt = datetime.strptime(time, "%I:%M%p")
    dt = datetime.combine(dt, dt.time()) + timedelta(minutes=value)

    return datetime.strftime(dt, "%I:%M%p")

def difference(x, y):
    return x - y

def generate_tracks(data):
    """
        Com base no payload recebido pela API, essa função gera as tracks.
        Realiza o calcula de quantas tracks serão possíveis de serem criadas
        com a quantidade de palestras submetidas, distribui as palestras entre
        as tracks com base na regra de negócio.
    """
    data = create_dict(data)
    MINUTES_BY_TRACK = 360
    MINUTES_TOTAL = total_minutes(data)
    TOTAL_TRACKS = MINUTES_TOTAL//MINUTES_BY_TRACK


    # Caso não seja possível criar ao menos 1 track, 
    # o programa gera uma exception
    if TOTAL_TRACKS < 1:
        raise NotEnoughLecturesError
    
    AVG_TRACK_DURATION = MINUTES_TOTAL/TOTAL_TRACKS

    response = {"data": []}

    for track, track_number in enumerate(range(TOTAL_TRACKS)):
        BEFORE_LUNCH = 180    
        AFTER_LUNCH = 240
        TRACK_DURATION = 0
        lectures = {"title": f"Track {track_number+1}", "data": []}

        # Ordena as palestras que serão realizadas antes do almoço
        start = '09:00AM'
        for key in sorted(data.keys(), reverse=True):
            while key <= BEFORE_LUNCH:
                if len(data.get(key)) == 0:
                    break

                else:
                    to_add = f'{start} {data.get(key)[0]}'
                    start = start_time(start, key)
                    lectures['data'].append(to_add)
                    TRACK_DURATION += key
                    data.get(key).pop(0)
                    BEFORE_LUNCH -= key

        # Ordena as palestras que serão realizadas depois do almoço
        lectures['data'].append('12:00PM Lunch')
        start = '01:00PM'
        result = 0

        for key in sorted(data.keys(), reverse=True):
            while key <= AFTER_LUNCH:
                if len(data.get(key)) == 0:
                    break

                else:
                    to_add = f'{start} {data.get(key)[0]}'
                    start = start_time(start, key)
                    lectures['data'].append(to_add)
                    TRACK_DURATION += key
                    data.get(key).pop(0)
                    AFTER_LUNCH -= key

                if (TRACK_DURATION + key) >= (AVG_TRACK_DURATION+result):
                    break
        
        # Pega o tempo que sobrou ou passou do tempo médio das tracks para
        # poder somar com a média da próxima track
        result = difference(TRACK_DURATION, AVG_TRACK_DURATION)
        happy_hour = datetime.strptime(start, "%I:%M%p")
        if track_number == 0:
            last_happy_hour = happy_hour

        else:
            if last_happy_hour < happy_hour:
                last_happy_hour = happy_hour
        
        response['data'].append(lectures)

    # Pega o horário mais tarde entre os happy hour das tracks e adiciona
    # a todas as tracks para que comecem no mesmo horário 
    for track in response['data']:
        happy_hour_time = datetime.strftime(last_happy_hour, '%I:%M%p')     
        track['data'].append(f"{happy_hour_time} Networking Event")

    return response
