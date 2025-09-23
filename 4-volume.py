import random
import ctypes
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Pega dispositivo de áudio
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Salva volume atual
volume_atual = volume.GetMasterVolumeLevelScalar()

# Sorteia novo volume
volume_random = random.randint(0, 100)

# Aplica novo volume
volume.SetMasterVolumeLevelScalar(volume_random / 100, None)

# Exibe pop-up com OK / Cancelar
mensagem = f"O volume foi ajustado para {volume_random}%.\n\nDeseja manter essa configuração?"
titulo = "Controle de Volume Aleatório"
resposta = ctypes.windll.user32.MessageBoxW(0, mensagem, titulo, 1)  # 1 = OK/Cancel

# Se o usuário clicar em Cancelar (resposta == 2), volta ao volume original
if resposta == 2:
    volume.SetMasterVolumeLevelScalar(volume_atual, None)
    ctypes.windll.user32.MessageBoxW(0, "O volume original foi restaurado.", titulo, 0)
else:
    ctypes.windll.user32.MessageBoxW(0, "O novo volume foi mantido.", titulo, 0)
