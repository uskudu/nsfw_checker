from PIL import Image
from transformers import pipeline
from schemas import SFWResponseSchema, NSWFResponseSchema


def find_nsfw(img_path: str) -> NSWFResponseSchema | SFWResponseSchema:
    img = Image.open(img_path)
    classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
    result = classifier(img)
    print(result)

    for res in result:
        if res['label'] == 'nsfw' and res['score'] > 0.7:

            return NSWFResponseSchema()
    return SFWResponseSchema()

