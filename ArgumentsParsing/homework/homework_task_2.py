import argparse
import csv
from time import gmtime


def sort_and_print_data(dictionary: dict, title_for_key, title_for_value):
    dictionary = sorted(dictionary.items(), key=lambda y: y[1], reverse=True)
    for k, v in dictionary:
        print(f"{title_for_key}: {k[:30]:30} | {title_for_value}: {v}")


def get_weekday(time_in_sec):
    week_day = gmtime(time_in_sec).tm_wday
    days = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[week_day]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-sfp", "--source_file_path",
                        required=True,
                        dest="source_file_path",
                        )

    parser.add_argument("-bt", "--beer_type",
                        required=False,
                        dest="beer_type",
                        help="Find most favorite beer type",
                        action='store_true'
                        )

    parser.add_argument("-bn", "--beer_name",
                        required=False,
                        dest="beer_name",
                        help="Find most favorite beer name",
                        action='store_true'
                        )

    parser.add_argument("-dor", "--day_of_review",
                        required=False,
                        dest="day_of_review",
                        help="Find day with they most number of review",
                        action='store_true'
                        )

    parser.add_argument("-rt", "--reviewer_stats",
                        required=False,
                        dest="reviewer_stats",
                        help="Show number of reviews for reviewer",
                        action='store_true'
                        )

    args = parser.parse_args()

    if args.beer_type:
        with open(args.source_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skips first line in csv file

            most_favourite_beer_type = {}
            for row in reader:
                review_overall = float(row[2])
                review_aroma = float(row[3])
                beer_type = row[5]
                most_favourite_beer_type.setdefault(beer_type, (review_overall + review_aroma) / 2)
            sort_and_print_data(most_favourite_beer_type, "beer type", "review rating")

    if args.beer_name:
        with open(args.source_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skips first line in csv file

            most_favourite_beer_name = {}
            for row in reader:
                review_overall = float(row[2])
                review_aroma = float(row[3])
                beer_name = row[7]
                most_favourite_beer_name.setdefault(beer_name, (review_overall + review_aroma) / 2)
            sort_and_print_data(most_favourite_beer_name, "beer name", "review rating")

    if args.day_of_review:
        with open(args.source_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skips first line in csv file

            data_dictionary = {}
            for row in reader:
                review_time = float(row[1])
                weekday = str(get_weekday(review_time))
                data_dictionary.setdefault(weekday, 0)
                data_dictionary[weekday] = data_dictionary[weekday] + 1
            sort_and_print_data(data_dictionary, "day of review", "number of reviews")

    if args.reviewer_stats:
        with open(args.source_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skips first line in csv file

            data_dictionary = {}
            for row in reader:
                review_profile_name = row[4]
                data_dictionary.setdefault(review_profile_name, 0)
                data_dictionary[review_profile_name] = data_dictionary[review_profile_name] + 1
            sort_and_print_data(data_dictionary, "review profile name", "number of reviews")
