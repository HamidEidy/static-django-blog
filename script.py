import os
import sys
from datetime import datetime

# تنظیمات
FILE_NAME = "sample.txt"  # نام فایل متنی
REPO_DIR = "/home/hamiddreza/Desktop/blog"  # مسیر ریپوی گیتهاب شما
GIT_REMOTE = "origin"  # نام ریموت گیت (معمولا origin است)
GIT_BRANCH = "master"  # نام برنچ (main یا master)

def modify_file():
    # اضافه کردن یک Space به فایل
    with open(FILE_NAME, 'a') as f:
        f.write(" ")
    print(f"یک Space به فایل {FILE_NAME} اضافه شد.")

def git_operations():
    # دستورات گیت
    os.system("git add .")
    commit_message = f"اضافه کردن Space در {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    os.system(f'git commit -m "{commit_message}"')
    os.system(f"git push {GIT_REMOTE} {GIT_BRANCH}")
    print("تغییرات با موفقیت به گیتهاب پوش شد.")

def main():
    # تغییر مسیر به دایرکتوری ریپو
    os.chdir(REPO_DIR)
    
    # ایجاد فایل اگر وجود نداشته باشد
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as f:
            f.write("")
    
    # دریافت تعداد دفعات از کاربر
    if len(sys.argv) < 2:
        print("لطفا تعداد دفعات را وارد کنید: python script.py <تعداد>")
        return
    
    try:
        count = int(sys.argv[1])
    except ValueError:
        print("لطفا یک عدد صحیح وارد کنید")
        return
    
    # اجرا به تعداد مشخص شده
    for i in range(count):
        print(f"\nاجرای شماره {i+1} از {count}")
        modify_file()
        git_operations()
    
    print(f"\n✅ {count} کامیت و پوش با موفقیت انجام شد.")

if __name__ == "__main__":
    main()