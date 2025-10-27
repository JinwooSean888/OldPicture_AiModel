from flask import Flask, request, send_file
import io
from colorizationModel import colorize_image  # Notebook 에서 변환된 함수

app = Flask(__name__)

@app.route('/colorize', methods=['POST'])
def colorize():
    image_file = request.files.get('image')
    if not image_file:
        return {"error": "No image received"}, 400

    input_data = image_file.read()
    output_img = colorize_image(input_data)   # -> bytes or PIL.Image

    # 만약 PIL.Image 형태라면 bytes로 바꿔서 반환
    if hasattr(output_img, 'save'):
        buffer = io.BytesIO()
        output_img.save(buffer, format='JPEG')
        buffer.seek(0)
        return send_file(buffer, mimetype='image/jpeg')

    return output_img  # 이미 bytes면 그대로 반환

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
