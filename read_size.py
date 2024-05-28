# the first ssh to python
# the second run file check_size.sh
# the finally get file

from os import getenv
from dotenv import load_dotenv, dotenv_values
import send_bot
import asyncio
import subprocess
load_dotenv()
SERVER = getenv("SERVER")
USER = getenv("USER_SSH")
PASSWORD = getenv("PASSWORD_SSH")


async def main():
    cmd = f"sshpass -p {PASSWORD} ssh {USER}@{SERVER} 'bash check.sh'"
    stdout, stderr = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    await send_bot.send_message(stdout.decode("utf-8"))


if __name__ == '__main__':
    asyncio.run(main())
