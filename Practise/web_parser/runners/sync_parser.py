from Practise.web_parser.common import input_goods, make_sync_request, time_it, csv_writer_to_file
from Practise.web_parser.parser import parse_html


@time_it
def run():
    """Sync parser"""

    results = []

    for good in input_goods():
        resp = make_sync_request(good)
        if resp is None:
            continue
        results.extend(parse_html(resp.text))

    csv_writer_to_file(results, file_name='sync_parser')
    print(f'Done with {len(results)} results')
