# MyAlgorithm One Note

## 목차
* 요약 정리
* 문제 특징 별 접근
* 코드 더미

---

## [기본 문법]

* 람다식으로 튜플 두 번째 값으로 정렬하기
* 집합자료형 합/교/차집합 연산자
* 집합 자료형에서 원소 추가/삭제 시간복잡도는 O(1)
* eval("(3+5)*7") // 수식에 대한 계산 결과 리턴
* itertools > permutations, combinations, product(repeat), combinations_with_replacement
* bisect > bisect_left(lower_bound), bisect_right(upper_bound) // count_by_range 구현 가능
* 딕셔너리에서 키 값 동시에 뽑고 싶으면 dic.items()
* 딕셔너리에서 in 연산은 O(1)





## [요약 정리]

### 그리디
* 개념만으로 풀 수 없다. 다양한 문제의 유형을 풀어야 함

### 그래프

- 플로이드 워셜 - 각 노드마다, 그 노드를 거쳐가는 경우를 고려하면 된다
- 유니온-파인드 : 사이클을 찾을 때 이용한다. union 연산과 find 연산으로 이루어져 있으며 find연산에서 루트를 업데이트하여 경로 압축할 수 있다.
- 크루스칼 알고리즘 : 최소신장트리(MST)를 만들 때 사용하며, 간선들을 비용순으로 정렬한 뒤 사이클이 발생하지 않으면 추가하는 방식으로 모든 간선에 대해 수행한다.
- 위상정렬 : 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것. 매 단계마다 진입차수가 0인 노드를 큐에 넣고, 큐가 빌 때까지 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거하여 진입차수를 업데이트한다.

### 이진탐색

* 개념대로 구현하면 되지만, 응용 버전인 lower_bound와 upper_bound는 범위 가장자리 인덱스 때문에 헷갈릴 때가 있음. a=b=mid인 경우를 생각하면 생각하기 쉬워짐



# 시간/날짜 데이터 관련

# 

---

## [문제 특징 별 접근]
### BOJ_2110_공유기설치 - 파라메트릭 서치

> 최적화 문제를 결정 문제(예 아니오로 답하는 문제)로 바꾸어 해결하는 기법

문제

> 수직선상의 좌표들이 주어졌을 때, c개의 좌표들을 선택하여 **가장 인접한 두 좌표 사이의 거리가 최대**가 되도록 하는 문제

접근과정

> 가장 인접한 두 좌표 사이의 거리가 최소 d 이상일 때, 선택할 수 있는 최대의 좌표를 반환하는 함수를 정의한 후, 나올 수 있는 거리를 lower_bound(이진탐색)하여 c이상인 가장 작은 값을 찾는다. 

### 가장 큰 증가하는 부분 수열

### 공유기 가장 넓게 설치

* 동전 문제
* 가장 큰 증가하는 부분 수열
* 공유기 가장 넓게 설치
* 스케쥴링 알고리즘 (공연 뭐시기)
* 이진 타
* 그래프
* 위상정렬

* 정규표현식