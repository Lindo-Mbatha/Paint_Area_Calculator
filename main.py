print("Paint Area Calculator")
print("Reminder: 1 can is equal to 5 square meters of wall and answer is always rounded up")
print("Provide the Height and Width of the wall you want to print")

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    print(f"You'll need {round(number_of_cans)} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

