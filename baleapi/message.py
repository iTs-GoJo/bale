from typing import Optional, Dict, Any

class Message:
    def __init__(self, data: dict, client: Optional[Any] = None, bot: Optional[Any] = None):
        self._data = data
        self.id = data.get("message_id")
        self.chat = data.get("chat", {})
        self.from_user = data.get("from", {})
        self.text = data.get("text")
        self.date = data.get("date")
        self.photo = data.get("photo")
        self.video = data.get("video")
        self.audio = data.get("audio")
        self.document = data.get("document")
        self.sticker = data.get("sticker")

        self._client = client
        self._bot = bot

    @property
    def chat_id(self) -> Optional[int]:
        return self.chat.get("id")

    async def reply(self, text: str, reply_markup: Optional[Dict] = None):
        if not self._client:
            raise RuntimeError("Client not attached to Message")
        return await self._client.send_message(self.chat_id, text, reply_markup=reply_markup)

    async def reply_photo(self, photo: str, caption: Optional[str] = None):
        if not self._client:
            raise RuntimeError("Client not attached to Message")
        return await self._client.send_photo(self.chat_id, photo, caption=caption)

    async def reply_keyboard(self, text: str, keyboard: Dict):
        """
        keyboard can be inline keyboard dict or already serialized string.
        """
        if not self._client:
            raise RuntimeError("Client not attached to Message")
        return await self._client.send_message(self.chat_id, text, reply_markup=keyboard)
