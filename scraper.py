import requests
import subprocess
import os
from datetime import datetime, timedelta
import json

#로그 저장 파일 설정    
log_file_path = './log.txt'
repository_name = open(log_file_path, "w", encoding='utf-8')

# Github API를 통한 repository 검색
def github_search():
    # GibHub API 인증 토큰 설정
    token = '개인 토큰'
    headers = {'Authorization': f'token {token}'}

    # 언어 설정, default = python
    language_input = 'python'

    # 검색 조건 설정
    min_stars = 10
    min_forks = 10
    updated_after = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    
    #로그 저장 파일 설정
    log_file_path = './log.txt'
    repository_name = open(log_file_path, "w", encoding='utf-8')

    # GitHub 검색 API를 사용하여 리포지토리 검색
    per_page = 100 # 최대값 100
    search_url = 'https://api.github.com/search/repositories'
    query = f'language:{language_input} stars:>{min_stars} forks:>{min_forks} pushed:>{updated_after}'
    params = {'q': query, 'sort': 'stars', 'order': 'desc', 'per_page': per_page}  # 검색할 페이지 수만큼 가져옴

    response = requests.get(search_url, headers=headers, params=params)

    # 응답 상태 및 내용 확인
    if response.status_code == 200:
        data = response.json()
        github_crawler(data)
    else:
        status_error = f"Unable to retrieve data. Status code: {response.status_code}"
        print(str)
        save_repository_info(status_error, repository_name)
        print(response.text)


# Githuc data 처리
def github_crawler(data):
    # 가져온 Repository의 개수 출력
    items_length = repository_count(data)
    index = 0
    if items_length == 0:
        repository_error = "No Repository error"
        save_repository_info(repository_error, repository_name)
        exit(1)

    # 추출한 개수만큼 clone 수헹
    if index < items_length:
        for repo in data['items']:
            # 현재 작업중인 Repository 정보 작성 및 출력
            current_repository = repository_info_to_string(repo, index)
            save_repository_info(current_repository, repository_name)
            print(repository_info_to_string(repo, index))

            # 레포지토리 클론
            repository_clone(repo['name'], repo['clone_url'])

            index += 1


# Repository clone
def repository_clone(name, url):
    # 클론 저장 위치 설정
    result_path = './repository/'
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    repo_name = name
    repo_url = url
    subprocess.run(['git', 'clone', repo_url, os.path.join(result_path, repo_name)])


# ------------------------------------------
# 선언 함수
# Repository 개수 
def repository_count(data):
    if 'items' in data:
        items_length = len(data['items'])
        return items_length
    else:
        print("No 'items' key found in the JSON data.")

# 파일의 라인 수를 세는 함수
def get_line_count(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except Exception as e:
        print(f"Error counting lines in {file_path}: {e}")
        return 0
    

# 레포지토리 리스트 정보 저장
def save_repository_info(info, text_file):
    try:
        text_file.write(info)
    except Exception as e:
        print(f"레포지토리 정보를 저장하는 중 오류 발생: {e}")

# 레포지토리 정보 터미널 출력
def repository_info_print(info):
    print(info)

# 레포지토리 정보 문자열 변환
def repository_info_to_string(repo, index):
    result =f"레포지토리 인덱스: {index}\n"\
            f"레포지토리 이름: {repo['name']}\n"\
            f"스타 수: {repo['stargazers_count']}\n"\
            f"포크 수: {repo['forks_count']}\n"\
            f"최근 업데이트: {repo['updated_at']}\n"\
            f"URL: {repo['html_url']}\n\n" 

    return result

# data.json 파일 txt 저장
def save_json_to_txt(data):
    json_file_path = './JSON.txt'
    try:
        with open(json_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"JSON data saved to '{json_file_path}' successfully.")
    except Exception as e:
        print(f"Error saving JSON data to '{json_file_path}': {e}")

if __name__ == "__main__":
    github_search()
