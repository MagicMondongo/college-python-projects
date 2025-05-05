from js import document, console
from datetime import datetime

def validate_date_time(selected_date, selected_time):
    now = datetime.now()
    try:
        selected_datetime = datetime.strptime(f"{selected_date} {selected_time}", "%Y-%m-%d %H:%M")
    except ValueError:
        return False
    
    # Verifica se a data é no futuro
    if selected_datetime <= now:
        return False
        
    # Verifica se está dentro do horário comercial
    hour = selected_datetime.hour
    day = selected_datetime.weekday()  # 0=segunda, 6=domingo
    
    if day == 6:  # Domingo
        return 9 <= hour < 13
    elif 0 <= day <= 4:  # Terça a Sábado
        return 9 <= hour < 19
    else:  # Segunda (fechado)
        return False

def handle_submit(event):
    event.preventDefault()
    
    # Coletar dados do formulário
    name = document.getElementById("name").value
    phone = document.getElementById("phone").value
    email = document.getElementById("email").value
    service = document.getElementById("service").value
    date = document.getElementById("date").value
    time = document.getElementById("time").value
    
    # Validação básica
    if not all([name, phone, service, date, time]):
        document.getElementById("confirmation").innerHTML = "Preencha todos os campos obrigatórios!"
        document.getElementById("confirmation").style.display = "block"
        document.getElementById("confirmation").style.backgroundColor = "#f44336"
        return
    
    # Validação de data/horário
    if not validate_date_time(date, time):
        document.getElementById("confirmation").innerHTML = "Horário indisponível ou barbearia fechada!"
        document.getElementById("confirmation").style.display = "block"
        document.getElementById("confirmation").style.backgroundColor = "#f44336"
        return
    
    # Simular envio (em produção, enviaria para um backend)
    console.log(f"Agendamento: {name}, {phone}, {service}, {date} {time}")
    
    # Mostrar confirmação
    confirmation = document.getElementById("confirmation")
    service_name = {
        "corte": "Corte de Cabelo",
        "barba": "Barba",
        "completo": "Pacote Completo"
    }.get(service, service)
    
    confirmation.innerHTML = f"""
        Agendamento confirmado!<br>
        <strong>{name}</strong>, seu horário para {service_name} foi marcado para {date} às {time}.<br>
        Entraremos em contato para confirmação.
    """
    confirmation.style.display = "block"
    confirmation.style.backgroundColor = "#4CAF50"
    
    # Limpar formulário
    document.getElementById("appointment-form").reset()

# Configurar evento de submit
document.getElementById("appointment-form").addEventListener("submit", handle_submit)