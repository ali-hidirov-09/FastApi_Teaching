d = {
    "name": "ali",
    "age": 20
}
updated_d = {
    "name": "ALI",
    "age": 25
}
for key, value in updated_d.items():
    print(f"{key},{value}")
    if hasattr(d, key):
        setattr(d, key, value)

print(d)
print(updated_d)