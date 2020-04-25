import functools
import requests
import json
import re
import datetime

access_token = "0926bf650926bf650926bf65510957de1f009260926bf6557858fbe4d4f268bc4685722"
url_id = "https://api.vk.com/method/users.get"
url_fr = "https://api.vk.com/method/friends.get"
v = "5.71"
now = datetime.datetime.now()


def validate(bd_date):
    pattern = r'(\d+.\d+.\d+)'
    matches = re.findall(pattern, bd_date)
    return matches


def sort(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        list_of_ages = func(*args, **kwargs)
        unordered = sorted(list_of_ages)

        # Сортируем на основе 2-го элемента
        def keyFunc(item):
            return item[1]

        unordered.sort(key=keyFunc, reverse=True)
        return unordered
    return wrapped


@sort
def calc_age(uid):
    list_of_ages = []
    response = requests.get(f"{url_id}?v={v}&access_token={access_token}&user_ids={uid}&fields=bdate")
    req_id = json.loads(response.text)
    for pack in req_id["response"]:
        id_vk = pack["id"]

    response = requests.get(f"{url_fr}?v={v}&access_token={access_token}&user_id={id_vk}&fields=bdate")
    req_friends = json.loads(response.text)
    response = req_friends["response"]
    for friend_pack in response["items"]:
        try:
            if validate(friend_pack['bdate']):
                bday_year = friend_pack['bdate'][-4:]
                age = int(now.year) - int(bday_year)
                i = 1
                j = -1
                flag = 0
                for x, y in list_of_ages:
                    j += 1
                    if x == age:
                        flag = 1
                        list_of_ages[j] = (x, y + 1)
                        continue
                if flag == 0:
                    list_of_ages.append((age, i), )
        except:
            pass
    return list_of_ages


if __name__ == '__main__':
    res = calc_age('rtacos')
    print(res)
