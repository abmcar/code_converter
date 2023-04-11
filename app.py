from flask import Flask, render_template, request
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_URL")
print(os.getenv("OPENAI_API_KEY"))
prompt = """
You are an expert programmer in all programming languages. Translate the code to "{}" code. Do not include \`\`\`.
  
      Example translating from JavaScript to Python:
  
      JavaScript code:
      for (let i = 0; i < 10; i++) {{
        console.log(i);
      }}
  
      Python code:
      for i in range(10):
        print(i)
      
      code:
      {}
      {} code (no \`\`\`):
"""


def convert_code(code, lang):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt.format(lang, code, lang),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    if response.choices[0].text:
        response_text = response.choices[0].text
        return response_text.strip()
    else:
        return None


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    code = request.form["code"]
    python_code = convert_code(code, "python")
    java_code = convert_code(code, "java")
    cpp_code = convert_code(code, "cpp")

    return render_template("result.html", python_code=python_code, java_code=java_code, cpp_code=cpp_code)


# 5. 启动应用程序
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
