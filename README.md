
## Instalacja

```
docker-compose build

```


Instalacja bazy danych:

```
docker-compose run web python src/eMenu_project/manage.py migrate

```

Tworzenie superuser:

```
docker-compose run web python src/eMenu_project/manage.py createsuperuser

```

Załadowanie danych początowych:

```
docker-compose run web python src/eMenu_project/manage.py loaddata initial_data.json

```

Nawigacja do localhost:8080


# Krótki opis aplikacji

Projekt i implementacja samodzielnego serwisu eMenu, służącego jako restauracyjna karta menu online.

Raportowanie:
1. mechanizm, który raz dziennie o 10:00 wyśle e-mail do wszystkich użytkowników
aplikacji
2. E-mail musi zawierać informację o nowo dodanych oraz ostatnio zmodyfikowanych daniach
3. Informacja dotyczy tylko tych dań, które zostały zmodyfikowane poprzedniego dnia.

## Karta menu

Aplikacja umożliwia:

* tworzenie karty (przez zautoryzowanego użykownika)
* usuwanie karty (przez użytkownika, który utworzył ten obiekt)
* modyfikowanie karty (przez użytkownika, który utworzył ten obiekt)
* przegląd niepustych kart/karty (bez autoryzacji)

CRUD dla modelu Karty

Karta:
* nazwa (name)
* opis (description)
* danie (dish)
* data dodania (created)
* data aktualizacji (updated)

## Danie

Aplikacja umozliwia:

* tworzenie dania (przez zautoryzowanego użykownika)
* usuwanie dania (przez użytkownika, który utworzył ten obiekt)
* modyfikowanie dania (przez użytkownika, który utworzył ten obiekt)
* przegląd dań/dania (bez autoryzacji)

CRUD dla modelu Danie

Danie:
* nazwa (name)
* opis (description)
* cena (price)
* czas przygotowania (preparation_tim)
* danie (dish)
* data dodania (created)
* data aktualizacji (updated)
* danie wegetariańskie (vegetarian)
* zdjęcie (photo)

Danie do karty dodaje się za pomocą metody join_dish (/api/cards/<pk>/join_dish - PUSH)


Możliwość sortowania listy kart po nazwie oraz liczbie dań (GET):
* /api/cards/?ordering=name
* /api/cards/?ordering=dishes_count

Możliwość filtrowanie listy po nazwie oraz okresie dodania i ostatniej aktualizacji (GET)
* /api/cards/?name=....
* /api/cards/?created=...
* /api/cards/?updated=...


Wysyłanie maila do użytkowników codziennie o 10.00 z informacją o dodanych/zauktualizowanych  - celery

Autoryzacja za pomocą tokena.

Dostęp do przeglądania, tworzenia, usuwania i modyfikowania uzytkowników ma tylko admin.

Dokumentacja generowana automatycznie  -  /swagger

Testy - pytest (coverage 91%)