"""
raw CSV 에서 필요없는 줄을 지우고,
컬럼명이 1줄에 오도록 정리해서 새 CSV 파일로 저장
"""

import csv

from column_detector import load_rows, find_data_block, extract_header


def preprocess(input_path, output_path):
    """
    이종헌 - 260922 생성
    input_path 파일을 정리해서 output_path 에 저장

    순서
        1. raw 파일을 통째로 읽는다.
        2. column_detector 로 컬럼명 줄과 데이터 시작 줄의 위치를 알아낸다.
        3. 컬럼명을 뽑아 새 파일의 1줄로 쓴다.
        4. 데이터 시작 줄부터 개수만큼만 가져와 2줄부터 쓴다.
           설명, 단위, 최소값 같은 줄은 이 범위 밖이라 자연히 빠진다.
    """
    rows = load_rows(input_path)
    header_line, data_start_line, data_count = find_data_block(rows)
    header = extract_header(rows, header_line)
    data_rows = []

    for i in range(data_start_line, data_start_line + data_count):
        row = rows[i]
        data_rows.append(row[1:])

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(header)
        writer.writerows(data_rows)
