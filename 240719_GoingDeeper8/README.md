🔑 **PRT(Peer Review Template)**

- 리뷰어 : , 코더 : 박장현  
  
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
        - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부
![Screenshot 2024-07-19 at 5 19 36 PM](https://github.com/user-attachments/assets/f51d9c9e-9333-4641-b07c-7a79944456b8)

    - training 시간이 오래걸려서 끝까지 결과를 보지못하신거 같아서 아쉬웠습니다<br>
<br>이 부분을 <br>
 ![Screenshot 2024-07-19 at 5 28 56 PM](https://github.com/user-attachments/assets/36b2b35b-5f8f-4411-b61e-6829efa69ff8)
  ```python
    maxlen = 55
    def tokenize_function_with_max(examples, maxlen=maxlen):
        encodings = tokenizer(examples['document'],max_length=maxlen, truncation=True, padding='max_length')
        return encodings
  ```
  이런식으로 바꾸시면 시간이 많이 줄어들 겁니다! bert에서 max_length는 512라고 합니다


- []  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
- [x]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
    - [x]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
![Screenshot 2024-07-19 at 5 20 12 PM](https://github.com/user-attachments/assets/f1144198-916a-4d42-87c3-db02701f12c1)

    - [ ]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
    - [ ]  각 실험을 시각화하여 비교하였나요?
    - [x]  모든 실험 결과가 기록되었나요?
아아![Screenshot 2024-07-19 at 5 22 51 PM](https://github.com/user-attachments/assets/f3d33f73-972d-40cf-bbba-41f77e41480a)

- [x]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
    - [x]  배운 점
    - [x]  아쉬운 점
    - [x]  느낀 점
    - [x]  어려웠던 점
![Screenshot 2024-07-19 at 5 17 57 PM](https://github.com/user-attachments/assets/118f4d25-9b57-4168-880c-9b6850cdb8da)

- 저도 덕분에 fp16=True 옵션을 알게되어 다음에 GPU가 부족할 때 해봐야겠습니다!
