Zadanie 1:
- Znaleziono dwa przesunięcia z najwyższym wynikiem równym 1, jednak tylko jedno z nich (k=233) dawało sensowny tekst, co zostało sprawdzone ręcznie
- Entropia nie wystarczy ponieważ szyfr cezara jest prostym przesunięciem, które nie zmienia prawdopodobieństwa występowania danych bajtów. Z tego powodu entropia jest taka sama dla każdego przesunięcia.

Zadanie 2:
- W pierwszym przypadku powtarzają się te same fragmenty, ponieważ długość klucza i powtarzanego w tekście BRAMA są takie same, więc każdy kolejny fragment, który się powtarza jest szyfrowany w ten sam sposób. Z kolei dla klucza KOD te długości różnią się, co prowadzi do korzystania z innych bajtów klucza do kolejnych powtórzeń


Zadanie 3:
Wybrany klucz: tat
Liczba prób: 17576 | Czas: 2.3196 s
Entropia kryptogramu: 7.9271
Entropia odszyfrowania: 4.3259
- Ponowne szyfrowanie z błędnym kluczem działa ze względu na logikę działania funkcji XOR - (A^K)^K = A. Nawet jeśli klucz jest błędny, to pierwotny strumień tekstu zostanie odtworzony
- Ranking entropii może zasugerować błędny klucz kiedy tekstem nie jest tekst naturalny, a coś co ma naturalnie wysoką entropię - np plik .png