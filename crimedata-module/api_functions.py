import requests


def get_crime_data(api_key: str, state_codes: list, crimes: list, start_year: int, end_year: int):
    """ Takes state codes and crimes as lists and returns a dictionary containing crime data for each crime for each state"""
    crime_data = {}
    response_list = []
    base_url = 'https://api.usa.gov/crime/fbi/sapi/'
    for crime in crimes:
        for state_code in state_codes:
            url = base_url+f'/api/summarized/state/{state_code.lower()}/{crime}/{start_year}/{end_year}?API_KEY={api_key}'
            response = requests.get(url).json()
            response_list+=response['results']
        crime_data[crime] = response_list
    return crime_data


