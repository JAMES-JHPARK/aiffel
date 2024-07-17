🔑 **PRT(Peer Review Template)**

- 리뷰어 : 김성연, 코더 : 박장현  
  
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
        - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부

1. 한글 코퍼스를 가공하여 BERT pretrain용 데이터셋을 잘 생성하였다.
  - MLM, NSP task의 특징이 잘 반영된 pretrain용 데이터셋 생성과정이 체계적으로 진행되었습니다.
      ![Screenshot 2024-07-17 at 5 24 05 PM](https://github.com/user-attachments/assets/beda05ff-a1ce-43b6-97c6-6ce3d03107b9)
2. 구현한 BERT 모델의 학습이 안정적으로 진행됨을 확인하였다.
  - MLM, NSP loss가 안정적으로 줄고 있고 acc도 상당히 높네요!
    ![Screenshot 2024-07-17 at 5 24 59 PM](https://github.com/user-attachments/assets/ce71c9d5-b635-4023-9af6-8a3db0ccf975)
3. 1M짜리 mini BERT 모델의 제작과 학습이 정상적으로 진행되었다.
  - 학습 시간이 오래걸려서 시각화는 힘들었던것 같지만 그래도 학습도 잘 되고 있는것 같네요!
  - 모델이 학습과정에서 저장도 되고 있는것 같습니다.
    
- [x]  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
    - [x]  모델 선정 이유
    - [x]  Metrics 선정 이유
    - [x]  Loss 선정 이유

- [x]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
  - 학습과정에서 vocab이 비는 문제가 발생하셨던 것 같습니다 그 과정에서 문제를 해결하기 위해서 단어를 직접 찍어보고 예외처리로 문제를 해결하셨다는 점이 인상깊었습니다.
  - 같은 데이터 셋인데 왜 문제가 발생했는지 잘 이해가 안가네요.....
![Screenshot 2024-07-17 at 5 29 48 PM](https://github.com/user-attachments/assets/fac64dcb-c76c-490b-a1c5-c32ee0e1dff4)
![Screenshot 2024-07-17 at 5 30 39 PM](https://github.com/user-attachments/assets/6ee13110-1399-486d-a90f-7e72e423bdc2)

- [x]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
    - [x]  배운 점
    - [x]  아쉬운 점
    - [x]  느낀 점
    - [x]  어려웠던 점
  ![Screenshot 2024-07-17 at 5 14 12 PM](https://github.com/user-attachments/assets/b03d0727-c8cb-4a44-a86c-66aa73940f05)
- 저도 상당히 공감되는 점이 많았던 회고였습니다! 실제로 scratch 부터 구현하려하면 막막하긴 할 것 같아요
- 그래도 이렇게 모델 구조를 파악한뒤 앞으로는 bert huggingface 모델을 불러오려구요 ...ㅎㅎ
