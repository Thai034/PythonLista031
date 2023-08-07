cpf = "3655521304" #cpf é do tipo str
print(f"CPF inserido: {cpf}")

if len(cpf) < 11:
    cpf = cpf.zfill(11) #zfill torne o str em 11 digitos preenchendo com zeros iniciais
    print(f"CPF com função zfill(11): {cpf}")

cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}.{cpf[9:]}"
print(f"CPF formatado: {cpf_formatado}")