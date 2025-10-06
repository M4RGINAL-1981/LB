import random
from datetime import datetime

def log_action(action, score):
    """Записывает указанное действие в файл coin_game_log.txt в формате дата время действие текущий

    Parameters:
    action (string): Победа или Проигрыш.
    score (int): Текущий счёт.
    """
    current_time = datetime.now().strftime("%Y-%m-%d | %H:%M:%S |")
    log_entry = f"{current_time} | {action} | {score}/5\n"

    with open("coin_game_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

def main():
    print("Давайте играть в орёл или решка! Для выбора введите 'о' или 'р'.")
    log_action("Игра началась", 0)

    wins = 0
    total_games = 0

    while wins < 5:
        player_choice = input("\nВаш выбор (о/р): ").lower().strip()

        # Обработка некорректного ввода
        if player_choice not in ['о', 'р']:
            print("Пожалуйста, введите только 'о' или 'р'")
            log_action(f"Некорректный ввод: '{player_choice}'", wins)
            continue

        # "Подбрасывание" монеты
        coin = random.choice(['О', 'Р'])
        print(f"Монета показала: {coin}")

        # Определение результата
        player_choice_full = 'О' if player_choice == 'о' else 'Р'
        if (player_choice_full == coin):
            wins += 1
            result = "Победа"
            print(f"Верно! Ваш счёт: {wins}/5")
        else:
            result = "Поражение"
            print(f"Неверно! Ваш счёт: {wins}/5")

        total_games += 1

        # Запись в лог
        log_action(f"{player_choice_full} | {coin} | {result}", wins) # Что выбрал игрок, что выплало, результат

    # Запись окончания игры
    print(f"\n🎉 Поздравляем! Вы достигли {wins} побед за {total_games} игр!")
    log_action(f"Игра завершена. Общее количество игр: {total_games}", wins)

if __name__ == "__main__":
    main()
