import requests
from log import *
from search.repository_clone import *
from search.search_option import *


def search_by_repository(headers):
    from search.search import log_txt

    save_repository_info("Search type: Repository\n", log_txt)
    option = search_option()

    # GitHub 검색 API를 사용하여 리포지토리 검색
    search_url = 'https://api.github.com/search/repositories'
    query = f'language:{option.language_input} stars:>{option.min_stars} forks:>{option.min_forks} pushed:>{option.updated_after}'
    params = {'q': query, 'sort': 'stars', 'order': 'desc', 'per_page': option.per_page, 'page': 1}

    response = requests.get(search_url, headers=headers, params=params)

    # 응답 상태 및 내용 확인
    if response.status_code == 200:
        data = response.json()
        total_count = data['total_count']
        total_page = int(total_count / option.per_page) + 1

        for i in range(1, total_page + 1):
            params = {'q': query, 'sort': 'stars', 'order': 'desc', 'per_page': option.per_page, 'page': i}
            response = requests.get(search_url, headers=headers, params=params)

            if response.status_code == 200:
                page_data = response.json()
                save_json_to_txt(page_data, f"repository{i}")
            else:
                status_error = f"Unable to retrieve data for page {i}. Status code: {response.status_code}"
                print(status_error)
                save_repository_info(status_error, log_txt)
                print(response.text)
    else:
        status_error = f"Unable to retrieve data. Status code: {response.status_code}"
        print(status_error)
        save_repository_info(status_error, log_txt)
        print(response.text)
