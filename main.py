import requests

URL = "https://openapi.rakuten.co.jp/services/api/BooksBook/Search/20170404"

APP_ID = "aa2f8790-0377-4a2d-b417-b8c20d524032"
ACCESS_KEY = "pk_7RbCf77D0DX7UiajQMG43jxaIawopWfOuCiG4ZtpStX"


def normalize_isbn(isbn):
    return isbn.replace("-", "").replace(" ", "")


def search_by_isbn(isbn):
    params = {
        "applicationId": APP_ID,
        "accessKey": ACCESS_KEY,
        "format": "json",
        "isbn": normalize_isbn(isbn),
    }

    response = requests.get(
        URL,
        params=params,
        timeout=10
    )

    print("status:", response.status_code)
    print(response.text)

    if response.status_code != 200:
        return None

    return response.json()


if __name__ == "__main__":
    result = search_by_isbn("978-4098543465")

    if result:
        print("検索件数:", result.get("count"))

        for item in result.get("Items", []):
            book = item["Item"]

            print()
            print("タイトル:", book.get("title"))
            print("ISBN:", book.get("isbn"))
            print("著者:", book.get("author"))
            print("出版社:", book.get("publisherName"))
            print("発売日:", book.get("salesDate"))
            print("価格:", book.get("itemPrice"))
