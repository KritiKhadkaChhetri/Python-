letter = '''Dear <|NAME|>,
You are selected!
<|DATE|> '''

print(letter.replace("<|NAME|>", "Alice").replace("<|DATE|>", "June 1, 2024"))