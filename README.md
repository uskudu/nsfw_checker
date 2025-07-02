## 🧼 API-сервис для автоматического определения NSFW-контента на изображениях с использованием модели `Falconsai/nsfw_image_detection` (Hugging Face Transformers) и FastAPI.

📦 Возможности
=
- Принимает изображения `.jpg` или `.png`
- Классифицирует изображение как `OK` или `REJECTED`
- Использует предобученную модель NSFW-детекции от Falconsai

  
🚀 Быстрый старт
=
1. клонировать (```git clone https://github.com/yourname/nsfw_checker.git
cd nsfw_checker
python3 -m venv venv
source venv/bin/activate```);
2. установить зависимости (`pip install -r requirements.txt`)
4. запустить uvicorn (`uvicorn src.main:app --reload`)
5. перейти по адресу `http://127.0.0.1:8000/docs`
_____________

пример работы
=

## (через терминал):

request: curl -X POST -F "file=@test_pics/safe.jpg" http://localhost:8000/moderate

response: {"status":"OK"}

## (через интерактивную документацию):

![image](https://github.com/user-attachments/assets/0c5214c1-00a2-40b6-8ee8-8f0bc7c30df0)
![image](https://github.com/user-attachments/assets/3b62928c-bab5-466e-8805-1c249b41e950)
---
![image](https://github.com/user-attachments/assets/b5dde3eb-8830-478c-805a-7b532c61ae9a)
![image](https://github.com/user-attachments/assets/bada498a-e36a-4ad7-9902-924bd93982e3)

_____________

#есть принты с точным значением nsfw:

![image](https://github.com/user-attachments/assets/4b78b40d-2b60-4ae2-b2eb-6bcf86295a4f)
![image](https://github.com/user-attachments/assets/c667d67f-e641-4be7-b4c3-3d19e1146537)


## ⚠️ Замечания
Модель скачивается автоматически при первом запуске.

При необходимости загрузки из HuggingFace нужно быть залогиненым (`huggingface-cli login`).
