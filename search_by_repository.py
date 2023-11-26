import requests
from log import *
from repository_clone import github_crawler
from search_option import *


def search_by_repository(headers):
    from search import log_txt

    save_repository_info("Search type : Repository\n", log_txt)
    option = search_option()

    # GitHub 검색 API를 사용하여 리포지토리 검색
    search_url = 'https://api.github.com/search/repositories'
    query = f'language:{option.language_input} stars:>{option.min_stars} forks:>{option.min_forks} pushed:>{option.updated_after}'
    params = {'q': query, 'sort': 'stars', 'order': 'desc', 'per_page': option.per_page}  # 검색할 페이지 수만큼 가져옴

    response = requests.get(search_url, headers=headers, params=params)

    # 응답 상태 및 내용 확인
    if response.status_code == 200:
        data = response.json()
        # json txt로 저장
        save_json_to_txt(data)
        github_crawler(data)
    else:
        status_error = f"Unable to retrieve data. Status code: {response.status_code}"
        print(status_error)
        save_repository_info(status_error, log_txt)
        print(response.text)
