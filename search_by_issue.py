from log import save_repository_info


def search_by_issues(headers):
    from search import repository_name
    save_repository_info("Search type : Issues", repository_name)





    return 0