import requests
from datetime import datetime, timedelta
from log import *

from repository_clone import github_crawler

# Log 파일 생성
log_file_path = './log.txt'
repository_name = open(log_file_path, "w", encoding='utf-8')

def set_token():
    token = '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'
    return token

# Github API를 통한 repository 검색
def github_search():
    # GibHub API 인증 토큰 설정
    token = set_token()
    headers = {'Authorization': f'token {token}'}

    # 검색 조건 설정, option
    language_input = 'python'
    min_stars = 10
    min_forks = 10
    updated_after = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    label = 'bug' # bug or vuln
    search_type = 'repositories' # issues, repositories

    # GitHub 검색 API를 사용하여 리포지토리 검색
    per_page = 10 # 최대값 100
    search_url = 'https://api.github.com/search/'+search_type
    query = f'language:{language_input} stars:>{min_stars} forks:>{min_forks} pushed:>{updated_after}'
    params = {'q': query, 'sort': 'stars', 'order': 'desc', 'per_page': per_page}  # 검색할 페이지 수만큼 가져옴

    response = requests.get(search_url, headers=headers, params=params)

    # 응답 상태 및 내용 확인
    if response.status_code == 200:
        data = response.json()
        # json txt로 저장
        save_json_to_txt(data)
        if search_type == 'repositories':
            github_crawler(data)
    else:
        status_error = f"Unable to retrieve data. Status code: {response.status_code}"
        print(status_error)
        save_repository_info(status_error, repository_name)
        print(response.text)
