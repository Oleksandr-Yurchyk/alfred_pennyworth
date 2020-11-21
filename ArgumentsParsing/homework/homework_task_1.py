import argparse
import csv
from datetime import datetime
import os
import time


def get_list_of_files(path_to_source_files, start_year, end_year):
    list_of_files = sorted(os.listdir(path_to_source_files))
    if not list_of_files:
        raise FileNotFoundError
    filtered_list = filter(lambda x: str(start_year) <= x <= str(int(end_year) + 1), list_of_files)
    return filtered_list


def create_destination_path(destination_path):
    if destination_path not in os.listdir():
        os.mkdir(destination_path)


def write_to_csv_file(destination_path, destination_filename, list_with_files, path_to_source_files):
    with open(os.path.join(destination_path, destination_filename) + ".csv", 'a') as file_writer:
        for csv_file in list_with_files:
            with open(os.path.join(path_to_source_files, csv_file), 'r') as file_reader:
                csv_reader = csv.reader(file_reader)
                next(csv_reader)
                writer = csv.writer(file_writer)
                writer.writerow([
                    f"---------------------------Loading data from file - {csv_file}-------------------------"])
                writer.writerows(csv_reader)
            print(f"Data from file '{csv_file}' loaded successfully")


def add_argument():
    parser = argparse.ArgumentParser()

    parser.add_argument("-sy", "--start_year", required=False, dest="start_year", help="Choose from what year start",
                        default=min(os.listdir('beer_review')))

    parser.add_argument("-ey", "--end_year", required=False, dest="end_year", help="Choose by what year end",
                        default=max((os.listdir('beer_review')[:4])))

    parser.add_argument('-p', '--path_to_source_files', required=True, help="Choose path to source files",
                        dest="path_to_source_files")

    parser.add_argument('-dp', '--destination_path', required=False, dest="destination_path",
                        help="Choose path to the new folder", default=" ")

    args1 = parser.parse_args()

    parser.add_argument('-df', '--destination_filename', required=False, dest="destination_filename",
                        help="Choose name of new file",
                        default=f"{args.start_year}-{args.end_year}_{datetime.now().ctime()}")

    args2 = parser.parse_args()
    return args1, args2


if __name__ == "__main__":
    args, arg_for_dest_filename = add_argument()

    if args.path_to_source_files:
        t1 = time.time()
        try:
            csv_files = get_list_of_files(args.path_to_source_files, args.start_year, args.end_year)

            create_destination_path(args.destination_path)

            write_to_csv_file(args.destination_path, arg_for_dest_filename.destination_filename,
                              csv_files, args.path_to_source_files)
        except FileNotFoundError:
            print("File not found error! Please enter path with files inside")
        finally:
            print(f"Ran in {time.time() - t1}")
