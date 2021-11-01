# Django Form Class

- Form은 데이터 손상에 대한 중요한 방어수단
- 주요 처리 기능
  1. 렌더링을 위한 데이터 준비 및 재구성
  2. 데이터에 대한 HTML forms 생성
  3. 클라이언트로부터 받은 데이터 수신 및 처리



#### Django 'Form Class'

- form 내 field, fields 배치, 디스플레이 widget, label, 초기값, 유효하지 않은 field에 관련된 여러 메세지를 결정
- Django는 사용자의 데이터를 받아야할 작업(데이터 유효성 검증, 필요시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등)과 반복 코드를 줄여 줌

