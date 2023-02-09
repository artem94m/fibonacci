# Спецификация
Написать программу на языке Python, для вычисления Fn (числа Фибоначи от n).

Программа должна:
1. запускаться и выводить результат в командную строку
2. включать алгоритм расчёта за O(N)
3. включать алгоритм расчёта за O(Log N)
4. включать комплект автотестов(unit)
5. работать с аргументами командной строки:
    - -n - порядковый номер искомого числа 0..500
    - -a - алгоритм расчёта N|LogN
    - --test - запустить только тесты
6. вывод результата должен включать:
    - результат расчёта числа Fn
    - время затраченное на расчёт

Примеры запуска:
```text
fib.py -n 10 -a N (программа вычислит десятое чисто Фибоначи, за время O(N))

fib.py -n 100 -a LogN (программа вычислит сотое чисто Фибоначи, за время O(LogN))

fib.py --test
```
