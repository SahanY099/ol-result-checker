import requests

RESULT_PRESENT_CHECKER_API_ENDPOINT = (
    "https://result.doenets.lk/result/service/examDetails"
)

NOTIFICATION_AUDIO_FILE_PATH = "./assets/notification_sound.mp3"


def is_results_available() -> bool:
    response = requests.get(RESULT_PRESENT_CHECKER_API_ENDPOINT)
    data = response.json()

    if data["yearOlResult"] == "2022":
        return True

    return False
