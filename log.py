import json
import requests


# 레포지토리 리스트 정보 저장
def save_repository_info(info, text_file):
    try:
        text_file.write(info)
    except Exception as e:
        print(f"레포지토리 정보를 저장하는 중 오류 발생: {e}")


# 레포지토리 리스트 정보 저장
def save_repository_info(info, text_file):
    try:
        text_file.write(info)
    except Exception as e:
        print(f"레포지토리 정보를 저장하는 중 오류 발생: {e}")


# data.json 파일 txt 저장
def save_json_to_txt(data, type):
    json_file_path = f'./loging/{type}.txt'
    try:
        with open(json_file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"JSON data saved to '{json_file_path}' successfully.")
    except Exception as e:
        print(f"Error saving JSON data to '{json_file_path}': {e}")

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

# 레포지토리 정보 터미널 출력
def repository_info_print(info):
    print(info)

# 레포지토리 정보 문자열 변환
def repository_info_to_string(repo, index, merge = 'false'):
    result =f"Repository index: {index}\n"\
            f"Repository name: {repo['name']}\n"\
            f"Language : {repo['language']}\n"\
            f"Stars count: {repo['stargazers_count']}\n"\
            f"Forks count: {repo['forks_count']}\n"\
            f"Last update: {repo['updated_at']}\n"\
            f"URL: {repo['html_url']}\n"\
            f"Merge: {merge}\n\n"
    return result

def pr_info_to_string(repo, index):
    result =f"Pull request index: {index}\n"\
            f"PR title: {repo['title']}\n"\
            f"PR URL: {repo['html_url']}\n"\
            f"created_at: {repo['created_at']}\n"\
            f"updated_at: {repo['updated_at']}\n"\
            f"closed_at: {repo['closed_at']}\n"\
            f"repository_url: {repo['repository_url']}\n\n"
    return result

def pr_info_to_dict(repo, index):
    # Pull Request 정보를 dictionary으로 저장
    clone_url, clone_name = find_clone_list(repo['repository_url'])
    pr_dict = {
        "Pull request index": index,
        "PR title": repo['title'],
        "PR URL": repo['html_url'],
        "created_at": repo['created_at'],
        "updated_at": repo['updated_at'],
        "closed_at": repo['closed_at'],
        "repository_url": repo['repository_url'],
        "repository_clone_url": clone_url,
        "repository_name": clone_name
    }
    
    return pr_dict

def save_pr_info_to_json(pr_info, json_file):
    # JSON 형식으로 변환
    json_data = json.dumps(pr_info, indent=2)

    # JSON 파일로 저장
    json_file.write(json_data)

def find_clone_list(repo_url):
    from search import get_header
    header = get_header()

    response = requests.get(repo_url, headers=header)

    if response.status_code == 200:
    # 요청이 성공하면 JSON 형식의 리포지토리 정보 반환
        repository_info = response.json()
        return repository_info['html_url'], repository_info['name']
    else:
        # 요청이 실패하면 None 반환
        print(f"Failed to fetch repository info. Status code: {response.status_code}")
        return None