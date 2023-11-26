from datetime import datetime, timedelta

class search_option():
    language_input = 'python'
    min_stars = 10
    min_forks = 10
    updated_after = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    per_page = 10 # 최대값 100
    merge = 'true'	
