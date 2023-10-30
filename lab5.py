from collections import Counter
import re

def most_common_word(text):
    """
    Функция для нахождения самого часто встречающегося слова в тексте.

    :param text: текст для анализа
    :type text: str
    :return: самое часто встречающееся слово и количество его вхождений
    :rtype: tuple
    """
    words = re.findall(r'\w+', text.lower())
    common_words = Counter(words).most_common(1)
    if common_words:
        return common_words[0]
    return None, 0

def count_words(text):
    """
    Функция для подсчета количества слов в тексте.

    :param text: текст для анализа
    :type text: str
    :return: количество слов
    :rtype: int
    """
    words = text.split()
    return len(words)
