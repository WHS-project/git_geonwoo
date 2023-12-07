import os
from log import *
from search_by_issue import search_by_issue
from search_by_pull import search_by_pull
from search_by_repository import search_by_repository

# Log 파일 생성
log_path = './loging'

if not os.path.exists(log_path):
    os.makedirs(log_path)

log_file_path = log_path + '/log.txt'
log_txt = open(log_file_path, "w", encoding='utf-8')

clone_list_path = log_path + '/clone_list.json'
clone_list = open(clone_list_path,"w", encoding='utf-8') 

# 토큰 세팅 함수
def set_token():
    token = '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'
    return token

# Github API를 통한 repository 검색
def github_search():
    # GibHub API 인증 토큰 설정
    headers = get_header()

    search_number = int(input("1: Repository\n2: Issues\n3: Pull Request\n검색 타입을 입력하세요: "))
    if search_number == 1:
        search_by_repository(headers)
    elif search_number == 2:
        search_by_issue(headers)
    else:
        search_by_pull(headers)


def get_header():
    token = set_token()
    headers = {'Authorization': f'token {token}'}
    return headers