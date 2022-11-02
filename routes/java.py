from fastapi import APIRouter
from mcstatus import JavaServer

from utils import remove_colours, parse_version
from models import Status

router = APIRouter(
    prefix="/java",
    tags=["Minecraft: Java Edition"]
)

@router.get("/ping/{address}", response_model=Status)
async def java_ping(address: str):
    data = {"online": False, "ip": address}

    try:
        server = await JavaServer.async_lookup(address)
        status = await server.async_status()

        data['online'] = True
        data['players'] = {'online': status.players.online, 'max': status.players.max}
        data['protocol'] = status.version.protocol
        data['version'] = parse_version(status.version.name)
        data['favicon'] = status.favicon

        motd_text = remove_colours(status.description)
        motd_normalized = ' '.join(motd_text.split())

        data['description'] = {
            'raw': status.description,
            'text': motd_text,
            'normalized': motd_normalized
        }

    except:
        pass

    return data