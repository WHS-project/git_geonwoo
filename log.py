import json

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
def save_json_to_txt(data):
    json_file_path = './loging/JSON.txt'
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
