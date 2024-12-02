
import nltk
nltk.download('all')
from nltk.chat.util import Chat, reflections
pairs = [
[
r"password_reset",
["I forgot my password|How do I reset my password?| Unable to log in, please help| My password is not working"]
],
[
r"account_issue",
["My account is locked|I cannot access my account|Why is my account suspended|I need help with my account"]
],
[
r"How_do_I_fix_my_computer_if_it_won’t_turn_on?",
["Check the power cable, outlet, and battery. Try a different outlet or power supply. If a desktop, ensure internal components like the RAM and power supply are connected securely"]
],
[
r"Why_is_my_internet_so_slow?",
["Restart your router, reduce the number of connected devices, and run a speed test. Check for bandwidth-heavy applications and ensure your device is close to the router."]
],
[
r"How_do_I_set_up_a_Wi-Fi_router?",
["Connect the router to your modem, access the router’s setup page via its IP address (usually 192.168.0.1), and configure the SSID and password"]
],
[
r"How_can_I_recover_a_deleted_file?",
["Use the Recycle Bin or Trash if not permanently deleted. For permanent deletion, try recovery tools like Recuva or Disk Drill."]
],
[
r"How can I improve my Wi-Fi signal strength?",
["Position your router centrally, use a Wi-Fi extender, reduce interference from other devices, and switch to a less crowded channel"]
],
[
r"greet",
["hi|hello"]
],
[
r"goodbye",
["Bye| See you later| Goodbye"]
],
]
chatbot = Chat(pairs, reflections)
chatbot.converse()