from mongo_db_assist.app_handler import app_handler
from redis_lru_cache.cache_redis import time_calculation


def main():
    while True:
        print('#'*40)
        print("Welcome to the Home Work 10 application!")
        print('#' * 40)
        print("Please choose one of the following options:")
        print("1. Redis LRU Cache")
        print("2. MongoDB_personal_assistant")
        print("3. Exit")
        user_input = int(input(">>>: "))
        try:
            if user_input == 1:
                time_calculation()
                print()
            elif user_input == 2:
                app_handler()
                print()
            elif user_input == 3:
                print("Goodbye!")
                break
        except ValueError:
            print("Please enter a number")
            main()


if __name__ == '__main__':
    main()


