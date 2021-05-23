## 1. 개요

문서가 변경대비표에 따라 제대로 변경되었는지 검증하기 위한 패키지입니다.

본 패키지에서는 검증을 위해 다음의 세 단계를 거칩니다.

### 1-1. PDF 파일의 TEXT 파일 전환

---

+ tika 패키지를 활용하여 PDF 파일을 TEXT 파일로 추출합니다.

+ 추출한 TEXT 파일에서 검수에 불필요한 문자를 삭제합니다. (특수문자 등)

### 1-2. 정규표현식 체크리스트 작성

---

+ 변경대비표 내용을 신설, 삭제 문구로 분해하고, 각각 내용을 정규표현식으로 작성합니다.

+ 조건부 문구 입력 시, 조건부 검수가 가능합니다.


### 1-3. TEXT 파일 검수 및 오류 출력

---


+ 체크리스트의 개별 정규표현식이 TEXT 파일에 존재하는지 검색하여 존재여부를 기록합니다.

+ 해당 TEXT파일에 체크리스트의 신설문구가 없는 경우, 삭제문구가 남아있는 경우 오류건으로 보고 출력합니다.

+ 조건부(정규표현식) 문구 입력 시, 해당 문구가 TEXT에 존재하는 경우에만 상기 프로세스에 따라 오류건을 출력합니다.


## 2. API 설명

### 2-1. pdf_to_txt

---

+ convert_pdf_to_txt(pdf_path, txt_path)

 : pdf_path의 pdf 파일을 txt 파일로 추출하여 동일한 파일명으로 txt_path에 저장



+ regex_txt(pattern, txt_path, regex_path)

 : txt_path의 txt파일 별 pattern에 해당하는 부분을 삭제 후 동일한 파일명으로 regex_path에 저장


### 2-2. regex_check

---

+ Checklist(checklist_path)

 : checklist_path의 checklist.txt 파일을 읽어 체크리스트 생성

+ Checklist.reset()

 : 체크리스트 검색 결과를 초기화

+ Checklist.check(search_line)

 : 체크리스트에 따라 search_line 검수

+ Checklist.update()

 : TEXT의 모든 line 검수 후 실행하여 결과를 체크리스트에 업데이트

+ Checklist.errorlog()

 : 체크리스트 업데이트 후 오류 내역을 문자열로 반환
 
### 2-3. checklist.txt 예시

---

| no | check | regex | cond |
| -- | ---- | --------------- | --------------- |
| 1 | delete | 감염병의병원체를확인할수있는기관	| 특정법감염병진단비 |
| 1 | insert | 감염병병원체확인기관	| 특정법감염병진단비 |
| 2 | delete | 장애등급판정기준|능력장해측정기준 | 장해분류표 |
| 2 | insert | 장애정도판정기준	| 장해분류표 |
| 2 | insert | 능력장애측정기준	| 장해분류표 |


## 3. 설치 필요 패키지

### 3-1. Apache Tika 

+ Apache Tika is a library that is used for document type detection and content extraction from various file formats.

+ Installation: pip install tika