# Automated-Canteen-Ordering-System-UC7
사용언어: python 3.7

### 사용 라이브러리
- pandas(db 제어)
- thinker(GUI 구현)
- pytest(테스팅)

## 5/16
- 기본적인 개발환경 설정
  -  DB의 경우 로컬에서 작업해야하는 특성상 csv 파일 사용한 Data Frame을 DB로 활용
  -  MongoDB의 활용 가능성 검토

## 5/18
- [Controller](controller.py)에 대한 논의 및 구현
  -  Pub-Sub pattern 을 적용
- 구현 파트에 대한 논의
  -  훈석:[UI 및 Interface Page](UI.py)에 대한 전반적인 부분 구현
  -  유지: [Reload 및 Balance Check](DB_related/connectionDB.ipynb)과 같은 [DB](DB_related)와 연관된 파트 구현
-  [Main Program](main.py) 작성

## 5/23
- 각자 구현한 파트에 대한 피드백 및 수정
- Controller 파트 구현
- Testing 에 대한 논의
  - Bottom-up integration testing 혹은 다른 테스팅 기법을 조사 후 5/26일 미팅

## 5/26
- Bottom-up integration testing 방법으로 테스팅 진행 결정 (end user가 없기 때문에 오직 장점만 존재)
- pytest를 활용하여 테스팅
 
