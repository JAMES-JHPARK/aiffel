

처음에 데이터셋을 잘못 설정해서, 기존대로 Input : Questions, Output : Answers로 했을때는 오히려 학습도 되고 출력도 한 단어만 반복하지만 나오긴 했었음.
<img width="781" alt="스크린샷 2024-06-21 오후 5 34 57" src="https://github.com/JAMES-JHPARK/aiffel/assets/37362505/7c14e2af-0418-4f08-9ae3-2f832f969550">
<img width="417" alt="스크린샷 2024-06-21 오후 5 35 06" src="https://github.com/JAMES-JHPARK/aiffel/assets/37362505/3b1b2dc6-95dc-4742-815d-2aba9f642ae2">
<img width="414" alt="스크린샷 2024-06-21 오후 5 35 15" src="https://github.com/JAMES-JHPARK/aiffel/assets/37362505/4707d5bb-399d-4678-a0af-af2defdb82e5">


데이터셋을 아래와 같이 바꾸고 나서 학습이 전혀 안되고, 따라서 출력도 없음.
dataset = tf.data.Dataset.from_tensor_slices((
    {
        'inputs': questions+answers
    },
    {
        'outputs': questions[:,1:]+answers[:,1:]
    }
))
<img width="755" alt="스크린샷 2024-06-21 오후 5 19 37" src="https://github.com/JAMES-JHPARK/aiffel/assets/37362505/51d4c421-10fe-4617-a659-abff0891c7fe">


**GPT MODEL** 
<img width="843" alt="스크린샷 2024-06-21 오후 5 28 59" src="https://github.com/JAMES-JHPARK/aiffel/assets/37362505/a6362177-40c3-4137-aba4-c960a997afcc">

![gpt_model](https://github.com/JAMES-JHPARK/aiffel/assets/37362505/e4258b61-731c-49f7-b5ca-b6913cc8b418)

**Decoder 안에 Layer 반복**
<img width="842" alt="스크린샷 2024-06-21 오후 5 29 53" src="https://github.com/JAMES-JHPARK/aiffel/assets/37362505/1c0d4793-55e5-4805-8f45-d51b440fa8c0">
<img width="837" alt="스크린샷 2024-06-21 오후 5 30 15" src="https://github.com/JAMES-JHPARK/aiffel/assets/37362505/8c5bf584-d2e5-4a5c-b977-64f723f02dfa">

![decoder_layers](https://github.com/JAMES-JHPARK/aiffel/assets/37362505/5cd755b5-d0a9-472a-93ac-1288404bfabe)
