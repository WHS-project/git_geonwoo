import subprocess
import os
from log import *

# Githuc data 처리
def github_crawler(data):
    from search import log_txt

    # 가져온 Repository의 개수 출력
    items_length = repository_count(data)
    index = 0
    if items_length == 0:
        repository_error = "No Repository error"
        save_repository_info(repository_error, log_txt)
        exit(1)

    # 추출한 개수만큼 clone 수헹
    if index < items_length:
        for repo in data['items']:
            # 현재 작업중인 Repository 정보 작성 및 출력
            current_repository = repository_info_to_string(repo, index)
            save_repository_info(current_repository, log_txt)
            print(repository_info_to_string(repo, index))

            # 레포지토리 클론
            repository_clone(repo['name'], repo['clone_url'])

            index += 1


# 레포지토리 정보 터미널 출력
def repository_info_print(info):
    print(info)

# 레포지토리 정보 문자열 변환
def repository_info_to_string(repo, index):
    result =f"Repository index: {index}\n"\
            f"Repository name: {repo['name']}\n"\
            f"Language : {repo['language']}\n"\
            f"Stars count: {repo['stargazers_count']}\n"\
            f"Forks count: {repo['forks_count']}\n"\
            f"Last update: {repo['updated_at']}\n"\
            f"URL: {repo['html_url']}\n\n" 
    return result


# Repository clone
def repository_clone(name, url):
    # 클론 저장 위치 설정
    result_path = './repository/'
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    repo_name = name
    repo_url = url
    subprocess.run(['git', 'clone', repo_url, os.path.join(result_path, repo_name)])
