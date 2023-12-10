import requests
from log import *
from search.search_option import search_option


def search_by_code(headers):
    from search.search import log_txt
    save_repository_info("Search type : code\n", log_txt)

    option = search_option()
    option.set_search_title("shell=True")

    url = 'https://api.github.com/search/code'
    query =f'{option.search_title} language:python'
    params = {'q': query}  # 검색할 페이지 수만큼 가져옴

    response = requests.get(url, headers=headers, params=params)

    # 응답 상태 및 내용 확인
    if response.status_code == 200:
        data = response.json()
        # json txt로 저장
        save_json_to_file(data, "code")
        print(params)
        print(data)
    else:
        status_error = f"Unable to retrieve data. Status code: {response.status_code}"
        print(status_error)
        save_repository_info(status_error, log_txt)
        print(response.text)