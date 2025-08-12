import random

def draw_dice_face(value):
    dice_faces = {
        1: ["-----",
            "|   |",
            "| o |",
            "|   |",
            "-----"],
        2: ["-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----"],
        3: ["-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----"],
        4: ["-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----"],
        5: ["-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----"],
        6: ["-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----"]
    }

    for line in dice_faces[value]:
        print(line)

# Roll a dice
dice_value = random.randint(1, 6)
print(f"DIACE ROLLED= {dice_value}")
draw_dice_face(dice_value)
