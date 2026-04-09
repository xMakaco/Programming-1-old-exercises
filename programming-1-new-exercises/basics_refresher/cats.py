'''
REFRESHER EXERCISE 1:

An old cat breeder is convinced that the maximum weight a cat can grow to is determined by some specific, odd factors related to its birth.
In particular, she believes those key elements to be:
1. the cat's weight at birth
2. its fur color
3. the day of the week in which it was born
4. the weather that there was outside

Her peculiar theory states that a cat's fur color determines its absolute minumum as well as maximum potential weight.
An adult calico cat can weigh at least 2.5 kg and at most 3.5 kg, a white cat at least 3.0 kg and at most 4.0 kg,
a black one can grow up to a minimum of 3.8 kg and a maximum of 4.8 kg, and finally tabby specimen can even weight
between 5.0 kg and 6.2 kg.
Some days of the week are luckier than others, allowing cats born on those days to approximate their maximum weight more closely.
Specifically, being born on a Friday gives a cat a boost of 0.3 kg, while being born on the weekend allows a boost of 0.4 kg.
Monday is the unluckiest day, robbing cats born on this day of 0.7 kg, while Tuesday, Wednesday and Thursday are neutral,
and thus do not affect the weight the cat will reach when it becomes an adult.
Finally, the breeder also believes that the weather that there was outside during a kitten's birth can positively or negatively
influence its growth. Being born on a sunny day will make the cat stronger, granting it 0.4 kg of weight,
while being born on a stormy day is detrimental for their health, causing a loss of 0.6 kg.

In order to more easily understand how much her newly born kittens will grow, the breeder asks you to write a program which
calculates it, of course according to her theory.
The kittens' names, fur color, and weather during their birthday are already stored in a CSV file she prepared for you.
Only the day of the week in which each kitten was born is missing, but the breeder said she remembers them by heart,
so she can manually input them when she runs the program. She also forgot to add the kittens' weight at birth,
but since she said she is fine with an approximated idea of their maximum possible weight,
generate  and store random ones between 0.07 kg and 0.25 kg.
Remember that, regardless of how lucky a cat was in terms of its weight at birth, its day of birth and the weather,
it can never surpass the upper bound determined by its fur color.

Modify the CSV provided with the missing details of:
1. the kittens' weight at birth (randomized)
2. the day of the week in which they were born (user's input)
3. the final computed maximum possible weight
'''

import csv
from pathlib import Path
import random

ROOT = Path(__file__).parent.resolve()
INPUT_FILE = ROOT / 'basics_refresher' / 'cats_csv.csv'
OUTPUT_FILE = ROOT / 'basics_refresher' / 'cats_csv_updated.csv'
COLOR_MIN = {'calico': 2.5, 'white': 3.0, 'black': 3.8, 'tabby': 5.0}
COLOR_MAX = {'calico': 3.5, 'white': 4.0, 'black': 4.8, 'tabby': 6.2}


def calculate_max_weight(input_file):
    '''
        This function calculates the maximum weight each cat listed in a CSV file cen reach, according to the breeder's theory

        Reads fur color and weather from the input CSV, generates a random birth
        weight, and prompts the user to input the day of birth for each cat.
        Results are written to OUTPUT_FILE with three additional columns:
        weight_at_birth, day_of_the_week, and max_weight.

        Parameters:
        input_file (Path): path to the input CSV file containing the columns: name, fur_color, weather_at_birth.
    '''
    with open(input_file, 'r') as f:
        reader = list(csv.reader(f))
        new_cols = ['weight_at_birth', 'day_of_the_week', 'max_weight']
        reader[0] = reader[0] + new_cols  # Add new columns to header
        for cat in reader[1:]:  # Start from the second row to skip header
            weight_at_birth = random.uniform(0.07, 0.25)
            cat.append(round(weight_at_birth, 2))  # Add weight at birth to csv
            max_weight = weight_at_birth
            max_weight += COLOR_MIN[cat[1]]
            if cat[2] == 'sunny':
                max_weight += 0.4
            elif cat[2] == 'stormy':
                max_weight -= 0.6
            print(f'Enter the day of the week in which {cat[0]} was born: ')
            while True:
                day = input()
                match day.casefold():
                    case 'monday':
                        max_weight -= 0.7
                        break
                    case 'tuesday' | 'wednesday' | 'thursday':
                        break
                    case 'friday':
                        max_weight += 0.3
                        break
                    case 'saturday' | 'sunday' | 'weekend':
                        max_weight += 0.4
                        break
                    case _:
                        print(
                            "Invalid entry. Please enter a valid day of the week with correct spelling")

            max_weight = min(max_weight, COLOR_MAX[cat[1]])
            cat.append(day.casefold())  # Add day of birth to csv
            max_weight = max(max_weight, COLOR_MIN[cat[1]])
            cat.append(round(max_weight, 2))  # Add max weight to csv

    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(reader)

    print(f"Done! Results saved to {OUTPUT_FILE}")


calculate_max_weight(INPUT_FILE)



