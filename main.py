from dummy_server.server import get_random_request
from datetime import datetime, timedelta

# Dummy server generates random requests, 
# your goal is to process them as per task requirements (see README.md)


def view_text(d: datetime, c: str) -> str:
    weekday = d.weekday()
    if weekday == 5:
        return '6️⃣'
    elif weekday == 6:
        return '7️⃣'
    else:
        string = c.lower().replace(',', '')
        list_words = string.split(' ')
        set_words = set(list_words)
        count_unique_words = str(len(set_words))
        return count_unique_words


def view_image(d: datetime, c: str) -> str:
    file_name, file_extension = c.split('.')
    file_extension.lower()
    if file_extension == 'jpg':
        return file_name
    else:
        date_substr_24_hour = d - timedelta(days=1)
        return date_substr_24_hour.strftime("%m/%d/%Y")


def view_video(d: datetime, c: str) -> str:
    weekday = d.weekday()
    file_name, file_extension = c.split('.')
    file_extension.lower()
    if weekday == 5 or weekday == 6:
        if len(file_extension) == 4:
            return "OK"
        else:
            return "REJECT"
    else:
        if len(file_extension) == 3:
            return "OK"
        else:
            return "REJECT"


def find_unique_char(s: str) -> str:
    cache = set()

    if s == '':
        return 'None'
    for item in s:
        if item not in cache:
            if s.count(item) == 1:
                return item
            else:
                cache.add(item)
    return 'None'


def view_sound(c: str) -> str:
    return find_unique_char(c)


if __name__ == "__main__":
    count_request_type = {
        'text': 0,
        'image': 0,
        'video': 0,
        'sound': 0
    }
    while count_request_type['text'] < 2 or count_request_type['video'] < 2 or count_request_type['image'] < 2 \
            or count_request_type['sound'] < 2:
        request = get_random_request()
        print(request)
        # process request below

        day = request['ts']
        content = request['content']
        request_type = request['type']
        if request_type == 'text':
            count_request_type['text'] += 1
            print(view_text(day, content))
        elif request_type == 'image' and day > datetime.today() - timedelta(days=4):
            count_request_type['image'] += 1
            print(view_image(day, content))
        elif request_type == 'video' and day > datetime.today() - timedelta(days=4):
            count_request_type['video'] += 1
            print(view_video(day, content))
        elif request_type == 'sound':
            count_request_type['sound'] += 1
            print(view_sound(content))
    print(count_request_type)

