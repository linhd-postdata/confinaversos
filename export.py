#!/usr/bin/env python
import pandas as pd
from langid import classify
from slugify import slugify
from tqdm import tqdm


def main():
    form = pd.read_excel("form.xlsx", names=[
        "id", "start_time", "completion_time", "email.old", "author.old",
        "language", "title", "text", "author", "email"
    ])

    form["filename"] = (
        form.author.apply(slugify)
        + "_"
        + form.text.str.strip().str.split("\n").str.get(0).apply(slugify)
        + ".txt")
    form["lang"] = form.apply(
        lambda row: (classify(row["text"])[0]
                    if pd.isna(row["language"])
                    else row["language"].lower()[:2]),
        axis=1
    )

    for _, row in tqdm(form.iterrows()):
        with open(f"corpus/{row.lang}/{row.filename}", "w") as f:
            f.write(row.text.strip())


if __name__ == "__main__":
    main()
