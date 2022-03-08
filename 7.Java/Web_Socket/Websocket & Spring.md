# Websocket & Spring



#### WebSocket

> - 기존의 단방향 HTTP 프로토콜과 호환되어 양방향 통신을 제공하기 위해 개발된 프로토콜
>
> - 일반 Socket통신과 달리 HTTP 80 Port를 사용하므로 방화벽에 제약이 없으며 통상 WebSocket으로 불린다
> - 접속까지는 HTTP 프로토콜을 이용하고, 그 이후 통신은 자체적인 WebSocket 프로토콜로 통신하게 된다





### Web Socket 이전의 방식

-----

#### polling

![img](https://blog.kakaocdn.net/dn/72boS/btq1ovGdhCT/z6rLZSGt7Nu91JceVB2cLk/img.gif)

> 출처: https://rubberduck-debug.tistory.com/123

- 클라이언트가 평범한 HTTP Request를 서버로 계속 요청해 이벤트 내용을 전달받는 방식

- 클라이언트가 지속적으로 Request를 요청하기 때문에 클라이언트의 수가 많아지면 서버의 부담이 급증

  -> 서버 부담 증가, 속도 문제 발생





#### Long polling

![img](https://blog.kakaocdn.net/dn/bkGQ0s/btq1pAUOs8A/ew01JYR616U6VFmytsvPf0/img.gif)

> 출처: https://rubberduck-debug.tistory.com/123

- 클라이언트에서 서버로 일단 HTTP Request 요청 후 서버에서 해당 클라이언트로 전달할 이벤트가 있다면 그 순간 Response 메세지를 전달하며 연결이 종료
- 곧이어 클라이언트가 다시 HTTP Request를 요청해 서버의 다음 이벤트를 기다리는 방식
- 이벤트 시간 간격이 좁은 채팅 방식일 경우 polling의 단점과 같은 문제 발생







### WebSocket 접속 과정

---



![img](https://blog.kakaocdn.net/dn/bgngGE/btq1BxWnQVW/fpCwx5sQirmCnqjwAk6NL1/img.png)



> 출처: https://blog.naver.com/eztcpcom/220070508655



- 웹소켓 접속 과정
  - TCP/IP 접속
  - 웹소켓 열기 HandShake



#### 웹소켓 열기 HandShake

- 클라이언트가 HandShake 요청을 보내고 응답을 서버가 클라이언트로 보내는 구조

- 서버와 클라이언트는 HTTP 1.1프로토콜을 사용



##### Request

| **Header Name**           | **div**     | **Description**                                              |
| ------------------------- | ----------- | ------------------------------------------------------------ |
| **GET**                   | **Require** | 요청 명령어는 GET을 사용해야 하며, HTTP 버전은 1.1 이상이어야 한다. |
| **Host**                  | **Require** | 웹소켓 서버의 주소                                           |
| **Upgrade**               | **Require** | WebSocket이라는 단어를 사용해야 한다. 대소문자는 구분 X      |
| **Connection**            | **Require** | Upgrade라는 단어를 사용해야 한다. 대소문자는 구분 X          |
| **Sec-WebSocket-Key**     | **Require** | 길이가 16Byte인 임의로 선택된 숫자를 base64 인코딩한 값 이다. |
| **Origin**                | **Require** | 클라이언트로 웹 브라우저를 사용하는 경우 필수항목으로, 클라이언트의 주소 |
| **Sec-WebSocket-Version** | **Require** | 13을 사용한다.                                               |
| Sec-WebSocket-Protocol    | Option      | 클라이언트가 사용하고 싶은 하위 프로토콜 이름을 명시한다.    |
| Sec-WebSocket-Extensions  | Option      | 클라이언트가 사용하고 싶은 추가 옵션을 기술한다.             |



##### Response

| **Header Name**          | **div**     | **Description**                                              |
| ------------------------ | ----------- | ------------------------------------------------------------ |
| **HTTP**                 | **Require** | HTTP 버전은 1.1이며, 클라이언트로부터의 요청이 이상 없는 경우 101을 상태코드로 사용한다. |
| **Upgrade**              | **Require** | WebSocket이라는 단어를 사용해야 한다. 대소문자는 구분 X      |
| **Connection**           | **Require** | Upgrade라는 단어를 사용해야 한다. 대소문자는 구분 X          |
| **Sec-WebSocket-Accept** | **Require** | 클라이언트로부터 받은 Sec-WebSocket-Key를 사용하여 계산된 값이다. |
| Sec-WebSocket-Protocol   | Option      | 서버에서 서비스하는 하위 프로토콜을 명시한다. 클라이언트가 요청하지 않는 하위 프로토콜을 명시하면 HandShake는 실패한다. |
| Sec-WebSocket-Extensions | Option      | 서버가 사용하는 추가 옵션을 기술한다. 클라이언트가 요청하지 않는 추가 옵션을 명시하면 HandShake는 실패한다. |





## 구현 테스트 Prequel

1. 라이브러리 추가

#### build.gradle

```java
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    implementation 'org.springframework.boot:spring-boot-starter-security'
    implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'
    
    ///////////////////////////////////////////////////////////////////////
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springframework.boot:spring-boot-starter-websocket'
    ///////////////////////////////////////////////////////////////////////
    
    implementation 'org.thymeleaf.extras:thymeleaf-extras-springsecurity5'
    compileOnly 'org.projectlombok:lombok'
    developmentOnly 'org.springframework.boot:spring-boot-devtools'
    runtimeOnly 'org.mariadb.jdbc:mariadb-java-client'
    annotationProcessor 'org.projectlombok:lombok'
    providedRuntime 'org.springframework.boot:spring-boot-starter-tomcat'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    testImplementation 'org.springframework.security:spring-security-test'

    compile group: 'org.thymeleaf.extras', name: 'thymeleaf-extras-java8time'
    implementation 'com.querydsl:querydsl-jpa'
    // https://mvnrepository.com/artifact/net.coobird/thumbnailator
    implementation group: 'net.coobird', name: 'thumbnailator', version: '0.4.8'

}
```

