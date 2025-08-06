from flask import Flask, request, jsonify
import re

app = Flask(__name__)

LOT_SIZE = 0.03  # حجم اللوت

@app.route('webhook', methods=['POST'])
def webhook()
    data = request.get_json()
    message = data.get(message, )

    # تحديد نوع الصفقة
    if message.startswith(BUY)
        order_type = buy
    elif message.startswith(SELL)
        order_type = sell
    else
        return jsonify({status error, message Invalid signal}), 400

    # استخراج القيم باستخدام Regex
    entry_match = re.search(r'ENTRY=([d.]+)', message)
    tp1_match = re.search(r'TP1=([d.]+)', message)
    sl_match = re.search(r'SL=([d.]+)', message)

    entry_price = float(entry_match.group(1)) if entry_match else None
    tp1_price = float(tp1_match.group(1)) if tp1_match else None
    sl_price = float(sl_match.group(1)) if sl_match else None

    print(fOrder {order_type}, Entry {entry_price}, SL {sl_price}, TP1 {tp1_price})

    return jsonify({
        status success,
        order order_type,
        lot LOT_SIZE,
        entry entry_price,
        sl sl_price,
        tp1 tp1_price
    }), 200

if __name__ == '__main__'
    app.run(host='0.0.0.0', port=5000)
