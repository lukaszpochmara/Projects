# Projects# PySpark ETL demo: CSV → Parquet na S3/MinIO

## Opis projektu

Ten projekt demonstruje prosty pipeline ETL oparty o PySpark i MinIO (symulację AWS S3).  
Celem jest pobranie pliku CSV z „chmury” (MinIO), przetworzenie (czyszczenie i agregacja) w PySpark,  
a następnie zapisanie efektu do formatu Parquet w MinIO.

---

## Krok po kroku: Jak uruchomić lokalnie?

### 1. Uruchom MinIO (Docker Compose)
```bash
docker-compose up -d
