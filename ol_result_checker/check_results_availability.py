import requests

RESULT_PRESENT_CHECKER_API_ENDPOINT = (
    "https://result.doenets.lk/result/service/examDetails"
)

NOTIFICATION_AUDIO_FILE_PATH = "./assets/notification_sound.mp3"


def is_results_available() -> bool:
    response = requests.get(RESULT_PRESENT_CHECKER_API_ENDPOINT)
    data = response.json()

    # Check if "2022" or "2022/2023" is a key
    if "2022" in data.keys() or "2022/2023" in data.keys():
        return True

    # Check if "2022" or "2022/2023" is a value
    if "2022" in data.values() or "2022/2023" in data.values():
        return True

    return False
