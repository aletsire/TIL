# WebSocket_Intro

웹소켓 프로토콜인 RFC 6455는 단일 TCP 연결을 통해 Client와 Server 사이에 전이중 방향 통신 채널을 설정하는 표준화 된 방법을 제공한다





#### Web Socket과 TCP

- 웹소켓은 연결과 요청에 대하여 HTTP를 통해 Switching 및 HandShaking이 이루어진다
- TCP는 이진(Binary) 데이터만 주고 받을 수 있으나, 웹 소켓은 Binary와 Text 데이터도 주고 받을 수 있다.





#### Web Socket과 HTTP

> 웹소켓은 HTTP 호환이 가능하게 설계 되었고, HTTP 요청으로 시작하나 두 Protocol의 아키텍쳐와 Application Programming Model은 매우 다르다

- 웹소켓은 일반적으로 URL이 한개만 존재
- 메시지는 TCP연결을 통해 흐름
- 웹소켓은 HTTP와 달리 메시지 내용에 의미 규정하지 않음
- Client와 Server가 메시지 시멘틱에 동의하지 않으면 메시지 라우팅 or 처리 불가





#### Web Socket 특징

1. HTTP 통신의 단점 개선(비연결성 문제 해결 -> 일시적인 데이터 연결 문제 개선)
2. 영구적 양방향 통신
3. HTML 5의 주요 API
4. HTTP 프로토콜을 기반으로하는 웹 브라우저의 웹 서버간 양방향 통신을 지원하기 위한 표준
5. Client/Server가 실시간으로 데이터를 주고 받을 수 있다