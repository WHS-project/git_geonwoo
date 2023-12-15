import base64

#test_text

def base64_decode(encoded_text):
    try:
        encoded_text.replace('\n','')
        # base64 디코딩
        decoded_bytes = base64.b64decode(encoded_text)
        
        # 바이트를 문자열로 변환
        decoded_text = decoded_bytes.decode('utf-8')
        
        return decoded_text
    except Exception as e:
        print(f"Error decoding base64: {e}")
        return None
    