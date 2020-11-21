import argparse
import csv
from time import gmtime


def add_argument():
    parser = argparse.ArgumentParser()

    parser.add_argument("-sfp", "--source_file_path", required=True, dest="source_file_path")

    parser.add_argument("-bt", "--beer_type", required=False, dest="beer_type", action='store_true',
                        help="Find most favorite beer type")

    parser.add_argument("-bn", "--beer_name", required=False, dest="beer_name", action='store_true',
                        help="Find most favorite beer name")

    parser.add_argument("-dor", "--day_of_review", required=False, dest="day_of_review", action='store_true',
                        help="Find day with they most number of review")

    parser.add_argument("-rt", "--reviewer_stats", required=False, dest="reviewer_stats", action='store_true',
                        help="Show number of reviews for reviewer")

    return parser.parse_args()


def get_weekday(time_in_sec):
    week_day = gmtime(time_in_sec).tm_wday
    days = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[week_day]


def sort_and_print_data(dictionary: dict, title_for_key, title_for_value):
    dictionary = sorted(dictionary.items(), key=lambda y: y[1], reverse=True)
    for k, v in dictionary:
        print(f"{title_for_key}: {k[:30]:30} | {title_for_value}: {v}")


def find_most_fav_beer(source_file_path, beer_type_or_name):
    with open(source_file_path, 'r') as file:
        reader = csv.DictReader(file)
        print(f'----------------------Data about {beer_type_or_name}----------------------')
        dict_of_beer_type = {}
        for row in reader:
            review_overall = float(row.get('review_overall'))
            review_aroma = float(row.get('review_aroma'))
            beer_type = row.get(beer_type_or_name)
            dict_of_beer_type.setdefault(beer_type, (review_overall + review_aroma) / 2)
    return dict_of_beer_type


def find_day_of_review(source_file_path):
    with open(source_file_path, 'r') as file:
        reader = csv.DictReader(file)
        print('----------------------Data about review_time----------------------')
        data_dict = {}
        for row in reader:
            review_time = float(row.get('review_time'))
            weekday = str(get_weekday(review_time))
            data_dict.setdefault(weekday, 0)
            data_dict[weekday] = data_dict[weekday] + 1
    return data_dict


def find_reviewer_stats(source_file_path):
    with open(source_file_path, 'r') as file:
        reader = csv.DictReader(file)
        print('----------------------Data about review_profile_name----------------------')
        data_dict = {}
        for row in reader:
            review_profile_name = row.get('review_profilename')
            data_dict.setdefault(review_profile_name, 0)
            data_dict[review_profile_name] = data_dict[review_profile_name] + 1
    return data_dict


if __name__ == "__main__":
    args = add_argument()

    if args.beer_type:
        try:
            most_favourite_beer_type = find_most_fav_beer(args.source_file_path, 'beer_style')
        except FileNotFoundError:
            print("File not found error! Please enter valid path or file name")
        else:
            sort_and_print_data(most_favourite_beer_type, "beer type", "review rating")

    if args.beer_name:
        try:
            most_favourite_beer_name = find_most_fav_beer(args.source_file_path, 'beer_name')
        except FileNotFoundError:
            print("File not found error! Please enter valid path or file name")
        else:
            sort_and_print_data(most_favourite_beer_name, "beer name", "review rating")

    if args.day_of_review:
        try:
            data_dictionary = find_day_of_review(args.source_file_path)
        except FileNotFoundError:
            print("File not found error! Please enter valid path or file name")
        else:
            sort_and_print_data(data_dictionary, "day of review", "number of reviews")

    if args.reviewer_stats:
        try:
            data_dictionary = find_reviewer_stats(args.source_file_path)
        except FileNotFoundError:
            print("File not found error! Please enter valid path or file name")
        else:
            sort_and_print_data(data_dictionary, "review profile name", "number of reviews")
