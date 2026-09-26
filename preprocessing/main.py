"""
Unity 에서 업로드한 raw CSV를 전처리해서 data/processed/ 에 저장한다.

사용법:
    python main.py exp2_008_시나리오1_CC_IMU_정방향.csv

파일 경로는 main.py의 위치를 기준으로 잡는다.
Unity 가 이 스크립트를 어느 폴더에서 실행할지 알 수 없기 때문이다.
"""

import os
import sys

from imu_processor import preprocess


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(THIS_DIR)

RAW_DIR = os.path.join(PROJECT_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(PROJECT_DIR, "data", "processed")


def main():
    """
    파일을 전처리해서 data/processed/ 에 저장한다.

    순서
        1. 실행할 때 파일 경로를 줬는지 확인한다. 없으면 사용법을 알리고 종료한다.
        2. 파일 이름만 줬으면 data/raw/ 안에서 찾는다.
           전체 경로를 줬으면 그대로 쓴다. (Unity 가 넘겨주는 경로)
        3. 저장할 폴더가 없으면 만든다.
        4. 전처리를 실행하고, 결과 파일 이름은 원본과 똑같이 한다.
        5. 저장 위치를 화면에 출력한다. Unity는 이 출력을 읽어 결과를 찾는다.

    종료 코드 1 = '실패했다'는 뜻 -> Unity 쪽에서 성공 여부를 판단할 수 있다.
    """
    if len(sys.argv) < 2:
        print("사용법: python main.py <파일이름>")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.isabs(input_path):
        input_path = os.path.join(RAW_DIR, input_path)

    if not os.path.exists(PROCESSED_DIR):
        os.makedirs(PROCESSED_DIR)

    file_name = os.path.basename(input_path)
    output_path = os.path.join(PROCESSED_DIR, file_name)

    preprocess(input_path, output_path)

    print("저장 완료:", output_path)


if __name__ == "__main__":
    main()
