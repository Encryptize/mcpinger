from fastapi import APIRouter
from mcstatus import BedrockServer

from utils import remove_colours
from models import Status

router = APIRouter(
    prefix="/bedrock",
    tags=["Minecraft: Bedrock Edition"]
)

@router.get("/ping/{address}", response_model=Status)
async def bedrock_ping(address: str):
    data = {"online": False, "ip": address}

    try:
        server = BedrockServer.lookup(address)
        status = await server.async_status()

        data['online'] = True
        data['players'] = {'online': status.players_online, 'max': status.players_max}
        data['protocol'] = status.version.protocol
        data['version'] = status.version.version
        data['favicon'] = None

        motd_text = remove_colours(status.motd)
        motd_normalized = ' '.join(motd_text.split())

        data['description'] = {
            'raw': status.motd,
            'text': motd_text,
            'normalized': motd_normalized
        }

    except:
        pass

    return data