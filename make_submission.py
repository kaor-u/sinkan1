import os
import shutil
import zipfile


# =========================================================
# 設定
# =========================================================

# このスクリプトを置いているフォルダ
base_dir = os.path.dirname(
    os.path.abspath(__file__)
)

# 提出用フォルダ
submission_dir = os.path.join(
    base_dir,
    "bookshelf_submission"
)

# 提出用ZIP
zip_path = os.path.join(
    base_dir,
    "bookshelf_submission.zip"
)


# =========================================================
# 提出用フォルダを作成
# =========================================================

os.makedirs(
    submission_dir,
    exist_ok=True
)

# templatesフォルダ
templates_dir = os.path.join(
    submission_dir,
    "templates"
)

os.makedirs(
    templates_dir,
    exist_ok=True
)

# staticフォルダ
static_dir = os.path.join(
    submission_dir,
    "static"
)

os.makedirs(
    static_dir,
    exist_ok=True
)


# =========================================================
# コピーするファイル
# =========================================================

files = [
    "app.py",
    "requirements.txt"
]

template_files = [
    "index.html",
    "book_detail.html",
    "email_preview.html"
]

static_files = [
    "style.css"
]


# =========================================================
# ファイルをコピー
# =========================================================

for filename in files:

    source = os.path.join(
        base_dir,
        filename
    )

    destination = os.path.join(
        submission_dir,
        filename
    )

    if not os.path.exists(source):

        print(
            f"⚠️ ファイルが見つかりません: {filename}"
        )

    else:

        shutil.copy2(
            source,
            destination
        )

        print(
            f"✅ コピー: {filename}"
        )


# =========================================================
# templates
# =========================================================

for filename in template_files:

    source = os.path.join(
        base_dir,
        "templates",
        filename
    )

    destination = os.path.join(
        templates_dir,
        filename
    )

    if not os.path.exists(source):

        print(
            f"⚠️ templates/{filename} が見つかりません"
        )

    else:

        shutil.copy2(
            source,
            destination
        )

        print(
            f"✅ コピー: templates/{filename}"
        )


# =========================================================
# static
# =========================================================

for filename in static_files:

    source = os.path.join(
        base_dir,
        "static",
        filename
    )

    destination = os.path.join(
        static_dir,
        filename
    )

    if not os.path.exists(source):

        print(
            f"⚠️ static/{filename} が見つかりません"
        )

    else:

        shutil.copy2(
            source,
            destination
        )

        print(
            f"✅ コピー: static/{filename}"
        )


# =========================================================
# ZIP作成
# =========================================================

print()
print("📦 ZIPを作成しています...")


# 以前のZIPがあれば削除
if os.path.exists(zip_path):

    os.remove(
        zip_path
    )


with zipfile.ZipFile(
    zip_path,
    "w",
    zipfile.ZIP_DEFLATED
) as zipf:

    for root, dirs, filenames in os.walk(
        submission_dir
    ):

        for filename in filenames:

            file_path = os.path.join(
                root,
                filename
            )

            # ZIP内での相対パス
            arcname = os.path.relpath(
                file_path,
                submission_dir
            )

            # WindowsでもZIP内は / 区切りにする
            arcname = arcname.replace(
                os.sep,
                "/"
            )

            zipf.write(
                file_path,
                arcname
            )


# =========================================================
# 完了
# =========================================================

print()
print("========================================")
print("🎉 提出用ファイルの作成が完了しました！")
print("========================================")

print()
print(
    f"📁 フォルダ:"
)
print(
    submission_dir
)

print()
print(
    f"📦 ZIP:"
)
print(
    zip_path
)

print()
print("ZIPの中身:")

with zipfile.ZipFile(
    zip_path,
    "r"
) as zipf:

    for name in zipf.namelist():

        print(
            f"  {name}"
        )

print()
print("※ books.db はコピーしていません。")
