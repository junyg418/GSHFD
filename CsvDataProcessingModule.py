import pandas as pd


def get_user_data() -> pd.DataFrame:
    """
    user_data.csv 파일을 불러와 데이터 프레임으로 변경하는 함수
    :return:
        pandas.DataFrame : user_data.csv -> DataFrame
    """
    user_data_df = pd.read_csv('./csv_file/user_data.csv')
    return user_data_df


def get_link_to_list() -> list:
    """
    user_data.csv 파일에서 link 를 추출 후 리스트로 변경하여 반환하는 함수
    :return:
        user_data.csv -> links -> list
    """
    user_data_df = get_user_data()
    link_df = user_data_df['link']
    link_list = link_df.values.tolist()
    return link_list


if __name__ == '__main__':
    print(get_link_to_list())
