
users = {}


def counter_character(word):
    sign = ['@', '$', '%', '&', '*', '_', '(', ')']
    c = 0
    for letter in word:
        if letter in sign:
            c += 1
    return c

def counter_number(pey):
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    k = 0
    for numbers in pey:
        if numbers in number:
            k += 1
    return k

def check_password(password):
    if " " in password:
        return False
    return True

def add_user(username, password):
    if username in users:
        return "Xatolik: Bu username ilgari ro'yxatda mavjud."
    elif len(password) < 6 or counter_character(password) == 0 or counter_number(password) == 0 or not check_password(
            password):
        return "Xatolik: Parol kamida 6 ta belgidan iborat bo'lishi kerak, maxsus belgilar va raqamlar bo'lishi zarur."
    else:
        users[username] = password
        return f"Foydalanuvchi {username} muvaffaqiyatli qo'shildi."


def change_password(username, old_password, new_password):
    if username in users and users[username] == old_password:
        if len(new_password) >= 6 and counter_character(new_password) > 0 and counter_number(
                new_password) > 0 and check_password(new_password):
            users[username] = new_password
            return f"{username}ning paroli muvaffaqiyatli yangilandi."
        else:
            return "Yangi parol shartlarga javob bermaydi."
    else:
        return "Xatolik: Eski parol noto'g'ri yoki foydalanuvchi topilmadi."


def change_username(old_username, new_username, password):
    if old_username in users and users[old_username] == password:
        if new_username in users:
            return f"Xatolik: Yangi username ilgari ro'yxatda mavjud."
        else:
            users[new_username] = users.pop(old_username)
            return f"Foydalanuvchi username {old_username} dan {new_username} ga muvaffaqiyatli o'zgartirildi."
    else:
        return "Xatolik: Foydalanuvchi yoki parol noto'g'ri."


def delete_user(username):
    if username in users:
        del users[username]
        return f"Foydalanuvchi {username} muvaffaqiyatli o'chirildi."
    else:
        return f"Xatolik: {username} topilmadi."


def login(username, password):
    if username in users and users[username] == password:
        return f"Foydalanuvchi {username} tizimga kirish muvaffaqiyatli."
    else:
        return "Xatolik: Noto'g'ri username yoki parol."


def is_user_registered(username):
    if username in users:
        return f"Foydalanuvchi {username} tizimda ro'yxatdan o'tgan."
    else:
        return "Foydalanuvchi ro'yxatda mavjud emas."


def main():
    while True:
        print("\n--- Login/Password tizimi ---")
        print("1. Yangi foydalanuvchi qo'shish")
        print("2. Login qilish")
        print("3. Parolni yangilash")
        print("4. Username o'zgartirish")
        print("5. Foydalanuvchini o'chirish")
        print("6. Foydalanuvchi ro'yxatda mavjudligini tekshirish")
        print("7. Chiqish")
        choice = input("Tanlovni kiriting (1-7): ")

        if choice == '1':
            username = input("Loginni kiriting: ")
            password = input("Parolni kiriting: ")
            print(add_user(username, password))

        elif choice == '2':
            username = input("Loginni kiriting: ")
            password = input("Parolni kiriting: ")
            print(login(username, password))

        elif choice == '3':
            username = input("Loginni kiriting: ")
            old_password = input("Eski parolni kiriting: ")
            new_password = input("Yangi parolni kiriting: ")
            print(change_password(username, old_password, new_password))

        elif choice == '4':
            old_username = input("Eski loginni kiriting: ")
            new_username = input("Yangi loginni kiriting: ")
            password = input("Parolni kiriting: ")
            print(change_username(old_username, new_username, password))
            

        elif choice == '5':
            username = input("O'chiriladigan loginni kiriting: ")
            print(delete_user(username))

        elif choice == '6':
            username = input("Foydalanuvchi loginini kiriting: ")
            print(is_user_registered(username))

        elif choice == '7':
            print("Tizimdan chiqish...")
            break

        else:
            print("Noto'g'ri tanlov. Iltimos, 1 dan 7 gacha bo'lgan raqamni tanlang.")


if __name__ == "__main__":
    main()

