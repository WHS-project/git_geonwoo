import base64

#test_text
encoded_text ='IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCmZyb20gc3VicHJvY2VzcyBpbXBvcnQg\nY2FsbAppbXBvcnQgb3MKaW1wb3J0IHJlCgoKdmVyc2lvbiA9IE5vbmUKCgpk\nZWYgZ2V0X25ld19zZXR1cF9weV9saW5lcygpOgogICAgZ2xvYmFsIHZlcnNp\nb24KICAgIHdpdGggb3Blbignc2V0dXAucHknLCAncicpIGFzIHNmOgogICAg\nICAgIGN1cnJlbnRfc2V0dXAgPSBzZi5yZWFkbGluZXMoKQogICAgZm9yIGxp\nbmUgaW4gY3VycmVudF9zZXR1cDoKICAgICAgICBpZiBsaW5lLnN0YXJ0c3dp\ndGgoJ1ZFUlNJT04gPSAnKToKICAgICAgICAgICAgbWFqb3IsIG1pbm9yID0g\ncmUuZmluZGFsbChyIlZFUlNJT04gPSAnKFxkKylcLihcZCspJyIsIGxpbmUp\nWzBdCiAgICAgICAgICAgIHZlcnNpb24gPSAie30ue30iLmZvcm1hdChtYWpv\nciwgaW50KG1pbm9yKSArIDEpCiAgICAgICAgICAgIHlpZWxkICJWRVJTSU9O\nID0gJ3t9J1xuIi5mb3JtYXQodmVyc2lvbikKICAgICAgICBlbHNlOgogICAg\nICAgICAgICB5aWVsZCBsaW5lCgoKbGluZXMgPSBsaXN0KGdldF9uZXdfc2V0\ndXBfcHlfbGluZXMoKSkKd2l0aCBvcGVuKCdzZXR1cC5weScsICd3JykgYXMg\nc2Y6CiAgICBzZi53cml0ZWxpbmVzKGxpbmVzKQoKY2FsbCgnZ2l0IHB1bGwn\nLCBzaGVsbD1UcnVlKQpjYWxsKCdnaXQgY29tbWl0IC1hbSAiQnVtcCB0byB7\nfSInLmZvcm1hdCh2ZXJzaW9uKSwgc2hlbGw9VHJ1ZSkKY2FsbCgnZ2l0IHRh\nZyB7fScuZm9ybWF0KHZlcnNpb24pLCBzaGVsbD1UcnVlKQpjYWxsKCdnaXQg\ncHVzaCcsIHNoZWxsPVRydWUpCmNhbGwoJ2dpdCBwdXNoIC0tdGFncycsIHNo\nZWxsPVRydWUpCgplbnYgPSBvcy5lbnZpcm9uCmVudlsnQ09OVkVSVF9SRUFE\nTUUnXSA9ICd0cnVlJwpjYWxsKCdybSAtcmYgZGlzdC8qJywgc2hlbGw9VHJ1\nZSwgZW52PWVudikKY2FsbCgncHl0aG9uIHNldHVwLnB5IHNkaXN0IGJkaXN0\nX3doZWVsJywgc2hlbGw9VHJ1ZSwgZW52PWVudikKY2FsbCgndHdpbmUgdXBs\nb2FkIGRpc3QvKicsIHNoZWxsPVRydWUsIGVudj1lbnYpCg==\n'

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
    

decoded_result = base64_decode(encoded_text)

if decoded_result is not None:
    print(f"Decoded text: {decoded_result}")
else:
    print("Decoding failed.")