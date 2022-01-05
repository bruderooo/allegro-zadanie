# Spis treści #

1. [Instrukcja instalacji](#instrukcja-instalacji)
2. [Instrukcja uruchomienia](#instrukcja-uruchomienia)
3. [Korzystanie z aplikacji](#korzystanie-z-aplikacji)
4. [Możliwe rozszerzenia do dodania](#moliwe-rozszerzenia-do-dodania)

----
<a name="instrukcja-instalacji"></a>

# Instrukcja instalacji # 

Sugerowana wersja pythona to Python 3.9 (wersje pythona można ustawić podając ją jako parametry --python dla polecenia
virtualenv).

Instalacja z użyciem pip w systemie Linux/MacOS:

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Instalacja z użyciem pip na Windowsie:

```commandline
py -m virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

----
<a name="instrukcja-uruchomienia"></a>

# Instrukcja uruchomienia #

Po zainstalowaniu aplikacji, można ją uruchomić za pomocą polecenia:

```commandline
python app.py
```

Jeżeli chcemy postawić aplikację na konkrentym adresie, możemy użyć parametru --ip.

```commandline
python app.py --ip 127.0.0.1
```

Jeżeli chcemy postawić aplikację na konkrentym porcie, możemy użyć parametru --port.

```commandline
python app.py --port 5000
```

Można również użyć dwóch parametrów:

```commandline
python app.py --ip 127.0.0.1 --port 5000
```

Żeby zobaczyć listę dostępnych komend, wpisz:

```commandline
python app.py --help
```

----
<a name="korzystanie-z-aplikacji"></a>

# Korzystanie z aplikacji #

Po uruchomieniu aplikacji możemy skorzystać z endpointów z użyciem curl, albo korzystając z dokumentacji swaggera pod
głównym adresem.

Przykład korzystania z endpointów:

```commandline
curl -X GET http://127.0.0.1:5000/list_repos/bruderooo
curl -X GET http://127.0.0.1:5000/percentage/bruderooo
```

----
<a name="moliwe-rozszerzenia-do-dodania"></a>

# Możliwe rozszerzenia do dodania #

* testy
* rozszerzenie funkcjonalności (o np możliwość logowania do GitHuba, tak żeby można było wysłać więcej zapytań)
* dodaiwanie nowych endpointów (np. endpoint do podawania gwiazdek)
