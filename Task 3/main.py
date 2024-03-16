import timeit

def build_bad_char_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = max(1, len(pattern) - i - 1)
    return table

def boyer_moore_search(text, pattern):
    table = build_bad_char_table(pattern)
    shifts = 0
    while shifts <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[shifts + j]:
            j -= 1
        if j < 0:
            shifts += (len(pattern) - table.get(text[shifts + len(pattern)], 0)) if shifts + len(pattern) < len(text) else 1
        else:
            shifts += max(1, j - table.get(text[shifts + j], 0))
    return -1

def KMP_search(s, pattern):
    prefix = compute_prefix(pattern)
    q = 0 
    for i in range(len(s)):
        while q > 0 and pattern[q] != s[i]:
            q = prefix[q - 1] 
        if pattern[q] == s[i]:
            q += 1
        if q == len(pattern):
            q = prefix[q - 1] 

def compute_prefix(pattern):
    prefix = [0] * len(pattern)
    k = 0
    for q in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[q]:
            k = prefix[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        prefix[q] = k
    return prefix

def rabin_karp_search(text, pattern, d, q):
    M = len(pattern)
    N = len(text)
    i, j = 0, 0
    p = 0 
    t = 0 
    h = 1
    results = []

    for i in range(M-1):
        h = (h*d)%q

    for i in range(M):
        p = (d*p + ord(pattern[i]))%q
        t = (d*t + ord(text[i]))%q

    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
            else:
                results.append(i)

        if i < N-M:
            t = (d*(t-ord(text[i])*h) + ord(text[i+M]))%q
            if t < 0:
                t = t+q
    return results

file_path_1 = 'art_1.txt'
file_path_2 = 'art_2.txt'

with open(file_path_1, 'r', encoding='utf-8') as file1, open(file_path_2, 'r', encoding='utf-8') as file2:
    text_1 = file1.read()
    text_2 = file2.read()

pattern_existing = 'Метою'
pattern_non_existing = 'рядок абракадабри'

execution_time_1 = str(timeit.timeit("boyer_moore_search(text_1, pattern_existing)", globals=globals(), number=1000))
execution_time_2 = str(timeit.timeit("boyer_moore_search(text_1, pattern_non_existing)", globals=globals(), number=1000))
execution_time_3 = str(timeit.timeit("boyer_moore_search(text_2, pattern_existing)", globals=globals(), number=1000))
execution_time_4 = str(timeit.timeit("boyer_moore_search(text_2, pattern_non_existing)", globals=globals(), number=1000))

print('Алгоритм Боєра-Мура:')
print('Існуючий підрядок, text_1: ' + execution_time_1)
print('Неіснуючий підрядок, text_1: ' + execution_time_2)
print('Існуючий підрядок, text_2: ' + execution_time_3)
print('Неіснуючий підрядок, text_2: ' + execution_time_4)

execution_time_1 = str(timeit.timeit("KMP_search(text_1, pattern_existing)", globals=globals(), number=1000))
execution_time_2 = str(timeit.timeit("KMP_search(text_1, pattern_non_existing)", globals=globals(), number=1000))
execution_time_3 = str(timeit.timeit("KMP_search(text_2, pattern_existing)", globals=globals(), number=1000))
execution_time_4 = str(timeit.timeit("KMP_search(text_2, pattern_non_existing)", globals=globals(), number=1000))

print('-------')
print('Алгоритм Кнута-Морріса-Пратта:')
print('Існуючий підрядок, text_1: ' + execution_time_1)
print('Неіснуючий підрядок, text_1: ' + execution_time_2)
print('Існуючий підрядок, text_2: ' + execution_time_3)
print('Неіснуючий підрядок, text_2: ' + execution_time_4)

execution_time_1 = str(timeit.timeit("rabin_karp_search(text_1, pattern_existing, 256, 101)", globals=globals(), number=1000))
execution_time_2 = str(timeit.timeit("rabin_karp_search(text_1, pattern_non_existing, 256, 101)", globals=globals(), number=1000))
execution_time_3 = str(timeit.timeit("rabin_karp_search(text_2, pattern_existing, 256, 101)", globals=globals(), number=1000))
execution_time_4 = str(timeit.timeit("rabin_karp_search(text_2, pattern_non_existing, 256, 101)", globals=globals(), number=1000))

print('-------')
print('Алгоритм Рабіна-Карпа:')
print('Існуючий підрядок, text_1: ' + execution_time_1)
print('Неіснуючий підрядок, text_1: ' + execution_time_2)
print('Існуючий підрядок, text_2: ' + execution_time_3)
print('Неіснуючий підрядок, text_2: ' + execution_time_4)