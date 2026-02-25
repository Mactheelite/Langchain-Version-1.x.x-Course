
# Multimodal
# Multimodality refers to the ability to work with data that comes in different forms, such as text, audio, images, and video. 
# LangChain includes standard types for these data that can be used across providers.

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage

load_dotenv()


llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

# From URL
message_1 = [
    {
    "role": "user",
    "content": [
        {"type": "text", "text": "Describe the content of this image."},
        {"type": "image", "url": "https://res.cloudinary.com/dw8j1umff/image/upload/v1769710064/orange_qegkzg.jpg"},
    ]
}
]


# From base64 data
message_2 = [
    { 
    "role": "user",
    "content" : [
        {"type": "text", "text": "Describe the content of this image."},
        {
            "type": "image_url",
            "image_url": {"url": "data:image/jpeg;base64,AAAAIGZ0eXBtcDQyAAAAAGlzb21tcDQyAAACAGlzb2..."}
        },
    ]}
    ]


# From provider-managed File ID
message_3 = [
    {
    "role": "user",
     "content":[
        {
            "type": "text", 
            "text": "Describe the content of this image."
        },
        {
            "type": "image_url", 
            "image_url": {"url": "file-abc123"}
        },
    ]
    }
]

response = llm.invoke(message_1) # Returns AIMessage

print(response.content)



#Notes
# 1. Image by URL
# What it means
# ~ The model fetches the image from the internet
# ~ You only pass a link

# 2. Image by base64 data
# What it means
# ~ You embed the raw image bytes directly in the request
# ~ No external fetching is needed

# 2. Image by provider-managed File ID
# What it means
# Image was uploaded earlier to the AI provider
# You reference it by ID

# Mental model (easy way to remember):

# URL → “Hey model, go look over there”
# Base64 → “Here, I brought the image with me”
# File ID → “You already have this image — use it”

# What should you use?
# ~ Quick demo? → URL
# ~ User uploads? → base64 → (then file_id if reused)
# ~ Production / scale? → file_id
# ~ Private images? → base64 or file_id

# For image input, the type field in the content can be either "image".
# For Pdf document input, the type field can be "file".
# For Audio input, the type field can be "audio".
# For Video input, the type field can be "video".