README.md ( PL/EN)
PySpark ETL demo — przetwarzanie danych z MinIO (S3) do Parquet

Cześć!
Ten projekt pokazuje w praktyce, jak zbudować prosty pipeline ETL z użyciem PySpark i MinIO, czyli lokalnej „chmury” S3.
Cały proces polega na pobraniu pliku CSV z MinIO, przetworzeniu danych (np. usunięciu braków, agregacji),
a potem zapisaniu efektu w formacie Parquet z powrotem do MinIO.

To idealny start, żeby zobaczyć, jak w praktyce działa Big Data, Spark i przechowywanie plików w stylu AWS S3 — ale lokalnie, bez kosztów!
Jak uruchomić projekt krok po kroku?

    Włącz MinIO przez Docker Compose
    Jeśli korzystasz z pliku docker-compose.yml, odpal:

docker-compose up -d

Stwórz bucket demo w MinIO
Otwórz przeglądarkę: http://localhost:9001
Zaloguj się (minioadmin / minioadmin), utwórz bucket demo i w nim foldery input oraz output.

Wgraj plik CSV
Wrzucasz swój plik (np. sample.csv) do katalogu demo/input/.

Uruchom pipeline PySpark
Przejdź do katalogu z projektem i uruchom:

    spark-submit --packages org.apache.hadoop:hadoop-aws:3.3.6,com.amazonaws:aws-java-sdk-bundle:1.12.367 src/etl_pipeline.py

    (Uwaga: Jeśli skrypt jest gdzie indziej, popraw ścieżkę.)

    Efekt zobaczysz w MinIO
    Wejdź w demo/output/ – tam pojawi się plik demo.parquet z przetworzonymi danymi.

Co dokładnie się dzieje?

    Wejście: Surowe dane CSV wpadają do bucketa demo/input/.

    Transformacja: PySpark czyści dane (usuwa puste rekordy), robi prostą agregację (np. zliczanie wierszy według wybranej kolumny).

    Wyjście: Gotowy plik Parquet pojawia się w demo/output/ – szybki, lekki i gotowy do dalszej analizy.

Co jest potrzebne do uruchomienia?

    Docker + Docker Compose

    PySpark (np. 3.3+)

    Python 3.8 lub wyżej

    MinIO (odpalony przez Docker Compose)

    (Opcjonalnie) narzędzia MinIO Client (mc) lub AWS CLI do pracy z bucketami

Schemat architektury (opis słowny):

    MinIO (S3):
    Przechowuje dane wejściowe i wyjściowe.

    PySpark:
    Pobiera plik CSV z MinIO, przetwarza dane, zapisuje efekt jako Parquet z powrotem do MinIO.

Całość działa lokalnie – ale układ jest dokładnie taki, jak przy prawdziwym AWS S3 + Spark!
PySpark ETL demo — from MinIO (S3) to Parquet

Hi!
This project shows how to build a simple ETL pipeline using PySpark and MinIO (a local S3-compatible cloud).
The whole process is about downloading a CSV file from MinIO, processing the data (cleaning, aggregation),
and saving the result as a Parquet file back to MinIO.

Perfect to see how real-life Big Data pipelines, Spark, and S3-like storage work – all locally, for free!
How to run the project, step by step?

    Start MinIO using Docker Compose
    If you have docker-compose.yml, just run:

docker-compose up -d

Create a demo bucket in MinIO
Open your browser: http://localhost:9001
Log in (minioadmin / minioadmin), create bucket demo and folders input and output.

Upload the CSV file
Put your file (e.g., sample.csv) into demo/input/.

Run the PySpark pipeline
In your project directory, run:

    spark-submit --packages org.apache.hadoop:hadoop-aws:3.3.6,com.amazonaws:aws-java-sdk-bundle:1.12.367 src/etl_pipeline.py

    (Adjust the path if your script is elsewhere.)

    Check the result in MinIO
    Go to demo/output/ – you'll find demo.parquet with processed data.

What happens under the hood?

    Input: Raw CSV data lands in demo/input/.

    Processing: PySpark cleans the data (drops empty rows), performs simple aggregation (e.g., count by selected column).

    Output: The final Parquet file appears in demo/output/ – ready for further analysis.

Requirements

    Docker + Docker Compose

    PySpark (e.g., 3.3+)

    Python 3.8+

    MinIO (via Docker Compose)

    (Optional) MinIO Client (mc) or AWS CLI for bucket operations

Architecture overview

    MinIO (S3):
    Stores input and output data.

    PySpark:
    Reads CSV from MinIO, processes it, writes Parquet back to MinIO.

Everything works locally, but the structure is just like a real AWS S3 + Spark solution!
