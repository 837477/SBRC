# SBRI Converter
> 서울특별시 노선정보 조회 서비스 API 결과 값 변환기

<p><img src="./rdm/sample.png"></p>

서울특별시 버스 노선 정보 Open API의 결과를 엑셀로 변환해주는 변환기입니다.

## Needs

- Python 3.7

## Installation

OS X & Linux:

```sh
git clone https://github.com/837477/SBRI_Converter.git
```

Windows:

```sh
git clone https://github.com/837477/SBRI_Converter.git
```

Development setup:

```sh
cd src
pip install -r requirements.txt
```

## Usage example

Execution:

```
cd src
python3 main.py
```

## Warning

- 본 프로그램에 입력된 API 주소는 저장되지 않습니다.
- 본 프로그램에서는 API service Key를 검증할 수 없습니다. 따라서 요청 실패 시 Url을 다시 한 번 확인해주세요.

## Release History

* 0.0.1
    * Converter version 0.0.1

## Meta

🙋🏻‍♂️ Name: 837477 

📧 E-mail: 8374770@gmail.com

📔 Blog: http://837477.pythonanywhere.com

🐱 Github: https://github.com/837477

## Contributing

1. Fork it (<https://github.com/837477/XXXXXXX>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request