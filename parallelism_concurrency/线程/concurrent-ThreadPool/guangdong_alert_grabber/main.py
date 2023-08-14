from itertools import islice
import time
from datetime import datetime, timedelta
import calendar
import requests
from lxml import html
import re
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_num(txt: str, **kwargs):
    try:
        tree = html.fromstring(txt)
        res = tree.xpath('//*[@id="pagelist1"]/div/span')
        if not res:
            print(f'没有数字文本,{kwargs}')
            return -1
        re_res = re.search(r'\d+', res[0].text)
        if re_res:
            return re_res.group()
        else:
            print(f'没从文本解析出数字,{kwargs}')
            return -2
    except Exception as e:
        print(f'未知错误(maybe html-tree build fail): error:{e}. {kwargs}')
        return -3


def get_country() -> list:
    import json
    with open('country.json', 'r') as file:
        res: dict = json.load(file)

    return [parse_country(c) for c in res.values()]


def parse_country(encoded_text):
    """

    :param encoded_text example: %u6C64%u52A0:
    :return: 汤加
    """

    def decode_unicode(match):
        code_point = int(match.group(1), 16)
        return chr(code_point)

    decoded_text = re.sub(r"%u([0-9A-Fa-f]{4})", decode_unicode, encoded_text)
    return decoded_text


def generate_month_ranges(start_year: int, end_year: int):
    month_ranges = []

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            days_in_month = calendar.monthrange(year, month)[1]
            first_day = datetime(year, month, 1)
            last_day = first_day + timedelta(days=days_in_month - 1)

            month_ranges.append((first_day.strftime('%Y-%m-%d'), last_day.strftime('%Y-%m-%d')))

    return month_ranges


def get_content(country, month_start_date, month_end_date, _type):
    time.sleep(0.2)
    # print('sleep..')
    url = f"http://www.gdtbt.org.cn/{_type}.aspx?keyword=&ics=&hs=&tbcy={country}&fgcp=&tbrq0={month_start_date}&tbrq1={month_end_date}&specialid="

    payload = {}
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'ASP.NET_SessionId=rivsf442pg15dxfg5fcckrkk; ASP.NET_SessionId=qaq1f1ihxx2fx0sv2jnbwiru',
        'Host': 'www.gdtbt.org.cn',
        'Referer': f'http://www.gdtbt.org.cn/{_type}.aspx?keyword=&ics=&hs=&tbcy=&fgcp=&tbrq0=2010-1-1&tbrq1=2023-8-1&specialid=',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


def generate_year_ranges(start_year, end_year):
    year_ranges = []

    for year in range(start_year, end_year + 1):
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        year_ranges.append((start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))

    return year_ranges


def split_list_into_n_parts(lst, n):
    avg = len(lst) // n
    remainder = len(lst) % n
    iter_lst = iter(lst)

    for _ in range(n):
        length = avg + (1 if remainder > 0 else 0)
        yield list(islice(iter_lst, length))
        remainder -= 1


_split = split_list_into_n_parts


def thread_task(countries, thres_num, _type):
    task_result = []

    thread_t1 = time.time()
    for country in countries:
        for _range in thread_ranges:
            start_date, end_date = _range
            time.sleep(throttle)
            tbt_number = get_num(
                get_content(country, start_date, end_date, _type=_type),
                country=country,
                month_start_date=start_date
            )
            print(f'Thread{thres_num}: Got {country} '
                  f'from {start_date} to {end_date} {TYPE.upper()} number is {tbt_number}')
            date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            year = date_obj.year
            # task_result.append((thres_num, year, country, tbt_number))
            task_result.append((year, country, tbt_number))

    thread_t2 = time.time() - thread_t1
    print(f'Time Cost Thread{thres_num}: {thread_t2}')

    return task_result


def merge_():
    def _apply_key(row):
        return f"{row['year']}|{row['country']}"

    file_time = '2010_2014'
    tbt_file = f'./tbt_number{file_time}.csv'
    sps_file = f'./sps_number{file_time}.csv'

    tbt_df = pd.read_csv(tbt_file)
    sps_df = pd.read_csv(sps_file)
    tbt_df['key'] = tbt_df.apply(_apply_key, axis=1)
    sps_df['key'] = sps_df.apply(_apply_key, axis=1)

    df = pd.merge(
        tbt_df,
        sps_df,
        on='key',
        suffixes=('', 'sps')
    )
    col = [
        'year',
        'country',
        'TBT_number',
        'SPS_number',
    ]
    df[col].to_csv(f'./tbt_sps_number_{file_time}.csv', index=False)


if __name__ == '__main__':
    start_year, end_year = 2010, 2010
    year = None
    THREAD_NUM = 16
    throttle = 2
    TYPE = 'sps'  # tbt
    mode = 'multi'

    country_list = get_country()
    if year:
        thread_ranges = generate_year_ranges(year, year)
        file_name = f'./{TYPE}_number{year}.csv'
    else:
        thread_ranges = generate_year_ranges(start_year, end_year)
        file_name = f'./{TYPE}_number{start_year}_{end_year}.csv'

    task_result = []
    print(f'run in {mode}-thread mode.')
    if mode == 'multi':
        with ThreadPoolExecutor(THREAD_NUM) as executor:
            task_list = []
            for num, countries in enumerate(list(_split(country_list, THREAD_NUM)), 1):
                task = executor.submit(thread_task, countries, num, TYPE)
                task_list.append(task)

            t1 = time.time()
            for task in as_completed(task_list):
                result = task.result()
                print(f'task complete. result: {result}')
                task_result.extend(result)
            time_cost = time.time() - t1
            print(f'time cost: {time_cost}')
        # 2010 一年，cost: 53.315s
    else:
        result = thread_task(country_list, 0, TYPE)
        task_result.extend(result)
        # 2010 一年，cost: 524.591s

    df = pd.DataFrame(task_result, columns=['year', 'country', f'{TYPE.upper()}_number'])
    df.to_csv(file_name, index=False)
