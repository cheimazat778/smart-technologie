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

# تشغيل التطبيق (هذا السطر مهم للسيرفر المحلي فقط)
if __name__ == '__main__':
    app.run(debug=True)