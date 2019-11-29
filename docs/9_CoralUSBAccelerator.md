# Coral USB Accelerator
  * https://mazdah.tistory.com/853
  
  1. Coral 사용시 필요 사항
     1. Edge TPU runtim
     2. Python 3.5
        * Python 3.6인 경우 install.sh 맨 마지막 줄에서 '<i>python3.5</i>' 대신 '<i>python3</i>'으로 수정 필요
     3. 클록 주파수를 최대로 할 경우 전력 소모량이 많아지고 발열이 심해짐
       * 권장: 기본 속도
     4. 전원: 5V 500mA

  2. TensorFlow models on the Edge TPU
     1. TensorFlow Lite 버전만 지원
        * TensorFlow의 경량 버전
     2. 모델을 바로 훈련시키지 못함
        * TensorFlow에서 훈련시킨 모델을 TensorFlow Lite Converter 툴을 이용하여 변환하는 과정 필요
     3. 구글의 데이터셋이 아닌 모델로 Edge TPU에서 사용시의 요구 조건
        1. 텐서 파라미터는 8비트 고정 소수점 타입
        2. 텐서의 크기는 컴파일 시에 그 크기가 고정되어 있어야 함
        3. bias 텐서 같은 모델 파라미터 역시 컴파일시에 크기가 고정되어 있어야 함
        4. 텐서들은 3차원 이하이어야 함
           * 3차원 이상 텐서 사용할 경우 가장 안쪽의 3개 차원만이 1보다 큰 크기를 가짐
        5. 모델은 Edge TPU를 지원하는 연산만 가능함

  * 설치
    - https://coral.withgoogle.com/docs/accelerator/get-started/
    - [Github tflite](https://github.com/google-coral/tflite/tree/master/python/examples/detection) : https://github.com/google-coral/tflite/tree/master/python/examples/detection
