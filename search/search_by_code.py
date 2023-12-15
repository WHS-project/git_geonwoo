import requests
from decoding import base64_decode
from log import *
from search.search_option import search_option



def search_by_code(headers):
    from search.search import log_txt, clone_list

    save_repository_info("Search type : code\n", log_txt)

    code_info_list = []
    index = 0

    option = search_option()
    # 검색어 setting
    option.set_search_title("shell=True")

    url = 'https://api.github.com/search/code'
    query =f'{option.search_title} language:python'
    params = {'q': query, 'per_page':5} 

    response = requests.get(url, headers=headers, params=params)

    # 응답 상태 및 내용 확인
    if response.status_code == 200:
        data = response.json()
        # json txt로 저장
        save_json_to_file(data, "code")
        index = code_parser(data, index, code_info_list)

    else:
        status_error = f"Unable to retrieve data. Status code: {response.status_code}"
        print(status_error)
        save_repository_info(status_error, log_txt)
        print(response.text)

    save_pr_info_to_json(code_info_list, clone_list)

def code_clone_list(repo, index):
    from search.search import code_path 
    decode = get_content(repo['git_url'])
    code_name = repo['name']
    file_path = f'{code_path}/{index}_{code_name}'
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(decode)
    print(f'save {file_path}')
    code_dict = {
        "code_index": index,
        "code_name": code_name,
        "code_path": repo['path'],
        "git_url":repo['git_url'],
        "code_URL": repo['html_url'],
        "repo_name":repo['repository']['name'],
        "repo_url":repo['repository']['html_url'],
        "merged_at":repo['repository']['name']
        }
    return code_dict
        
# code 정보 parser
def code_parser(data, index, code_info_list):
    for repo in data['items']:
        index += 1
        pr_info = code_clone_list(repo, index)
        code_info_list.append(pr_info)
        if(index == 100):
            break
    return index

def get_content(url):
    from search.search import get_header
    header = get_header()

    response = requests.get(url, headers=header)

    if response.status_code == 200:
    # 요청이 성공하면 JSON 형식의 리포지토리 정보 반환
        content_info = response.json()
        decode = base64_decode(content_info['content'])
        return decode
    else:
        # 요청이 실패하면 None 반환
        print(f"Failed to fetch repository info. Status code: {response.status_code}")
        return 'Fail'
