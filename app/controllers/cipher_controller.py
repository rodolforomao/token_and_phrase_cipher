from flask import Blueprint, request, redirect, flash, jsonify
from app.models.cipher_model import CipherModel

cipher_bp = Blueprint('cipher', __name__)

@cipher_bp.route('/generate', methods=['POST'])
def generate():
    phrase = request.form.get('seeds')
    user_token1 = request.form.get('token1')

    if not phrase:
        flash("The field 'seeds' is required.", 'error')
        return redirect(request.referrer)

    try:
        if not user_token1:
            model = CipherModel(phrase)  # Gera token1 e token2 automaticamente
        else:
            from app.config import Config
            model = CipherModel(phrase, token1=user_token1, token2=Config.TOKEN2_ENV)

        encrypted = model.encrypt()
        success = model.verify(encrypted)

        return jsonify({
            'encrypted': encrypted,
            'token1': model.token1,
            'token2': model.token2,
            'success': success
        })

    except Exception as e:
        return jsonify({'error': f"Erro na criptografia: {str(e)}"}), 500


@cipher_bp.route('/decipher', methods=['POST'])
def decipher():
    encrypted_phrase = request.form.get('seeds')
    user_token1 = request.form.get('token1')
    user_token2 = request.form.get('token2')

    if not encrypted_phrase:
        return jsonify({'error': "The field 'seeds' (encrypted) is required."}), 400
    if not user_token1 or not user_token2:
        return jsonify({'error': "Both 'token1' and 'token2' are required for decryption."}), 400

    try:
        model = CipherModel(token1=user_token1, token2=user_token2)
        decrypted = model.decrypt(encrypted_phrase)

        return jsonify({
            'decrypted': decrypted,
            'token1': model.token1,
            'token2': model.token2,
            'success': True
        })

    except Exception as e:
        return jsonify({'error': f"Erro na descriptografia: {str(e)}"}), 500
