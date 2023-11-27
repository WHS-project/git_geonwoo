import requests
from log import save_json_to_txt, save_repository_info
from search_option import *


def search_by_pull(headers):
    from search import log_txt
    save_repository_info("Search type : pull\n", log_txt)

    option = search_option()

    url = 'https://api.github.com/search/issues'
    # 선택한 언어 중에서 issues, label이 bug인것, closed 된 것들을 가져옴
    query = f'language:{option.language_input} 	is:pr is:{option.state} label:{option.label}'
    params = {'q': query , 'per_page':{option.per_page}}  # 검색할 페이지 수만큼 가져옴

    response = requests.get(url, headers=headers, params=params)

    # 응답 상태 및 내용 확인
    if response.status_code == 200:
        data = response.json()
        # json txt로 저장
        save_json_to_txt(data, "pull")
    else:
        status_error = f"Unable to retrieve data. Status code: {response.status_code}"
        print(status_error)
        save_repository_info(status_error, log_txt)
        print(response.text)