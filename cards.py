suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

print("\n".join(f"{v} of {s}" for s in suits for v in values))


