import requests
from log import save_json_to_txt, save_repository_info
from repository_clone import repository_clone
from search_option import *
from pull_json_parser import *


def search_by_pull(headers):
    from search import log_txt, clone_list, clone_list_path
    save_repository_info("Search type : pull\n", log_txt)
    
    option = search_option()
    option.set_search_title("exec")
    page = option.page
    index = 0
    ''' 
    original code
    url = 'https://api.github.com/search/issues'
    # 선택한 언어 중에서 issues, label이 bug인것, closed 된 것들을 가져옴
    query = f'language:{option.language_input} 	is:pr is:{option.state} label:{option.label}'
    params = {'q': query , 'page':{page} ,'per_page':{option.per_page}}  # 검색할 페이지 수만큼 가져옴

    response = requests.get(url, headers=headers, params=params)
    '''
    pr_info_list = []

    url = 'https://api.github.com/search/issues'
        # 선택한 언어 중에서 issues, label이 bug인것, closed 된 것들을 가져옴
    query = f'language:{option.language_input} 	is:pr is:{option.state} label:{option.label} {option.search_title} sort:created-desc '
    params = {'q': query}  # 검색할 페이지 수만큼 가져옴


    response = requests.get(url, headers=headers, params=params)
    # 응답 상태 및 내용 확인
    if response.status_code == 200:
        data = response.json()
        # json txt로 저장
        save_json_to_txt(data, "pull")
        index = parser(data, index, pr_info_list)

        '''            
        # 처리해야할 데이터 전송
        if(index >= 100):
        break
        page += 1
        '''
    else:
        status_error = f"Unable to retrieve data. Status code: {response.status_code}"
        print(status_error)
        save_repository_info(status_error, log_txt)
        print(response.text)
        
    save_pr_info_to_json(pr_info_list, clone_list)


    print("Save Finish")
    if input("clone??").lower() == 'y':
        with open(clone_list_path, 'r') as json_file:
            clone_repository_list = json.load(json_file)

        for repo in clone_repository_list:
            name = repo['repository_name']
            url =  repo['repository_clone_url']
            index = repo['Pull request index']
            current_repository = f"index = {index}\n"\
                                 f"name = {name}\n"\
                                 f"url = {url}\n"\
                                 f"PR title = {repo['PR title']}\n"\
                                 f"PR URL = {repo['PR URL']}\n\n"
            save_repository_info(current_repository, log_txt)

            repository_clone(name, url)
            print('\n')