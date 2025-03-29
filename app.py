from flask import Flask, render_template

# إنشاء تطبيق فلاسك
app = Flask(__name__)

# صفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# صفحة التجارة الإلكترونية
@app.route('/ecommerce')
def ecommerce():
    return render_template('ecommerce.html')

# تشغيل التطبيق (معدل للعمل على Render)
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # يجعل الخادم قابل للوصول من الخارج
        port=10000,      # البورت الذي يتطلبه Render
        debug=False      # يجب أن يكون False في البيئة الإنتاجية
    )
