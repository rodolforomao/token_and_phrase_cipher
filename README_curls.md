
✅ 1. Criptografar (POST /generate)
🔹 Sem token1 (gera token1 e token2 automaticamente)
	curl -X POST http://127.0.0.1:5000/generate \
	  -d "seeds=frase secreta para cifrar"
    
    📌 Resposta (exemplo):
        {
        "encrypted": "gAAAAABobqrUhNf4dpTzxkVLy3soWyNf5ImxiiKu9ib8Sy0KxXMJfKmbDm0i81zGmNgXhq4OQxqAlYclIWLUMGkwt2GkTVkHJav0OVMQdqeaOl5Sm0MthjiMqjM2e-zFoTHO9vdkTN7J2_5Omu7QYGVPsQnx0LZdj-FgUeXZC5CZ7okb92tCUvH3YQcRHsvGzd9B0JEbhdDNDKE32RnnUXWEBzjm3iRWjwbFqPv73qYu538q_DpzlKs=",
        "success": true,
        "token1": "8mbOkrCHXS9f3MX3OFey8W7gODHKHdi_RCR8nfaAU7o=",
        "token2": "41LIsGCDvqR3Teq38wbGNMWkcyk_HPiN85rLLpzETQE="
        }



🔹 Com token1 (usa o fornecido + token2 da variável de ambiente)
	curl -X POST http://127.0.0.1:5000/generate \
	  -d "seeds=mensagem ultra secreta" \
	  -d "token1=SEU_TOKEN_1_BASE64"


🔓 2. Descriptografar (POST /decipher)
	curl -X POST http://127.0.0.1:5000/decipher \
        -d "seeds=gAAAAABobqrUhNf4dpTzxkVLy3soWyNf5ImxiiKu9ib8Sy0KxXMJfKmbDm0i81zGmNgXhq4OQxqAlYclIWLUMGkwt2GkTVkHJav0OVMQdqeaOl5Sm0MthjiMqjM2e-zFoTHO9vdkTN7J2_5Omu7QYGVPsQnx0LZdj-FgUeXZC5CZ7okb92tCUvH3YQcRHsvGzd9B0JEbhdDNDKE32RnnUXWEBzjm3iRWjwbFqPv73qYu538q_DpzlKs=" \
        -d "token1=8mbOkrCHXS9f3MX3OFey8W7gODHKHdi_RCR8nfaAU7o=" \
        -d "token2=41LIsGCDvqR3Teq38wbGNMWkcyk_HPiN85rLLpzETQE="
    📌 Resposta esperada:
        {
        "decrypted": "frase secreta para cifrar",
        "token1": "8mbOkrCHXS9f3MX3OFey8W7gODHKHdi_RCR8nfaAU7o=",
        "token2": "41LIsGCDvqR3Teq38wbGNMWkcyk_HPiN85rLLpzETQE=",
        "success": true
        }



🔧 Gerar token manualmente em Python
Se quiser gerar um token1 para usar nos testes:
	import base64, os
	print(base64.urlsafe_b64encode(os.urandom(32)).decode())
