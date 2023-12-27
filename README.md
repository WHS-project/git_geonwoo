## git hub 스크래퍼

검색 조건에 따른 git Repository를 검색하고 클론하는 코드입니다.

```python
    language_input = 'python'
    min_stars = 10000
    min_forks = 1000
    updated_after = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
    per_page = 100 # 최대값 100
    page = 1
    label= 'bug'
    state = 'closed'
    search_title = ''
```

search_option.py 에서 검색하고자 하는 조건을 입력하면 됩니다.
현재 설정된 조건 이외의 조건을 추가하고자 한다면, serarch_option.py에 설정을 하여 param에 추가를 하거나, 직접 param에 추가를 해야합니다.

추가적인 내용은 노션에 작성된 문서를 참고하시고

추가적인 문의는 DM 주세요
