# fix_bom.py
with open("tests/fixtures/result_recursive.txt", "rb") as f:
    content = f.read()

# Удали BOM если есть
if content.startswith(b"\xef\xbb\xbf"):
    content = content[3:]

with open("tests/fixtures/result_recursive.txt", "wb") as f:
    f.write(content)

print("BOM removed if existed")
