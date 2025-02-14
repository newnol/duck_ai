import requests
import json

def fetch_vqd():
    response = requests.get("https://duckduckgo.com/duckchat/v1/status", headers={"x-vqd-accept": "1"})
    if response.status_code == 200:
        return response.headers.get("x-vqd-4")
    raise Exception(f"Failed to initialize chat: {response.status_code}")

def send_message(vqd, model, messages):
    response = requests.post(
        "https://duckduckgo.com/duckchat/v1/chat",
        headers={
            "accept": "text/event-stream",
            "accept-language": "en-US,en;q=0.5",
            "content-type": "application/json",
            "priority": "u=1, i",
            "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Brave\";v=\"133\", \"Chromium\";v=\"133\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "x-vqd-4": vqd,
            "cookie": "dcs=1; dcm=8",
            "Referer": "https://duckduckgo.com/",
            "Referrer-Policy": "origin"
        },
        json={"model": model, "messages": messages},
        stream=True
    )
    if response.status_code != 200:
        raise Exception(f"Failed to send message: {response.status_code}")
    
    collected_messages = []
    for line in response.iter_lines():
        if line and line.decode("utf-8").startswith("data: "):
            try:
                data = json.loads(line[6:])
                if message := data.get("message"):
                    collected_messages.append(message)
            except json.JSONDecodeError:
                pass
    
    if collected_messages:
        print("AI:", "".join(collected_messages))

def main():
    vqd = fetch_vqd()
    model = "o3-mini"  # Chọn model mặc định
    messages = []
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break
        messages.append({"content": user_input, "role": "user"})
        send_message(vqd, model, messages)
        
        # Đợi AI phản hồi xong trước khi nhận input tiếp theo
        print("\n--- AI đã trả lời xong ---\n")

if __name__ == "__main__":
    main()
