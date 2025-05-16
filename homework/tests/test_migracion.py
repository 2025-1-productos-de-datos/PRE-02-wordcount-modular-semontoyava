# import os


# def test_migracion():
#     filepath = "data/output/results.tsv"

#     if not os.path.exists(filepath):
#         raise FileNotFoundError(f"El archivo {filepath} no existe")

#     results = {}
#     with open(filepath, "r", encoding="utf-8") as f:
#         for line in f:
#             key, value = line.strip().split("\t")
#             results[key] = value

#     assert results.get("computational") == "3"
#     assert results.get("analytics") == "5"
