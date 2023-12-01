from log import *


def parser(data, index, pr_info_list):
    for repo in data['items']:
        if 'pull_request' in repo:
            index += 1
            pr_info = pr_info_to_dict(repo, index)
            pr_info_list.append(pr_info)
        if index == 100:
            break
    return index