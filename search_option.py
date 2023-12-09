from datetime import datetime, timedelta

class search_option():
    language_input = 'python'
    min_stars = 10
    min_forks = 10
    updated_after = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    per_page = 100 # 최대값 100
    page = 1
    label= 'bug'
    state = 'closed'
    search_title = ''

    def set_search_title(self, title):
        self.search_title = title
        
    def get_search_title(self):
        return self.search_title 