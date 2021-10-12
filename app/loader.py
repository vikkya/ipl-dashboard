import csv
import datetime

import models
from databases import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("matches.db", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_records = models.Record(
            date=datetime.datetime.strptime(row["date"], "%Y-%m-%d"),
            country=row["country"],
            cases=row["cases"],
            deaths=row["deaths"],
            recoveries=row["recoveries"]
        )

        db.add(db_records)
    db.commit()
db.close()