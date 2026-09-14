import smtplib

from email.mime.text import MIMEText
from email.utils import formatdate


# =========================================================
# Gmail設定
# =========================================================

MY_EMAIL = "kaoruoza@gmail.com"

APP_PASSWORD = "owmernjntujwlafw"


# =========================================================
# テストメール
# =========================================================

def send_test_mail():

    msg = MIMEText(
        "これは本棚アプリからのテストメールです。",
        "plain",
        "utf-8"
    )

    msg["Subject"] = "【本棚アプリ】メール送信テスト"

    msg["From"] = MY_EMAIL

    msg["To"] = MY_EMAIL

    msg["Date"] = formatdate(
        localtime=True
    )


    try:

        server = smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465,
            timeout=10
        )


        server.login(
            MY_EMAIL,
            APP_PASSWORD
        )


        server.send_message(
            msg
        )


        server.quit()


        print()
        print("================================")
        print("✅ メール送信成功！")
        print("================================")


    except Exception as e:

        print()
        print("================================")
        print("❌ メール送信失敗")
        print(f"エラー: {e}")
        print("================================")


# =========================================================
# 実行
# =========================================================

if __name__ == "__main__":

    send_test_mail()
