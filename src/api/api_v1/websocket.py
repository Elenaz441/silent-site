from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from uuid import UUID

from websocket import manager


router = APIRouter(tags=["WS"])


@router.websocket("/{room_id}/{user_id}")
async def websocket_endpoint(
        websocket: WebSocket,
        room_id: UUID,
        user_id: UUID):
    await manager.connect(room_id, websocket)
    await manager.broadcast(room_id, {'command': 'join', 'user_id': str(user_id)}, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.broadcast(room_id, data, websocket)
    except WebSocketDisconnect:
        await manager.broadcast(room_id, {'command': 'leave', 'user_id': str(user_id)}, websocket)
        manager.disconnect(room_id, websocket)
