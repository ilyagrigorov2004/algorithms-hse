import pytest
from anagrams import group_anagrams


# ========== ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ ==========

def sorted_groups(result):
    """
    Приводит результат к сравнимому виду:
    сортирует группы и слова внутри каждой группы.
    Нужно, потому что порядок групп не фиксирован.
    """
    return sorted([sorted(group) for group in result])


# ========== БАЗОВЫЕ ТЕСТЫ ==========

def test_example():
    """Пример из условия"""
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert sorted_groups(result) == sorted_groups(expected)


def test_single_word():
    """Одно слово"""
    assert group_anagrams(["abc"]) == [["abc"]]


def test_two_words_same():
    """Два слова-анаграммы"""
    result = group_anagrams(["abc", "bca"])
    assert len(result) == 1
    assert sorted(result[0]) == ["abc", "bca"]


def test_two_words_different():
    """Два слова не анаграммы"""
    result = group_anagrams(["abc", "def"])
    assert len(result) == 2


# ========== ГРАНИЧНЫЕ СЛУЧАИ ==========

def test_empty_list():
    """Пустой список"""
    assert group_anagrams([]) == []


def test_empty_string():
    """Пустая строка"""
    assert group_anagrams([""]) == [[""]]


def test_multiple_empty_strings():
    """Несколько пустых строк — все анаграммы"""
    result = group_anagrams(["", "", ""])
    assert len(result) == 1
    assert result[0] == ["", "", ""]


def test_single_characters():
    """Однобуквенные слова"""
    result = group_anagrams(["a", "b", "c"])
    assert len(result) == 3


def test_duplicates():
    """Одинаковые слова"""
    result = group_anagrams(["a", "a", "a"])
    assert len(result) == 1
    assert result[0] == ["a", "a", "a"]


# ========== НЕТРИВИАЛЬНЫЕ СЛУЧАИ ==========

def test_all_anagrams():
    """Все слова — анаграммы"""
    result = group_anagrams(["abc", "bca", "cab", "acb"])
    assert len(result) == 1
    assert sorted(result[0]) == ["abc", "acb", "bca", "cab"]


def test_no_anagrams():
    """Нет анаграмм — каждое слово в своей группе"""
    result = group_anagrams(["abc", "def", "ghi"])
    assert len(result) == 3


def test_different_lengths():
    """Слова разной длины"""
    result = group_anagrams(["ab", "ba", "abc", "cab"])
    assert len(result) == 2


def test_case_sensitive():
    """Регистр важен: 'Abc' != 'abc'"""
    result = group_anagrams(["Abc", "abc"])
    assert len(result) == 2


def test_long_words():
    """Длинные слова"""
    result = group_anagrams(["abcdefghij", "jihgfedcba"])
    assert len(result) == 1


def test_mixed():
    """Смешанный случай"""
    result = group_anagrams(["eat", "tea", "ate", "dog", "god", "cat"])
    expected = [["eat", "tea", "ate"], ["dog", "god"], ["cat"]]
    assert sorted_groups(result) == sorted_groups(expected)


def test_with_spaces():
    """Слова с пробелами — все анаграммы"""
    result = group_anagrams(["a b", "b a", "ab "])
    assert len(result) == 1  # все три — анаграммы


def test_with_spaces_different():
    """Слова с пробелами и без"""
    result = group_anagrams(["a b", "b a", "abc"])
    assert len(result) == 2


def test_numbers_and_letters():
    """Буквы и цифры"""
    result = group_anagrams(["a1", "1a", "b2"])
    assert len(result) == 2


# ========== СТРЕСС-ТЕСТ ==========

def test_large():
    """Большой список — проверяем, что все слова на месте"""
    words = []
    for i in range(100):
        word = f"word{i}"
        words.append(word)
        words.append(word[::-1])

    result = group_anagrams(words)

    # Проверяем, что все слова на месте
    all_words = []
    for group in result:
        all_words.extend(group)
    assert sorted(all_words) == sorted(words)


def test_large_unique():
    """Большой список с уникальными анаграммами"""
    words = []
    for i in range(26):
        letter = chr(ord('a') + i)  # 'a', 'b', ..., 'z'
        word = letter * 3  # "aaa", "bbb", ..., "zzz"
        words.append(word)
        words.append(word[::-1])  # "aaa" → "aaa" (та же)

    result = group_anagrams(words)
    assert len(result) == 26


def test_many_groups():
    """Много групп"""
    words = ["abc", "bca", "def", "ghi", "jkl", "lkj"]
    result = group_anagrams(words)
    assert len(result) == 4  # ["abc","bca"], ["def"], ["ghi"], ["jkl","lkj"]