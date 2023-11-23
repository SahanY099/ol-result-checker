from time import sleep

from check_results_availability import is_results_available
from launch_result_page import launch_result_page
from playsound import playsound

INDEX_NO = 11111111  # Change this to your index number
NOTIFICATION_AUDIO_FILE_PATH = "./assets/notification_sound.mp3"


if __name__ == "__main__":
    is_has_published = False
    is_result_page_launched = False
    try:
        sound_play_count = 0

        while True:
            if is_has_published:
                playsound(NOTIFICATION_AUDIO_FILE_PATH)
                sound_play_count += 1

                if not is_result_page_launched:
                    is_result_page_launched = True
                    launch_result_page(index_no=INDEX_NO)

                if sound_play_count == 5:
                    break
                sleep(5)
            else:
                is_has_published = is_results_available()

                if not is_has_published:
                    print("No results available.")
                    sleep(60)
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
    except Exception as e:
        print(e)
