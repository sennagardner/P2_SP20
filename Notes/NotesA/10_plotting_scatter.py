import csv
import matplotlib.pyplot as plt

with open("World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter="\t")  # split up by tabs
    data = list(reader)

