"""
raw CSV 파일에서 '진짜 데이터'가 몇 번째 줄에 있는지 찾아주는 파일.
줄 번호를 정해두지 않고, 항상 파일 안에서 찾아낸다.
"""

import csv


def load_rows(path):
    """
    이종헌 - 260922 생성
    CSV 파일을 읽어서 [[1줄의 칸들], [2줄의 칸들], ...] 모양으로 돌려준다.
    """
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        rows = list(csv.reader(f))

    return rows


def find_data_block(rows):
    """
    이종헌 - 260922 생성
    진짜 데이터 묶음의 위치를 찾아 값 3개를 돌려줌.

        header_line     : 컬럼명이 있는 줄 번호
        data_start_line : 데이터가 시작하는 줄 번호
        data_count      : 데이터가 총 몇 줄인지

    순서
        1. 파일 전체를 훑으며 첫 칸이 "trace_size"인 줄을 찾는다.
           그런 줄이 여러 개면, 뒤에 적힌 숫자가 가장 큰 줄을 고른다.
        2. 고른 줄부터 아래로 내려가며 "trace_names" 줄을 찾는다. (컬럼명 위치)
        3. 그 아래로 이어서 "trace_values" 줄을 찾는다. (데이터 시작 위치)
           사이에 낀 단위/최소값/최대값 줄들은 이 과정에서 저절로 건너뛴다.

    줄 번호는 0부터 센다.
    """
    best_line = -1
    best_count = -1

    for i in range(len(rows)):
        row = rows[i]

        if len(row) == 0:
            continue

        if row[0] != "trace_size":
            continue

        count = int(row[1])

        if count > best_count:
            best_count = count
            best_line = i

    if best_line == -1:
        raise ValueError("trace_size 를 찾을 수 없습니다.")

    header_line = find_line(rows, "trace_names", best_line)
    data_start_line = find_line(rows, "trace_values", header_line)

    return header_line, data_start_line, best_count


def find_line(rows, word, start):
    """
    이종헌 - 260922 생성
    start 줄부터 아래로 한 줄씩 내려가며, 첫 칸이 word 인 줄의 번호를 찾음.
    끝까지 못 찾으면 예상한 파일 모양이 아니라는 뜻이므로 에러 발생.
    """
    for i in range(start, len(rows)):
        row = rows[i]

        if len(row) > 0 and row[0] == word:
            return i

    raise ValueError(word + " 줄을 찾을 수 없습니다.")


def extract_header(rows, header_line):
    """
    컬럼명 줄에서 컬럼명만 뽑아냄.

    맨 앞 칸에는 "trace_names" 라는 이름표가 들어있을 뿐 컬럼명이 아니라서 버림.
    시간 컬럼은 원래 이름이 비어 있으므로 "Time" 이라고 채워줌.
    """
    names = list(rows[header_line][1:])

    if names[0] == "":
        names[0] = "Time"

    return names
