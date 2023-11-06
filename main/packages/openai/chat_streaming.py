import httpx
import asyncio
import os

async def fetch_url():
    client = httpx.AsyncClient()
    api_key = os.environ.get("OPENAI_API_KEY")
    
    question = "What is flask python?"

    async with client as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization":  f"Bearer {api_key}"},
            json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": question}],
                "max_tokens": 1024,
                "n": 1,
                "stop": None,
                "temperature": 0.7,
                "stream": True  # Look Here
            }
        )

        async for chunk in response.aiter_bytes():
            # Process the response chunk as it arrives
            print(chunk)

if __name__ == "__main__":
    asyncio.run(fetch_url())