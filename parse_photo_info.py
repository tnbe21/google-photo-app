import csv
import pprint


with open('photo_info_list.csv') as fp:
    reader = csv.DictReader(fp)

    d5300_focal_length_sum = 0
    d5300_count = 0
    d5300_focal_length_count_map = {}

    xz_2_focal_length_sum = 0
    xz_2_count = 0

    focal_length_sum = 0
    focal_length_total_count = 0
    focal_length_count_map = {}
    for row in reader:
        focal_length = row.get('focal_length(35mm equivalent)')
        if not focal_length:
            continue

        focal_length_sum += float(focal_length)
        focal_length_total_count += 1

        if 'D5300' in row.get('camera_model'):
            d5300_focal_length_sum += float(focal_length)
            d5300_count += 1
            d5300_focal_length_count_map.setdefault(focal_length, 0)
            d5300_focal_length_count_map[focal_length] += 1

        if 'XZ-2' in row.get('camera_model'):
            xz_2_focal_length_sum += float(focal_length)
            xz_2_count += 1

        focal_length_count_map.setdefault(focal_length, 0)
        focal_length_count_map[focal_length] += 1

    print(f'D5300: focal length average(35mm equivalent): {d5300_focal_length_sum / d5300_count}')
    print(f'XZ-2: focal length average(35mm equivalent): {xz_2_focal_length_sum / xz_2_count}')
    print(f'focal length average(35mm equivalent): {focal_length_sum / focal_length_total_count}')
    print(f'focal length count:')
    pprint.pprint(sorted(focal_length_count_map.items(), key=lambda x: -x[1]))
    print(f'D5300 focal length count:')
    pprint.pprint(sorted(d5300_focal_length_count_map.items(), key=lambda x: -x[1]))

