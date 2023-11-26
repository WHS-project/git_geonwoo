import requests
from datetime import datetime, timedelta
from log import *
from repository_clone import github_crawler


def search_by_repository(headers):
    from search import repository_name

    save_repository_info("Search type : Repository", repository_name)
    language_input = 'python'
    min_stars = 10
    min_forks = 10
    updated_after = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

    # GitHub 검색 API를 사용하여 리포지토리 검색
    per_page = 10 # 최대값 100
    search_url = 'https://api.github.com/search/repositories'
    query = f'language:{language_input} stars:>{min_stars} forks:>{min_forks} pushed:>{updated_after}'
    params = {'q': query, 'sort': 'stars', 'order': 'desc', 'per_page': per_page}  # 검색할 페이지 수만큼 가져옴

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
        save_repository_info(status_error, repository_name)
        print(response.text)

    return 0