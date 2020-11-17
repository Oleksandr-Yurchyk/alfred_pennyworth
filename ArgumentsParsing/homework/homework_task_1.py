import argparse
import csv
import glob
from datetime import datetime
import os
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-sy", "--start_year",
                        required=False,
                        dest="start_year",
                        help="Choose from what year start",
                        default=min(os.listdir('beer_review/')),
                        )

    parser.add_argument("-ey", "--end_year",
                        required=False,
                        dest="end_year",
                        help="Choose by what year end",
                        default=str(sorted(os.listdir('beer_review/'), reverse=True))[2:6],
                        )

    parser.add_argument('-p', '--path_to_source_files',
                        required=True,
                        help="Choose path to source files",
                        dest="path_to_source_files",
                        )

    parser.add_argument('-dp', '--destination_path',
                        required=False,
                        dest="destination_path",
                        help="Choose path to the new folder",
                        default=" "
                        )
    args = parser.parse_args()

    parser.add_argument('-df', '--destination_filename',
                        required=False,
                        dest="destination_filename",
                        help="Choose name of new file",
                        default=f"{args.start_year}-{args.end_year}_{datetime.now().ctime()}",
                        )
    kwargs = parser.parse_args()

    if args.path_to_source_files:
        t1 = time.time()
        list_of_files = sorted([csv_file for csv_file in os.listdir(args.path_to_source_files)])
        csv_files = filter(lambda x: str(args.start_year) <= x <= str(int(args.end_year) + 1), list_of_files)

        if args.destination_path not in os.listdir():
            os.mkdir(args.destination_path)
        with open(os.path.join(args.destination_path, kwargs.destination_filename) + ".csv", 'a') as file_writer:
            for csv_file in csv_files:
                with open(os.path.join(args.path_to_source_files, csv_file), 'r') as file_reader:
                    csv_reader = csv.reader(file_reader)
                    next(csv_reader)
                    writer = csv.writer(file_writer)
                    writer.writerow([
                        f"---------------------------Loading data from file - {csv_file}-------------------------"])
                    writer.writerows(csv_reader)
                print(f"Data from file '{csv_file}' loaded successfully")
        print(f"Ran in {time.time() - t1}")
